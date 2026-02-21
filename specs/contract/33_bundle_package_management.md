# Bundle Package Management Contract (v1)

Defines package-based bundle producer/consumer behavior for runner repositories.

## Purpose

- Replace snapshot-style spec sync workflows with bundle package pull + verify
  semantics.
- Keep package source immutable through release-asset URLs and checksums.
- Preserve deterministic runner-side materialization contracts.

## Producer Responsibilities (`data-contracts`)

- Publish bundle package release assets:
  - `data-contract-bundle-{bundle_id}-v{bundle_version}.tar.gz`
  - `data-contract-bundle-{bundle_id}-v{bundle_version}.tar.gz.sha256`
  - `data-contract-bundle-{bundle_id}-v{bundle_version}.tar.gz.intoto.json`
- Ensure package payload contains:
  - resolved filesystem tree
  - `resolved_bundle_lock_v1.yaml`
  - `resolved_files.sha256`
- Ensure package checksums are reproducible from published bytes.

## Consumer Responsibilities (Runner Repositories)

Runner repositories MUST pin one root bundle using
`/specs/schema/runner_bundle_lock_v1.yaml`.

Runner repositories MUST implement:

- `bundle-sync`: fetch release asset package URL, verify checksum, unpack
  package, and verify `resolved_bundle_lock_v1.yaml`.
- `bundle-sync-check`: re-verify package checksum, lock checksum, and
  materialized file manifest drift.

## Deterministic Resolution and Locking

- Bundle dependency resolution MUST be deterministic and hard-fail on cycles,
  missing dependencies, and conflicting file bytes.
- Resolved lock schema:
  `/specs/schema/resolved_bundle_lock_v1.yaml`
- Bundle manifest schema:
  `/specs/schema/bundle_manifest_v1.yaml`
- Runner lock schema:
  `/specs/schema/runner_bundle_lock_v1.yaml`

## Failure Behavior

Failure messages MUST be direct and actionable:

- missing release asset URL in runner lock
- missing or malformed checksum file
- checksum mismatch between package bytes and lock/checksum metadata
- missing `resolved_bundle_lock_v1.yaml` in unpacked package
- local materialization drift vs `resolved_files.sha256`

## Legacy Compatibility

- `scripts/contract-set` is a deprecated alias command.
- Runner task IDs `spec-sync` and `spec-sync-check` are not part of required
  build tool contract surface.
