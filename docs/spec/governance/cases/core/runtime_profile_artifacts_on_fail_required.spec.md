# Governance Cases

## SRGOV-RUNTIME-FAILFAST-003

```yaml spec-test
id: SRGOV-RUNTIME-FAILFAST-003
title: gate failures emit profile artifacts when profile-on-fail is enabled
purpose: Ensures failure paths generate deterministic run-trace and run-trace-summary artifacts.
type: governance.check
check: runtime.profile_artifacts_on_fail_required
harness:
  root: .
  profile_on_fail:
    files:
    - /scripts/ci_gate_summary.py
    - /scripts/rust/spec_runner_cli/src/main.rs
    required_tokens:
    - profile-on-fail
    - .artifacts/run-trace.json
    - .artifacts/run-trace-summary.md
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
