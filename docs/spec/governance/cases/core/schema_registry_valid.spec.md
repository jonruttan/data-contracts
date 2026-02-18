# Governance Cases

## SRGOV-SCHEMA-REG-001

```yaml contract-spec
id: SRGOV-SCHEMA-REG-001
title: schema registry model is present and valid
purpose: Ensures schema registry source files and contract docs are present and compile without
  registry errors.
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
      check: schema.registry_valid
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        MUST:
        - std.logic.eq:
          - std.object.get:
            - {var: subject}
            - check_id
          - schema.registry_valid
        - std.logic.eq:
          - std.object.get:
            - {var: subject}
            - passed
          - true
  target: summary_json
```
