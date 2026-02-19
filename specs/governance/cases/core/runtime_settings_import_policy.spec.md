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
  check:
    profile: governance.scan
    config:
      check: runtime.settings_import_policy
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
    target: violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    target: summary_json
    assert:
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
```
