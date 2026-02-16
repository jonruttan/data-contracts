# Governance Cases

## SRGOV-DOCS-QUAL-001

```yaml spec-test
id: SRGOV-DOCS-QUAL-001
title: docs metadata schema is valid for canonical reference chapters
purpose: Ensures each canonical reference chapter contains valid machine-checkable doc metadata.
type: governance.check
check: docs.meta_schema_valid
harness:
  root: .
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.meta_schema_valid
```
