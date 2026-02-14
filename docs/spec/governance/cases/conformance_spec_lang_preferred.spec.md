# Governance Cases

## SRGOV-CONF-SPECLANG-001

```yaml spec-test
id: SRGOV-CONF-SPECLANG-001
title: conformance fixtures prefer evaluate spec-lang assertions
purpose: Enforces spec-lang-first conformance authoring so new fixtures default to evaluate expressions.
type: governance.check
check: conformance.spec_lang_preferred
harness:
  root: .
  spec_lang_preferred:
    roots:
      - docs/spec/conformance/cases
    allow_non_evaluate_files:
      - docs/spec/conformance/cases/api_http.spec.md
      - docs/spec/conformance/cases/assertion_health.spec.md
      - docs/spec/conformance/cases/cli_run_entrypoint.spec.md
      - docs/spec/conformance/cases/failure_context.spec.md
      - docs/spec/conformance/cases/php_text_file_subset.spec.md
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.spec_lang_preferred"]
```
