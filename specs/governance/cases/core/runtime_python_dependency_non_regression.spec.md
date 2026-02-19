# Governance Cases

## SRGOV-RUNTIME-PYDEP-002

```yaml contract-spec
id: SRGOV-RUNTIME-PYDEP-002
title: python dependency metric is non-regressing
purpose: Enforces monotonic non-regression for python dependency metrics against checked-in
  baseline.
type: contract.check
harness:
  root: .
  python_dependency_non_regression:
    baseline_path: /specs/metrics/python_dependency_baseline.json
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
      check: runtime.python_dependency_non_regression
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
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
  - id: assert_2
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
      - runtime.python_dependency_non_regression
    imports:
      subject:
        from: artifact
        key: summary_json
```
