# Governance Cases

## SRGOV-REF-SYMBOLS-003

```yaml spec-test
id: SRGOV-REF-SYMBOLS-003
title: library exports are referenced
purpose: Ensures exported library symbols are referenced by case policies/expressions or harness
  exports.
type: governance.check
check: reference.library_exports_used
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
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - reference.library_exports_used
  target: summary_json
```
