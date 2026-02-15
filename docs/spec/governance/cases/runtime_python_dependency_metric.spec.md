# Governance Cases

## SRGOV-RUNTIME-PYDEP-001

```yaml spec-test
id: SRGOV-RUNTIME-PYDEP-001
title: python dependency metric report generation is valid
purpose: Ensures python dependency metric report is generated with required summary fields and deterministic structure.
type: governance.check
check: runtime.python_dependency_metric
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  python_dependency:
    policy_evaluate:
    - and:
      - {has_key: [{ref: subject}, summary]}
      - has_key:
        - {get: [{ref: subject}, summary]}
        - non_python_lane_python_exec_count
      - has_key:
        - {get: [{ref: subject}, summary]}
        - transitive_adapter_python_exec_count
      - has_key:
        - {get: [{ref: subject}, summary]}
        - default_lane_python_free_ratio
      - has_key:
        - {get: [{ref: subject}, summary]}
        - python_usage_scope_violation_count
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
      - runtime.python_dependency_metric
```
