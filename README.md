# Data Contracts

`data-contracts` is the implementation-agnostic control plane for the Data Contracts ecosystem.
runtime execution ownership lives in runner repositories.

It defines and governs:
- canonical specs, contracts, and schemas
- documentation and reader-facing guidance
- compatibility/status telemetry ingestion and policy evaluation

It does **not** own runner implementation code and does **not** execute runtime lanes as canonical project behavior.
This repository does not execute runtime lanes.

## What This Project Is

- Source of truth for contract semantics and schema shape.
- Source of truth for docs quality, information architecture, and governance checks.
- Consumer of runner release telemetry via status exchange artifacts.
- Policy source: executable spec-lang governance cases.
- Policy composition: chained spec cases (`harness.chain`) with reusable policy-library exports.

## What This Project Is Not

- Not a runtime implementation repository.
- Not a required-lane executor.
- Not the owner of runner internals (`dc-runner-rust`, `dc-runner-python`, `dc-runner-php`).

## How Users Use This Project

### 1) Author a spec change
- Start with `/Users/jon/Workspace/Development/data-contracts/docs/book/index.md`
- Use task guides at `/Users/jon/Workspace/Development/data-contracts/docs/book/35_usage_guides_index.md`
- Validate contract and schema intent under `/Users/jon/Workspace/Development/data-contracts/specs/contract/index.md`

### 2) Validate docs and contract coherence
- Run control-plane checks through CI and governance surfaces in this repo.
- Use `/Users/jon/Workspace/Development/data-contracts/docs/book/90_reference_guide.md` for narrative-to-normative mapping.

### 3) Read compatibility and status telemetry
- See `/Users/jon/Workspace/Development/data-contracts/docs/book/65_runner_status_and_compatibility.md`
- Inspect generated ingest artifacts under `/.artifacts/runner-status-*`

### 4) Debug governance or documentation drift
- Use troubleshooting and governance chapters in the docs book.
- Inspect generated governance/docs summary artifacts from CI.

## Canonical Entry Points

- Book index: `/Users/jon/Workspace/Development/data-contracts/docs/book/index.md`
- Usage guides index: `/Users/jon/Workspace/Development/data-contracts/docs/book/35_usage_guides_index.md`
- Status exchange and compatibility: `/Users/jon/Workspace/Development/data-contracts/docs/book/65_runner_status_and_compatibility.md`
- Contract index: `/Users/jon/Workspace/Development/data-contracts/specs/contract/index.md`
- Policy execution boundary: `/Users/jon/Workspace/Development/data-contracts/specs/contract/28_spec_lang_policy_execution.md`

## Runner Test Packs

- `/Users/jon/Workspace/Development/data-contracts/specs/packs/runner_contract_pack_v1.yaml`
- `/Users/jon/Workspace/Development/data-contracts/specs/packs/spec_core_maintenance_pack_v1.yaml`
- `/Users/jon/Workspace/Development/data-contracts/specs/packs/project_docs_maintenance_pack_v1.yaml`

## Portable CLI Contract

- `/Users/jon/Workspace/Development/data-contracts/specs/contract/29_runner_cli_interface.md`
- `/Users/jon/Workspace/Development/data-contracts/specs/schema/runner_cli_contract_v1.yaml`

## Bundle Resolver and Package Tooling

- Canonical librarian repo: [`jonruttan/data-contracts-bundles`](https://github.com/jonruttan/data-contracts-bundles)
- Resolve: `/Users/jon/Workspace/Development/data-contracts/scripts/bundle resolve --runner <runner> --root <bundle_id> --out <dir> --source-repo https://github.com/jonruttan/data-contracts-bundles.git --source-ref main`
- Package: `/Users/jon/Workspace/Development/data-contracts/scripts/bundle package --runner <runner> --root <bundle_id> --version <bundle_version> --out <dir> --source-repo https://github.com/jonruttan/data-contracts-bundles.git --source-ref main`
- Verify package: `/Users/jon/Workspace/Development/data-contracts/scripts/bundle package-check --package <path> --sha256 <path>`
- Install bundles: `/Users/jon/Workspace/Development/data-contracts/scripts/bundle install --project-lock bundles.lock.yaml --out <workspace>`
- Verify install: `/Users/jon/Workspace/Development/data-contracts/scripts/bundle install-check --project-lock bundles.lock.yaml --out <workspace>`
- Manifest schema: `/Users/jon/Workspace/Development/data-contracts/specs/schema/bundle_manifest_v1.yaml`
- Resolved lock schema: `/Users/jon/Workspace/Development/data-contracts/specs/schema/resolved_bundle_lock_v1.yaml`
- Project lock schema: `/Users/jon/Workspace/Development/data-contracts/specs/schema/project_bundle_lock_v1.yaml`
- Legacy runner lock schema (deprecated): `/Users/jon/Workspace/Development/data-contracts/specs/schema/runner_bundle_lock_v1.yaml`
- Implementation overlay schema: `/Users/jon/Workspace/Development/data-contracts/specs/schema/implementation_bundle_overlay_v1.yaml`
- Implementation build lock schema: `/Users/jon/Workspace/Development/data-contracts/specs/schema/implementation_bundle_build_lock_v1.yaml`
- Implementation overlay contract: `/Users/jon/Workspace/Development/data-contracts/specs/contract/34_runner_implementation_spec_bundles.md`
- Implementation spec bundle repos:
  - [`jonruttan/dc-runner-rust-specs`](https://github.com/jonruttan/dc-runner-rust-specs)
  - [`jonruttan/dc-runner-python-specs`](https://github.com/jonruttan/dc-runner-python-specs)
  - [`jonruttan/dc-runner-php-specs`](https://github.com/jonruttan/dc-runner-php-specs)
- `bundles.lock.yaml` supports multi-bundle entries using `role: primary|additional` with isolated non-overlapping `install_dir` per bundle.

Legacy alias:

- `/Users/jon/Workspace/Development/data-contracts/scripts/contract-set` is deprecated and forwards to `scripts/bundle`.

## Core Script Allowlist

- `/Users/jon/Workspace/Development/data-contracts/scripts/bundle`
- `/Users/jon/Workspace/Development/data-contracts/scripts/contract-set`
- `/Users/jon/Workspace/Development/data-contracts/scripts/control_plane.sh`
- `/Users/jon/Workspace/Development/data-contracts/scripts/ci_gate.sh`
- `/Users/jon/Workspace/Development/data-contracts/scripts/runner_status_ingest.sh`
- `/Users/jon/Workspace/Development/data-contracts/scripts/runner_bin.sh`
- `/Users/jon/Workspace/Development/data-contracts/scripts/governance_catalog_validate.sh`
- `/Users/jon/Workspace/Development/data-contracts/scripts/spec_schema_pin_validate.sh`
- `/Users/jon/Workspace/Development/data-contracts/scripts/governance_optional_report.sh`
- `/Users/jon/Workspace/Development/data-contracts/scripts/governance_triage.sh`
