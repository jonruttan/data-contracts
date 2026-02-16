# Governance Cases

## SRGOV-CHAIN-012

```yaml spec-test
id: SRGOV-CHAIN-012
title: chain state sharing uses explicit exports only
purpose: Ensures chain state propagation is declared through explicit target-derived exports.
type: governance.check
check: runtime.chain_exports_explicit_only
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
