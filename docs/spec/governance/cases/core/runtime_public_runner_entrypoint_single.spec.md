# Governance Cases

## SRGOV-RUNTIME-ENTRY-001

```yaml spec-test
id: SRGOV-RUNTIME-ENTRY-001
title: gate scripts use a single public runner entrypoint
purpose: Ensures gate scripts reference only the canonical public runner entrypoint.
type: governance.check
check: runtime.public_runner_entrypoint_single
harness:
  root: .
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  public_runner_entrypoint:
    required_entrypoint: scripts/runner_adapter.sh
    gate_files:
    - scripts/ci_gate.sh
    - scripts/core_gate.sh
    - scripts/docs_doctor.sh
    forbidden_tokens:
    - scripts/rust/runner_adapter.sh
    - scripts/python/runner_adapter.sh
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - check_id
      - runtime.public_runner_entrypoint_single
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
```
