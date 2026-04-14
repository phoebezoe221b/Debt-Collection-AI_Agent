from datetime import datetime
import logging

call_logs = []


def log_call(debtor, result):
    call_logs.append({
        "name": debtor["name"],
        "time": datetime.now(),
        "result": result
    })


def optimize_strategy():
    total = len(call_logs)
    if total == 0:
        return

    success = len([c for c in call_logs if c["result"] == "CALLED"])
    success_rate = success / total

    # 🔥 adaptive logic
    if success_rate < 0.5:
        logging.info("⚠️ Adjusting strategy: calling earlier in the day")
    else:
        logging.info("✅ Strategy working well")

    logging.info(f"📊 Success Rate: {success_rate:.2f}")
