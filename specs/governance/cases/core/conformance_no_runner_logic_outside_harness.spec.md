# Governance Cases

## SRGOV-CONF-PORT-001

```yaml contract-spec
id: SRGOV-CONF-PORT-001
title: conformance cases keep runner logic under harness
purpose: Ensures portable conformance fixtures do not place runner/setup keys at top level.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: conformance.no_runner_logic_outside_harness
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
      - conformance.no_runner_logic_outside_harness
```
