# Governance Cases

## SRGOV-LIB-INDEX-001

```yaml spec-test
id: SRGOV-LIB-INDEX-001
title: library domain indexes are synchronized
purpose: Ensures each library domain index lists all library files and exported symbols without stale entries.
type: governance.check
check: library.domain_index_sync
harness:
  root: .
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - {call: [{var: policy.pass_when_no_violations}, {var: subject}]}
assert:
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{var: subject}, check_id]}
      - library.domain_index_sync
```
