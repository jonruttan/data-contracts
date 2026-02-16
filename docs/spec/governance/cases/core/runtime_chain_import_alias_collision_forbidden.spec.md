# Governance Cases

## SRGOV-CHAIN-008

```yaml spec-test
id: SRGOV-CHAIN-008
title: chain import alias collisions are forbidden
purpose: Ensures harness.chain.imports bindings are valid and do not collide or shadow reserved
  symbols.
type: governance.check
check: runtime.chain_import_alias_collision_forbidden
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
