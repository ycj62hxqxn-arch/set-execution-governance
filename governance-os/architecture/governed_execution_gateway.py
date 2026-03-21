from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Any, Dict

app = FastAPI(title="Governed Execution Gateway")

# --- Models ---
class GovernedExecutionRequest(BaseModel):
    ai_decision: str
    action_request: Dict[str, Any]
    authority_token: str

class GovernedExecutionResponse(BaseModel):
    status: str  # 'approved' or 'denied'
    reason: str
    evidence_id: str = None

# --- Mocked Subsystems (replace with real logic) ---
def admissibility_layer(ai_decision, action_request):
    # Placeholder: check if action is admissible
    return ai_decision in {"GO", "HOLD", "DIAGNOSE"}

def authority_verification(authority_token):
    # Placeholder: verify authority token
    return authority_token.startswith("AUTH-")

def execution_gate(ai_decision, action_request):
    # Placeholder: QGED logic
    if ai_decision == "GO":
        return True, "Execution allowed"
    elif ai_decision == "HOLD":
        return False, "Action on hold"
    elif ai_decision == "DIAGNOSE":
        return True, "Diagnostic allowed"
    return False, "Unknown decision"

def evidence_freeze(action_request, status):
    # Placeholder: log evidence and return an ID
    return f"EVID-{hash(str(action_request)+status)%1000000}"


# --- In-memory execution history for demo ---
execution_history = []

# --- API Endpoints ---
@app.post("/governed-execution", response_model=GovernedExecutionResponse)
def governed_execution(req: GovernedExecutionRequest):
    # 1. Admissibility
    if not admissibility_layer(req.ai_decision, req.action_request):
        raise HTTPException(status_code=400, detail="Action not admissible")
    # 2. Authority Verification
    if not authority_verification(req.authority_token):
        resp = GovernedExecutionResponse(status="denied", reason="Invalid authority token")
        execution_history.append({"input": req.dict(), "output": resp.dict()})
        return resp
    # 3. Execution Gate
    allowed, reason = execution_gate(req.ai_decision, req.action_request)
    # 4. Evidence Freeze
    evidence_id = evidence_freeze(req.action_request, "approved" if allowed else "denied")
    resp = GovernedExecutionResponse(
        status="approved" if allowed else "denied",
        reason=reason,
        evidence_id=evidence_id
    )
    execution_history.append({"input": req.dict(), "output": resp.dict()})
    return resp

# --- GET /system/state ---
@app.get("/system/state")
def get_system_state():
    # Demo: return static system state
    return {
        "system": "Governed Execution Gateway",
        "status": "operational",
        "version": "1.0",
        "risk_level": "normal"
    }

# --- GET /governance/report ---
@app.get("/governance/report")
def get_governance_report():
    # Demo: return static governance report
    return {
        "policy": "Authority-first, multi-layered governance",
        "signing_rules": "Complexity-based, multi-signature for high-risk actions",
        "audit": "All actions logged, evidence chain maintained",
        "last_audit": "2026-03-16"
    }

# --- GET /execution/history ---
@app.get("/execution/history")
def get_execution_history():
    # Return the in-memory execution history (last 100 for demo)
    return execution_history[-100:]

# --- To run: uvicorn governed_execution_gateway:app --reload ---
