# Governance Cases

## DCGOV-RUNTIME-PYDEP-003

```yaml contract-spec
id: DCGOV-RUNTIME-PYDEP-003
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: non-python lanes avoid direct python execution tokens
purpose: Ensures default gate/orchestration and rust adapter lane files do not contain python
  execution tokens.
type: contract.check
harness:
  root: .
  python_dependency: {}
  check:
    profile: governance.scan
    config:
      check: runtime.non_python_lane_no_python_exec
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
      - runtime.non_python_lane_no_python_exec
    imports:
    - from: artifact
      names:
      - summary_json
```
