# Governance Cases

## SRGOV-DOCS-QUAL-002

```yaml spec-test
id: SRGOV-DOCS-QUAL-002
title: reference index is generated from manifest
purpose: Ensures reference index markdown remains synchronized with the manifest source of
  truth.
type: governance.check
check: docs.reference_manifest_sync
harness:
  root: .
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
    index_out: /docs/book/reference_index.md
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
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.reference_manifest_sync
  target: summary_json
```
