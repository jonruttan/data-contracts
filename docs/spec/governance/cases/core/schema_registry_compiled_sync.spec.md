# Governance Cases

## SRGOV-SCHEMA-REG-003

```yaml spec-test
id: SRGOV-SCHEMA-REG-003
title: schema registry compiled artifact is synchronized
purpose: Ensures checked-in schema registry compiled artifact matches current registry source files.
type: governance.check
check: schema.registry_compiled_sync
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
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{var: subject}, check_id]}
      - schema.registry_compiled_sync
    - eq:
      - {get: [{var: subject}, passed]}
      - true
```
