# Governance Cases

## SRGOV-RUNTIME-FAILFAST-003

```yaml contract-spec
id: SRGOV-RUNTIME-FAILFAST-003
title: gate failures emit profile artifacts when profile-on-fail is enabled
purpose: Ensures failure paths generate deterministic run-trace and run-trace-summary artifacts.
type: contract.check
harness:
  root: .
  profile_on_fail:
    files:
    - /runners/python/spec_runner/script_runtime_commands.py
    - /runners/rust/spec_runner_cli/src/main.rs
    required_tokens:
    - profile-on-fail
    - .artifacts/run-trace.json
    - .artifacts/run-trace-summary.md
  check:
    profile: governance.scan
    config:
      check: runtime.profile_artifacts_on_fail_required
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
    target: violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```
