# Governance Cases

## SRGOV-OPS-003

```yaml contract-spec
id: SRGOV-OPS-003
title: orchestration ops registries are synchronized and complete
purpose: Ensures runner tool registries include required fields and declared tool ids.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: orchestration.ops_registry_sync
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
      key: summary_json
  steps:
  - id: assert_1
    assert:
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
```
