# Development

## Purpose

This repository is developed as a control plane: specs, contracts, schemas, governance, docs, and status-ingest policy.
This repository is an implementation-agnostic control plane.
runtime execution ownership lives in runner repositories.

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

Canonical bundle package operations:

```sh
./scripts/bundle resolve --runner rust --root runner_contract_bundle --out .artifacts/bundles/runner_contract_bundle
./scripts/bundle package --runner rust --root runner_contract_bundle --version 1.0.0 --out .artifacts/bundles
./scripts/bundle package-check --package .artifacts/bundles/data-contract-bundle-runner_contract_bundle-v1.0.0.tar.gz --sha256 .artifacts/bundles/data-contract-bundle-runner_contract_bundle-v1.0.0.tar.gz.sha256
```

Canonical runner-ingestible pack manifests:

- `/Users/jon/Workspace/Development/data-contracts/specs/packs/runner_contract_pack_v1.yaml`
- `/Users/jon/Workspace/Development/data-contracts/specs/packs/spec_core_maintenance_pack_v1.yaml`
- `/Users/jon/Workspace/Development/data-contracts/specs/packs/project_docs_maintenance_pack_v1.yaml`

## Runtime Ownership Boundary

Runner execution ownership is external:
- `dc-runner-rust`
- `dc-runner-python`
- `dc-runner-php`

This repo governs interface and telemetry contracts; it does not own runner implementation execution.
