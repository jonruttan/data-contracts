# Governance Cases

## DCGOV-ARCH-COMPONENTS-002

```yaml contract-spec
id: DCGOV-ARCH-COMPONENTS-002
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: non-canonical harness workflow duplication is forbidden
purpose: Prevents harness modules from reintroducing local spec-lang setup and direct assertion-evaluation
  glue after component hard cut.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: architecture.harness_local_workflow_duplication_forbidden
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.no_violations}
      - std.object.assoc:
        - violation_count
        - {var: violation_count}
        - lit: {}
```

