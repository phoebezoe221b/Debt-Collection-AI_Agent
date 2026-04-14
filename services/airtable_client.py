import requests
from datetime import datetime, date
from config import AIRTABLE_API_KEY, BASE_ID, TABLE_NAME


def fetch_airtable_data():
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Airtable Error: {response.text}")

    return response.json()["records"]


def transform_record(record):
    fields = record.get("fields", {})

    try:
        due_date = datetime.strptime(fields.get("due_date"), "%Y-%m-%d").date()
    except:
        due_date = date.today()

    return {
        "name": fields.get("name", "Unknown"),
        "phone": fields.get("phone", ""),
        "due_date": due_date,
        "amount": fields.get("debt_amount", 0),
        "company": fields.get("company", "Unknown")
    }
