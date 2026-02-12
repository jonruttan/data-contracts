# Development

## Install (Editable)

```sh
python3 -m pip install -e '.[dev]'
```

## Run Tests

```sh
python3 scripts/check_contract_governance.py
python3 scripts/contract_coverage_report.py --out .artifacts/contract-coverage.json
python3 scripts/conformance_purpose_report.py --out .artifacts/conformance-purpose.json
python3 -m pytest
```

Canonical pre-merge check:

```sh
./scripts/ci_gate.sh
```

## Required CI Gate

Merges are expected to pass the `spec_runner` CI job, which runs:

- contract governance check
- contract coverage report generation
- conformance purpose report generation
- Python/PHP conformance parity command
- `tools/spec_runner` pytest suite
- artifact upload of `.artifacts/contract-coverage.json`
- artifact upload of `.artifacts/conformance-purpose.json`
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
python3 scripts/check_contract_governance.py
```

## Contract Coverage Report

```sh
python3 scripts/contract_coverage_report.py --out .artifacts/contract-coverage.json
```

## Conformance Purpose Report

```sh
python3 scripts/conformance_purpose_report.py --out .artifacts/conformance-purpose.json
```

The purpose report includes `policy` metadata resolved from:

- `docs/spec/conformance/purpose-lint-v1.yaml`

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
python3 scripts/validate_conformance_report.py .artifacts/php-conformance-report.json
```

Run end-to-end Python/PHP parity over canonical conformance cases:

```sh
python3 scripts/compare_conformance_parity.py \
  --cases docs/spec/conformance/cases \
  --php-runner scripts/php/conformance_runner.php \
  --out .artifacts/conformance-parity.json
```

Parity diffs are evaluated on case IDs where `expect` resolves to the same
`status` + `category` for both implementations.

## Build / Publish

```sh
python3 -m pip install -U build twine
python3 -m build
python3 -m twine check dist/*
```
