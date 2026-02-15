# Runner Interface Contract (v1)

Defines the language-neutral command boundary used by local gate scripts.

## Required Interface

Gate orchestration SHOULD invoke a runner command boundary via `SPEC_RUNNER_BIN`
instead of calling implementation-specific Python script paths directly.

Required subcommands:

- `governance`
- `style-check`
- `lint`
- `typecheck`
- `compilecheck`
- `conformance-purpose-json`
- `conformance-purpose-md`
- `conformance-parity`
- `test-core`
- `test-full`

CI expectation:

- CI MUST exercise at least one non-default adapter lane via `SPEC_RUNNER_BIN`
  (currently `scripts/rust/runner_adapter.sh`) using core gate commands.

## Default Adapter

Repository default adapter:

- `scripts/runner_adapter.sh`
- `scripts/rust/runner_adapter.sh` (Rust lane adapter; invokes Rust CLI)
- `scripts/rust/spec_runner_cli` (Rust runner-interface CLI crate)

Adapters may call implementation-specific scripts/tools internally.
Alternative implementations can replace the adapter by setting `SPEC_RUNNER_BIN`
to a different compatible command.

Adapter semantic contract:

- adapters MUST preserve assertion semantics from schema/contract docs
- universal `evaluate` core and sugar compile-only behavior are runner
  semantics, not adapter-specific policy

Runtime scope note:

- required support targets in v1 remain Python runner and PHP runner
- adding required support targets requires contract/governance expansion

## Compatibility Expectation

- Runner interface subcommand names are contributor-facing operational contract.
- Gate scripts (`ci_gate.sh`, `core_gate.sh`, `docs_doctor.sh`) SHOULD remain
  implementation-neutral and call the runner interface boundary.
