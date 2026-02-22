```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.ops_job_capability_required'}}}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-JOB-DISPATCH-004
    title: ops.job.dispatch requires ops.job capability
    purpose: Ensures cases that call ops.job.dispatch declare harness.spec_lang.capabilities including ops.job.
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
- type: legacy.root_check_profile_governance_scan_config_check_runtime_ops_job_capability_required
  actions:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_ops_job_capability_required.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_check_profile_governance_scan_config_check_runtime_ops_job_capability_required.default.1
  consumes:
  - svc.root_check_profile_governance_scan_config_check_runtime_ops_job_capability_required.default.1
```
