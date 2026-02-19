# Governance Cases

## SRGOV-DOCS-REF-006

```yaml contract-spec
id: SRGOV-DOCS-REF-006
title: assertion tokens stay aligned across book contract and schema docs
purpose: Ensures core assertion terminology remains synchronized across author-facing and
  normative specification documents.
type: contract.check
harness:
  root: .
  doc_sync:
    files:
    - docs/book/03_assertions.md
    - specs/contract/03_assertions.md
    - specs/schema/schema_v1.md
    tokens:
    - must
    - can
    - cannot
    - evaluate
  check:
    profile: governance.scan
    config:
      check: docs.contract_schema_book_sync
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
  - id: assert_2
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.contract_schema_book_sync
    imports:
      subject:
        from: artifact
        key: summary_json
```
