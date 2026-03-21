# Copilot Instructions for PMS_GOVERN

## Architecture: Command → QGED Gate → Ledger
Every action flows through a single governed pipeline:
**Command Interface → QGED Authority Gate → Execution Layer → Evidence Record → Ledger Append → State Freeze**

The decision engine is **QGED** (gating), backed by the **GCC** governance cycle engine. QGED cannot render a decision without all three runtime context objects loaded simultaneously: `SYSTEM_STATE` + `DOMAIN_STATE` + `AUTHORITY_STATE`. Missing any one means risk level, domain conditions, or escalation requirements are unknown — the gate must block.

## File Canonicity — Critical
Two parallel directory trees exist. **Do not treat them as equivalent.**

| Tree | Role | Trust |
|---|---|---|
| `Governance Operating System/` | Live runtime state, populated schemas, active policy | **Source of truth** |
| `PMS_GOVERN/` | Canonical implementation scaffold | Many sub-files are **empty stubs** (`LAW/`, `STATE/`, `MANIFEST/`) |
| Root-level files (`command_schema.json`, `governanace_policy.yaml`, `ai_manifest.json`) | Prototype / reference copies | Do not edit as canonical |

Always read from `Governance Operating System/` for schemas, policy, and state. Write new implementation into `PMS_GOVERN/` but populate from the live files above.

## Directory Layout
- `PMS_GOVERN/CORE/` — four engines: `authority_engine`, `command_engine`, `execution_runtime`, `policy_engine`
- `PMS_GOVERN/DOMAINS/` — per-domain files: `bpb`, `carshunter`, `ibn_sina` (flat files, not subdirectories)
- `PMS_GOVERN/LEDGER/` — `audit_records`, `evidence_log`, `freeze_snapshots` (subdirectory stubs)
- `Governance Operating System/schemas/` — `command_schema.json`, `ledger_schema.json`
- `Governance Operating System/policy/` — `governance_policy.yaml`, `authority_registry.yaml`
- `Governance Operating System/ai/` — `llm_governance_context.json` (AI hard constraints)

## Authority Chain
| Actor | Level | Max Complexity | Execution Rights | Sectors |
|---|---|---|---|---|
| `AA` (sovereign) | 5 | 10 | ✅ | all |
| `BPB_OPERATOR` (delegated) | 3 | 5 | ✅ | trade, logistics |
| `YAI_AGENT` (AI advisory) | 1 | 3 | ❌ | diagnose only |

Live authority mode in `.github/AUTHORITY_STATE.json`: `direct` | `delegated` | `restricted` | `emergency`

## Signing Rules (`Governance Operating System/policy/governance_policy.yaml`)
- Complexity **1–3**: 1 signer
- Complexity **4–7**: 2 signers required
- Complexity **8–10**: AA signature mandatory
- Sector baselines raise the floor: `automotive` → 4, `medical` → 6
- Financial: any payment >€10,000 requires multi-sign regardless of complexity score

## AI Agent (YAI) Hard Constraints
YAI may only perform: `diagnose`, `analysis`, `proposal`
YAI is permanently blocked from: `financial_execution`, `authority_override`, `policy_modification`
Source of truth: `Governance Operating System/ai/llm_governance_context.json`

## Command Schema
All commands conform to `Governance Operating System/schemas/command_schema.json`. Required fields:
`command_id` (UUID), `actor` (`type`: human|ai|delegated, `id`), `action` (`type`: GO|HOLD|DIAGNOSE, `sector`, `operation`), `complexity_score` (1–10), `risk_level` (low|medium|high), `signer`, `payload`, `gate_decision` (ALLOW|BLOCK)

**Action type semantics:** `GO` = execute, `HOLD` = pause/defer, `DIAGNOSE` = analyse only (always safe for YAI).

## Ledger Format (append-only, hash-chained)
`Governance Operating System/schemas/ledger_schema.json` defines each entry: `entry_id`, `command_id`, `decision`, `actor`, `signer`, `complexity`, `sector`, `operation`, `hash` (SHA256), `previous_hash`. The chain is blockchain-style — **never modify or delete existing entries**. Root-level `ledger.jsonl` is the active file; `Governance Operating System/ledger/` is currently empty.

## Evidence Metadata Pattern
Every executed command produces an evidence record (`Evidence Metadata Extension.json` template):
`event_id`, `command`, `actor`, `domain`, `authority_validated`, `system_state`, `domain_risk_tier`, `timestamp`, `hash`

## Domains
Active domains and their sectors/risk tiers:
- `CARSHUNTER` — automotive, risk_tier 2, operator authority, transaction_threshold 100,000
- `BPB` — finance/advisory (BPB Solutions LTD)
- `IBN_SINA` — medical (sector baseline complexity 6)

Each domain has its own `DOMAIN_STATE` shape: `domain_status`, `risk_tier`, `authority_required`, `transaction_threshold`, `compliance_mode`.

## Runtime Modes
`runtime_mode`: `development` | `operational` | `audit` | `freeze`
`risk_level`: `normal` | `elevated` | `critical`
`freeze_state: true` → no new commands may be executed under any authority level.

## Key Reference Files
- `.github/AUTHORITY_STATE.json` — live authority mode
- `Governance Operating System/SYSTEM_STATE.json` — live runtime mode and risk level
- `Governance Operating System/DOMAIN_STATE.json` — per-domain operational state
- `actor_manifest.json` — actor definitions with authority levels and execution rights
- `Governance Operating System/policy/authority_registry.yaml` — sector-scoped actor permissions
- `Governance Operating System/policy/governance_policy.yaml` — signing rules and financial thresholds
- `system_manifest.json` — top-level system identity (PMS_GOVERN v1.0, QGED engine, SHA256 ledger)

## Operations Tools (AI-Agent Use)
All outputs are proposals — distribution requires AA review.

| Tool | Invocation | Output |
|---|---|---|
| PPTX / PDF Engine | `.venv/bin/python generate_pptx.py` | `BPB_Governance_Architecture_Report.pptx` (14 slides, 16:9) |
| HTML Reveal | `open BPB_Governance_Architecture_Reveal.html` | Interactive slides (keyboard/swipe) |
| HTML Review Doc | `open Copilot_Instructions_Review.html` | Static full-document review |

**PDF export:** Browser → `Cmd+P` → Save as PDF → Background graphics ON, no margins.

---
_Last updated: 11 March 2026_
