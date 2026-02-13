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
assert:
  - target: text
    must:
      - contain: ["PASS: runtime.settings_import_policy"]
```
