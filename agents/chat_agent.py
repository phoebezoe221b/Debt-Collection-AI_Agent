def chat_agent(message, debtor):
    prompt = f"""
    You are a strict debt collection assistant.

    Rules:
    - Only answer debt-related queries
    - Be polite but firm
    - Do not answer unrelated questions

    User: {message}
    Debt: ₹{debtor['amount']}
    Due date: {debtor['due_date']}
    """

    return ask_llm(prompt)
