# Governance Cases

## SRGOV-SCHEMA-REG-002

```yaml spec-test
id: SRGOV-SCHEMA-REG-002
title: schema registry docs snapshot is synchronized
purpose: Ensures schema_v1 markdown contains synchronized generated registry snapshot markers
  and tokens.
type: governance.check
check: schema.registry_docs_sync
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - schema.registry_docs_sync
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
