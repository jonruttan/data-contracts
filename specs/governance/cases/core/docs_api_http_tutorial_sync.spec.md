# Governance Cases

## SRGOV-DOCS-APIHTTP-001

```yaml contract-spec
id: SRGOV-DOCS-APIHTTP-001
title: api.http tutorials remain present in howto and troubleshooting docs
purpose: Ensures contributor docs cover practical REST verbs, CORS preflight, and round-trip
  scenario guidance.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.api_http_tutorial_sync
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
    'on': violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    'on': summary_json
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.api_http_tutorial_sync
```
