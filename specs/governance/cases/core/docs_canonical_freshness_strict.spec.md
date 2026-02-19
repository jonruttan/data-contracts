# Governance Cases

## SRGOV-DOCS-CANON-003

```yaml contract-spec
id: SRGOV-DOCS-CANON-003
title: docs freshness strict checker passes
purpose: Ensures specs freshness checks are strict, deterministic, and currently clean.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.canonical_freshness_strict
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
```
