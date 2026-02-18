# Governance Cases

## SRGOV-LIVENESS-HARDCAP-001

```yaml contract-spec
id: SRGOV-LIVENESS-HARDCAP-001
title: run trace includes hard-cap and kill escalation reason tokens
purpose: Ensures emergency hard-cap watchdog behavior is represented in trace token taxonomy.
type: governance.check
check: runtime.liveness_hard_cap_token_emitted
harness:
  root: .
  liveness_trace_tokens:
    trace_path: docs/spec/governance/cases/fixtures/run_trace_liveness_sample.json
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
