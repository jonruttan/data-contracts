# Governance Cases

## SRGOV-CHAIN-009

```yaml contract-spec
id: SRGOV-CHAIN-009
title: chain contract uses harness.chain only
purpose: Ensures chain declarations appear only at harness.chain and not in alternate top-level
  or type-specific locations.
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
      check: runtime.chain_contract_single_location
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.logic.eq:
            - {var: subject}
            - 0
  target: violation_count
```
