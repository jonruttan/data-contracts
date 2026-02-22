# Chapter 65: Runner Status And Compatibility

```yaml doc-meta
doc_id: DOC-REF-165
title: Chapter 65 Runner Status And Compatibility
status: active
audience: maintainer
owns_tokens:
- status_exchange_lifecycle
requires_tokens:
- rust_required_lane
commands:
- run: ./scripts/runner_status_ingest.sh --max-age-hours 72 --enforce-freshness
  purpose: Ingest external runner status artifacts and enforce compatibility freshness.
examples:
- id: EX-RUNNER-STATUS-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Define how `data-contracts` ingests runner status from external repos and applies
policy effects without importing runner implementation logic.

## Inputs

- `/specs/01_schema/runner_status_report_v1.yaml`
- `/specs/01_schema/runner_status_matrix_v1.yaml`
- `/specs/01_schema/runner_certification_registry_v1.yaml`
- release assets from `dc-runner-rust`, `dc-runner-python`, `dc-runner-php`

## Outputs

- `/.artifacts/runner-status-matrix.json`
- `/.artifacts/runner-status-matrix.md`
- `/.artifacts/runner-status-ingest-log.json`

## Failure Modes

- missing release metadata for active runner lanes
- missing or invalid status report asset
- stale compatibility telemetry older than 72 hours
- checksum mismatch on status report artifact

## Freshness Semantics

- Rust lane remains merge-blocking by required-lane policy.
- Compatibility lanes are non-blocking for execution parity.
- Compatibility telemetry older than 72 hours is a governance policy failure.

## Incident Actions

1. Identify stale or missing lane in `runner-status-matrix.md`.
2. Inspect `runner-status-ingest-log.json` for fetch/shape/checksum errors.
3. Refresh runner release status asset in the owning `dc-runner-*` repository.
4. Re-run `./scripts/runner_status_ingest.sh --max-age-hours 72 --enforce-freshness`.

