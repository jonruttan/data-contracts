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
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
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
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.rust_adapter_transitive_no_python
```
