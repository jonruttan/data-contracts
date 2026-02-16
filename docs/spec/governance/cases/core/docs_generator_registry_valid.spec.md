# Governance Cases

## SRGOV-DOCS-GEN-001

```yaml spec-test
id: SRGOV-DOCS-GEN-001
title: docs generator registry is valid and complete
purpose: Ensures docs generator registry exists, validates, and includes required surfaces.
type: governance.check
check: docs.generator_registry_valid
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
      - docs.generator_registry_valid
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
```
