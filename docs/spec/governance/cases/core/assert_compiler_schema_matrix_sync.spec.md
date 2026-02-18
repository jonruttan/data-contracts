# Governance Cases

## SRGOV-ASSERT-SYNC-001

```yaml contract-spec
id: SRGOV-ASSERT-SYNC-001
title: compiler behavior stays aligned with universal assertion contract
purpose: Ensures compiler operator handling, schema wording, and assertion contract
  wording stay synchronized for universal evaluate core semantics.
type: governance.check
check: assert.compiler_schema_matrix_sync
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
- id: assert_2
  class: MUST
  asserts:
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - assert.compiler_schema_matrix_sync
  target: summary_json
```
