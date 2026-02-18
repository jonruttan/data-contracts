# Governance Cases

## SRGOV-RUNTIME-CONTRACT-BLOCK-002

```yaml contract-spec
id: SRGOV-RUNTIME-CONTRACT-BLOCK-002
title: legacy assert block is forbidden
purpose: Enforces hard-cut removal of top-level assert key from executable cases.
type: governance.check
check: runtime.legacy_assert_block_forbidden
contract:
- id: assert_1
  class: MUST
  target: violation_count
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
```
