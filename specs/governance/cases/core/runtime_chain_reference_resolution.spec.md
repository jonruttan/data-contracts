# Governance Cases

## SRGOV-CHAIN-001

```yaml contract-spec
id: SRGOV-CHAIN-001
title: chain references resolve deterministically
purpose: Ensures harness.chain step references resolve by contract for
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.chain_reference_resolution
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
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
  - id: assert_2
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.chain_reference_resolution
    imports:
      subject:
        from: artifact
        key: summary_json
```
