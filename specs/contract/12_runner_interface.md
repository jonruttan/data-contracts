# Runner Interface Contract (v1)

Defines the language-neutral command boundary used by local gate scripts.

Execution classes:

- `default lane`: canonical adapter with rust mode
  (`runners/public/runner_adapter.sh` with `SPEC_RUNNER_IMPL=rust` default)
- `rust standalone lane`: Rust runner MUST execute on hosts without Python
  installed.

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
- `job-run`

CI expectation:

- CI default lane MUST run core gate through `runners/public/runner_adapter.sh`
  in rust mode.
- Local pre-push gate is Rust-only by default
  (`make prepush` / `scripts/local_ci_parity.sh`).
- Fast mode is Rust-only as well (`SPEC_PREPUSH_MODE=fast` or
  `make prepush-fast`).
- Repository-managed pre-push hook MUST invoke `make prepush` and block push
  on failure unless explicit emergency bypass is set (`SPEC_PREPUSH_BYPASS=1`).

## Default Adapter

Repository adapters:

- `runners/public/runner_adapter.sh` (single public entrypoint; rust default router)
- `runners/rust/runner_adapter.sh` (internal rust adapter; invokes Rust CLI)
- `runners/python/runner_adapter.sh` (internal adapter path)
- `runners/rust/spec_runner_cli` (Rust runner-interface CLI crate)

Rust adapters MUST NOT require Python process delegation for supported
subcommands.
Alternative implementations can replace the adapter by setting `SPEC_RUNNER_BIN`
to a different compatible command.

Runtime hard-cut:

- `runners/public/runner_adapter.sh --impl python ...` is forbidden and must hard-fail
  with migration guidance to Rust commands.

Rust adapter target behavior:

- preferred target may be selected by platform (for example
  `aarch64-apple-darwin` on Apple Silicon)
- when preferred target is unavailable locally, adapter MUST fallback to host
  target cargo execution by default
- strict mode is opt-in via `SPEC_RUNNER_RUST_TARGET_STRICT=1` and MUST hard-fail
  on missing preferred target

Adapter semantic contract:

- adapters MUST preserve assertion semantics from schema/contract docs
- universal `evaluate` core and sugar compile-only behavior are runner
  semantics, not adapter-specific policy

Job dispatch contract:

- `job-run` MUST accept scalar `--ref` in path+anchor form:
  - `/path/to/file.spec.md#CASE-ID`
  - `#CASE-ID` (same-document form; requires a document context)
- `job-run` MUST reject non-scalar or malformed refs with deterministic errors.
- Referenced case MUST resolve to `type: contract.job`.
- `contract.job` dispatch MUST be contract-driven via `ops.job.dispatch`.
- `contract.job` metadata MUST be declared under `harness.jobs.<name>`.
- non-canonical singular `harness.job` fields are forbidden.
- `ops.job.dispatch` MUST fail when capability `ops.job` is not declared.
- nested dispatch is forbidden and MUST emit deterministic token
  `runtime.dispatch.nested_forbidden`.
- `when` lifecycle hooks (`must|may|must_not|fail|complete`) are part of
  contract runtime semantics and MUST be honored in native evaluators.
- non-canonical `harness.on` is forbidden.
- class hooks run only after successful clause pass for matching class.
- `fail` runs once on first failure; `complete` runs after all clauses and
  class hooks pass.
- hook evaluation failures are fail-fast runtime errors.

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

Governance triage controls (prepush + ci-gate-summary governance step):

- `SPEC_GOV_TRIAGE_ENABLED` (`1|0`, default `1`)
- `SPEC_GOV_TRIAGE_MAX_RETRIES` (default `1`)
- `SPEC_GOV_TRIAGE_FALLBACK_PREFIXES` (default `docs.,normalization.,runtime.`)
- `SPEC_GOV_TRIAGE_PROFILE_LEVEL` (default `basic`)
- `SPEC_GOV_TRIAGE_MODE_DEFAULT` (`targeted-first|broad-first`, default `targeted-first`)
- `SPEC_GOV_TRIAGE_BROAD_ON_TARGETED_PASS` (`1|0`, default `0`)
- `SPEC_GOV_TRIAGE_REQUIRE_BROAD` (`1|0`, default `0` local prepush, required in CI merge gate)
- `SPEC_GOV_TRIAGE_STALL_TIMEOUT_SECONDS` (default `90`)

Governance triage entrypoint:

- `scripts/governance_triage.sh --mode auto|targeted|broad-first`
- targeted selection supports `--check-id`, `--check-prefix`, `--from-failures`
- auto mode is targeted-first by default and uses changed-path prefix selection before fallback prefixes
- CI gate must run targeted governance then mandatory broad governance before merge pass

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

## Docs Freshness Contract

- Canonical specs organization is enforced by `python3 -m spec_runner.spec_lang_commands check-docs-freshness --strict`.
- Local parity and CI gate must execute this check as a blocking step.
- Freshness checker output must be written to `.artifacts/docs-freshness-report.json`.
