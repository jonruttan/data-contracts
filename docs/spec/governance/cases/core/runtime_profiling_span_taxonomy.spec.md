# Governance Cases

## SRGOV-PROFILE-SPANS-001

```yaml contract-spec
id: SRGOV-PROFILE-SPANS-001
title: run trace records required span taxonomy for timeout diagnosis
purpose: Ensures the canonical run trace includes required run, case, check, and subprocess
  spans used by timeout diagnostics.
type: contract.check
harness:
  root: .
  profiling_span_taxonomy:
    trace_path: docs/spec/governance/cases/fixtures/run_trace_sample.json
    required_spans:
    - run.total
    - runner.dispatch
    - case.run
    - case.chain
    - case.harness
    - check.execute
    - subprocess.exec
    - subprocess.wait
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.profiling_span_taxonomy
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.logic.eq:
            - {var: subject}
            - 0
  target: violation_count
```

