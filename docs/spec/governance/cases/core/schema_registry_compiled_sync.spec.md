# Governance Cases

## SRGOV-SCHEMA-REG-003

```yaml contract-spec
id: SRGOV-SCHEMA-REG-003
title: schema registry compiled artifact is synchronized
purpose: Ensures checked-in schema registry compiled artifact matches current registry source
  files.
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
      check: schema.registry_compiled_sync
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            MUST:
            - std.logic.eq:
              - std.object.get:
                - {var: subject}
                - check_id
              - schema.registry_compiled_sync
            - std.logic.eq:
              - std.object.get:
                - {var: subject}
                - passed
              - true
  target: summary_json
```
