# Governance Cases

## SRGOV-OPS-003

```yaml spec-test
id: SRGOV-OPS-003
title: orchestration ops registries are synchronized and complete
purpose: Ensures runner tool registries include required fields and declared tool ids.
type: governance.check
check: orchestration.ops_registry_sync
harness:
  root: .
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
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - orchestration.ops_registry_sync
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
