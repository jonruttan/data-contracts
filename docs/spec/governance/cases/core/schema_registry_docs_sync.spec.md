# Governance Cases

## SRGOV-SCHEMA-REG-002

```yaml spec-test
id: SRGOV-SCHEMA-REG-002
title: schema registry docs snapshot is synchronized
purpose: Ensures schema_v1 markdown contains synchronized generated registry snapshot markers and tokens.
type: governance.check
check: schema.registry_docs_sync
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
      - schema.registry_docs_sync
    - eq:
      - {get: [{var: subject}, passed]}
      - true
```
