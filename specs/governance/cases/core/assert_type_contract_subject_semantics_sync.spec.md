# Governance Cases

## SRGOV-ASSERT-SUBJECT-001

```yaml contract-spec
id: SRGOV-ASSERT-SUBJECT-001
title: type contracts define subject semantics
purpose: Ensures harness and type contracts define target subject semantics and avoid per-type
  operator allowlists.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: assert.type_contract_subject_semantics_sync
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
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
  - id: assert_2
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
      - assert.type_contract_subject_semantics_sync
    imports:
      subject:
        from: artifact
        key: summary_json
```
