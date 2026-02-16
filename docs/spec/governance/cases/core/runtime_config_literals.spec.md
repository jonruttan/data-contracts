# Governance Cases

## SRGOV-RUNTIME-CONFIG-001

```yaml spec-test
id: SRGOV-RUNTIME-CONFIG-001
title: runtime python code does not duplicate governed config literals
purpose: Enforces centralized configuration by rejecting duplicated governed literals in runtime
  python sources.
type: governance.check
check: runtime.config_literals
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
      - runtime.config_literals
```
