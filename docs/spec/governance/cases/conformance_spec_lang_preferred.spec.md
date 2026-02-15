# Governance Cases

## SRGOV-CONF-SPECLANG-001

```yaml spec-test
id: SRGOV-CONF-SPECLANG-001
title: conformance fixtures prefer sugar unless evaluate is required
purpose: Enforces sugar-first conformance authoring and requires explicit allowlisting for fixtures that intentionally use evaluate expressions.
type: governance.check
check: conformance.spec_lang_preferred
harness:
  root: .
  spec_lang_preferred:
    roots:
    - docs/spec/conformance/cases
    allow_evaluate_files:
    - docs/spec/conformance/cases/assertion_health.spec.md
    - docs/spec/conformance/cases/php_text_file_subset.spec.md
    - docs/spec/conformance/cases/spec_lang.spec.md
    policy_evaluate:
    - eq:
      - count:
        - filter:
          - fn:
            - {row: []}
            - gt:
              - count:
                - {get: [{var: [row]}, evaluate_ops]}
              - 0
          - {subject: []}
      - 0
  policy_evaluate:
  - is_empty:
    - {get: [{subject: []}, violations]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - conformance.spec_lang_preferred
```
