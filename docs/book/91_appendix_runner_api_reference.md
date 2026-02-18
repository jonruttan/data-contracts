# Runner API Reference

```yaml doc-meta
doc_id: DOC-REF-091
title: Appendix Runner API Reference
status: active
audience: reviewer
owns_tokens:
- appendix_runner_api_reference
requires_tokens:
- trusted_inputs_required
commands:
- run: ./runners/public/runner_adapter.sh docs-generate-check
  purpose: Verify generated runner API surface is in sync.
examples:
- id: EX-APP-RUNNER-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

Machine-generated runner command catalog.

## Purpose

Provide generated command-surface documentation for the canonical runner interface.

## Inputs

- runner adapter scripts and rust CLI command registrations

## Outputs

- deterministic command parity table across implementations

## Failure Modes

- stale generated block when command surfaces change
- missing generated markers
- catalog/parity drift

<!-- GENERATED:START runner_api_catalog -->

## Generated Runner API Catalog

- command_count: 74
- python_command_count: 0
- rust_command_count: 74
- parity_command_count: 0
- all_commands_parity: false
- doc_quality_score: 0.6

| command | group | python | rust | parity |
|---|---|---|---|---|
| `--changed-only` | `reporting` | false | true | false |
| `--doc` | `reporting` | false | true | false |
| `--expr-file` | `reporting` | false | true | false |
| `--expr-json` | `metrics` | false | true | false |
| `--input` | `reporting` | false | true | false |
| `--liveness-hard-cap-ms` | `reporting` | false | true | false |
| `--liveness-kill-grace-ms` | `reporting` | false | true | false |
| `--liveness-level` | `reporting` | false | true | false |
| `--liveness-min-events` | `reporting` | false | true | false |
| `--liveness-stall-ms` | `reporting` | false | true | false |
| `--path` | `reporting` | false | true | false |
| `--paths` | `reporting` | false | true | false |
| `--profile-heartbeat-ms` | `reporting` | false | true | false |
| `--profile-level` | `reporting` | false | true | false |
| `--profile-out` | `reporting` | false | true | false |
| `--profile-stall-threshold-ms` | `reporting` | false | true | false |
| `--profile-summary-out` | `reporting` | false | true | false |
| `--ref` | `reporting` | false | true | false |
| `--subject-file` | `reporting` | false | true | false |
| `--subject-json` | `metrics` | false | true | false |
| `-v` | `reporting` | false | true | false |
| `-vv` | `reporting` | false | true | false |
| `-vvv` | `reporting` | false | true | false |
| `ci-cleanroom` | `ci` | false | true | false |
| `ci-gate-summary` | `ci` | false | true | false |
| `compilecheck` | `reporting` | false | true | false |
| `conformance-parity` | `reporting` | false | true | false |
| `conformance-purpose-json` | `metrics` | false | true | false |
| `conformance-purpose-md` | `metrics` | false | true | false |
| `contract-assertions-json` | `metrics` | false | true | false |
| `contract-assertions-md` | `metrics` | false | true | false |
| `critical-gate` | `reporting` | false | true | false |
| `docs-build` | `docs` | false | true | false |
| `docs-build-check` | `docs` | false | true | false |
| `docs-generate` | `docs` | false | true | false |
| `docs-generate-check` | `docs` | false | true | false |
| `docs-graph` | `docs` | false | true | false |
| `docs-lint` | `docs` | false | true | false |
| `docs-operability-json` | `docs` | false | true | false |
| `docs-operability-md` | `docs` | false | true | false |
| `governance` | `verification` | false | true | false |
| `governance-broad-native` | `reporting` | false | true | false |
| `governance-heavy` | `reporting` | false | true | false |
| `job-run` | `reporting` | false | true | false |
| `lint` | `verification` | false | true | false |
| `meta_json` | `reporting` | false | true | false |
| `normalize-check` | `verification` | false | true | false |
| `normalize-fix` | `verification` | false | true | false |
| `objective-scorecard-json` | `metrics` | false | true | false |
| `objective-scorecard-md` | `metrics` | false | true | false |
| `perf-smoke` | `reporting` | false | true | false |
| `python-dependency-json` | `metrics` | false | true | false |
| `python-dependency-md` | `metrics` | false | true | false |
| `runner-independence-json` | `metrics` | false | true | false |
| `runner-independence-md` | `metrics` | false | true | false |
| `schema-docs-build` | `docs` | false | true | false |
| `schema-docs-check` | `docs` | false | true | false |
| `schema-registry-build` | `docs` | false | true | false |
| `schema-registry-check` | `docs` | false | true | false |
| `spec-eval` | `reporting` | false | true | false |
| `spec-lang-adoption-json` | `metrics` | false | true | false |
| `spec-lang-adoption-md` | `metrics` | false | true | false |
| `spec-lang-stdlib-json` | `metrics` | false | true | false |
| `spec-lang-stdlib-md` | `metrics` | false | true | false |
| `spec-portability-json` | `metrics` | false | true | false |
| `spec-portability-md` | `metrics` | false | true | false |
| `spec-ref` | `reporting` | false | true | false |
| `style-check` | `reporting` | false | true | false |
| `summary_json` | `reporting` | false | true | false |
| `test-core` | `verification` | false | true | false |
| `test-full` | `verification` | false | true | false |
| `typecheck` | `verification` | false | true | false |
| `validate-report` | `reporting` | false | true | false |
| `violation_count` | `reporting` | false | true | false |


### Command Semantics

#### `--changed-only`

- Summary: Runs `--changed-only` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --changed-only`: Execute command with canonical adapter routing.


