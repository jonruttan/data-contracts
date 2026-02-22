```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.case_contract_block_required'}}}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-CONTRACT-BLOCK-001
    title: cases must use contract block
    purpose: Enforces top-level contract block requirement for executable cases.
    asserts:
      imports:
      - from: artifact
        names:
        - violation_count
      checks:
      - id: assert_1
        assert:
          call:
          - var: policy.assert.no_violations
          - std.object.assoc:
            - violation_count
            - var: violation_count
            - lit: {}
adapters:
- type: legacy.check_profile_governance_scan_config_check_runtime_case_contract_block_required
  actions:
  - id: svc.check_profile_governance_scan_config_check_runtime_case_contract_block_required.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.check_profile_governance_scan_config_check_runtime_case_contract_block_required.default.1
  consumes:
  - svc.check_profile_governance_scan_config_check_runtime_case_contract_block_required.default.1
```
