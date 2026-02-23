# Guide 04: Debugging Failures

## When to read this

Read this when a gate reports violations and you need fast root-cause isolation.

## What you will do

- classify failure type
- apply minimal corrective changes

## Step-by-step

1. Read failing check ID and summary artifact.
2. Locate corresponding governance case and policy rule.
3. Fix source-of-truth file (schema/contract/manifest), not derived output.
4. Re-run affected checks and then full required flow.

## Common failure signals

- fixing symptoms in generated docs only
- editing unrelated files before reproducing failure
- mismatch between policy and traceability updates

## Normative refs

- `specs/02_contracts/15_governance_subject_model.md`
- `specs/02_contracts/policy_v1.yaml`
- `specs/02_contracts/traceability_v1.yaml`
