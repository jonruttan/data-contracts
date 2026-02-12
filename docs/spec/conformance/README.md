# Conformance Fixtures

This folder defines cross-language fixture conventions for validating runner
parity.

Planned contents:

- fixture case files
- expected outcome files
- parity checks between Python and PHP implementations

Current seed:

- `fixtures/conformance/cases/cli-run-entrypoint.yaml`
- `fixtures/conformance/cases/assertion-health.yaml`
- `fixtures/conformance/expected/cli-run-entrypoint.yaml`
- `fixtures/conformance/expected/assertion-health.yaml`

Python reference execution is covered by:

- `tools/spec_runner/tests/test_conformance_runner_unit.py`

Coverage artifact command:

- `python3 scripts/contract_coverage_report.py --out .artifacts/contract-coverage.json`
