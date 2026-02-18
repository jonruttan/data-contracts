# Governance Cases

## SRGOV-CHAIN-012

```yaml contract-spec
id: SRGOV-CHAIN-012
title: chain state sharing uses explicit exports only
purpose: Ensures chain state propagation is declared through explicit target-derived exports.
type: governance.check
check: runtime.chain_exports_explicit_only
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
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
