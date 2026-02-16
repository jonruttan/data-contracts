# Governance Cases

## SRGOV-ASSERT-SYNC-001

```yaml spec-test
id: SRGOV-ASSERT-SYNC-001
title: compiler behavior stays aligned with universal assertion contract
purpose: Ensures compiler operator handling, schema wording, and assertion contract wording
  stay synchronized for universal evaluate core semantics.
type: governance.check
check: assert.compiler_schema_matrix_sync
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
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - assert.compiler_schema_matrix_sync
```
