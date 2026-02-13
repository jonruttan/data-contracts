# Governance Cases

## SRGOV-CONF-INDEX-001

```yaml spec-test
id: SRGOV-CONF-INDEX-001
title: conformance README index stays in sync with fixture ids
purpose: Ensures conformance case index includes all fixture ids and no stale ids.
type: governance.check
check: conformance.case_index_sync
harness:
  root: .
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.case_index_sync"]
```
