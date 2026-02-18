# Governance Cases

## SRGOV-PROFILE-REDACT-001

```yaml contract-spec
id: SRGOV-PROFILE-REDACT-001
title: run trace redaction policy prevents secret leakage
purpose: Ensures profiling env metadata does not store raw values and trace payloads do not
  include common secret-like tokens.
type: contract.check
harness:
  root: .
  profiling_redaction:
    trace_path: docs/spec/governance/cases/fixtures/run_trace_sample.json
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
      check: runtime.profiling_redaction_policy
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
  target: violation_count
```

