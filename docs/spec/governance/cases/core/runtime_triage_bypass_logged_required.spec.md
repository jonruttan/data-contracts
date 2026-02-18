# Governance Cases

## SRGOV-RUNTIME-TRIAGE-006

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-006
title: emergency bypass remains explicit and logged
purpose: Ensures pre-push bypass remains explicit and emits deterministic warning output.
type: contract.check
harness:
  root: .
  triage_bypass_logging:
    path: /.githooks/pre-push
    required_tokens:
    - SPEC_PREPUSH_BYPASS
    - 'WARNING: bypass enabled'
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
      check: runtime.triage_bypass_logged_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        std.logic.eq:
        - {var: subject}
        - 0
  target: violation_count
```
