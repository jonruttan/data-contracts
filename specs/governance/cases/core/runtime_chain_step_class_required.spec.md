# Governance Cases

## SRGOV-CHAIN-007

```yaml contract-spec
id: SRGOV-CHAIN-007
title: chain steps declare must can cannot class
purpose: Ensures harness.chain.steps[*].class is explicit and valid for all chained cases.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.chain_step_class_required
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
    as:
      violation_count: subject
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```
