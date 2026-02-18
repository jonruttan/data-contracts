# Governance Cases

## SRGOV-DOCS-LAYOUT-004

```yaml contract-spec
id: SRGOV-DOCS-LAYOUT-004
title: review artifacts live under docs/history/reviews
purpose: Enforces canonical historical review namespace and forbids non-canonical docs/history/reviews.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: docs.history_reviews_namespace
contract:
- id: assert_1
  class: MUST
  asserts:
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
  target: summary_json
```
