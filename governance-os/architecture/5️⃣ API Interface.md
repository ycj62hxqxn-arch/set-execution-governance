Primary API Endpoint

POST /governed-execution

Request Payload:
{
  "ai_decision": "string",
  "action_request": { "object": "data" },
  "authority_token": "string"
}

Response:
{
  "status": "approved | denied",
  "reason": "string",
  "evidence_id": "string"
}