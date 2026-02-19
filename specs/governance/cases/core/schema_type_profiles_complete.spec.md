# Governance Cases

## SRGOV-SCHEMA-REG-005

```yaml contract-spec
id: SRGOV-SCHEMA-REG-005
title: required schema type profiles exist
purpose: Ensures required type profiles are defined in registry for core runtime case types.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: schema.type_profiles_complete
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
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
    imports:
      subject:
        from: artifact
        key: summary_json
```
