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
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.api_http_tutorial_sync
```
