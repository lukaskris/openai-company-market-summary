import config

import time
import gspread
from openai import OpenAI
from gspread.exceptions import WorksheetNotFound

OPENAI_API_KEY = config.OPENAI_API_KEY
if not OPENAI_API_KEY:
    raise ValueError("Please set your OPENAI_API_KEY environment variable.")

GOOGLE_CREDENTIALS_PATH = config.GOOGLE_CREDENTIALS_PATH
if not GOOGLE_CREDENTIALS_PATH:
    raise ValueError("Please set your GOOGLE_CREDENTIALS_PATH environment variable.")

SPREADSHEET_ID = "1MAU5ouftcs0zQsIsjs1Ik8kmADqhGjsPBYn5JcpYc3w"

client = OpenAI(api_key=OPENAI_API_KEY)
gc = gspread.service_account(filename=GOOGLE_CREDENTIALS_PATH)

def get_company_names(sheet):
    worksheet = sheet.sheet1
    values = worksheet.col_values(1)
    # Skip header, filter out empty
    company_names = [name for name in values[1:] if name.strip()]
    return company_names

def create_summary_prompt(company_name):
    
    prompt = (
        f"Provide a comprehensive and factual summary of the company '{company_name}', "
        "covering the following points in a single well-structured paragraph:\n"
        "- A brief description of what the company does\n"
        "- Key financial information (like revenue, profit, or market value if publicly available)\n"
        "- Number of employees or size of workforce\n"
        "- Industry position and relevant market research insights\n"
        "Use publicly available information such as the company's website, annual reports, press releases, or LinkedIn profile. "
        "Write clearly and professionally, suitable for competitor analysis or market research. "
        "Ensure the summary is accurate and up-to-date."
    )
    return prompt

def generate_summary(company_name):
    prompt = create_summary_prompt(company_name)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.5,
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        print(f"Error generating summary for '{company_name}': {str(e)}")
        return "Error: Could not generate summary."

def write_summaries(sheet, company_names, summaries):
    try:
        summary_sheet = sheet.worksheet("Summaries")
        summary_sheet.clear()
    except WorksheetNotFound:
        summary_sheet = sheet.add_worksheet(title="Summaries", rows="100", cols="2")

    # Prepare data with header
    data = [["Company Name", "Summary"]]
    for name, summ in zip(company_names, summaries):
        data.append([name, summ])

    # Update the worksheet
    summary_sheet.update(data)

def main():
    sheet = gc.open_by_key(SPREADSHEET_ID)

    company_names = get_company_names(sheet)
    print(f"Found {len(company_names)} companies.")

    # Generate summaries
    summaries = []
    for idx, company in enumerate(company_names, start=1):
        print(f"[{idx}/{len(company_names)}] Summarizing: {company}")
        summary = generate_summary(company)
        print(f"Summary for {company}: {summary}")
        summaries.append(summary)
        # To avoid rate limits, sleep if needed
        time.sleep(1)

    # Write summaries to new tab
    write_summaries(sheet, company_names, summaries)
    print("Summaries written to 'Summaries' sheet.")

if __name__ == "__main__":
    main()
