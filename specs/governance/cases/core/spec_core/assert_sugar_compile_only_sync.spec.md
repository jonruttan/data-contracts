# Governance Cases

## DCGOV-ASSERT-COMPILE-001

```yaml contract-spec
id: DCGOV-ASSERT-COMPILE-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: compiler keeps sugar operators compile-only
purpose: Ensures compiler and runtime assertion path keep non-evaluate operators as compile-only
  sugar with spec-lang execution.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: assert.sugar_compile_only_sync
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults:
    class: MUST
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
  - id: assert_2
    assert:
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
    - call:
      - {var: policy.assert.summary_check_id}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
      - assert.sugar_compile_only_sync
    imports:
    - from: artifact
      names:
      - summary_json
```
