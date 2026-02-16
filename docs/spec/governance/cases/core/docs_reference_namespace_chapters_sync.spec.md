# Governance Cases

## SRGOV-DOCS-GEN-025

```yaml spec-test
id: SRGOV-DOCS-GEN-025
title: spec lang namespace chapters are present and manifest-synced
purpose: Ensures generated namespace chapter files exist and are listed in the book manifest.
type: governance.check
check: docs.reference_namespace_chapters_sync
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
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.reference_namespace_chapters_sync
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
