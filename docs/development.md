# Development

## Install (Editable)

```sh
python3 -m pip install -e '.[dev]'
```

## Run Tests

```sh
python3 -m pytest
```

## Contract Governance Check

```sh
python3 scripts/check_contract_governance.py
```

## Conformance Fixture Layout

Cross-language fixture data lives in:

- `fixtures/conformance/cases/`
- `fixtures/conformance/expected/`

Contract docs for interpreting those fixtures live in:

- `docs/spec/contract/06-conformance.md`
- `docs/spec/conformance/report-format.md`

## Build / Publish

```sh
python3 -m pip install -U build twine
python3 -m build
python3 -m twine check dist/*
```
