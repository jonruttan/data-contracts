# Governance Cases

## DCGOV-RUNTIME-CONFIG-001

```yaml contract-spec
id: DCGOV-RUNTIME-CONFIG-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: runtime python code does not duplicate governed config literals
purpose: Enforces centralized configuration by rejecting duplicated governed literals in runtime
  python sources.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.config_literals
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
      - runtime.config_literals
    imports:
    - from: artifact
      names:
      - summary_json
```
