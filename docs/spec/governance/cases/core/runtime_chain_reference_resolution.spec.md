# Governance Cases

## SRGOV-CHAIN-001

```yaml contract-spec
id: SRGOV-CHAIN-001
title: chain references resolve deterministically
purpose: Ensures harness.chain step references resolve by contract for
type: governance.check
check: runtime.chain_reference_resolution
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
- id: assert_2
  class: must
  asserts:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - runtime.chain_reference_resolution
  target: summary_json
```
