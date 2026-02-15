# Governance Cases

## SRGOV-DOCS-REF-006

```yaml spec-test
id: SRGOV-DOCS-REF-006
title: assertion tokens stay aligned across book contract and schema docs
purpose: Ensures core assertion terminology remains synchronized across author-facing and normative specification documents.
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
    - contain
    - regex
    - evaluate
    - json_type
    - exists
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - subject: []
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - subject: []
        - passed
      - true
    - eq:
      - get:
        - subject: []
        - check_id
      - docs.contract_schema_book_sync
```
