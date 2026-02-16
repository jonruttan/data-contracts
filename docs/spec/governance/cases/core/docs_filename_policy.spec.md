# Governance Cases

## SRGOV-DOCS-LAYOUT-003

```yaml spec-test
id: SRGOV-DOCS-LAYOUT-003
title: docs filenames follow canonical lowercase policy
purpose: Enforces lowercase, underscore, and hyphen filename policy across docs.
type: governance.check
check: docs.filename_policy
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
      - docs.filename_policy
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
```
