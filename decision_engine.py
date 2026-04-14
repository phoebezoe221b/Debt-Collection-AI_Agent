import requests
from datetime import datetime
from config import APIFY_TOKEN
import logging


def get_holidays():
    try:
        year = datetime.now().year

        url = "https://api.apify.com/v2/acts/vivid_astronaut~holiday-calendar/run-sync-get-dataset-items"

        payload = {"countryCode": "US", "year": year}
        params = {"token": APIFY_TOKEN}

        response = requests.post(url, json=payload, params=params)

        if response.status_code != 200:
            return []

        data = response.json()
        holidays = data[0]["result"]["holidays"]

        return [h["date"] for h in holidays]

    except Exception as e:
        logging.error(f"Holiday fetch error: {e}")
        return []
def should_call(debtor, holidays):
    now = datetime.now()

    if now.weekday() >= 5:
        return False, "Weekend"

    if now.hour < 9 or now.hour > 19:
        return False, "Outside working hours"

    if now.strftime("%Y-%m-%d") in holidays:
        return False, "Holiday"

    days_left = (debtor["due_date"] - now.date()).days
    logging.info(f"{debtor['name']} days_left: {days_left}")

    if days_left <= 0:
        return True, "Overdue"

    return False, "Not due yet"