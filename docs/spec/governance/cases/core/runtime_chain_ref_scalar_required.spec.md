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
      check: runtime.chain_ref_scalar_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        std.logic.eq:
        - {var: subject}
        - 0
  target: violation_count
```
