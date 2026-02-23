# Guide 09: Status Exchange Operations

## When to read this

Read this when operating or debugging status matrix ingestion.

## What you will do

- verify matrix/report artifact production
- validate freshness and compatibility state

## Step-by-step

1. Execute status exchange flow via runner command surface.
2. Verify matrix/report/log artifacts exist and parse.
3. Check freshness windows and policy effect fields.
4. Investigate stale/missing rows by runner ID.

## Common failure signals

- missing matrix artifacts
- malformed command result rows
- stale freshness windows

## Normative refs

- `specs/02_contracts/27_runner_status_exchange.md`
- `specs/01_schema/runner_status_report_v1.yaml`
- `specs/01_schema/runner_status_matrix_v1.yaml`
