# openai-company-market-summary

## Important Setup Note

Before using this project, ensure you have configured the following environment variables or settings:

- `OPENAI_API_KEY`: Your OpenAI API key for authentication.
- `GOOGLE_CREDENTIALS_PATH`: Path to your Google credentials JSON file for accessing Google Sheets API.
- `SPREADSHEET_ID`: The ID of the Google Spreadsheet containing the company list.

Properly setting these up is essential for the tool to access APIs and function as intended.

## Description

This project leverages OpenAI's GPT-4o-mini model to generate detailed, concise, and factual summaries of companies focused on competitive analysis and market research. Given a company name, the tool produces a structured summary describing what the company does, its market role, financial highlights, employee size, and industry position by querying publicly available sources like company websites, LinkedIn profiles, and annual reports.

## Key Features

- Automatically creates custom prompts to ask an OpenAI language model for comprehensive company insights.
- Covers multiple aspects including business activities, mission, financial data, workforce size, and market research insights.
- Produces a cohesive summary suitable for competitive analysis and business intelligence.
- Includes robust error handling for reliable API interaction.
- Suitable for market analysts, business strategists, and researchers.

## Core Code Outline

- `create_summary_prompt(company_name)`: Builds a sophisticated prompt instructing the model to cover multiple dimensions of a company in a single paragraph.
- `generate_summary(company_name)`: Calls OpenAI's chat completion API with the crafted prompt to retrieve a detailed company summary including its market role and context.
- Parameters like `max_tokens=350` and temperature are optimized for factual, professional summaries.

## Project Flow

1. **Input**: The tool reads a list of company names from a Google Spreadsheet tab. This list acts as the input source for companies to analyze.

2. **Processing**: For each company name, the system:

   - Generates a detailed prompt tailored to gather comprehensive company and market insights.
   - Sends the prompt to the OpenAI API to obtain a well-structured company summary.

3. **Output**: The generated summaries are written back to a separate tab in the same Google Spreadsheet, keeping the original list intact and providing easy review and export.

4. **Automation**: This workflow can be automated using Google Apps Script or any Python script using the Google Sheets API to:
   - Read input lists,
   - Fetch summaries from OpenAI,
   - Save results back systematically in the spreadsheet.

## Usage Example

```python
company_name = "Tesla, Inc."
summary = generate_summary(company_name)
print(summary)
```
