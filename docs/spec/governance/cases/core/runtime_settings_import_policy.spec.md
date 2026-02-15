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
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - {call: [{var: policy.pass_when_no_violations}, {var: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{var: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{var: subject}, passed]}
      - true
    - eq:
      - {get: [{var: subject}, check_id]}
      - runtime.settings_import_policy
```
