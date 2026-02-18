# Governance Cases

## SRGOV-ASSERT-PROFILE-001

```yaml contract-spec
id: SRGOV-ASSERT-PROFILE-001
title: subject profile contract artifacts are declared
purpose: Ensures subject profile contract/schema/type docs and domain libraries are
  present as required artifacts.
type: governance.check
check: assert.subject_profiles_declared
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
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
