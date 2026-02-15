# Governance Cases

## SRGOV-CONTRACT-001

```yaml spec-test
id: SRGOV-CONTRACT-001
title: contract governance rules pass via governance harness
purpose: Ensures contract policy and traceability integrity checks are enforced through the governance spec pipeline.
type: governance.check
check: contract.governance_check
harness:
  root: .
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - subject: []
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - subject: []
        - passed
      - true
    - eq:
      - get:
        - subject: []
        - check_id
      - contract.governance_check
```
