# Spec Runner

`spec_runner` is a contract-first executable spec system for Markdown-authored cases.
It discovers `yaml contract-spec` blocks in `*.spec.md`, validates schema/contract
shape, and executes typed harnesses through a stable runner interface.

The source of truth is split by role:

- `specs/`: executable specs, contracts, schema, governance
- `docs/`: author and operator documentation

## Status and Trust Model

This project is **pre-alpha** and changes quickly.

Trust model:

- `spec_runner` is **not a sandbox**.
- Specs are trusted inputs.
- Running untrusted specs is unsafe and out of scope for v1.

Reference contracts:

- `/Users/jon/Workspace/Development/spec_runner/specs/contract/08_v1_scope.md`
- `/Users/jon/Workspace/Development/spec_runner/specs/contract/04_harness.md`

## Quick Start (Rust Required Lane)

Setup:

```sh
make setup
```

Canonical local verification:

```sh
make verify-docs
make core-check
make check
```

Run the canonical required lane:

```sh
./runners/public/runner_adapter.sh --impl rust critical-gate
./runners/public/runner_adapter.sh --impl rust governance
./runners/public/runner_adapter.sh --impl rust docs-generate-check
```

## Required Local Pre-Push

Use the required local gate before pushing:

```sh
make prepush
```

Fast mode for local iteration:

```sh
make prepush-fast
```

Install managed hooks:

```sh
make hooks-install
```

Emergency bypass (only when necessary):

```sh
SPEC_PREPUSH_BYPASS=1 git push
```

## Compatibility Matrix (Non-Blocking)

Lane classes:

- `required`: rust
- `compatibility_non_blocking`: python, php, node, c

These compatibility lanes are non-blocking telemetry; merge blocking is Rust-first.

Contract reference:

- `/Users/jon/Workspace/Development/spec_runner/specs/contract/25_compatibility_matrix.md`

## Adoption Profiles

- Core profile: `make core-check`
- Full profile: `make check`

## Minimal Canonical Spec Example

```yaml contract-spec
id: EX-README-001
title: README canonical contract.check shape
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.make_commands_sync
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: violation_count}
      - 0
```

## Repository Entry Points

- Specs root: `/Users/jon/Workspace/Development/spec_runner/specs/`
- Book index: `/Users/jon/Workspace/Development/spec_runner/docs/book/index.md`
- Generated reference gateway: `/Users/jon/Workspace/Development/spec_runner/docs/book/99_generated_reference_index.md`
- Development workflows: `/Users/jon/Workspace/Development/spec_runner/docs/development.md`
- Schema: `/Users/jon/Workspace/Development/spec_runner/specs/schema/schema_v1.md`
- Contract index: `/Users/jon/Workspace/Development/spec_runner/specs/contract/index.md`

## Repo Layout

- `runners/`: runtime adapters and implementations
- `scripts/`: operational entrypoints for local/CI workflows
- `specs/`: executable specs and normative contracts
- `docs/`: narrative and generated documentation surfaces
- `tests/`: test suite
