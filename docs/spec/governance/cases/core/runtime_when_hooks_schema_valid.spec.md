# Governance Cases

## SRGOV-RUNTIME-HOOKS-001

```yaml contract-spec
id: SRGOV-RUNTIME-HOOKS-001
title: when hooks schema must be valid
purpose: Enforces when shape and hook expression list requirements.
type: governance.check
check: runtime.when_hooks_schema_valid
harness:
  root: .
contract:
- id: assert_1
  class: MUST
  target: violation_count
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
```
