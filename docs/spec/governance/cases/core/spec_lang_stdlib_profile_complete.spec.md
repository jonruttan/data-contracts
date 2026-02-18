# Governance Cases

## SRGOV-STDLIB-001

```yaml contract-spec
id: SRGOV-STDLIB-001
title: spec-lang stdlib profile is complete
purpose: Ensures the declared stdlib profile symbols are implemented in Python and PHP.
type: governance.check
check: spec_lang.stdlib_profile_complete
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
