# Governance Cases

## SRGOV-RUNTIME-PYDEP-001

```yaml spec-test
id: SRGOV-RUNTIME-PYDEP-001
title: python dependency metric report generation is valid
purpose: Ensures python dependency metric report is generated with required summary fields
  and deterministic structure.
type: governance.check
check: runtime.python_dependency_metric
harness:
  root: .
  python_dependency:
    policy_evaluate:
    - std.logic.and:
      - std.object.has_key:
        - {var: subject}
        - summary
      - std.object.has_key:
        - std.object.get:
          - {var: subject}
          - summary
        - non_python_lane_python_exec_count
      - std.object.has_key:
        - std.object.get:
          - {var: subject}
          - summary
        - transitive_adapter_python_exec_count
      - std.object.has_key:
        - std.object.get:
          - {var: subject}
          - summary
        - default_lane_python_free_ratio
      - std.object.has_key:
        - std.object.get:
          - {var: subject}
          - summary
        - python_usage_scope_violation_count
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.python_dependency_metric
```
