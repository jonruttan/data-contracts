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
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - {call: [{var: [policy.pass_when_no_violations]}, {ref: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{ref: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{ref: subject}, passed]}
      - true
    - eq:
      - {get: [{ref: subject}, check_id]}
      - pending.no_resolved_markers
```
