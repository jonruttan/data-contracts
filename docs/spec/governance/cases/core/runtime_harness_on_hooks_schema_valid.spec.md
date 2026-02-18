# Governance Cases

## SRGOV-RUNTIME-HOOKS-001

```yaml contract-spec
id: SRGOV-RUNTIME-HOOKS-001
title: harness.on hooks schema must be valid
purpose: Enforces harness.on shape and hook expression list requirements.
type: governance.check
check: runtime.harness_on_hooks_schema_valid
harness:
  root: .
contract:
- id: assert_1
  class: must
  target: violation_count
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
```
