# Governance Cases

## SRGOV-DOCS-GEN-023

```yaml spec-test
id: SRGOV-DOCS-GEN-023
title: harness reference includes semantic sections
purpose: Ensures generated harness reference includes summary/defaults/failure modes/examples
  per case type.
type: governance.check
check: docs.harness_reference_semantics_complete
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
      - docs.harness_reference_semantics_complete
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
