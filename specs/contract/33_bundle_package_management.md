# Bundle Package Management Contract (v1)

Defines package-based bundle producer/consumer behavior for runner repositories
and projects installing multiple bundles.

## Purpose

- Replace snapshot-style spec sync workflows with bundle package pull + verify
  semantics.
- Keep package source immutable through release-asset URLs and checksums.
- Preserve deterministic runner-side materialization contracts.

## Canonical Librarian Repository

Canonical bundle manifests and release assets are owned by:

- `https://github.com/jonruttan/data-contracts-bundles`

`data-contracts` defines contracts and schemas for bundle behavior but is not
the canonical manifest source.

## Producer Responsibilities (`data-contracts-bundles`)

- Publish bundle package release assets:
  - `data-contract-bundle-{bundle_id}-v{bundle_version}.tar.gz`
  - `data-contract-bundle-{bundle_id}-v{bundle_version}.tar.gz.sha256`
  - `data-contract-bundle-{bundle_id}-v{bundle_version}.tar.gz.intoto.json`
- Ensure package payload contains:
  - resolved filesystem tree
  - `resolved_bundle_lock_v1.yaml`
  - `resolved_files.sha256`
- Ensure package checksums are reproducible from published bytes.

## Consumer Responsibilities (Projects and Runner Repositories)

Projects MUST pin bundle installs in root `bundles.lock.yaml` using:

- `/specs/schema/project_bundle_lock_v1.yaml`

Installers and runner wrappers MUST implement:

- `bundle-sync` / `install`: fetch package URLs, verify checksums, unpack each
  bundle into dedicated install directories, and verify
  `resolved_bundle_lock_v1.yaml`.
- `bundle-sync-check` / `install-check`: re-verify package checksums and
  materialized file manifest drift.

Multiple bundle entries are supported and MUST be install-isolated.
Install directory overlap is forbidden.

## Deterministic Resolution and Locking

- Bundle dependency resolution MUST be deterministic and hard-fail on cycles,
  missing dependencies, and conflicting file bytes.
- Resolved lock schema:
  `/specs/schema/resolved_bundle_lock_v1.yaml`
- Bundle manifest schema:
  `/specs/schema/bundle_manifest_v1.yaml`
- Project lock schema:
  `/specs/schema/project_bundle_lock_v1.yaml`
- Runner lock schema:
  `/specs/schema/runner_bundle_lock_v1.yaml`

`runner_bundle_lock_v1` is deprecated and retained only for migration
compatibility.

## Failure Behavior

Failure messages MUST be direct and actionable:

- missing release asset URL in runner lock
- missing root `bundles.lock.yaml` project lock
- duplicate bundle lock entries
- overlapping bundle install directories
- missing or malformed checksum file
- checksum mismatch between package bytes and lock/checksum metadata
- missing `resolved_bundle_lock_v1.yaml` in unpacked package
- local materialization drift vs `resolved_files.sha256`

## Legacy Compatibility

- `scripts/contract-set` is a deprecated alias command.
- canonical bundle manifests are no longer sourced from local
  `/specs/bundles/*.yaml` in this repository.
- Runner task IDs `spec-sync` and `spec-sync-check` are not part of required
  build tool contract surface.
