# Rust-Primary Transition Contract (v1)

Defines the contract for operating this repository with a Rust-primary runner
path while preserving schema/contract behavior guarantees.

## Intent

- Rust adapter is the primary operational runner boundary.
- Python/PHP implementations remain supported for compatibility and parity.
- Gate/policy behavior remains implementation-neutral and deterministic.

## Required Rust-Primary Guarantees

1. CI Rust-primary gate path
- CI MUST exercise core gate commands through the Rust adapter path
  (`SPEC_RUNNER_BIN=./scripts/rust/runner_adapter.sh`).

2. No Python-hardcoded gate dependency
- Gate scripts MUST use runner-interface boundaries instead of direct Python
  script entrypoints.

3. Runner-interface stability under Rust primary
- Required runner-interface subcommands and exit-code contracts MUST remain
  stable when Rust is selected as the primary adapter.

4. Shared-capability parity
- Shared-capability conformance behavior MUST remain parity-checked across
  implementations.

5. Adapter executable smoke
- Governance MUST include an executable Rust-adapter smoke check that validates
  deterministic command behavior (exit code and output tokens).

6. Adapter/CLI subcommand parity
- Governance MUST enforce parity between subcommands exposed by the shell
  adapter and those handled by the Rust CLI implementation.

## Adoption and Scope

- Contributor docs SHOULD describe Rust-primary operation as the default
  interface path while preserving compatibility notes for Python/PHP lanes.
- Adding/removing required runtime support targets is governed by:
  - `docs/spec/contract/08_v1_scope.md`
  - `docs/spec/contract/13_runtime_scope.md`

## Non-Goals

- This contract does not remove Python/PHP implementations.
- This contract does not alter assertion/schema semantics.
