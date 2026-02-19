# Governance Cases

## SRGOV-CHAIN-006

```yaml contract-spec
id: SRGOV-CHAIN-006
title: chain refs use canonical scalar format
purpose: Ensures harness.chain step refs are scalar [path][#case_id] values and reject non-canonical
  mapping form.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.chain_ref_scalar_required
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
