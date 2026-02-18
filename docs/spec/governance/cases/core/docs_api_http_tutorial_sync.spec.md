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
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: docs.api_http_tutorial_sync
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.logic.eq:
            - {var: subject}
            - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.logic.eq:
            - std.object.get:
              - {var: subject}
              - check_id
            - docs.api_http_tutorial_sync
  target: summary_json
```
