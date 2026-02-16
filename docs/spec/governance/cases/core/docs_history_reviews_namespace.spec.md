# Governance Cases

## SRGOV-DOCS-LAYOUT-004

```yaml spec-test
id: SRGOV-DOCS-LAYOUT-004
title: review artifacts live under docs/history/reviews
purpose: Enforces canonical historical review namespace and forbids legacy docs/reviews.
type: governance.check
check: docs.history_reviews_namespace
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
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.history_reviews_namespace
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
