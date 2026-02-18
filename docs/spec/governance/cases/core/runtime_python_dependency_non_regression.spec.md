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
    baseline_path: /docs/spec/metrics/python_dependency_baseline.json
    summary_fields:
      non_python_lane_python_exec_count: non_increase
      transitive_adapter_python_exec_count: non_increase
      python_usage_scope_violation_count: non_increase
      default_lane_python_free_ratio: non_decrease
    segment_fields: {}
    epsilon: 1.0e-12
    python_dependency: {}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.python_dependency_non_regression
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        std.logic.eq:
        - {var: subject}
        - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - evaluate:
    - lit:
        MUST:
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
  target: summary_json
```
