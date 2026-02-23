# Guide 03: Running Checks and Gates

## When to read this

Read this when validating local changes before push.

## What you will do

- execute the canonical gate flow
- interpret artifacts and check IDs

## Step-by-step

1. Run governance.
2. Run critical-gate.
3. Run docs-generate-check.
4. Capture failing check IDs and map them to source files.

## Common failure signals

- check set references missing case IDs
- governance interface sync drift
- docs generation output mismatch

## Normative refs

- `specs/02_contracts/12_runner_interface.md`
- `specs/04_governance/check_sets_v1.yaml`
- `docs/book/90_reference_guide.md`
