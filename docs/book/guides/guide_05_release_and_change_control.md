# Guide 05: Release and Change Control

## When to read this

Read this when preparing changes for merge and release readiness.

## What you will do

- ensure policy and traceability completeness
- keep changes bounded and auditable

## Step-by-step

1. Verify policy rule impacts are represented.
2. Verify traceability entries map to active checks/cases.
3. Re-run required checks.
4. Document migration impacts in release notes if needed.

## Common failure signals

- policy change without traceability row
- case ID updates without check set updates
- docs references stale after refactor

## Normative refs

- `specs/02_contracts/policy_v1.yaml`
- `specs/02_contracts/traceability_v1.yaml`
- `specs/04_governance/check_sets_v1.yaml`
