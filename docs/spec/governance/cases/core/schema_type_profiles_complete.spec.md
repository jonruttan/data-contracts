# Governance Cases

## SRGOV-SCHEMA-REG-005

```yaml contract-spec
id: SRGOV-SCHEMA-REG-005
title: required schema type profiles exist
purpose: Ensures required type profiles are defined in registry for core runtime case types.
type: contract.check
harness:
  root: .
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
      check: schema.type_profiles_complete
contract:
- id: assert_1
  class: MUST
  asserts:
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
  target: summary_json
```
