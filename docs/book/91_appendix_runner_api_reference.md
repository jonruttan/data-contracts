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
- run: ./scripts/runner_adapter.sh docs-generate-check
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

- command_count: 42
- python_command_count: 42
- rust_command_count: 42
- parity_command_count: 42
- all_commands_parity: true
- doc_quality_score: 1.0

| command | group | python | rust | parity |
|---|---|---|---|---|
| `ci-cleanroom` | `ci` | true | true | true |
| `ci-gate-summary` | `ci` | true | true | true |
| `compilecheck` | `reporting` | true | true | true |
| `conformance-parity` | `reporting` | true | true | true |
| `conformance-purpose-json` | `metrics` | true | true | true |
| `conformance-purpose-md` | `metrics` | true | true | true |
| `contract-assertions-json` | `metrics` | true | true | true |
| `contract-assertions-md` | `metrics` | true | true | true |
| `docs-build` | `docs` | true | true | true |
| `docs-build-check` | `docs` | true | true | true |
| `docs-generate` | `docs` | true | true | true |
| `docs-generate-check` | `docs` | true | true | true |
| `docs-graph` | `docs` | true | true | true |
| `docs-lint` | `docs` | true | true | true |
| `docs-operability-json` | `docs` | true | true | true |
| `docs-operability-md` | `docs` | true | true | true |
| `governance` | `verification` | true | true | true |
| `governance-heavy` | `reporting` | true | true | true |
| `lint` | `verification` | true | true | true |
| `normalize-check` | `verification` | true | true | true |
| `normalize-fix` | `verification` | true | true | true |
| `objective-scorecard-json` | `metrics` | true | true | true |
| `objective-scorecard-md` | `metrics` | true | true | true |
| `perf-smoke` | `reporting` | true | true | true |
| `python-dependency-json` | `metrics` | true | true | true |
| `python-dependency-md` | `metrics` | true | true | true |
| `runner-independence-json` | `metrics` | true | true | true |
| `runner-independence-md` | `metrics` | true | true | true |
| `schema-docs-build` | `docs` | true | true | true |
| `schema-docs-check` | `docs` | true | true | true |
| `schema-registry-build` | `docs` | true | true | true |
| `schema-registry-check` | `docs` | true | true | true |
| `spec-lang-adoption-json` | `metrics` | true | true | true |
| `spec-lang-adoption-md` | `metrics` | true | true | true |
| `spec-lang-stdlib-json` | `metrics` | true | true | true |
| `spec-lang-stdlib-md` | `metrics` | true | true | true |
| `spec-portability-json` | `metrics` | true | true | true |
| `spec-portability-md` | `metrics` | true | true | true |
| `style-check` | `reporting` | true | true | true |
| `test-core` | `verification` | true | true | true |
| `test-full` | `verification` | true | true | true |
| `typecheck` | `verification` | true | true | true |


### Command Semantics

#### `ci-cleanroom`

- Summary: Runs `ci-cleanroom` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh ci-cleanroom`: Execute command with canonical adapter routing.


#### `ci-gate-summary`

- Summary: Runs `ci-gate-summary` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh ci-gate-summary`: Execute command with canonical adapter routing.


#### `compilecheck`

- Summary: Runs `compilecheck` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh compilecheck`: Execute command with canonical adapter routing.


#### `conformance-parity`

- Summary: Runs `conformance-parity` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh conformance-parity`: Execute command with canonical adapter routing.


#### `conformance-purpose-json`

- Summary: Runs `conformance-purpose-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh conformance-purpose-json`: Execute command with canonical adapter routing.


#### `conformance-purpose-md`

- Summary: Runs `conformance-purpose-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh conformance-purpose-md`: Execute command with canonical adapter routing.


#### `contract-assertions-json`

- Summary: Runs `contract-assertions-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh contract-assertions-json`: Execute command with canonical adapter routing.


#### `contract-assertions-md`

- Summary: Runs `contract-assertions-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh contract-assertions-md`: Execute command with canonical adapter routing.


#### `docs-build`

- Summary: Runs `docs-build` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh docs-build`: Execute command with canonical adapter routing.


#### `docs-build-check`

- Summary: Runs `docs-build-check` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh docs-build-check`: Execute command with canonical adapter routing.


#### `docs-generate`

- Summary: Runs `docs-generate` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh docs-generate`: Execute command with canonical adapter routing.


#### `docs-generate-check`

- Summary: Runs `docs-generate-check` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh docs-generate-check`: Execute command with canonical adapter routing.


