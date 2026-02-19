# Governance Cases

## SRGOV-PENDING-001

```yaml contract-spec
id: SRGOV-PENDING-001
title: pending specs remain draft-only and must not include resolved/completed markers
purpose: Ensures pending-spec files do not retain completed markers and keeps completed work
  out of pending.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: pending.no_resolved_markers
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
      - pending.no_resolved_markers
```
