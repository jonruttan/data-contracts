# Conformance Fixtures

This folder defines the cross-runtime conformance contract used to compare
runner behavior (currently Python and PHP bootstrap subset coverage).

## What Lives Here

- Authoring rules: `docs/spec/conformance/style.md`
- Report shape contract: `docs/spec/conformance/report_format.md`
- Purpose lint policy: `docs/spec/conformance/purpose_lint_v1.yaml`
- Case fixtures: `docs/spec/conformance/cases/*.spec.md`

## Case Set (Current)

- `docs/spec/conformance/cases/core/cli_run_entrypoint.spec.md`
- `docs/spec/conformance/cases/core/assertion_health.spec.md`
- `docs/spec/conformance/cases/core/failure_context.spec.md`
- `docs/spec/conformance/cases/core/php_text_file_subset.spec.md`

## Execution Coverage

- Python reference conformance: `tests/test_conformance_runner_unit.py`
- PHP bootstrap subset: `tests/test_php_conformance_subset_unit.py`
- Python/PHP parity command:
  - `python scripts/compare_conformance_parity.py --cases docs/spec/conformance/cases --php-runner scripts/php/conformance_runner.php --php-timeout-seconds 30 --out .artifacts/conformance-parity.json`

## Artifacts

- Contract coverage:
  - `python scripts/contract_coverage_report.py --out .artifacts/contract-coverage.json`
- Purpose report:
  - `python scripts/conformance_purpose_report.py --out .artifacts/conformance-purpose.json`
