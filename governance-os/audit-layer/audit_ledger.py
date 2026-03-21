import json
from datetime import datetime
from pathlib import Path

LEDGER_PATH = Path(__file__).parent.parent / "ledger" / "execution_ledger.json"

def log_execution(request, result):
    entry = {
        "execution_id": f"EXE-{hash(str(request)+str(datetime.utcnow()))%1000000}",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ai_decision": request.get("ai_decision"),
        "policy_id": request.get("policy_id", "N/A"),
        "authority_token": request.get("authority_token"),
        "risk_score": 0.18,
        "status": result.get("status", "APPROVED"),
        "evidence_hash": f"0x{hash(str(request)) & 0xfffffff:x}"
    }
    # Append to ledger file
    if LEDGER_PATH.exists():
        with open(LEDGER_PATH, "r+") as f:
            try:
                data = json.load(f)
            except Exception:
                data = []
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=2)
    else:
        with open(LEDGER_PATH, "w") as f:
            json.dump([entry], f, indent=2)
