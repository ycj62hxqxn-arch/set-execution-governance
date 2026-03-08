# Copilot Instructions for PMS_GOVERN

## Architecture: Command → QGED Gate → Ledger
Every action flows through a single governed pipeline:
**Command Interface → Authority/Policy Engine → Execution Layer → Evidence Ledger → State Freeze**

QGED cannot make a decision without three-part runtime context: `SYSTEM_STATE` + `DOMAIN_STATE` + `AUTHORITY_STATE`. Without all three, risk level, domain conditions, and authority escalation requirements are unknown — no command may proceed.

## Directory Layout
- `PMS_GOVERN/` — canonical implementation tree: `CORE/`, `LAW/`, `STATE/`, `LEDGER/`, `MANIFEST/`, `DOMAINS/`, `AI/`
- `Governance Operating System/` — parallel runtime organisation with its own `schemas/`, `policy/`, `ledger/`, state files
- Root-level files (`command_schema.json`, `governanace_policy.yaml`, `ai_manifest.json`) — prototype/reference copies; canonical versions live inside the subdirectories
- `CORE/` contains four engines: `authority_engine`, `command_engine`, `execution_runtime`, `policy_engine`

## Authority Chain
| Actor | Level | Max Complexity | Execution Rights | Sectors |
|---|---|---|---|---|
| `AA` (sovereign) | 5 | 10 | ✅ | all |
| `BPB_OPERATOR` (delegated) | 3 | 5 | ✅ | trade, logistics |
| `YAI_AGENT` (AI advisory) | 1 | 3 | ❌ | diagnose only |

Authority modes (`.github/AUTHORITY_STATE.json`): `direct` | `delegated` | `restricted` | `emergency`

## Signing Rules (`governance_policy.yaml`)
- Complexity **1–3**: 1 signer
- Complexity **4–7**: 2 signers required
- Complexity **8–10**: AA signature mandatory
- Sector baselines: `automotive` → 4, `medical` → 6
- Financial: payments >€10,000 require multi-sign regardless of complexity score

## AI Agent (YAI) Hard Constraints
YAI may only perform: `diagnose`, `analysis`, `proposal`
YAI is permanently blocked from: `financial_execution`, `authority_override`, `policy_modification`
Source of truth: `Governance Operating System/ai/llm_governance_context.json`

## Command Schema
All commands must conform to `Governance Operating System/schemas/command_schema.json`. Required fields:
`command_id` (UUID), `actor` (type + id), `action` (type: GO|HOLD|DIAGNOSE, sector, operation), `complexity_score` (1–10), `risk_level` (low|medium|high), `signer`, `payload`, `gate_decision` (ALLOW|BLOCK)

## Ledger Format (append-only, hash-chained)
Each entry in `ledger/ledger.jsonl` includes `previous_hash` — the ledger is blockchain-style chained. Never modify existing entries. New entries require: `entry_id`, `command_id`, `decision`, `hash` (SHA256), `previous_hash`. See `Governance Operating System/schemas/ledger_schema.json`.

## Evidence Metadata Pattern
Every executed command produces an evidence record (see `Evidence Metadata Extension.json`):
`event_id`, `command`, `actor`, `domain`, `authority_validated`, `system_state`, `domain_risk_tier`, `timestamp`, `hash`

## Domains
Active domains: `CARSHUNTER` (automotive, risk_tier 2), `BPB` (finance/advisory), `IBN_SINA` (medical). Each domain has its own `DOMAIN_STATE` tracking: `domain_status`, `risk_tier`, `authority_required`, `transaction_threshold`, `compliance_mode`.

## Runtime Modes
`runtime_mode`: `development` | `operational` | `audit` | `freeze`
`risk_level`: `normal` | `elevated` | `critical`
When `freeze_state: true`, no new commands may be executed.

## Key Reference Files
- `Governance Operating System/policy/authority_registry.yaml` — who can act in which sectors
- `Governance Operating System/policy/governance_policy.yaml` — signing rules, sector baselines, financial thresholds
- `.github/AUTHORITY_STATE.json` — live authority mode
- `Governance Operating System/SYSTEM_STATE.json` — live runtime mode and risk level
- `Governance Operating System/DOMAIN_STATE.json` — per-domain operational state
- `actor_manifest.json` — actor definitions with authority levels and execution rights

---
_Last updated: 8 March 2026_
