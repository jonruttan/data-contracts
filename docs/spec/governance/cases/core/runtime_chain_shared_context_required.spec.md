# Governance Cases

## SRGOV-CHAIN-011

```yaml contract-spec
id: SRGOV-CHAIN-011
title: chain shared context is declared in dispatcher
purpose: Ensures chain state, trace, imports, and chain payload surfaces are carried in shared
  runtime context.
type: governance.check
check: runtime.chain_shared_context_required
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
