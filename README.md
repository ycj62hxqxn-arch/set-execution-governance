![SET Compliant](./assets/badges/set-compliant.svg)
# SET — Execution Governance

## The Missing Layer in AI Systems

AI systems today optimize for:

- correctness
- performance
- alignment

But they assume:

> if (correct) → execute

This assumption is false.

---

## The Problem

Execution is not controlled.

Between:

decision → execution

there exists a control boundary.

Right now, it is unmanaged.

---

## What SET Does

SET defines the conditions under which execution is allowed to become real.

It determines:

- whether execution is allowed
- when execution is blocked
- how authority governs action

---

## Core Principle

Execution is not automatic.

Execution is admissible.

---

## Failure Condition

A system that allows execution without authority:

- is uncontrolled  
- cannot guarantee correctness  
- cannot prevent invalid state transitions  

Such a system is considered non-governed.
## Example

System: Vehicle Trade Pipeline (CARSHUNTER)

State: VERIFIED → LIVE

- Verification: vehicle data confirmed  
- Invariance: constraints satisfied  
- Execution Authority: ALLOW  

→ Transition COMMITTED

Without execution authority:

→ Transition would not be permitted
---
## Why It Matters

Systems don’t fail because they break.

They fail because they continue executing correctly  
on a state that is no longer valid.

---

## Who This Is For

- AI infrastructure builders  
- autonomous systems designers  
- high-stakes decision systems  

---

## Key Question

In your system today:

👉 Can an action be refused AFTER it is validated  
but BEFORE it executes?

If not — you don’t control execution.

---

## Access

Architecture and specification are available in this repository.

For deeper discussion:

→ Reach out / open an issue
## Statement

Any system that cannot refuse execution after validation  
does not control execution.
