# Development

## Install (Editable)

```sh
python3 -m pip install -e '.[dev]'
```

## Run Tests

```sh
python3 scripts/check_contract_governance.py
python3 scripts/contract_coverage_report.py --out .artifacts/contract-coverage.json
python3 -m pytest
```

## Required CI Gate

Merges are expected to pass the `spec_runner` CI job, which runs:

- contract governance check
- contract coverage report generation
- `tools/spec_runner` pytest suite
- artifact upload of `.artifacts/contract-coverage.json`

## Contract Governance Check

```sh
python3 scripts/check_contract_governance.py
```

## Contract Coverage Report

```sh
python3 scripts/contract_coverage_report.py --out .artifacts/contract-coverage.json
```

## Conformance Fixture Layout

Cross-language fixture data lives in:

- `fixtures/conformance/cases/`
- `fixtures/conformance/expected/`

Contract docs for interpreting those fixtures live in:

- `docs/spec/contract/06-conformance.md`
- `docs/spec/conformance/report-format.md`

## PHP Bootstrap Parity

Generate a bootstrap PHP report:

```sh
php scripts/php/conformance_runner.php \
  --cases fixtures/conformance/cases/php-text-file-subset.yaml \
  --out .artifacts/php-conformance-report.json
```

Validate bootstrap report shape:

```sh
python3 scripts/validate_conformance_report.py .artifacts/php-conformance-report.json
```

## Build / Publish

```sh
python3 -m pip install -U build twine
python3 -m build
python3 -m twine check dist/*
```
