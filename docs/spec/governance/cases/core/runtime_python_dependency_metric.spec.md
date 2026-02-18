# Governance Cases

## SRGOV-RUNTIME-PYDEP-001

```yaml contract-spec
id: SRGOV-RUNTIME-PYDEP-001
title: python dependency metric report generation is valid
purpose: Ensures python dependency metric report is generated with required summary
  fields and deterministic structure.
type: governance.check
check: runtime.python_dependency_metric
harness:
  root: .
  python_dependency:
    policy_evaluate:
    - std.logic.and:
      - std.object.has_key:
        - var: subject
        - summary
      - std.object.has_key:
        - std.object.get:
          - var: subject
          - summary
        - non_python_lane_python_exec_count
      - std.object.has_key:
        - std.object.get:
          - var: subject
          - summary
        - transitive_adapter_python_exec_count
      - std.object.has_key:
        - std.object.get:
          - var: subject
          - summary
        - default_lane_python_free_ratio
      - std.object.has_key:
        - std.object.get:
          - var: subject
          - summary
        - python_usage_scope_violation_count
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - runtime.python_dependency_metric
  target: summary_json
```
