# Governance Cases

## SRGOV-DOCS-LAYOUT-004

```yaml contract-spec
id: SRGOV-DOCS-LAYOUT-004
title: review artifacts live under docs/history/reviews
purpose: Enforces canonical historical review namespace and forbids non-canonical docs/history/reviews.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.history_reviews_namespace
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - summary_json
    as:
      summary_json: subject
  steps:
  - id: assert_1
    assert:
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
