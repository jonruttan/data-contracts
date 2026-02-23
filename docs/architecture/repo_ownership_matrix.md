# Repository Ownership Matrix

## Canonical Repositories

- `data-contracts` (this repository)
- `dc-runner-rust` (runtime owner)
- `dc-runner-python` (compatibility lane, non-blocking)
- `dc-runner-php` (compatibility lane, non-blocking)

## Ownership Boundaries

### data-contracts
- Spec schema and language contracts under `specs/01_schema` and `specs/02_contracts`
- Governance policy model and check-set declarations under `specs/04_governance`
- Narrative documentation under `docs/`
- Rust runner lock and resolver (`specs/01_schema/dc_runner_rust_lock_v1.yaml`, `dc-runner`)
- Public compatibility adapter entrypoint (`dc-runner`)

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

## Status Exchange Data Flow

| Producer Repo | Produced Artifact | Consumer | Policy Role |
|---|---|---|---|
| `dc-runner-rust` | `runner-status-report-v1.json` release asset | `data-contracts` (`scripts/runner_status_ingest.sh`) | blocking-class status input |
| `dc-runner-python` | `runner-status-report-v1.json` release asset | `data-contracts` (`scripts/runner_status_ingest.sh`) | compatibility freshness input |
| `dc-runner-php` | `runner-status-report-v1.json` release asset | `data-contracts` (`scripts/runner_status_ingest.sh`) | compatibility freshness input |

Ingest outputs are emitted as:

- `/.artifacts/runner-status-matrix.json`
- `/.artifacts/runner-status-matrix.md`
- `/.artifacts/runner-status-ingest-log.json`
