```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.contract_job_hooks_refactor_applied'}}}"
services:
- type: legacy.root_check_profile_governance_scan_config_check_runtime_contract_job_hooks_refactor_applied
  operations:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_contract_job_hooks_refactor_applied.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCGOV-RUNTIME-JOB-HOOKS-001
    title: rust contract.job specs adopt fail and complete lifecycle hooks
    purpose: Ensures Rust job contract-spec cases include when fail and complete dispatches
      with matching hook job metadata.
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
