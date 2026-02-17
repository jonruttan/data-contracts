# Governance Cases

## SRGOV-CHAIN-006

```yaml spec-test
id: SRGOV-CHAIN-006
title: chain refs use canonical scalar format
purpose: Ensures harness.chain step refs are scalar [path][#case_id] values and reject legacy
  mapping form.
type: governance.check
check: runtime.chain_ref_scalar_required
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
      - as: policy.pass_when_no_violations
        from: library.symbol
        required: true
        path: /policy.pass_when_no_violations
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
```
