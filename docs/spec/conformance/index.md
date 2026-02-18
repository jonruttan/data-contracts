# Conformance Index

Source of truth: spec.conformance.index

Cross-runner conformance fixtures and report contracts.

## Canonical Inputs

- Style contract: `/docs/spec/conformance/style.md`
- Report format: `/docs/spec/conformance/report_format.md`
- Purpose lint policy: `/docs/spec/conformance/purpose_lint_v1.yaml`
- Cases index: `/docs/spec/conformance/cases/index.md`

## Execution

```sh
python -m spec_runner.spec_lang_commands compare-conformance-parity --cases docs/spec/conformance/cases --out .artifacts/conformance-parity.json
```
