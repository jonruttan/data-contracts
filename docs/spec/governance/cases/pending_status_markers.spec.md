# Governance Cases

## SRGOV-PENDING-001

```yaml spec-test
id: SRGOV-PENDING-001
title: pending specs remain draft-only and must not include resolved/completed markers
purpose: Ensures pending-spec files do not retain completed markers and keeps completed work out of pending.
type: governance.check
check: pending.no_resolved_markers
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
      - pending.no_resolved_markers
```
