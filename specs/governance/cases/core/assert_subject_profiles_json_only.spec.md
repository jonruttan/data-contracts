# Governance Cases

## SRGOV-ASSERT-PROFILE-002

```yaml contract-spec
id: SRGOV-ASSERT-PROFILE-002
title: evaluator and schema enforce json-core subjects
purpose: Ensures subject profile schema and evaluator enforce JSON-core subject values.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: assert.subject_profiles_json_only
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
```
