# Governance Cases

## SRGOV-PROFILE-SPANS-001

```yaml spec-test
id: SRGOV-PROFILE-SPANS-001
title: run trace records required span taxonomy for timeout diagnosis
purpose: Ensures the canonical run trace includes required run, case, check, and subprocess
  spans used by timeout diagnostics.
type: governance.check
check: runtime.profiling_span_taxonomy
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
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```

