# Governance Cases

## SRGOV-DOCS-GEN-004

```yaml spec-test
id: SRGOV-DOCS-GEN-004
title: runner api catalog artifacts are synchronized
purpose: Ensures generated runner API JSON and markdown artifacts are up-to-date.
type: governance.check
check: docs.runner_api_catalog_sync
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
      - docs.runner_api_catalog_sync
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
```
