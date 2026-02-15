# Governance Cases

## SRGOV-CONF-PURPOSE-001

```yaml spec-test
id: SRGOV-CONF-PURPOSE-001
title: purpose warning code doc stays in sync with implementation codes
purpose: Ensures docs for purpose warning codes include all implementation codes and no stale entries.
type: governance.check
check: conformance.purpose_warning_codes_sync
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
      - conformance.purpose_warning_codes_sync
```
