# Governance Cases

## SRGOV-ASSERT-COMPILE-001

```yaml spec-test
id: SRGOV-ASSERT-COMPILE-001
title: compiler keeps sugar operators compile-only
purpose: Ensures compiler and runtime assertion path keep non-evaluate operators as compile-only sugar with spec-lang execution.
type: governance.check
check: assert.sugar_compile_only_sync
harness:
  root: .
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: assert.sugar_compile_only_sync'
```
