# Governance Cases

## SRGOV-RUNTIME-CONFIG-001

```yaml spec-test
id: SRGOV-RUNTIME-CONFIG-001
title: runtime python code does not duplicate governed config literals
purpose: Enforces centralized configuration by rejecting duplicated governed literals in runtime python sources.
type: governance.check
check: runtime.config_literals
harness:
  root: .
  policy_evaluate:
  - is_empty:
    - {get: [{subject: []}, violations]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - runtime.config_literals
```
