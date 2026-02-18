# Governance Cases

## SRGOV-ASSERT-COMPILE-001

```yaml contract-spec
id: SRGOV-ASSERT-COMPILE-001
title: compiler keeps sugar operators compile-only
purpose: Ensures compiler and runtime assertion path keep non-evaluate operators as compile-only
  sugar with spec-lang execution.
type: governance.check
check: assert.sugar_compile_only_sync
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
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  asserts:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - assert.sugar_compile_only_sync
  target: summary_json
```
