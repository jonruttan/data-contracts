# Governance Cases

## SRGOV-DOC-CURRENT-001

```yaml spec-test
id: SRGOV-DOC-CURRENT-001
title: current-spec-only contract forbids prior-schema references and shims
purpose: Ensures pre-v1 docs and parser paths stay focused on current schema only, without prior-spec wording or compatibility rewrites.
type: governance.check
check: docs.current_spec_only_contract
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
      - docs.current_spec_only_contract
```
