import requests
import logging
from config import ELEVEN_API_KEY, AGENT_ID


def trigger_voice_call(debtor):
    logging.info(f"📞 CALLING: {debtor['name']}")

    url = "https://api.elevenlabs.io/v1/agents/run"

    headers = {
        "xi-api-key": ELEVEN_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "agent_id": AGENT_ID,
        "input": f"""
        Call {debtor['name']}.
        Their due amount is ₹{debtor['amount']}.
        Due date was {debtor['due_date']}.
        Ask them to pay immediately.
        """
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return "CALLED"
    else:
        logging.error(f"Call failed: {response.text}")
        return "FAILED"
