# Governance Cases

## SRGOV-STDLIB-003

```yaml spec-test
id: SRGOV-STDLIB-003
title: stdlib profile references are synchronized in schema contract and book docs
purpose: Ensures core docs reference the canonical stdlib profile artifacts.
type: governance.check
check: spec_lang.stdlib_docs_sync
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
```
