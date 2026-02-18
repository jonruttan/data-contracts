# Governance Cases

## SRGOV-ASSERT-PROFILE-002

```yaml contract-spec
id: SRGOV-ASSERT-PROFILE-002
title: evaluator and schema enforce json-core subjects
purpose: Ensures subject profile schema and evaluator enforce JSON-core subject values.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: assert.subject_profiles_json_only
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
```
