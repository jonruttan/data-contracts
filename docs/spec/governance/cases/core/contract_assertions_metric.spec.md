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
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  contract_assertions:
    paths:
    - docs/spec/contract/03_assertions.md
    - docs/spec/schema/schema_v1.md
    - docs/book/03_assertions.md
    - docs/spec/contract/03b_spec_lang_v1.md
    policy_evaluate:
    - and:
      - has_key:
        - {var: subject}
        - summary
      - has_key:
        - {var: subject}
        - segments
      - has_key:
        - get:
          - {var: subject}
          - summary
        - overall_contract_assertions_ratio
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - spec.contract_assertions_metric
```
