# Development

## Toolchain

`data-contracts` is Rust + shell only.

Required local tools:

- `cargo`
- `php` with `yaml` extension
- `bash`

Quick setup check:

```sh
make setup
```

## Canonical Commands

Required lane (Rust) commands:

```sh
./runners/public/runner_adapter.sh --impl rust critical-gate
./runners/public/runner_adapter.sh --impl rust governance
./runners/public/runner_adapter.sh --impl rust docs-generate-check
```

Common local flows:

```sh
make verify-docs
make core-check
make check
make prepush
make prepush-fast
make ci-cleanroom
```

## Migration Utilities (Rust-backed)

Stable shell entrypoints:

```sh
./scripts/migrate_case_domain_prefix_v1.sh --check specs
./scripts/migrate_case_doc_metadata_v1.sh --check specs
./scripts/migrate_contract_step_imports_v1.sh --check specs
./scripts/migrate_library_docs_metadata_v1.sh --check specs/libraries
```

Write mode:

```sh
./scripts/migrate_case_domain_prefix_v1.sh --write specs
./scripts/migrate_case_doc_metadata_v1.sh --write specs
./scripts/migrate_contract_step_imports_v1.sh --write specs
./scripts/migrate_library_docs_metadata_v1.sh --write specs/libraries
```

Exit semantics are stable:

- `0`: clean/success
- `1`: drift/functional failure
- `2`: invalid usage/config

## CI and Triage

Run full gate locally:

```sh
./scripts/ci_gate.sh
```

Governance triage artifacts:

- `/.artifacts/governance-triage.json`
- `/.artifacts/governance-triage-summary.md`

Generate them directly:

```sh
./scripts/governance_triage.sh --mode auto --impl rust
```

## Compatibility Lanes

Compatibility lanes are external-only and non-blocking in this repo:

- `dc-runner-python`
- `dc-runner-php`
- `node` (planned)
- `c` (planned)

`data-contracts` does not execute compatibility lanes directly.
