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
  policy_evaluate:
  - is_empty:
    - {get: [{subject: []}, violations]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - conformance.case_index_sync
```
