# Governance Cases

## DCGOV-PROFILE-SPANS-001

```yaml contract-spec
id: DCGOV-PROFILE-SPANS-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: run trace records required span taxonomy for timeout diagnosis
purpose: Ensures the canonical run trace includes required run, case, check, and subprocess
  spans used by timeout diagnostics.
type: contract.check
harness:
  root: .
  profiling_span_taxonomy:
    trace_path: specs/governance/cases/fixtures/run_trace_sample.json
    required_spans:
    - run.total
    - runner.dispatch
    - case.run
    - case.chain
    - case.harness
    - check.execute
    - subprocess.exec
    - subprocess.wait
  check:
    profile: governance.scan
    config:
      check: runtime.profiling_span_taxonomy
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.no_violations}
      - std.object.assoc:
        - violation_count
        - {var: violation_count}
        - lit: {}
```

