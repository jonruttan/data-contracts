# Governance Cases

## SRGOV-DOCS-GEN-006

```yaml spec-test
id: SRGOV-DOCS-GEN-006
title: spec lang builtin catalog artifacts are synchronized
purpose: Ensures generated spec-lang builtin JSON and markdown artifacts are up-to-date.
type: governance.check
check: docs.spec_lang_builtin_catalog_sync
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
      - docs.spec_lang_builtin_catalog_sync
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
```
