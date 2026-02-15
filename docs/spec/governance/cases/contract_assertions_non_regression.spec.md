# Governance Cases

## SRGOV-CONTRACT-ASSERT-002

```yaml spec-test
id: SRGOV-CONTRACT-ASSERT-002
title: contract assertions metric is non-regressing
purpose: Enforces monotonic non-regression for contract assertions metrics against checked-in baseline.
type: governance.check
check: spec.contract_assertions_non_regression
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  contract_assertions_non_regression:
    baseline_path: docs/spec/metrics/contract_assertions_baseline.json
    summary_fields:
      overall_contract_assertions_ratio: non_decrease
      overall_required_token_coverage_ratio: non_decrease
      contract_must_coverage_ratio: non_decrease
      token_sync_ratio: non_decrease
    epsilon: 1.0e-12
    contract_assertions:
      paths:
      - docs/spec/contract/03_assertions.md
      - docs/spec/schema/schema_v1.md
      - docs/book/03_assertions.md
      - docs/spec/contract/03b_spec_lang_v1.md
  policy_evaluate:
  - {call: [{var: [policy.pass_when_no_violations]}, {ref: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{ref: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{ref: subject}, passed]}
      - true
    - eq:
      - {get: [{ref: subject}, check_id]}
      - spec.contract_assertions_non_regression
```
