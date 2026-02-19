# Development

## Purpose

This repository is developed as a control plane: specs, contracts, schemas, governance, docs, and status-ingest policy.

## Inputs

- changes under `specs/**`, `docs/**`, `.github/workflows/**`, `scripts/**`
- runner status release assets from runner repositories

## Outputs

- coherent contract/schema/docs surfaces
- governance and docs integrity verdicts
- compatibility/status matrix artifacts

## Failure Modes

- implementation-specific assumptions reintroduced into control-plane surfaces
- docs and contracts drifting out of sync
- status-ingest artifacts missing or stale

## Control-Plane Commands

Canonical status-ingest operation:

```sh
./scripts/runner_status_ingest.sh --max-age-hours 72 --enforce-freshness
```

Canonical local gate for this repository:

```sh
./scripts/ci_gate.sh
```

## Runtime Ownership Boundary

Runner execution ownership is external:
- `dc-runner-rust`
- `dc-runner-python`
- `dc-runner-php`

This repo governs interface and telemetry contracts; it does not own runner implementation execution.
