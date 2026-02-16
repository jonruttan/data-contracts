# Governance Cases

## SRGOV-DOCS-GEN-007

```yaml spec-test
id: SRGOV-DOCS-GEN-007
title: policy rule catalog artifacts are synchronized
purpose: Ensures generated policy rule JSON and markdown artifacts are up-to-date.
type: governance.check
check: docs.policy_rule_catalog_sync
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
      - docs.policy_rule_catalog_sync
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
```
