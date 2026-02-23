# Spec Lifecycle

## When to read this

Read this when planning or reviewing a spec change from draft to merge.

## What you will do

- Follow lifecycle stages with deterministic checks.
- Keep schema/contracts/governance/docs synchronized.

## Step-by-step

1. Draft the change in schema/contracts first.
2. Update executable specs and governance expectations.
3. Update docs/book narrative and reference surfaces.
4. Run governance, critical-gate, and docs-generate-check.
5. Merge only when all required gates are clean.

## Common failure signals

- Policy/traceability references not updated for renamed paths.
- Governance cases still expecting removed chapter surfaces.
- Narrative docs contradicting normative sources.

## Normative refs

- `specs/02_contracts/15_governance_subject_model.md`
- `specs/02_contracts/policy_v1.yaml`
- `specs/02_contracts/traceability_v1.yaml`
