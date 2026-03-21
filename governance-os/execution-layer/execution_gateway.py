from fastapi import FastAPI
from decision_layer.decision_engine import evaluate_decision
from control_plane.policy_engine import check_policy
from control_plane.authority_engine import verify_authority
from execution_layer.workflow_engine import execute_action
from audit_layer.audit_ledger import log_execution

app = FastAPI()

@app.post("/governed-execution")
def governed_execution(request: dict):
    decision = evaluate_decision(request)
    if not check_policy(decision):
        return {"status": "blocked", "reason": "policy violation"}
    if not verify_authority(request["authority_token"]):
        return {"status": "blocked", "reason": "invalid authority"}
    result = execute_action(decision)
    log_execution(request, result)
    return {"status": "approved", "result": result}
