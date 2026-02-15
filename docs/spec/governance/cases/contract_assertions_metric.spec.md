# Governance Cases

## SRGOV-CONTRACT-ASSERT-001

```yaml spec-test
id: SRGOV-CONTRACT-ASSERT-001
title: contract assertions metric report generation is valid
purpose: Ensures contract assertions report generation and shape are valid.
type: governance.check
check: spec.contract_assertions_metric
harness:
  root: .
  contract_assertions:
    paths:
    - docs/spec/contract/03_assertions.md
    - docs/spec/schema/schema_v1.md
    - docs/book/03_assertions.md
    - docs/spec/contract/03b_spec_lang_v1.md
    policy_evaluate:
    - and:
      - has_key:
        - subject: []
        - summary
      - has_key:
        - subject: []
        - segments
      - has_key:
        - get:
          - subject: []
          - summary
        - overall_contract_assertions_ratio
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: spec.contract_assertions_metric'
```
