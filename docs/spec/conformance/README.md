# Conformance Fixtures

This folder defines cross-language fixture conventions for validating runner
parity.

Authoring style:

- `docs/spec/conformance/style.md`

Planned contents:

- fixture case files
- inline expected outcomes on case records
- parity checks between Python and PHP implementations

Current seed:

- `docs/spec/conformance/purpose-lint-v1.yaml`
- `docs/spec/conformance/cases/cli-run-entrypoint.spec.md`
- `docs/spec/conformance/cases/assertion-health.spec.md`
- `docs/spec/conformance/cases/failure-context.spec.md`
- `docs/spec/conformance/cases/php-text-file-subset.spec.md`

Python reference execution is covered by:

- `tools/spec_runner/tests/test_conformance_runner_unit.py`

PHP bootstrap parity subset is covered by:

- `tools/spec_runner/tests/test_php_conformance_subset_unit.py`

Coverage artifact command:

- `python3 scripts/contract_coverage_report.py --out .artifacts/contract-coverage.json`
