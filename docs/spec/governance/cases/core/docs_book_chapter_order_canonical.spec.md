# Governance Cases

## SRGOV-DOCS-REF-018

```yaml spec-test
id: SRGOV-DOCS-REF-018
title: docs book chapter order is canonical
purpose: Enforces the hard-cut Learn -> Do -> Debug chapter order and appendix namespace ordering
  in the reference manifest.
type: governance.check
check: docs.book_chapter_order_canonical
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
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
      - docs.book_chapter_order_canonical
```
