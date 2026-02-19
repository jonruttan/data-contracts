# Governance Cases

## SRGOV-OPS-004

```yaml contract-spec
id: SRGOV-OPS-004
title: orchestration ops capability bindings are enforced
purpose: Ensures orchestration tools and case capability bindings remain synchronized.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: orchestration.ops_capability_bindings
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
    target: summary_json
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - orchestration.ops_capability_bindings
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
