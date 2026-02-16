# Governance Cases

## SRGOV-DOCS-REF-002

```yaml spec-test
id: SRGOV-DOCS-REF-002
title: reference index stays synced with chapter files
purpose: Ensures the machine-checked reference index entries stay aligned with the actual
  chapter set and order.
type: governance.check
check: docs.reference_index_sync
harness:
  root: .
  reference_index:
    path: /docs/book/reference_index.md
    include_glob: docs/book/*.md
    exclude_files:
    - docs/book/index.md
    - docs/book/reference_index.md
    - docs/book/reference_coverage.md
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
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
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
      - docs.reference_index_sync
  target: summary_json
```
