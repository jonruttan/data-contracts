# Governance Cases

## SRGOV-RUNTIME-CONFIG-001

```yaml contract-spec
id: SRGOV-RUNTIME-CONFIG-001
title: runtime python code does not duplicate governed config literals
purpose: Enforces centralized configuration by rejecting duplicated governed literals in runtime
  python sources.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.config_literals
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
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
      - runtime.config_literals
    imports:
      subject:
        from: artifact
        key: summary_json
```
