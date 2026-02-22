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
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.ops_job_capability_required'}}}"
services:
- id: svc.root_check_profile_governance_scan_config_check_runtime_ops_job_capability_required.default.1
  type: legacy.root_check_profile_governance_scan_config_check_runtime_ops_job_capability_required
  mode: default
  direction: bidirectional
contracts:
- id: DCGOV-RUNTIME-JOB-DISPATCH-004
  title: ops.job.dispatch requires ops.job capability
  purpose: Ensures cases that call ops.job.dispatch declare harness.spec_lang.capabilities
    including ops.job.
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
