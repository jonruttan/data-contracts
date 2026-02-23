# Guide 06: Governance Tuning

## When to read this

Read this when adding/removing/tuning governance checks.

## What you will do

- adjust check contracts safely
- maintain policy/traceability alignment

## Step-by-step

1. Add or update governance case.
2. Update check set and check prefix mapping if required.
3. Update policy and traceability links.
4. Validate with governance + critical-gate.

## Common failure signals

- new check ID not registered in check sets
- policy rule missing applies_to references
- inconsistent check semantics across docs and cases

## Normative refs

- `specs/04_governance/check_sets_v1.yaml`
- `specs/02_contracts/policy_v1.yaml`
- `specs/02_contracts/traceability_v1.yaml`
