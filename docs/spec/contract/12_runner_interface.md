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

## Default Adapter

Repository default adapter:

- `scripts/runner_adapter.sh`

The default adapter may call Python implementation scripts internally.
Alternative implementations can replace it by setting `SPEC_RUNNER_BIN` to a
different compatible command.

## Compatibility Expectation

- Runner interface subcommand names are contributor-facing operational contract.
- Gate scripts (`ci_gate.sh`, `core_gate.sh`, `docs_doctor.sh`) SHOULD remain
  implementation-neutral and call the runner interface boundary.
