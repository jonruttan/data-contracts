```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.contract_job_dispatch_in_contract_required'}}}"
services:
- type: legacy.root_check_profile_governance_scan_config_check_runtime_contract_job_dispatch_in_contract_required
  operations:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_contract_job_dispatch_in_contract_required.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCGOV-RUNTIME-JOB-DISPATCH-001
    title: contract.job dispatch must be declared in contract
    purpose: Ensures contract.job cases dispatch jobs via ops.job.dispatch in contract
      assertions.
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
```