#### `--doc`

- Summary: Runs `--doc` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --doc`: Execute command with canonical adapter routing.


#### `--expr-file`

- Summary: Runs `--expr-file` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --expr-file`: Execute command with canonical adapter routing.


#### `--expr-json`

- Summary: Runs `--expr-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --expr-json`: Execute command with canonical adapter routing.


#### `--input`

- Summary: Runs `--input` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --input`: Execute command with canonical adapter routing.


#### `--liveness-hard-cap-ms`

- Summary: Runs `--liveness-hard-cap-ms` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --liveness-hard-cap-ms`: Execute command with canonical adapter routing.


#### `--liveness-kill-grace-ms`

- Summary: Runs `--liveness-kill-grace-ms` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --liveness-kill-grace-ms`: Execute command with canonical adapter routing.


#### `--liveness-level`

- Summary: Runs `--liveness-level` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --liveness-level`: Execute command with canonical adapter routing.


#### `--liveness-min-events`

- Summary: Runs `--liveness-min-events` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --liveness-min-events`: Execute command with canonical adapter routing.


#### `--liveness-stall-ms`

- Summary: Runs `--liveness-stall-ms` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --liveness-stall-ms`: Execute command with canonical adapter routing.


#### `--path`

- Summary: Runs `--path` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --path`: Execute command with canonical adapter routing.


#### `--paths`

- Summary: Runs `--paths` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --paths`: Execute command with canonical adapter routing.


#### `--profile-heartbeat-ms`

- Summary: Runs `--profile-heartbeat-ms` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --profile-heartbeat-ms`: Execute command with canonical adapter routing.


#### `--profile-level`

- Summary: Runs `--profile-level` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --profile-level`: Execute command with canonical adapter routing.


#### `--profile-out`

- Summary: Runs `--profile-out` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --profile-out`: Execute command with canonical adapter routing.


#### `--profile-stall-threshold-ms`

- Summary: Runs `--profile-stall-threshold-ms` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --profile-stall-threshold-ms`: Execute command with canonical adapter routing.


#### `--profile-summary-out`

- Summary: Runs `--profile-summary-out` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --profile-summary-out`: Execute command with canonical adapter routing.


#### `--ref`

- Summary: Runs `--ref` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --ref`: Execute command with canonical adapter routing.


#### `--subject-file`

- Summary: Runs `--subject-file` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --subject-file`: Execute command with canonical adapter routing.


#### `--subject-json`

- Summary: Runs `--subject-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh --subject-json`: Execute command with canonical adapter routing.


#### `-v`

- Summary: Runs `-v` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh -v`: Execute command with canonical adapter routing.


#### `-vv`

- Summary: Runs `-vv` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh -vv`: Execute command with canonical adapter routing.


#### `-vvv`

- Summary: Runs `-vvv` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh -vvv`: Execute command with canonical adapter routing.


#### `ci-cleanroom`

- Summary: Runs `ci-cleanroom` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh ci-cleanroom`: Execute command with canonical adapter routing.


#### `ci-gate-summary`

- Summary: Runs `ci-gate-summary` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh ci-gate-summary`: Execute command with canonical adapter routing.


#### `compilecheck`

- Summary: Runs `compilecheck` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh compilecheck`: Execute command with canonical adapter routing.


#### `conformance-parity`

- Summary: Runs `conformance-parity` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh conformance-parity`: Execute command with canonical adapter routing.


#### `conformance-purpose-json`

- Summary: Runs `conformance-purpose-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh conformance-purpose-json`: Execute command with canonical adapter routing.


#### `conformance-purpose-md`

- Summary: Runs `conformance-purpose-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh conformance-purpose-md`: Execute command with canonical adapter routing.


#### `contract-assertions-json`

- Summary: Runs `contract-assertions-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh contract-assertions-json`: Execute command with canonical adapter routing.


#### `contract-assertions-md`

- Summary: Runs `contract-assertions-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh contract-assertions-md`: Execute command with canonical adapter routing.


#### `critical-gate`

- Summary: Runs `critical-gate` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh critical-gate`: Execute command with canonical adapter routing.


#### `docs-build`

- Summary: Runs `docs-build` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh docs-build`: Execute command with canonical adapter routing.


#### `docs-build-check`

- Summary: Runs `docs-build-check` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh docs-build-check`: Execute command with canonical adapter routing.


#### `docs-generate`

- Summary: Runs `docs-generate` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh docs-generate`: Execute command with canonical adapter routing.


#### `docs-generate-check`

