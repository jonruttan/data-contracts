# Governance Cases

## SRGOV-RUNTIME-IMPORT-001

```yaml contract-spec
id: SRGOV-RUNTIME-IMPORT-001
title: runtime python code uses SETTINGS object instead of settings constants
purpose: Enforces settings access policy by rejecting DEFAULT and ENV constant imports outside
  settings module.
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
      check: runtime.settings_import_policy
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          MUST:
          - std.logic.eq:
            - std.object.get:
              - {var: subject}
              - passed
            - true
          - std.logic.eq:
            - std.object.get:
              - {var: subject}
              - check_id
            - runtime.settings_import_policy
  target: summary_json
```
