# Governance Cases

## SRGOV-RUNTIME-CONTRACT-BLOCK-001

```yaml contract-spec
id: SRGOV-RUNTIME-CONTRACT-BLOCK-001
title: cases must use contract block
purpose: Enforces top-level contract block requirement for executable cases.
type: governance.check
check: runtime.case_contract_block_required
contract:
- id: assert_1
  class: MUST
  target: violation_count
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
```
