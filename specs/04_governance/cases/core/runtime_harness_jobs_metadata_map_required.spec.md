```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.harness_jobs_metadata_list_required'}}}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-JOB-DISPATCH-002
    title: contract.job harness uses jobs metadata list
    purpose: Ensures contract.job cases declare helper metadata under harness.jobs entries.
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
- type: legacy.root_check_profile_governance_scan_config_check_runtime_harness_jobs_metadata_list_required
  actions:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_harness_jobs_metadata_list_required.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_check_profile_governance_scan_config_check_runtime_harness_jobs_metadata_list_required.default.1
  consumes:
  - svc.root_check_profile_governance_scan_config_check_runtime_harness_jobs_metadata_list_required.default.1
```
