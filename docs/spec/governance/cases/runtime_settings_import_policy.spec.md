# Governance Cases

## SRGOV-RUNTIME-IMPORT-001

```yaml spec-test
id: SRGOV-RUNTIME-IMPORT-001
title: runtime python code uses SETTINGS object instead of settings constants
purpose: Enforces settings access policy by rejecting DEFAULT and ENV constant imports outside settings module.
type: governance.check
check: runtime.settings_import_policy
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
      - runtime.settings_import_policy
```
