# Governance Cases

## SRGOV-DOCS-REF-006

```yaml spec-test
id: SRGOV-DOCS-REF-006
title: assertion tokens stay aligned across book contract and schema docs
purpose: Ensures core assertion terminology remains synchronized across author-facing and
  normative specification documents.
type: governance.check
check: docs.contract_schema_book_sync
harness:
  root: .
  doc_sync:
    files:
    - docs/book/03_assertions.md
    - docs/spec/contract/03_assertions.md
    - docs/spec/schema/schema_v1.md
    tokens:
    - must
    - can
    - cannot
    - evaluate
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
      - as: policy.pass_when_no_violations
        from: library.symbol
        required: true
        path: /policy.pass_when_no_violations
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
      - docs.contract_schema_book_sync
  target: summary_json
```
