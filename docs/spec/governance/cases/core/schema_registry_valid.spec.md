# Governance Cases

## SRGOV-SCHEMA-REG-001

```yaml spec-test
id: SRGOV-SCHEMA-REG-001
title: schema registry model is present and valid
purpose: Ensures schema registry source files and contract docs are present and compile without
  registry errors.
type: governance.check
check: schema.registry_valid
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
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - schema.registry_valid
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