- Summary: Runs `docs-generate-check` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh docs-generate-check`: Execute command with canonical adapter routing.


#### `docs-graph`

- Summary: Runs `docs-graph` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh docs-graph`: Execute command with canonical adapter routing.


#### `docs-lint`

- Summary: Runs `docs-lint` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh docs-lint`: Execute command with canonical adapter routing.


#### `docs-operability-json`

- Summary: Runs `docs-operability-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh docs-operability-json`: Execute command with canonical adapter routing.


#### `docs-operability-md`

- Summary: Runs `docs-operability-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh docs-operability-md`: Execute command with canonical adapter routing.


#### `governance`

- Summary: Runs `governance` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh governance`: Execute command with canonical adapter routing.


#### `governance-broad-native`

- Summary: Runs `governance-broad-native` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh governance-broad-native`: Execute command with canonical adapter routing.


#### `governance-heavy`

- Summary: Runs `governance-heavy` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh governance-heavy`: Execute command with canonical adapter routing.


#### `job-run`

- Summary: Runs `job-run` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh job-run`: Execute command with canonical adapter routing.


#### `lint`

- Summary: Runs `lint` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh lint`: Execute command with canonical adapter routing.


#### `meta_json`

- Summary: Runs `meta_json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh meta_json`: Execute command with canonical adapter routing.


#### `normalize-check`

- Summary: Runs `normalize-check` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh normalize-check`: Execute command with canonical adapter routing.


#### `normalize-fix`

- Summary: Runs `normalize-fix` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh normalize-fix`: Execute command with canonical adapter routing.


#### `objective-scorecard-json`

- Summary: Runs `objective-scorecard-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh objective-scorecard-json`: Execute command with canonical adapter routing.


#### `objective-scorecard-md`

- Summary: Runs `objective-scorecard-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh objective-scorecard-md`: Execute command with canonical adapter routing.


#### `perf-smoke`

- Summary: Runs `perf-smoke` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh perf-smoke`: Execute command with canonical adapter routing.


#### `python-dependency-json`

- Summary: Runs `python-dependency-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh python-dependency-json`: Execute command with canonical adapter routing.


#### `python-dependency-md`

- Summary: Runs `python-dependency-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh python-dependency-md`: Execute command with canonical adapter routing.


#### `runner-independence-json`

- Summary: Runs `runner-independence-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh runner-independence-json`: Execute command with canonical adapter routing.


#### `runner-independence-md`

- Summary: Runs `runner-independence-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh runner-independence-md`: Execute command with canonical adapter routing.


#### `schema-docs-build`

- Summary: Runs `schema-docs-build` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh schema-docs-build`: Execute command with canonical adapter routing.


#### `schema-docs-check`

- Summary: Runs `schema-docs-check` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh schema-docs-check`: Execute command with canonical adapter routing.


#### `schema-registry-build`

- Summary: Runs `schema-registry-build` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh schema-registry-build`: Execute command with canonical adapter routing.


#### `schema-registry-check`

- Summary: Runs `schema-registry-check` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh schema-registry-check`: Execute command with canonical adapter routing.


#### `spec-eval`

- Summary: Runs `spec-eval` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh spec-eval`: Execute command with canonical adapter routing.


#### `spec-lang-adoption-json`

- Summary: Runs `spec-lang-adoption-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh spec-lang-adoption-json`: Execute command with canonical adapter routing.


#### `spec-lang-adoption-md`

- Summary: Runs `spec-lang-adoption-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh spec-lang-adoption-md`: Execute command with canonical adapter routing.


#### `spec-lang-stdlib-json`

- Summary: Runs `spec-lang-stdlib-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh spec-lang-stdlib-json`: Execute command with canonical adapter routing.


#### `spec-lang-stdlib-md`

- Summary: Runs `spec-lang-stdlib-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh spec-lang-stdlib-md`: Execute command with canonical adapter routing.


#### `spec-portability-json`

- Summary: Runs `spec-portability-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh spec-portability-json`: Execute command with canonical adapter routing.


#### `spec-portability-md`

- Summary: Runs `spec-portability-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh spec-portability-md`: Execute command with canonical adapter routing.


#### `spec-ref`

- Summary: Runs `spec-ref` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh spec-ref`: Execute command with canonical adapter routing.


#### `style-check`

- Summary: Runs `style-check` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh style-check`: Execute command with canonical adapter routing.


#### `summary_json`

- Summary: Runs `summary_json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh summary_json`: Execute command with canonical adapter routing.


#### `test-core`

- Summary: Runs `test-core` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh test-core`: Execute command with canonical adapter routing.


#### `test-full`

- Summary: Runs `test-full` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh test-full`: Execute command with canonical adapter routing.


#### `typecheck`

- Summary: Runs `typecheck` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh typecheck`: Execute command with canonical adapter routing.


#### `validate-report`

- Summary: Runs `validate-report` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh validate-report`: Execute command with canonical adapter routing.


#### `violation_count`

- Summary: Runs `violation_count` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through runners/public/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./runners/public/runner_adapter.sh violation_count`: Execute command with canonical adapter routing.
<!-- GENERATED:END runner_api_catalog -->
