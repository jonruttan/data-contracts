# Governance Cases

## SRGOV-DOCS-GEN-004

```yaml contract-spec
id: SRGOV-DOCS-GEN-004
title: runner api catalog artifacts are synchronized
purpose: Ensures generated runner API JSON and markdown artifacts are up-to-date.
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
      check: docs.runner_api_catalog_sync
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          MUST:
          - std.logic.eq:
            - std.object.get:
              - {var: subject}
              - check_id
            - docs.runner_api_catalog_sync
          - std.logic.eq:
            - std.object.get:
              - {var: subject}
              - passed
            - true
  target: summary_json
```
