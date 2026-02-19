# Governance Cases

## SRGOV-CHAIN-003

```yaml contract-spec
id: SRGOV-CHAIN-003
title: chain exports remain target-derived only
purpose: Ensures harness.chain step exports declare only explicit target-derived extraction
  keys.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.chain_exports_target_derived_only
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```
