# Governance Cases

## SRGOV-DOCS-CANON-003

```yaml contract-spec
id: SRGOV-DOCS-CANON-003
title: docs freshness strict checker passes
purpose: Ensures docs/spec freshness checks are strict, deterministic, and currently clean.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.canonical_freshness_strict
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
```
