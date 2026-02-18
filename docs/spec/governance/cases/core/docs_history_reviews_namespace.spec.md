# Governance Cases

## SRGOV-DOCS-LAYOUT-004

```yaml spec-test
id: SRGOV-DOCS-LAYOUT-004
title: review artifacts live under docs/history/reviews
purpose: Enforces canonical historical review namespace and forbids legacy docs/history/reviews.
type: governance.check
check: docs.history_reviews_namespace
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
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.history_reviews_namespace
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
