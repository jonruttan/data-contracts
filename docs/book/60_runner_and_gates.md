# Runner and Gates

## When to read this

Read this when operating required checks and understanding runner responsibilities.

## What you will do

- Use canonical gate commands.
- Interpret governance/critical/docs outcomes.

## Step-by-step

1. Execute governance.
2. Execute critical-gate.
3. Execute docs-generate-check.
4. Inspect `.artifacts` summaries for failures.

## Common failure signals

- Wrapper scripts containing semantic policy logic.
- Missing governance interface synchronization.
- Check IDs referenced but not resolved by active cases.

## Normative refs

- `specs/02_contracts/12_runner_interface.md`
- `specs/02_contracts/29_runner_cli_interface.md`
- `specs/04_governance/check_sets_v1.yaml`
