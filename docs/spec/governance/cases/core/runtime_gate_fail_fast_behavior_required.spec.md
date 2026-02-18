# Governance Cases

## SRGOV-RUNTIME-FAILFAST-001

```yaml contract-spec
id: SRGOV-RUNTIME-FAILFAST-001
title: gate summary enforces fail-fast orchestration semantics
purpose: Ensures CI gate orchestration supports deterministic fail-fast with explicit abort
  markers.
type: governance.check
check: runtime.gate_fail_fast_behavior_required
harness:
  root: .
  gate_fail_fast:
    files:
    - /scripts/ci_gate_summary.py
    - /scripts/rust/spec_runner_cli/src/main.rs
    required_tokens:
    - fail_fast
    - gate.fail_fast.abort
    - fail_fast.after_failure
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
