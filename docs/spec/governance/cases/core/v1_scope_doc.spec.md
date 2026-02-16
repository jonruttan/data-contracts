# Governance Cases

## SRGOV-DOC-V1-001

```yaml spec-test
id: SRGOV-DOC-V1-001
title: v1 scope contract doc exists and includes required sections
purpose: Ensures v1 scope and compatibility commitments remain explicit and discoverable.
type: governance.check
check: docs.v1_scope_contract
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - docs.v1_scope_contract
```
