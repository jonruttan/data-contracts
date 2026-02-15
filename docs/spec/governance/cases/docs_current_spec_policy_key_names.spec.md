# Governance Cases

## SRGOV-DOCS-CURRENT-KEYS-001

```yaml spec-test
id: SRGOV-DOCS-CURRENT-KEYS-001
title: current spec policy key names stay canonical
purpose: Enforces policy expression naming consistency by allowing only `policy_evaluate` in `.spec.md` cases.
type: governance.check
check: docs.current_spec_policy_key_names
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
    - 'PASS: docs.current_spec_policy_key_names'
```
