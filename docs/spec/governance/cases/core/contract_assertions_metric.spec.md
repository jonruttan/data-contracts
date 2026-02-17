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
    - std.logic.and:
      - std.object.has_key:
        - {var: subject}
        - summary
      - std.object.has_key:
        - {var: subject}
        - segments
      - std.object.has_key:
        - std.object.get:
          - {var: subject}
          - summary
        - overall_contract_assertions_ratio
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - spec.contract_assertions_metric
  target: summary_json
```
