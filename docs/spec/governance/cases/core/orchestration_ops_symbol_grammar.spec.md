# Governance Cases

## SRGOV-OPS-001

```yaml contract-spec
id: SRGOV-OPS-001
title: orchestration ops symbols follow deep-dot grammar
purpose: Ensures effect symbols use canonical deep-dot ops names.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: orchestration.ops_symbol_grammar
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - orchestration.ops_symbol_grammar
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - passed
    - true
  target: summary_json
```
