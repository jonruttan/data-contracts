# Governance Cases

## SRGOV-DOCS-GEN-011

```yaml spec-test
id: SRGOV-DOCS-GEN-011
title: spec schema field catalog artifacts are synchronized
purpose: Ensures generated spec schema field catalog JSON and markdown artifacts are up-to-date.
type: governance.check
check: docs.spec_schema_field_catalog_sync
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
      - docs.spec_schema_field_catalog_sync
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
