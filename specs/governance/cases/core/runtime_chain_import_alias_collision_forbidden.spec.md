# Governance Cases

## SRGOV-CHAIN-008

```yaml contract-spec
id: SRGOV-CHAIN-008
title: chain import alias collisions are forbidden
purpose: Ensures harness.chain.imports bindings are valid and do not collide or shadow reserved
  symbols.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.chain_import_alias_collision_forbidden
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
```
