# Governance Cases

## SRGOV-DOCS-GEN-007

```yaml spec-test
id: SRGOV-DOCS-GEN-007
title: policy rule catalog artifacts are synchronized
purpose: Ensures generated policy rule JSON and markdown artifacts are up-to-date.
type: governance.check
check: docs.policy_rule_catalog_sync
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.policy_rule_catalog_sync
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
