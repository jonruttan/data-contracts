# Runner Interface Contract (v1)

Defines the language-neutral command boundary used by local gate scripts.

Execution classes:

- `default lane`: canonical adapter with rust mode
  (`scripts/runner_adapter.sh` with `SPEC_RUNNER_IMPL=rust` default)
- `python runner lane`: explicit opt-in mode through the same adapter
  (`scripts/runner_adapter.sh --impl python` or `SPEC_RUNNER_IMPL=python`)

## Required Interface

Gate orchestration MUST invoke a runner command boundary via `SPEC_RUNNER_BIN`
instead of calling implementation-specific Python script paths directly.

Required subcommands:

- `governance`
- `style-check`
- `lint`
- `typecheck`
- `compilecheck`
- `conformance-purpose-json`
- `conformance-purpose-md`
- `runner-independence-json`
- `runner-independence-md`
- `python-dependency-json`
- `python-dependency-md`
- `ci-gate-summary`
- `docs-generate`
- `docs-generate-check`
- `conformance-parity`
- `test-core`
- `test-full`

CI expectation:

- CI default lane MUST run core gate through `scripts/runner_adapter.sh`
  in rust mode.
- Python lane is explicit opt-in and is not required in every merge-gate run.

## Default Adapter

Repository adapters:

- `scripts/runner_adapter.sh` (single public entrypoint; rust default router)
- `scripts/rust/runner_adapter.sh` (internal rust adapter; invokes Rust CLI)
- `scripts/python/runner_adapter.sh` (internal python adapter)
- `scripts/rust/spec_runner_cli` (Rust runner-interface CLI crate)

Adapters may call implementation-specific scripts/tools internally.
Alternative implementations can replace the adapter by setting `SPEC_RUNNER_BIN`
to a different compatible command.

Adapter semantic contract:

- adapters MUST preserve assertion semantics from schema/contract docs
- universal `evaluate` core and sugar compile-only behavior are runner
  semantics, not adapter-specific policy

Profiling controls (opt-in; all adapters):

- `--profile-level off|basic|detailed|debug` (default `off`)
- `--profile-out <path>` (default `/.artifacts/run-trace.json`)
- `--profile-summary-out <path>` (default `/.artifacts/run-trace-summary.md`)
- `--profile-heartbeat-ms <int>` (default `1000`)
- `--profile-stall-threshold-ms <int>` (default `10000`)

Environment equivalents:

- `SPEC_RUNNER_PROFILE_LEVEL`
- `SPEC_RUNNER_PROFILE_OUT`
- `SPEC_RUNNER_PROFILE_SUMMARY_OUT`
- `SPEC_RUNNER_PROFILE_HEARTBEAT_MS`
- `SPEC_RUNNER_PROFILE_STALL_THRESHOLD_MS`

Gate fail-fast controls (`ci-gate-summary`):

- `--fail-fast` (default `true`)
- `--continue-on-fail` (sets fail-fast false)
- `--profile-on-fail off|basic|detailed` (default `basic`)

Environment equivalents:

- `SPEC_RUNNER_FAIL_FAST`
- `SPEC_RUNNER_PROFILE_ON_FAIL`

Liveness controls (governance-first):

- `--liveness-level off|basic|strict`
- `--liveness-stall-ms <int>`
- `--liveness-min-events <int>`
- `--liveness-hard-cap-ms <int>`
- `--liveness-kill-grace-ms <int>`

Environment equivalents:

- `SPEC_RUNNER_LIVENESS_LEVEL`
- `SPEC_RUNNER_LIVENESS_STALL_MS`
- `SPEC_RUNNER_LIVENESS_MIN_EVENTS`
- `SPEC_RUNNER_LIVENESS_HARD_CAP_MS`
- `SPEC_RUNNER_LIVENESS_KILL_GRACE_MS`

Runtime scope note:

- required support targets in v1 remain Python runner and PHP runner
- adding required support targets requires contract/governance expansion

## Compatibility Expectation

- Runner interface subcommand names are contributor-facing operational contract.
- Gate scripts (`ci_gate.sh`, `core_gate.sh`, `docs_doctor.sh`) MUST remain
  implementation-neutral and call the runner interface boundary.
