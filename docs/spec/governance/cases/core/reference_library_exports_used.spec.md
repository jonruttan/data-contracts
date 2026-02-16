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
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - reference.library_exports_used
```