#### `docs-graph`

- Summary: Runs `docs-graph` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh docs-graph`: Execute command with canonical adapter routing.


#### `docs-lint`

- Summary: Runs `docs-lint` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh docs-lint`: Execute command with canonical adapter routing.


#### `docs-operability-json`

- Summary: Runs `docs-operability-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh docs-operability-json`: Execute command with canonical adapter routing.


#### `docs-operability-md`

- Summary: Runs `docs-operability-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh docs-operability-md`: Execute command with canonical adapter routing.


#### `governance`

- Summary: Runs `governance` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh governance`: Execute command with canonical adapter routing.


#### `governance-heavy`

- Summary: Runs `governance-heavy` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh governance-heavy`: Execute command with canonical adapter routing.


#### `lint`

- Summary: Runs `lint` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh lint`: Execute command with canonical adapter routing.


#### `normalize-check`

- Summary: Runs `normalize-check` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh normalize-check`: Execute command with canonical adapter routing.


#### `normalize-fix`

- Summary: Runs `normalize-fix` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh normalize-fix`: Execute command with canonical adapter routing.


#### `objective-scorecard-json`

- Summary: Runs `objective-scorecard-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh objective-scorecard-json`: Execute command with canonical adapter routing.


#### `objective-scorecard-md`

- Summary: Runs `objective-scorecard-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh objective-scorecard-md`: Execute command with canonical adapter routing.


#### `perf-smoke`

- Summary: Runs `perf-smoke` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh perf-smoke`: Execute command with canonical adapter routing.


#### `python-dependency-json`

- Summary: Runs `python-dependency-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh python-dependency-json`: Execute command with canonical adapter routing.


#### `python-dependency-md`

- Summary: Runs `python-dependency-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh python-dependency-md`: Execute command with canonical adapter routing.


#### `runner-independence-json`

- Summary: Runs `runner-independence-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh runner-independence-json`: Execute command with canonical adapter routing.


#### `runner-independence-md`

- Summary: Runs `runner-independence-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh runner-independence-md`: Execute command with canonical adapter routing.


#### `schema-docs-build`

- Summary: Runs `schema-docs-build` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh schema-docs-build`: Execute command with canonical adapter routing.


#### `schema-docs-check`

- Summary: Runs `schema-docs-check` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh schema-docs-check`: Execute command with canonical adapter routing.


#### `schema-registry-build`

- Summary: Runs `schema-registry-build` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh schema-registry-build`: Execute command with canonical adapter routing.


#### `schema-registry-check`

- Summary: Runs `schema-registry-check` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh schema-registry-check`: Execute command with canonical adapter routing.


#### `spec-lang-adoption-json`

- Summary: Runs `spec-lang-adoption-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh spec-lang-adoption-json`: Execute command with canonical adapter routing.


#### `spec-lang-adoption-md`

- Summary: Runs `spec-lang-adoption-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh spec-lang-adoption-md`: Execute command with canonical adapter routing.


#### `spec-lang-stdlib-json`

- Summary: Runs `spec-lang-stdlib-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh spec-lang-stdlib-json`: Execute command with canonical adapter routing.


#### `spec-lang-stdlib-md`

- Summary: Runs `spec-lang-stdlib-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh spec-lang-stdlib-md`: Execute command with canonical adapter routing.


#### `spec-portability-json`

- Summary: Runs `spec-portability-json` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh spec-portability-json`: Execute command with canonical adapter routing.


#### `spec-portability-md`

- Summary: Runs `spec-portability-md` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh spec-portability-md`: Execute command with canonical adapter routing.


#### `style-check`

- Summary: Runs `style-check` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh style-check`: Execute command with canonical adapter routing.


#### `test-core`

- Summary: Runs `test-core` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh test-core`: Execute command with canonical adapter routing.


#### `test-full`

- Summary: Runs `test-full` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh test-full`: Execute command with canonical adapter routing.


#### `typecheck`

- Summary: Runs `typecheck` through the canonical runner entrypoint.
- Details: Deterministic command dispatch through scripts/runner_adapter.sh.
- Defaults:
  - `impl=rust`: Default runner implementation lane.

- Failure Modes:
  - Unknown subcommand.
  - Underlying command returns non-zero status.

- Examples:
  - `./scripts/runner_adapter.sh typecheck`: Execute command with canonical adapter routing.
<!-- GENERATED:END runner_api_catalog -->
