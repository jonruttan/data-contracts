```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-CONTRACT-ASSERT-002
  title: contract assertions metric is non-regressing
  purpose: Enforces monotonic non-regression for contract assertions metrics against checked-in baseline.
  harness:
    root: "."
    contract_assertions_non_regression:
      baseline_path: "/specs/governance/metrics/contract_assertions_baseline.json"
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
        - docs/book/30_assertion_model.md
        - specs/contract/03b_spec_lang_v1.md
    check:
      profile: governance.scan
      config:
        check: spec.contract_assertions_non_regression
    use:
    - ref: "/specs/libraries/policy/policy_assertions.spec.md"
      as: lib_policy_core_spec
      symbols:
      - policy.assert.no_violations
      - policy.assert.summary_passed
      - policy.assert.summary_check_id
      - policy.assert.scan_pass
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.no_violations
        - std.object.assoc:
          - violation_count
          - var: violation_count
          - lit: {}
    - id: assert_2
      assert:
      - call:
        - var: policy.assert.summary_passed
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
      - call:
        - var: policy.assert.summary_check_id
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
        - spec.contract_assertions_non_regression
      imports:
      - from: artifact
        names:
        - summary_json
```
