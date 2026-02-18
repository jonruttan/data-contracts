# Governance Cases

## SRGOV-LIVENESS-STALL-001

```yaml contract-spec
id: SRGOV-LIVENESS-STALL-001
title: run trace contains liveness stall reason tokens
purpose: Ensures watchdog reason tokens for runner/subprocess stall semantics are
  observable in run trace artifacts.
type: governance.check
check: runtime.liveness_stall_token_emitted
harness:
  root: .
  liveness_trace_tokens:
    trace_path: docs/spec/governance/cases/fixtures/run_trace_liveness_sample.json
    required_tokens:
    - stall.runner.no_progress
    - stall.subprocess.no_output_no_event
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
