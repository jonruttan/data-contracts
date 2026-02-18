# Conformance Index

Source of truth: spec.conformance.index

Cross-runner conformance fixtures and report contracts.

## Canonical Inputs

- Style contract: `/specs/conformance/style.md`
- Report format: `/specs/conformance/report_format.md`
- Purpose lint policy: `/specs/conformance/purpose_lint_v1.yaml`
- Cases index: `/specs/conformance/cases/index.md`

## Execution

```sh
python -m spec_runner.spec_lang_commands compare-conformance-parity --cases specs/conformance/cases --out .artifacts/conformance-parity.json
```
