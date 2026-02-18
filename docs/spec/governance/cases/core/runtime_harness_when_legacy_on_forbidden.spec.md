# Governance Cases

## SRGOV-RUNTIME-HOOKS-005

```yaml contract-spec
id: SRGOV-RUNTIME-HOOKS-005
title: legacy harness.on key is forbidden
purpose: Enforces hard-cut lifecycle hook key migration to harness.when.
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
