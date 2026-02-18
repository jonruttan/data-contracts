# Governance Cases

## SRGOV-DOCS-APIHTTP-001

```yaml spec-test
id: SRGOV-DOCS-APIHTTP-001
title: api.http tutorials remain present in howto and troubleshooting docs
purpose: Ensures contributor docs cover practical REST verbs, CORS preflight, and round-trip
  scenario guidance.
type: governance.check
check: docs.api_http_tutorial_sync
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
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - docs.api_http_tutorial_sync
  target: summary_json
```
