# Governance Cases

## SRGOV-NORM-001

```yaml spec-test
id: SRGOV-NORM-001
title: normalization profile defines required source-of-truth fields
purpose: Ensures normalization profile exists and includes all required top-level keys and path scopes.
type: governance.check
check: normalization.profile_sync
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
      - normalization.profile_sync
```
