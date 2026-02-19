# Governance Cases

## SRGOV-RUNTIME-CONTRACT-BLOCK-001

```yaml contract-spec
id: SRGOV-RUNTIME-CONTRACT-BLOCK-001
title: cases must use contract block
purpose: Enforces top-level contract block requirement for executable cases.
type: contract.check
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
    as:
      violation_count: subject
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
harness:
  check:
    profile: governance.scan
    config:
      check: runtime.case_contract_block_required
```
