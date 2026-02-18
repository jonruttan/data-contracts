# Governance Cases

## SRGOV-DOCS-REF-018

```yaml contract-spec
id: SRGOV-DOCS-REF-018
title: docs book chapter order is canonical
purpose: Enforces the hard-cut Learn -> Do -> Debug chapter order and appendix namespace ordering
  in the reference manifest.
type: governance.check
check: docs.book_chapter_order_canonical
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  asserts:
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
      - docs.book_chapter_order_canonical
  target: summary_json
```
