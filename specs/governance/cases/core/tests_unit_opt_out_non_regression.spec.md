```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-TEST-UNIT-OPT-OUT-001
  title: unit test opt-out usage is measured and non-regressing
  purpose: Tracks unit-test opt-out usage and enforces a non-regression baseline so opt-out coverage is reduced over time.
  harness:
    root: "."
    check:
      profile: governance.scan
      config:
        check: tests.unit_opt_out_non_regression
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
      - summary_json
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.summary_check_id
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
        - tests.unit_opt_out_non_regression
```
