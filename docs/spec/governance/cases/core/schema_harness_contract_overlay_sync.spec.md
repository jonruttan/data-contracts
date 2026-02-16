# Governance Cases

## SRGOV-ARCH-COMPONENTS-004

```yaml spec-test
id: SRGOV-ARCH-COMPONENTS-004
title: harness contract and overlays remain synchronized
purpose: Verifies contract/current docs and harness type overlays describe the same orchestration.run
  and docs.generate architecture.
type: governance.check
check: schema.harness_contract_overlay_sync
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
```

