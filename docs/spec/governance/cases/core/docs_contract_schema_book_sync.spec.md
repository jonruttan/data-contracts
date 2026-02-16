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
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
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
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - docs.contract_schema_book_sync
```
