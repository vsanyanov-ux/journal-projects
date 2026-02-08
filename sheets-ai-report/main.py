from fastapi import FastAPI
import gspread
from google.oauth2.service_account import Credentials
from pydantic import BaseModel
from dotenv import load_dotenv
from mistralai import Mistral
import os
import json

load_dotenv()

app = FastAPI()


class SheetData(BaseModel):
    sheet_id: str
    range: str = "A1:U300"


def get_sheet_data(sheet_id: str, range_str: str):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly",
    ]

    creds_info = json.loads(os.getenv("SHEET_CREDS"))
    creds = Credentials.from_service_account_info(creds_info, scopes=scopes)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id).sheet1
    return sheet.get(range_str)


api_key = os.getenv("MISTRAL_API_KEY")
mistral = Mistral(api_key=api_key)


def call_mistral(prompt: str) -> str:
    res = mistral.chat.complete(
        model="mistral-small-latest",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    try:
        # запрос к Mistral
        except Exception as e:
            if "rate_limited" in str(e):
                return {"error": "Превышен лимит запросов к AI. Попробуйте через 1-2 минуты."}
            raise

    return res.choices[0].message.content


@app.post("/analyze")
async def analyze_report(payload: SheetData):
    raw_data = get_sheet_data(payload.sheet_id, payload.range)

    table_text = "\n".join([", ".join(row) for row in raw_data])

    analysis_prompt = f"""
You are an AI assistant that analyzes journaling data from a Google Sheet.

Table data:
{table_text}

Your task:
- Briefly summarize what these entries are about.
- Highlight the main themes, emotions, and topics.
- Keep the answer under 200 words.
"""

    summary = call_mistral(analysis_prompt)

    return {"summary": summary, "raw": raw_data}
