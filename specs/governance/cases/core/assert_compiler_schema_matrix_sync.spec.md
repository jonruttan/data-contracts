# Governance Cases

## SRGOV-ASSERT-SYNC-001

```yaml contract-spec
id: SRGOV-ASSERT-SYNC-001
title: compiler behavior stays aligned with universal assertion contract
purpose: Ensures compiler operator handling, schema wording, and assertion contract wording
  stay synchronized for universal evaluate core semantics.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: assert.compiler_schema_matrix_sync
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
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
      - assert.compiler_schema_matrix_sync
    imports:
      subject:
        from: artifact
        key: summary_json
```
