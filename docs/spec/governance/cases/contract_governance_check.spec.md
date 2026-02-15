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
- target: text
  must:
  - contain:
    - 'PASS: contract.governance_check'
```
