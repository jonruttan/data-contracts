# Governance Cases

## SRGOV-SCHEMA-REG-005

```yaml spec-test
id: SRGOV-SCHEMA-REG-005
title: required schema type profiles exist
purpose: Ensures required type profiles are defined in registry for core runtime case types.
type: governance.check
check: schema.type_profiles_complete
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
      - schema.type_profiles_complete
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
