# Governance Cases

## SRGOV-DOCS-REF-018

```yaml contract-spec
id: SRGOV-DOCS-REF-018
title: docs book chapter order is canonical
purpose: Enforces the hard-cut Learn -> Do -> Debug chapter order and appendix namespace ordering
  in the reference manifest.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.book_chapter_order_canonical
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
      - docs.book_chapter_order_canonical
    imports:
      subject:
        from: artifact
        key: summary_json
```
