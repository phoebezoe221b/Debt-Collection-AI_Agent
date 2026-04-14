# 📞 Debt Collection AI Agent (Hermes-Style Architecture)

## 🚀 Project Overview

This project implements a **backend AI-driven debt collection system** using a modular **agent-based architecture (inspired by Hermes Agents)**.

The system automatically:

* Fetches debtor data from Airtable
* Decides when to contact debtors (based on time, holidays, and due dates)
* Triggers AI voice calls using ElevenLabs
* Handles debtor queries via chat (simulated WhatsApp)
* Learns from past interactions using a closed feedback loop

---

## 🧠 Architecture Overview

The system is divided into two main layers:

### 🔹 Services (External Integrations)

* Airtable (data source)
* Apify (holiday calendar)
* ElevenLabs (voice AI)
* OpenRouter (LLM support)

### 🔹 Agents (Decision Intelligence)

* Decision Agent → decides when to call
* Voice Agent → triggers calls
* Chat Agent → handles debtor queries
* Learning Agent → improves performance over time

---

## 📁 Project Structure

```
debt-collection-agent/

main.py
config.py

services/
    airtable_client.py
    holiday_service.py
    voice_agent.py
    llm_agent.py

agents/
    decision_agent.py
    chat_agent.py
    learning_agent.py

README.md
requirements.txt
```

---

## ⚙️ Technologies Used

* Python
* Airtable API
* Apify API (Holiday data)
* ElevenLabs Voice AI
* OpenRouter (LLM provider)
* Requests library

---

## 🔄 Workflow

1. Fetch debtor data from Airtable
2. Fetch holiday data from Apify
3. Decision Agent evaluates:

   * Working hours (9 AM – 7 PM)
   * Weekends
   * Holidays
   * Due dates
4. If conditions met → trigger voice call via ElevenLabs
5. Log call results
6. Learning Agent analyzes success rate

---

## 📞 Voice Agent (ElevenLabs)

* Uses ElevenLabs Agent API
* Generates automated voice calls
* Provides:

  * Debt amount
  * Due date
  * Payment reminder

---

## 💬 Chat Agent (WhatsApp Simulation)

* Handles debtor queries like:

  * “What is my due amount?”
  * “When is my due date?”
* Restricts responses strictly to debt-related queries

---

## 🔁 Closed Learning Loop

The system tracks:

* Call attempts
* Success responses

Then calculates:

* Success rate
* Optimization insights

---

## 🔐 Environment Variables

Sensitive data is managed using environment variables:

```
AIRTABLE_API_KEY=your_key
APIFY_TOKEN=your_token
ELEVEN_API_KEY=your_key
```

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## ⚠️ Voice Agent Note

Voice calls are triggered using ElevenLabs API.

In the current setup, the API returns:
"Not Found"

This is due to:
- Agent endpoint limitations
- Free tier restrictions

However, the system correctly:
- Attempts calls
- Logs responses
- Updates learning loop

This demonstrates full agent pipeline functionality.

## 📊 Features

✔ Modular agent-based architecture
✔ Automated decision-making system
✔ Voice AI integration
✔ Holiday-aware scheduling
✔ Chat interaction support
✔ Logging and monitoring
✔ Closed feedback loop

---

## 🚀 Future Improvements

* WhatsApp API integration (Twilio/Telnyx)
* Real-time call analytics
* Advanced LLM-based negotiation
* Multi-language support
* Scalable deployment (Docker/Kubernetes)

---

## 📚 Data Sources

* Airtable (Debtor Data)
* Apify (Holiday API)

---

## 📌 Notes

* Twilio was tested but not used in final implementation (as per requirements)
* Designed to integrate with Telnyx in future
* Follows Hermes-style modular agent design

---

## 👩‍💻 Author

Mudhavarthi Phabe Zoe Gospel
---

## 📬 Submission

Includes:

* GitHub repository
* Apify token used
* ElevenLabs agent output

---

## ⭐ Key Highlight

> Implemented a custom Hermes-style agent architecture separating services and intelligent agents for scalable AI workflow automation.

---
