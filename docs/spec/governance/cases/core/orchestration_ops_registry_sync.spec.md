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
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - orchestration.ops_registry_sync
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
