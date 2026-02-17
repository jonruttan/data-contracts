# Governance Cases

## SRGOV-RUNTIME-PYDEP-004

```yaml spec-test
id: SRGOV-RUNTIME-PYDEP-004
title: rust adapter boundary avoids transitive python delegation tokens
purpose: Ensures rust adapter boundary files do not delegate to python adapter entrypoints
  or direct python execution tokens.
type: governance.check
check: runtime.rust_adapter_transitive_no_python
harness:
  root: .
  rust_transitive_no_python:
    files:
    - scripts/rust/runner_adapter.sh
    - scripts/rust/spec_runner_cli/src/main.rs
    forbidden_tokens:
    - scripts/runner_adapter.sh
    - scripts/run_governance_specs.py
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
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
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - runtime.rust_adapter_transitive_no_python
  target: summary_json
```
