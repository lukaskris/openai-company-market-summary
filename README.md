# openai-company-market-summary

## Description

This project leverages OpenAI's GPT-4o-mini model to generate detailed, concise, and factual summaries of companies focused on competitive analysis and market research. Given a company name, the tool produces a structured summary describing what the company does, its market role, financial highlights, employee size, and industry position by querying publicly available sources like company websites, LinkedIn profiles, and annual reports.

## Key Features

- Automatically creates custom prompts to ask an OpenAI language model for comprehensive company insights.
- Covers multiple aspects including business activities, mission, financial data, workforce size, and market research insights.
- Produces a cohesive summary suitable for competitive analysis and business intelligence.
- Includes robust error handling for reliable API interaction.
- Suitable for market analysts, business strategists, and researchers.

## Core Code Outline

- `create_detailed_summary_prompt_with_role(company_name)`: Builds a sophisticated prompt instructing the model to cover multiple dimensions of a company in a single paragraph.
- `generate_detailed_summary_with_role(company_name)`: Calls OpenAI's chat completion API with the crafted prompt to retrieve a detailed company summary including its market role and context.
- Parameters like `max_tokens=350` and temperature are optimized for factual, professional summaries.

## Usage Example

```python
company_name = "Tesla, Inc."
summary = generate_detailed_summary_with_role(company_name)
print(summary)
