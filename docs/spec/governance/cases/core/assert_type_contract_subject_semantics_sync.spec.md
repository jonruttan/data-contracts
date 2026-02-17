# Governance Cases

## SRGOV-ASSERT-SUBJECT-001

```yaml spec-test
id: SRGOV-ASSERT-SUBJECT-001
title: type contracts define subject semantics
purpose: Ensures harness and type contracts define target subject semantics and avoid per-type
  operator allowlists.
type: governance.check
check: assert.type_contract_subject_semantics_sync
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
      - as: policy.pass_when_no_violations
        from: library.symbol
        required: true
        path: /policy.pass_when_no_violations
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - assert.type_contract_subject_semantics_sync
  target: summary_json
```
