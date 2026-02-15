# Governance Cases

## SRGOV-CONTRACT-001

```yaml spec-test
id: SRGOV-CONTRACT-001
title: contract governance rules pass via governance harness
purpose: Ensures contract policy and traceability integrity checks are enforced through the
  governance spec pipeline.
type: governance.check
check: contract.governance_check
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
      - contract.governance_check
```
