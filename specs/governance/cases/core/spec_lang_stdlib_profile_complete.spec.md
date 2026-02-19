# Governance Cases

## SRGOV-STDLIB-001

```yaml contract-spec
id: SRGOV-STDLIB-001
title: spec-lang stdlib profile is complete
purpose: Ensures the declared stdlib profile symbols are implemented in Python and PHP.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: spec_lang.stdlib_profile_complete
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
```
