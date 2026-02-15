# Governance Cases

## SRGOV-RUNTIME-PYDEP-004

```yaml spec-test
id: SRGOV-RUNTIME-PYDEP-004
title: rust adapter shell entrypoint avoids direct python delegation tokens
purpose: Ensures rust adapter shell boundary does not directly delegate to python shell adapter entrypoint tokens.
type: governance.check
check: runtime.rust_adapter_transitive_no_python
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  rust_transitive_no_python:
    files:
    - scripts/rust/runner_adapter.sh
    forbidden_tokens:
    - scripts/runner_adapter.sh
    - scripts/run_governance_specs.py
  policy_evaluate:
  - {call: [{var: [policy.pass_when_no_violations]}, {subject: []}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - runtime.rust_adapter_transitive_no_python
```
