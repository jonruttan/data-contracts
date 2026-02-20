# Governance Cases

## DCGOV-CONF-PORT-003

```yaml contract-spec
id: DCGOV-CONF-PORT-003
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: extension type conformance cases declare requires.capabilities
purpose: Ensures non-core type fixtures explicitly declare required capabilities for portable
  parity.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: conformance.extension_requires_capabilities
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
      - conformance.extension_requires_capabilities
    imports:
    - from: artifact
      names:
      - summary_json
```
