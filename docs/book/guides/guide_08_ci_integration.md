# Guide 08: CI Integration

## When to read this

Read this when mapping local commands to CI lanes.

## What you will do

- align local and CI gate behavior
- preserve deterministic outputs

## Step-by-step

1. Mirror local gate sequence in CI.
2. Ensure required artifacts are retained for debugging.
3. Keep CI using canonical command entrypoints.
4. Monitor lane-specific compatibility telemetry separately.

## Common failure signals

- CI command drift from local required flow
- artifacts missing from CI upload set
- compatibility lane failures treated as required-lane blockers

## Normative refs

- `specs/02_contracts/25_compatibility_matrix.md`
- `specs/02_contracts/12_runner_interface.md`
- `specs/02_contracts/27_runner_status_exchange.md`
