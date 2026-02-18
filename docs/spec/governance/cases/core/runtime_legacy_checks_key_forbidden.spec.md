# Governance Cases

## SRGOV-RUNTIME-CONTRACT-STEP-002

```yaml contract-spec
id: SRGOV-RUNTIME-CONTRACT-STEP-002
title: legacy checks key is forbidden in contract trees
purpose: Enforces hard-cut rename checks to asserts for step-form contract entries.
type: governance.check
check: runtime.legacy_checks_key_forbidden
contract:
- id: assert_1
  class: MUST
  target: violation_count
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
```
