```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.harness_exports_schema_valid'}}}"
services:
  entries:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_harness_exports_schema_valid.default.1
    type: legacy.root_check_profile_governance_scan_config_check_runtime_harness_exports_schema_valid
    io: io
    profile: default
    config: {}
contracts:
- id: DCGOV-HARNESS-EXPORTS-003
  title: harness exports schema is valid
  purpose: Ensures harness.exports entries enforce as/from/path/params/required schema requirements.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.summary_passed
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
```
