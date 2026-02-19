# Repository Ownership Matrix

## Canonical Repositories

- `data-contracts` (this repository)
- `dc-runner-rust` (required lane)
- `dc-runner-python` (compatibility lane, non-blocking)
- `dc-runner-php` (compatibility lane, non-blocking)

## Ownership Boundaries

### data-contracts
- Spec schema and language contracts under `specs/schema` and `specs/contract`
- Governance policy model and check-set declarations under `specs/governance`
- Narrative documentation under `docs/`
- Rust runner lock and resolver (`specs/schema/dc_runner_rust_lock_v1.yaml`, `scripts/runner_bin.sh`)
- Public required-lane adapter entrypoint (`runners/public/runner_adapter.sh`)

### dc-runner-rust
- Rust adapter and CLI implementation
- Rust-native runtime behavior checks and runner-internal certification execution
- Rust runner implementation-owned spec suites

### dc-runner-python
- Python runner implementation and compatibility-lane behavior
- Python implementation-owned spec suites and governance checks
- Python-specific docs and release artifacts

### dc-runner-php
- PHP runner implementation and compatibility-lane behavior
- PHP implementation-owned spec suites and governance checks
- PHP-specific docs and release artifacts

## Cross-Repo Reference Policy

- `data-contracts` must not reference runner-internal file paths in `dc-runner-*` repositories.
- Allowed references in `data-contracts`:
  - repo identifiers (`dc-runner-rust`, `dc-runner-python`, `dc-runner-php`)
  - release artifact metadata (URLs, checksums, version pins)
  - interface-level command contracts and lane classifications
