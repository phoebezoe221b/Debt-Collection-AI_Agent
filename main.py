import logging
from airtable_client import fetch_airtable_data, transform_record
from decision_engine import should_call, get_holidays
from voice_agent import trigger_voice_call
from learning import log_call, optimize_strategy

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def run_agent():
    try:
        logging.info("🚀 Agent Started")

        records = fetch_airtable_data()
        debtors = [transform_record(r) for r in records]

        holidays = get_holidays()

        for debtor in debtors:
            decision, reason = should_call(debtor, holidays)

            if decision:
                result = trigger_voice_call(debtor)
                log_call(debtor, result)
            else:
                logging.info(f"⏭️ SKIP: {debtor['name']} ({reason})")

        optimize_strategy()

        logging.info("✅ Agent Finished")

    except Exception as e:
        logging.error(f"Agent failed: {e}")


if __name__ == "__main__":
    run_agent()
