# Governance Cases

## SRGOV-REF-PATHS-001

```yaml spec-test
id: SRGOV-REF-PATHS-001
title: contract paths referenced by specs exist
purpose: Ensures referenced contract-root paths fail fast when missing.
type: governance.check
check: reference.contract_paths_exist
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
      - reference.contract_paths_exist
```
