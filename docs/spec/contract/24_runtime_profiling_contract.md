# 24 Runtime Profiling Contract

## Scope

- Defines the canonical runtime profiling artifact for timeout diagnosis.
- Applies to Python and Rust runner implementations.
- Profiling is opt-in and disabled by default.

## Activation

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

## Artifact

- Schema: `/docs/spec/schema/run_trace_v1.yaml`
- JSON artifact: `/.artifacts/run-trace.json`
- Summary artifact: `/.artifacts/run-trace-summary.md`

Required top-level fields:

- `version`, `run_id`, `runner_impl`, `started_at`, `ended_at`, `status`
- `command`, `args`, `env_profile`
- `spans`, `events`, `summary`

## Required Span Taxonomy

- `run.total`
- `runner.dispatch`
- `case.run`
- `case.chain`
- `case.harness`
- `check.execute`
- `subprocess.exec`
- `subprocess.wait`

## Required Event Kinds

- `heartbeat`
- `stall_warning`
- `watchdog`
- `subprocess_state`
- `checkpoint`

## Timeout Reason Tokens

- `timeout.subprocess.wait`
- `timeout.subprocess.io_drain`
- `timeout.case.harness`
- `timeout.case.chain`

## Redaction

- Profiling artifacts MUST NOT expose raw secret values.
- Secret-like keys (`token`, `secret`, `password`, `authorization`, `cookie`, `key`) MUST be redacted.
- `env_profile` may include metadata (set/length/hash) but not raw values.

