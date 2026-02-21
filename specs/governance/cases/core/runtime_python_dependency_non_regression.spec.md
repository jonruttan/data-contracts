```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-PYDEP-002
  title: python dependency metric is non-regressing
  purpose: Enforces monotonic non-regression for python dependency metrics against checked-in baseline.
  harness:
    root: "."
    python_dependency_non_regression:
      baseline_path: "/specs/governance/metrics/python_dependency_baseline.json"
      summary_fields:
        non_python_lane_python_exec_count: non_increase
        transitive_adapter_python_exec_count: non_increase
        python_usage_scope_violation_count: non_increase
        default_lane_python_free_ratio: non_decrease
      segment_fields: {}
      epsilon: 1.0e-12
      python_dependency: {}
    check:
      profile: governance.scan
      config:
        check: runtime.compatibility_python_lane_dependency_non_regression
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
        - runtime.compatibility_python_lane_dependency_non_regression
      imports:
      - from: artifact
        names:
        - summary_json
```
