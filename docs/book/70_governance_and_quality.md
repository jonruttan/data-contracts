# Governance and Quality

## When to read this

Read this when tuning checks, policy mappings, and documentation quality controls.

## What you will do

- Keep policy, traceability, and checks synchronized.
- Use governance cases as enforcement surfaces.

## Step-by-step

1. Add or modify policy rules in `policy_v1.yaml`.
2. Update traceability mappings.
3. Add/adjust governance executable cases.
4. Run required gate sequence and resolve drift.

## Common failure signals

- Policy rule exists without traceability link.
- Check IDs in sets lack executable case coverage.
- Docs chapter references drift from manifest/index.

## Normative refs

- `specs/02_contracts/policy_v1.yaml`
- `specs/02_contracts/traceability_v1.yaml`
- `specs/04_governance/`
