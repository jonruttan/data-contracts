# Governance Cases

## SRGOV-RUNTIME-PYDEP-004

```yaml contract-spec
id: SRGOV-RUNTIME-PYDEP-004
title: rust adapter boundary avoids transitive python delegation tokens
purpose: Ensures rust adapter boundary files do not delegate to python adapter entrypoints
  or direct python execution tokens.
type: contract.check
harness:
  root: .
  rust_transitive_no_python:
    files:
    - runners/rust/runner_adapter.sh
    - runners/rust/spec_runner_cli/src/main.rs
    forbidden_tokens:
    - runners/public/runner_adapter.sh
    - scripts/run_governance_specs.py
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
      check: runtime.rust_adapter_transitive_no_python
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
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
  target: summary_json
```
