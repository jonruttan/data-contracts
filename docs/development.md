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
python scripts/evaluate_style.py --check docs/spec
```

## Adoption Profiles

Use one of these lanes depending on depth needed:

- Core profile (lightweight, fast local confidence): `make core-check`
- Full profile (release/pre-merge parity confidence): `make check`

Core profile runs:

- governance specs
- evaluate-style checks
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

## Run Core Gate Checks

```sh
python scripts/run_governance_specs.py
python scripts/evaluate_style.py --check docs/spec
python scripts/conformance_purpose_report.py --out .artifacts/conformance-purpose.json
python scripts/conformance_purpose_report.py --format md --out .artifacts/conformance-purpose-summary.md
python scripts/compare_conformance_parity.py --cases docs/spec/conformance/cases --php-runner scripts/php/conformance_runner.php --out .artifacts/conformance-parity.json
python -m pytest
```

Canonical pre-merge check:

```sh
./scripts/ci_gate.sh
make core-check
make check
```

Gate summary artifact produced by `ci_gate.sh`:

- `.artifacts/gate-summary.json` (machine-readable step status, exit code, and duration)

Fast docs-only gate:

```sh
./scripts/docs_doctor.sh
make docs-doctor
make verify-docs
```

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
- evaluate-expression style lint (`scripts/evaluate_style.py --check`)
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
`docs/spec/conformance/cases/README.md`, and stale ids in that index fail CI.

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
python scripts/evaluate_style.py --check docs/spec
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
python scripts/contract_coverage_report.py --out .artifacts/contract-coverage.json
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
  --cases docs/spec/conformance/cases/php_text_file_subset.spec.md \
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

## External Format Conversion

Convert between external case formats without changing semantics:

```sh
python scripts/convert_cases.py \
  --in docs/spec/conformance/cases/spec_lang.spec.md \
  --out .artifacts/spec_lang.spec.json \
  --out-format json
```

Default execution discovery remains Markdown-only (`*.spec.md`). YAML/JSON are
opt-in external adapter formats.

## Build / Publish

```sh
python -m pip install -U build twine
python -m build
python -m twine check dist/*
```
