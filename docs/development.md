# Development

## Install (Editable)

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
```

Using Homebrew/system Python without a venv may fail with
`externally-managed-environment` (PEP 668). Prefer the venv flow above.

Installable CLI entrypoints exposed by packaging metadata:

- `spec-runner-conformance` (Python conformance runner)
- `spec-runner-parity` (Python/PHP parity comparison)
- `spec-runner-validate-report` (conformance report validator)

## Run Checks

```sh
python -m ruff check .
python -m mypy spec_runner
python -m compileall -q spec_runner scripts tests
python scripts/spec_lang_lint.py --cases docs/spec
python scripts/spec_lang_format.py --check docs/spec
python scripts/docs_generate_all.py --check
python -m spec_runner.spec_lang_commands docs-lint
```

## Adoption Profiles

Use one of these lanes depending on depth needed:

- Core profile (lightweight, fast local confidence): `make core-check`
- Full profile (release/pre-merge parity confidence): `make check`

Core profile runs:

- governance specs
- spec-lang lint + format checks
- focused core runner unit tests (`doc_parser`, `dispatcher`, `assertions`, `conformance_runner`)

Full profile runs the complete CI-equivalent gate including parity and full test suite.

Runner interface override:

- Gate scripts call `SPEC_RUNNER_BIN` (default: `scripts/runner_adapter.sh`).
- To exercise a non-Python runner implementation while keeping gate orchestration
  unchanged:

```sh
SPEC_RUNNER_BIN=/path/to/compatible-runner ./scripts/core_gate.sh
SPEC_RUNNER_BIN=/path/to/compatible-runner ./scripts/ci_gate.sh
```

Rust-primary transition contract:

- `docs/spec/contract/16_rust_primary_transition.md`

Rust-default lane (canonical):

```sh
SPEC_RUNNER_BIN=./scripts/runner_adapter.sh ./scripts/core_gate.sh
```

Runtime Python impl selection (forbidden):

```sh
SPEC_RUNNER_BIN=./scripts/runner_adapter.sh SPEC_RUNNER_IMPL=python ./scripts/core_gate.sh
# exits non-zero with rust migration guidance
```

Optional local prebuild for Rust lane:

```sh
cargo build --manifest-path scripts/rust/spec_runner_cli/Cargo.toml
```

## Run Core Gate Checks

```sh
./scripts/runner_adapter.sh governance
./scripts/runner_adapter.sh style-check
./scripts/runner_adapter.sh conformance-purpose-json
./scripts/runner_adapter.sh conformance-purpose-md
./scripts/runner_adapter.sh conformance-parity
./scripts/runner_adapter.sh python-dependency-json
./scripts/runner_adapter.sh python-dependency-md
./scripts/runner_adapter.sh test-full
```

Canonical pre-merge check:

```sh
./scripts/ci_gate.sh
make core-check
make check
```

Release readiness checklist:

- `docs/release_checklist.md`

Gate summary artifact produced by `ci_gate.sh`:

- `.artifacts/gate-summary.json` (machine-readable step status, exit code, and duration)

Fast docs-only gate:

```sh
./scripts/docs_doctor.sh
make docs-doctor
make verify-docs
make docs-generate
make docs-check
make ci-smoke

# Clean-checkout parity (recommended before push)
make ci-cleanroom
```

Required local pre-push gate:

```sh
make prepush
```

The pre-push gate runs the fast CI-critical contract path:

- `normalize-check`
- `governance` via `scripts/governance_triage.sh --mode auto`
- `governance-heavy`
- `docs-generate-check`
- `perf-smoke --mode strict --compare-only`

`governance-heavy` and `docs-generate-check` are path-scoped and only run when
relevant files changed.

`make prepush` is Rust-only on the runtime path.

Fast local opt-out mode:

```sh
make prepush-fast
# or
SPEC_PREPUSH_MODE=fast make prepush
```

Runtime impl is rust-only; `SPEC_RUNNER_IMPL=python` is rejected by
`scripts/runner_adapter.sh` with migration guidance.

Install managed git hooks to enforce local pre-push parity gate:

```sh
make hooks-install
```

Emergency bypass for blocked pushes (use sparingly and follow with parity run):

```sh
SPEC_PREPUSH_BYPASS=1 git push
```

Governance triage artifacts:

- `/.artifacts/governance-triage.json`
- `/.artifacts/governance-triage-summary.md`

## CI Triage (Docs Quality)

When CI fails with `SRGOV-DOCS-QUAL-*`:

1. Reproduce quickly:

```sh
make ci-smoke

