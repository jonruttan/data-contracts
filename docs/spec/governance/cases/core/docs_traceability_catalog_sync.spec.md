# Governance Cases

## SRGOV-DOCS-GEN-008

```yaml spec-test
id: SRGOV-DOCS-GEN-008
title: traceability catalog artifacts are synchronized
purpose: Ensures generated traceability catalog JSON and markdown artifacts are up-to-date.
type: governance.check
check: docs.traceability_catalog_sync
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
      - docs.traceability_catalog_sync
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
