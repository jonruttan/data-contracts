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
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.harness_exports_location_required'}}}"
services:
  entries:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_harness_exports_location_required.default.1
    type: legacy.root_check_profile_governance_scan_config_check_runtime_harness_exports_location_required
    io: io
    profile: default
    config: {}
contracts:
- id: DCGOV-HARNESS-EXPORTS-001
  title: producer exports are declared at harness.exports
  purpose: Ensures producer symbol declarations are declared at harness.exports and non-canonical harness.chain.exports is rejected.
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
