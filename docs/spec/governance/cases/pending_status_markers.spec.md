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
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: pending.no_resolved_markers'
```
