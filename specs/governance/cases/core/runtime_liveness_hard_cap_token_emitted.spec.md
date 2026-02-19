# Governance Cases

## SRGOV-LIVENESS-HARDCAP-001

```yaml contract-spec
id: SRGOV-LIVENESS-HARDCAP-001
title: run trace includes hard-cap and kill escalation reason tokens
purpose: Ensures emergency hard-cap watchdog behavior is represented in trace token taxonomy.
type: contract.check
harness:
  root: .
  liveness_trace_tokens:
    trace_path: specs/governance/cases/fixtures/run_trace_liveness_sample.json
  check:
    profile: governance.scan
    config:
      check: runtime.liveness_hard_cap_token_emitted
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```
