# Governance Cases

## SRGOV-SCHEMA-REG-003

```yaml spec-test
id: SRGOV-SCHEMA-REG-003
title: schema registry compiled artifact is synchronized
purpose: Ensures checked-in schema registry compiled artifact matches current registry source
  files.
type: governance.check
check: schema.registry_compiled_sync
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
      - schema.registry_compiled_sync
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
