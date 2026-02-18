# Governance Cases

## SRGOV-DOCS-GEN-007

```yaml contract-spec
id: SRGOV-DOCS-GEN-007
title: policy rule catalog artifacts are synchronized
purpose: Ensures generated policy rule JSON and markdown artifacts are up-to-date.
type: governance.check
check: docs.policy_rule_catalog_sync
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
contract:
- id: assert_1
  class: must
  asserts:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.policy_rule_catalog_sync
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
