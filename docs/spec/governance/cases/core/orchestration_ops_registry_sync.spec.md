# Governance Cases

## SRGOV-OPS-003

```yaml contract-spec
id: SRGOV-OPS-003
title: orchestration ops registries are synchronized and complete
purpose: Ensures runner tool registries include required fields and declared tool ids.
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
      check: orchestration.ops_registry_sync
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          MUST:
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
  target: summary_json
```
