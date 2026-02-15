# Governance Cases

## SRGOV-CONF-STYLE-001

```yaml spec-test
id: SRGOV-CONF-STYLE-001
title: conformance case documents satisfy style and purpose lint rules
purpose: Ensures conformance fixtures remain readable, deterministic, and policy-compliant.
type: governance.check
check: conformance.case_doc_style_guard
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
      - conformance.case_doc_style_guard
```
