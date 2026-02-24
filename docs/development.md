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
- review workflow outputs (prompt rendering + snapshots) are produced from `data-contracts-library` bundles and are not committed into this repository.

## Failure Modes

- implementation-specific assumptions reintroduced into control-plane surfaces
- docs and contracts drifting out of sync
- status-ingest artifacts missing or stale

## Control-Plane Commands

Canonical status-ingest operation:

```sh
dc-runner governance run
```

Canonical local gate for this repository:

```sh
dc-runner governance critical
```

Canonical bundle package operations:

```sh
/Users/jon/Workspace/Development/data-contracts-bundles/scripts/bundle resolve --runner rust --root runner_contract_bundle --out .artifacts/bundles/runner_contract_bundle --source-repo https://github.com/jonruttan/data-contracts-bundles.git --source-ref main
/Users/jon/Workspace/Development/data-contracts-bundles/scripts/bundle package --runner rust --root runner_contract_bundle --version 1.0.0 --out .artifacts/bundles --source-repo https://github.com/jonruttan/data-contracts-bundles.git --source-ref main
/Users/jon/Workspace/Development/data-contracts-bundles/scripts/bundle package-check --package .artifacts/bundles/data-contract-bundle-runner_contract_bundle-v1.0.0.tar.gz --sha256 .artifacts/bundles/data-contract-bundle-runner_contract_bundle-v1.0.0.tar.gz.sha256
/Users/jon/Workspace/Development/data-contracts-bundles/scripts/bundle install --project-lock bundles.lock.yaml --out .artifacts/installed-bundles
/Users/jon/Workspace/Development/data-contracts-bundles/scripts/bundle install-check --project-lock bundles.lock.yaml --out .artifacts/installed-bundles
/Users/jon/Workspace/Development/data-contracts-bundles/scripts/bundle list
/Users/jon/Workspace/Development/data-contracts-bundles/scripts/bundle info --bundle-id runner_contract_bundle
/Users/jon/Workspace/Development/data-contracts-bundles/scripts/bundle bootstrap --lock .artifacts/bundles/bundles.lock.yaml --out .bundles
/Users/jon/Workspace/Development/data-contracts-bundles/scripts/bundle outdated --project-lock bundles.lock.yaml --format json
/Users/jon/Workspace/Development/data-contracts-bundles/scripts/bundle upgrade --project-lock bundles.lock.yaml --dry-run
```

Portable runner bundle command surface:

```sh
dc-runner bundle list
dc-runner bundle info --bundle-id runner_contract_bundle
dc-runner bundle install --project-lock bundles.lock.yaml --out .artifacts/installed-bundles
dc-runner bundle install-check --project-lock bundles.lock.yaml --out .artifacts/installed-bundles
dc-runner bundle bootstrap --lock .artifacts/bundles/bundles.lock.yaml --out .bundles
dc-runner bundle bootstrap-check --lock .artifacts/bundles/bundles.lock.yaml --out .bundles
dc-runner bundle outdated --project-lock bundles.lock.yaml --format json
dc-runner bundle upgrade --project-lock bundles.lock.yaml --dry-run
dc-runner bundle run --bundle-id data-contracts-lang-project-scaffold --bundle-version 1.0.0 --entrypoint scaffold
dc-runner bundle scaffold --project-root /tmp/example --bundle-id data-contracts-lang-project-scaffold --bundle-version 1.0.0
```

Project lock guidance:

- Use root `bundles.lock.yaml` with multiple `bundles[]` entries.
- Keep the base runner contract bundle as `role: primary`.
- Add implementation-specific bundles from `dc-runner-*-specs` as
  `role: additional`.
- Keep each bundle install isolated via unique, non-overlapping `install_dir`.

Canonical runner-ingestible pack manifests:

- `/Users/jon/Workspace/Development/data-contracts/specs/00_core/packs/runner_contract_pack_v1.yaml`
- `/Users/jon/Workspace/Development/data-contracts/specs/00_core/packs/spec_core_maintenance_pack_v1.yaml`
- `/Users/jon/Workspace/Development/data-contracts/specs/00_core/packs/project_docs_maintenance_pack_v1.yaml`

## Runtime Ownership Boundary

Runner execution ownership is external:
- `dc-runner-rust`
- `dc-runner-python`
- `dc-runner-php`

This repo governs interface and telemetry contracts; it does not own runner implementation execution.
