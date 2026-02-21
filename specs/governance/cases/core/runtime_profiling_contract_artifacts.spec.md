# Governance Cases

## DCGOV-PROFILE-CONTRACT-001

```yaml contract-spec
id: DCGOV-PROFILE-CONTRACT-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: runtime profiling contract artifacts exist and are discoverable
purpose: Ensures run trace schema and profiling contract docs are present and linked in current
  snapshot notes.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.profiling_contract_artifacts
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

