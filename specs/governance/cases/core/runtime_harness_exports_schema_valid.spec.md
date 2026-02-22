```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.harness_exports_schema_valid'}}}"
services:
- type: legacy.root_check_profile_governance_scan_config_check_runtime_harness_exports_schema_valid
  operations:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_harness_exports_schema_valid.default.1
    mode: default
    direction: bidirectional
contracts:
  clauses:
  - id: DCGOV-HARNESS-EXPORTS-003
    title: harness exports schema is valid
    purpose: Ensures harness.exports entries enforce as/from/path/params/required schema requirements.
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
