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
```