# Run full gate exactly from a fresh worktree clone state
make ci-cleanroom
```

2. Regenerate docs artifacts:

```sh
make docs-generate
```

3. Re-run docs checks:

```sh
make docs-check
```

Common failures:

- `SRGOV-DOCS-QUAL-002`: `docs/book/reference_index.md` is out of sync with
  `docs/book/reference_manifest.yaml`.
- `SRGOV-DOCS-QUAL-008`: generated files drifted
  (`reference_index.md`, `reference_coverage.md`, `docs_graph.json`).
- `SRGOV-DOCS-QUAL-003/004`: token ownership/dependency issues in chapter
  `doc-meta`.

Suggested pre-commit hook:

```sh
cat > .git/hooks/pre-commit <<'SH'
#!/usr/bin/env bash
set -euo pipefail
./scripts/docs_doctor.sh
SH
chmod +x .git/hooks/pre-commit
```

## Runner Exit-Code Contract

The following exit codes are stable command contracts for CI/scripting.

| Command | `0` | `1` | `2` |
| --- | --- | --- | --- |
| `python scripts/python/conformance_runner.py` | runner completed and all case statuses are `pass`/`skip` | at least one case status is `fail`, or runtime execution error occurred | CLI usage/argument validation error (for example missing required args, empty `--case-file-pattern`, nonexistent `--cases` path) |
| `php scripts/php/conformance_runner.php` | runner completed and report written (case-level failures are reported in JSON, not promoted to process failure) | fatal runtime error (for example YAML extension missing, unreadable path, write failure) | CLI usage/argument validation error (for example missing required args, empty `--case-file-pattern`) |
| `php scripts/php/spec_runner.php` | runner completed, report written, and all cases passed | one or more cases failed, or fatal runtime error occurred | CLI usage/argument validation error (for example missing required args, empty `--case-file-pattern`) |

Notes:

- `--help` exits `0` for all three commands.
- `2` is reserved for invocation/argument issues so automation can distinguish
  operator errors from runner/case failures.

## Required CI Gate

Merges are expected to pass the `spec_runner` CI job, which runs:

- contract governance check
- governance spec-runner checks
- pedantic spec-lang lint (`scripts/spec_lang_lint.py --cases docs/spec`)
- pedantic spec-lang format check (`scripts/spec_lang_format.py --check docs/spec`)
- ruff lint check (`F` + `E9` rules)
- mypy type check (`spec_runner` package)
- Python bytecode compile pass (`compileall`)
- conformance purpose report generation
- conformance purpose markdown summary generation
- Python/PHP conformance parity command
- `tools/spec_runner` pytest suite
- artifact upload of `.artifacts/conformance-purpose.json`
- artifact upload of `.artifacts/conformance-purpose-summary.md`
- artifact upload of `.artifacts/conformance-parity.json`
- artifact upload of `.artifacts/gate-summary.json`

`run_governance_specs.py` (via `contract.governance_check`) enforces
conformance case doc freshness:
every `SRCONF-*` fixture case id must be listed in
`docs/spec/conformance/cases/index.md`, and stale ids in that index fail CI.

Local equivalent:

```sh
./scripts/ci_gate.sh
```

## Contract Governance Check (via Governance Specs)

```sh
python scripts/run_governance_specs.py
```

## Lint

```sh
python -m ruff check .
python scripts/spec_lang_lint.py --cases docs/spec
python scripts/spec_lang_format.py --check docs/spec
```

## Type Check

```sh
python -m mypy spec_runner
```

## Static Analysis (Syntax/Import-Time Parse)

```sh
python -m compileall -q spec_runner scripts tests
```

## Contract Coverage Report

Optional wrapper (reporting artifact; not a primary gate):

```sh
python -m spec_runner.spec_lang_commands contract-coverage-report --out .artifacts/contract-coverage.json
```

## Conformance Purpose Report

```sh
python scripts/conformance_purpose_report.py --out .artifacts/conformance-purpose.json
python scripts/conformance_purpose_report.py --format md --out .artifacts/conformance-purpose-summary.md
```

The purpose report includes `policy` metadata resolved from:

- `docs/spec/conformance/purpose_lint_v1.yaml`

Optional strict mode for automation:

```sh
python scripts/conformance_purpose_report.py --fail-on-warn
python scripts/conformance_purpose_report.py --fail-on-severity warn
python scripts/conformance_purpose_report.py --fail-on-severity error
python scripts/conformance_purpose_report.py --only-warnings --format md --out .artifacts/conformance-purpose-warnings.md
python scripts/conformance_purpose_report.py --only-warnings --emit-patches .artifacts/conformance-purpose-patches
```

Purpose warning codes:

- `PUR001`: purpose duplicates title
- `PUR002`: purpose word count below minimum
- `PUR003`: purpose contains placeholder token
- `PUR004`: purpose lint configuration/policy error

Canonical source for these codes:

- `docs/spec/conformance/purpose_warning_codes.md`

## Conformance Fixture Layout

Cross-language fixture data lives in:

- `docs/spec/conformance/cases/`

Contract docs for interpreting those fixtures live in:

- `docs/spec/contract/06_conformance.md`
- `docs/spec/conformance/report_format.md`

## PHP Bootstrap Parity

Generate a Python conformance report:

```sh
spec-runner-conformance \
  --cases docs/spec/conformance/cases \
  --case-formats md \
  --out .artifacts/python-conformance-report.json
```

Validate report shape:

```sh
spec-runner-validate-report .artifacts/python-conformance-report.json
```

Generate a bootstrap PHP report:

```sh
# Requires PHP yaml_parse extension.
php scripts/php/conformance_runner.php \
  --cases docs/spec/conformance/cases/core/php_text_file_subset.spec.md \
  --out .artifacts/php-conformance-report.json
```

Validate bootstrap report shape:

```sh
spec-runner-validate-report .artifacts/php-conformance-report.json
```

Run end-to-end Python/PHP parity over canonical conformance cases:

```sh
spec-runner-parity \
  --cases docs/spec/conformance/cases \
  --case-formats md \
  --php-runner scripts/php/conformance_runner.php \
  --php-timeout-seconds 30 \
  --out .artifacts/conformance-parity.json
```

Parity diffs are evaluated on case IDs where `expect` resolves to the same
`status` + `category` for both implementations.

On slower CI runners, increase `--php-timeout-seconds` (for example `60`) to
avoid false-negative parity failures caused by host contention.

## Build / Publish

```sh
python -m pip install -U build twine
python -m build
python -m twine check dist/*
```

## Canonical Docs/Spec Checks

Run this before `make prepush` when touching docs or governance:

```sh
python3 scripts/check_docs_freshness.py --strict
```

The checker validates canonical index ownership, link integrity, stale-term drift, governance family-map coverage, and generated docs sync.
