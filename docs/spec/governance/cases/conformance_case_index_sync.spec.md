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
      - conformance.case_index_sync
```
