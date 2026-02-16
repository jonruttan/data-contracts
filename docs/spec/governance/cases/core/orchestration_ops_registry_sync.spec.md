# Governance Cases

## SRGOV-OPS-003

```yaml spec-test
id: SRGOV-OPS-003
title: orchestration ops registries are synchronized and complete
purpose: Ensures runner tool registries include required fields and declared tool ids.
type: governance.check
check: orchestration.ops_registry_sync
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
    - eq:
      - get:
        - {var: subject}
        - check_id
      - orchestration.ops_registry_sync
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
```
