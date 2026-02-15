# Governance Cases

## SRGOV-RUNTIME-PYDEP-002

```yaml spec-test
id: SRGOV-RUNTIME-PYDEP-002
title: python dependency metric is non-regressing
purpose: Enforces monotonic non-regression for python dependency metrics against checked-in baseline.
type: governance.check
check: runtime.python_dependency_non_regression
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  python_dependency_non_regression:
    baseline_path: docs/spec/metrics/python_dependency_baseline.json
    summary_fields:
      non_python_lane_python_exec_count: non_increase
      transitive_adapter_python_exec_count: non_increase
      python_usage_scope_violation_count: non_increase
      default_lane_python_free_ratio: non_decrease
    segment_fields: {}
    epsilon: 1.0e-12
    python_dependency: {}
  policy_evaluate:
  - {call: [{var: [policy.pass_when_no_violations]}, {subject: []}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - runtime.python_dependency_non_regression
```
