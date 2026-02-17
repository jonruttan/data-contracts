# Governance Cases

## SRGOV-LIB-INDEX-001

```yaml spec-test
id: SRGOV-LIB-INDEX-001
title: library domain indexes are synchronized
purpose: Ensures each library domain index lists all library files and exported symbols without
  stale entries.
type: governance.check
check: library.domain_index_sync
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
    - std.object.get:
      - var: subject
      - check_id
    - library.domain_index_sync
  target: summary_json
```
