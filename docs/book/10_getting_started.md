# Getting Started

## When to read this

Read this when setting up a local workspace and running canonical checks the first time.

## What you will do

- Run the required governance flow.
- Understand expected artifacts and pass/fail behavior.

## Step-by-step

1. Run `/Users/jon/Workspace/Development/data-contracts/dc-runner governance`.
2. Run `/Users/jon/Workspace/Development/data-contracts/dc-runner critical-gate`.
3. Run `/Users/jon/Workspace/Development/data-contracts/dc-runner docs-generate-check`.
4. Use `.artifacts/*` summaries to diagnose failures.

## Common failure signals

- Missing required docs/governance assets.
- Manifest/index drift in docs/book.
- Schema/reference token mismatches in contract docs.

## Normative refs

- `specs/02_contracts/12_runner_interface.md`
- `specs/02_contracts/10_docs_quality.md`
- `specs/04_governance/check_sets_v1.yaml`
