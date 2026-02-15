# Governance Cases

## SRGOV-RUNTIME-ENTRY-003

```yaml spec-test
id: SRGOV-RUNTIME-ENTRY-003
title: python lane is explicit opt-in
purpose: Ensures contributor docs require explicit impl selection when using the python runner
  lane.
type: governance.check
check: runtime.python_lane_explicit_opt_in
harness:
  root: .
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  python_lane_opt_in:
    files:
    - docs/development.md
    - docs/spec/contract/12_runner_interface.md
    required_opt_in_tokens:
    - SPEC_RUNNER_IMPL=python
    - --impl python
    forbidden_default_tokens:
    - SPEC_RUNNER_IMPL="python"
    - SPEC_RUNNER_IMPL=python ./scripts/ci_gate.sh
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
      - runtime.python_lane_explicit_opt_in
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
```
