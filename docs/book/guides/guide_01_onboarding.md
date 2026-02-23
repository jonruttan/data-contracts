# Guide 01: Onboarding

## When to read this

Read this to prepare your environment and run the first full validation cycle.

## What you will do

- run canonical required checks
- inspect emitted artifacts

## Step-by-step

1. Run `/Users/jon/Workspace/Development/data-contracts/scripts/runner_bin.sh governance`.
2. Run `/Users/jon/Workspace/Development/data-contracts/scripts/runner_bin.sh critical-gate`.
3. Run `/Users/jon/Workspace/Development/data-contracts/scripts/runner_bin.sh docs-generate-check`.
4. Inspect `.artifacts` summaries for status.

## Common failure signals

- command not found for runner adapter
- governance check ID failures
- docs/book manifest/index drift

## Normative refs

- `specs/02_contracts/12_runner_interface.md`
- `specs/04_governance/check_sets_v1.yaml`
