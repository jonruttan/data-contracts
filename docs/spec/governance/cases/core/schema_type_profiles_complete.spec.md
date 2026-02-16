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
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - schema.type_profiles_complete
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
