# Governance Cases

## SRGOV-CONTRACT-ASSERT-002

```yaml contract-spec
id: SRGOV-CONTRACT-ASSERT-002
title: contract assertions metric is non-regressing
purpose: Enforces monotonic non-regression for contract assertions metrics against checked-in
  baseline.
type: contract.check
harness:
  root: .
  contract_assertions_non_regression:
    baseline_path: /specs/metrics/contract_assertions_baseline.json
    summary_fields:
      overall_contract_assertions_ratio: non_decrease
      overall_required_token_coverage_ratio: non_decrease
      contract_must_coverage_ratio: non_decrease
      token_sync_ratio: non_decrease
    epsilon: 1.0e-12
    contract_assertions:
      paths:
      - specs/contract/03_assertions.md
      - specs/schema/schema_v1.md
      - docs/book/03_assertions.md
      - specs/contract/03b_spec_lang_v1.md
  check:
    profile: governance.scan
    config:
      check: spec.contract_assertions_non_regression
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    target: summary_json
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - spec.contract_assertions_non_regression
```
