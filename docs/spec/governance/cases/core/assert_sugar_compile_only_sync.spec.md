# Governance Cases

## SRGOV-ASSERT-COMPILE-001

```yaml spec-test
id: SRGOV-ASSERT-COMPILE-001
title: compiler keeps sugar operators compile-only
purpose: Ensures compiler and runtime assertion path keep non-evaluate operators as compile-only
  sugar with spec-lang execution.
type: governance.check
check: assert.sugar_compile_only_sync
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
      - assert.sugar_compile_only_sync
```
