# Guide 10: Reference Navigation Patterns

## When to read this

Read this when converting a failure signal into exact source edits.

## What you will do

- map check IDs to governance cases
- map narrative to schema/contract authority

## Step-by-step

1. Start from failing check ID in summary artifacts.
2. Find corresponding governance case under `specs/04_governance/cases/core/`.
3. Follow policy/traceability links to normative contracts.
4. Apply minimal source-of-truth fix and re-run checks.

## Common failure signals

- editing book prose when schema contract is wrong
- updating check sets without case/policy sync
- stale manifest/index references after path edits

## Normative refs

- `docs/book/90_reference_guide.md`
- `specs/02_contracts/policy_v1.yaml`
- `specs/02_contracts/traceability_v1.yaml`
