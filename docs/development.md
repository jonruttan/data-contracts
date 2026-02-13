# Development

## Install (Editable)

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
```

Using Homebrew/system Python without a venv may fail with
`externally-managed-environment` (PEP 668). Prefer the venv flow above.

## Run Checks

```sh
python -m ruff check .
python -m compileall -q spec_runner scripts tests
```

## Run Core Gate Checks

```sh
python scripts/check_contract_governance.py
python scripts/contract_coverage_report.py --out .artifacts/contract-coverage.json
python scripts/conformance_purpose_report.py --out .artifacts/conformance-purpose.json
python scripts/conformance_purpose_report.py --format md --out .artifacts/conformance-purpose-summary.md
python scripts/compare_conformance_parity.py --cases docs/spec/conformance/cases --php-runner scripts/php/conformance_runner.php --out .artifacts/conformance-parity.json
python -m pytest
```

Canonical pre-merge check:

```sh
./scripts/ci_gate.sh
```

## Required CI Gate

Merges are expected to pass the `spec_runner` CI job, which runs:

- contract governance check
- ruff lint check (`F` + `E9` rules)
- Python bytecode compile pass (`compileall`)
- contract coverage report generation
- conformance purpose report generation
- conformance purpose markdown summary generation
- Python/PHP conformance parity command
- `tools/spec_runner` pytest suite
- artifact upload of `.artifacts/contract-coverage.json`
- artifact upload of `.artifacts/conformance-purpose.json`
- artifact upload of `.artifacts/conformance-purpose-summary.md`
- artifact upload of `.artifacts/conformance-parity.json`

`check_contract_governance.py` enforces conformance case doc freshness:
every `SRCONF-*` fixture case id must be listed in
`docs/spec/conformance/cases/README.md`, and stale ids in that index fail CI.

Local equivalent:

```sh
./scripts/ci_gate.sh
```

## Contract Governance Check

```sh
python scripts/check_contract_governance.py
```

## Lint

```sh
python -m ruff check .
```

## Static Analysis (Syntax/Import-Time Parse)

```sh
python -m compileall -q spec_runner scripts tests
```

## Contract Coverage Report

```sh
python scripts/contract_coverage_report.py --out .artifacts/contract-coverage.json
```

## Conformance Purpose Report

```sh
python scripts/conformance_purpose_report.py --out .artifacts/conformance-purpose.json
python scripts/conformance_purpose_report.py --format md --out .artifacts/conformance-purpose-summary.md
```

The purpose report includes `policy` metadata resolved from:

- `docs/spec/conformance/purpose-lint-v1.yaml`

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

- `docs/spec/conformance/purpose-warning-codes.md`

## Conformance Fixture Layout

Cross-language fixture data lives in:

- `docs/spec/conformance/cases/`

Contract docs for interpreting those fixtures live in:

- `docs/spec/contract/06-conformance.md`
- `docs/spec/conformance/report-format.md`

## PHP Bootstrap Parity

Generate a bootstrap PHP report:

```sh
# Requires PHP yaml_parse extension.
php scripts/php/conformance_runner.php \
  --cases docs/spec/conformance/cases/php-text-file-subset.spec.md \
  --out .artifacts/php-conformance-report.json
```

Validate bootstrap report shape:

```sh
python scripts/validate_conformance_report.py .artifacts/php-conformance-report.json
```

Run end-to-end Python/PHP parity over canonical conformance cases:

```sh
python scripts/compare_conformance_parity.py \
  --cases docs/spec/conformance/cases \
  --php-runner scripts/php/conformance_runner.php \
  --php-timeout-seconds 30 \
  --out .artifacts/conformance-parity.json
```

Parity diffs are evaluated on case IDs where `expect` resolves to the same
`status` + `category` for both implementations.

## Build / Publish

```sh
python -m pip install -U build twine
python -m build
python -m twine check dist/*
```
