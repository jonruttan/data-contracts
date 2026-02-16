# Governance Cases

## SRGOV-DOCS-GEN-002

```yaml spec-test
id: SRGOV-DOCS-GEN-002
title: docs generator outputs are synchronized
purpose: Ensures all registry-backed docs generator outputs are up-to-date in check mode.
type: governance.check
check: docs.generator_outputs_sync
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
    - from_step: lib_policy_core_spec
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
      - docs.generator_outputs_sync
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
