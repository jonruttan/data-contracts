# Governance Cases

## SRGOV-SPECLAYOUT-INDEX-001

```yaml spec-test
id: SRGOV-SPECLAYOUT-INDEX-001
title: spec domain indexes are synchronized
purpose: Ensures each domain index tracks all spec files in its subtree and has no stale paths.
type: governance.check
check: spec.domain_index_sync
harness:
  root: .
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - check_id
      - spec.domain_index_sync
```
