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
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.harness_jobs_metadata_list_required'}}}"
services:
  actions:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_harness_jobs_metadata_list_required.default.1
    type: legacy.root_check_profile_governance_scan_config_check_runtime_harness_jobs_metadata_list_required
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-JOB-DISPATCH-002
  title: contract.job harness uses jobs metadata list
  purpose: Ensures contract.job cases declare helper metadata under harness.jobs entries.
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.no_violations
        - std.object.assoc:
          - violation_count
          - var: violation_count
          - lit: {}
```
