# Governance Cases

## SRGOV-RUNTIME-ENTRY-004

```yaml spec-test
id: SRGOV-RUNTIME-ENTRY-004
title: public docs do not instruct direct rust adapter invocation
purpose: Ensures public docs point to the canonical adapter entrypoint rather than internal rust adapter paths.
type: governance.check
check: runtime.no_public_direct_rust_adapter_docs
harness:
  root: .
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  public_docs:
    files:
    - /README.md
    - /docs/development.md
    - /docs/spec/current.md
    - /docs/spec/contract/12_runner_interface.md
    - /docs/spec/contract/16_rust_primary_transition.md
    forbidden_tokens:
    - scripts/rust/runner_adapter.sh
    allowlist:
    - /docs/spec/contract/12_runner_interface.md
    - /docs/spec/contract/16_rust_primary_transition.md
  policy_evaluate:
  - {call: [{var: policy.pass_when_no_violations}, {var: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{var: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{var: subject}, check_id]}
      - runtime.no_public_direct_rust_adapter_docs
    - eq:
      - {get: [{var: subject}, passed]}
      - true
```
