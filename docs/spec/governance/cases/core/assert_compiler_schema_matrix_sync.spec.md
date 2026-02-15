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
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - assert.compiler_schema_matrix_sync
```
