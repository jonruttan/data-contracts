# Runner Status and Compatibility

## When to read this

Read this when working with compatibility telemetry and status ingestion.

## What you will do

- Understand required lane vs compatibility lane status handling.
- Validate status matrix/report artifacts.

## Step-by-step

1. Generate runner status artifacts via canonical runner command paths.
2. Validate freshness and compatibility signals.
3. Review matrix and ingest logs for drift.

## Common failure signals

- Missing status artifacts.
- Freshness windows exceeded.
- Inconsistent runner ID/reference metadata.

## Normative refs

- `specs/02_contracts/25_compatibility_matrix.md`
- `specs/02_contracts/27_runner_status_exchange.md`
- `specs/01_schema/runner_status_matrix_v1.yaml`
