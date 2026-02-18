# Governance Cases

## SRGOV-DOCS-GEN-010

```yaml contract-spec
id: SRGOV-DOCS-GEN-010
title: metrics field catalog artifacts are synchronized
purpose: Ensures generated metrics field catalog JSON and markdown artifacts are up-to-date.
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
      check: docs.metrics_field_catalog_sync
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - docs.metrics_field_catalog_sync
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - passed
    - true
  target: summary_json
```
