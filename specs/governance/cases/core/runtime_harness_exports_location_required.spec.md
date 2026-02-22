```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.harness_exports_location_required'}}}"
services:
- type: legacy.root_check_profile_governance_scan_config_check_runtime_harness_exports_location_required
  operations:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_harness_exports_location_required.default.1
    mode: default
    direction: bidirectional
contracts:
  clauses:
  - id: DCGOV-HARNESS-EXPORTS-001
    title: producer exports are declared at harness.exports
    purpose: Ensures producer symbol declarations are declared at harness.exports and non-canonical harness.chain.exports is rejected.
    asserts:
      imports:
      - from: artifact
        names:
        - summary_json
      checks:
      - id: assert_1
        assert:
          call:
          - var: policy.assert.summary_passed
          - std.object.assoc:
            - summary_json
            - var: summary_json
            - lit: {}
```
