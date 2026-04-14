import requests

OPENROUTER_API_KEY = "your_key"

def ask_llm(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a strict debt collection assistant. Only answer debt-related queries."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, json=data, headers=headers)

    return response.json()["choices"][0]["message"]["content"]