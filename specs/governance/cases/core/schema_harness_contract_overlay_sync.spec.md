# Governance Cases

## SRGOV-ARCH-COMPONENTS-004

```yaml contract-spec
id: SRGOV-ARCH-COMPONENTS-004
title: harness contract and overlays remain synchronized
purpose: Verifies contract/current docs and harness type overlays describe the same orchestration.run
  and docs.generate architecture.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: schema.harness_contract_overlay_sync
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
    target: violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```

