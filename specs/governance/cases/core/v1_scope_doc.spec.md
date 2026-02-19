# Governance Cases

## SRGOV-DOC-V1-001

```yaml contract-spec
id: SRGOV-DOC-V1-001
title: v1 scope contract doc exists and includes required sections
purpose: Ensures v1 scope and compatibility commitments remain explicit and discoverable.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.v1_scope_contract
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
    'on': violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    'on': summary_json
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
      - docs.v1_scope_contract
```
