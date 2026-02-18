# Governance Cases

## SRGOV-ARCH-COMPONENTS-004

```yaml contract-spec
id: SRGOV-ARCH-COMPONENTS-004
title: harness contract and overlays remain synchronized
purpose: Verifies contract/current docs and harness type overlays describe the same orchestration.run
  and docs.generate architecture.
type: governance.check
check: schema.harness_contract_overlay_sync
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

