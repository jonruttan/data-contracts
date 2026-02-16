# Governance Cases

## SRGOV-RUNTIME-ENTRY-004

```yaml spec-test
id: SRGOV-RUNTIME-ENTRY-004
title: public docs do not instruct direct rust adapter invocation
purpose: Ensures public docs point to the canonical adapter entrypoint rather than internal
  rust adapter paths.
type: governance.check
check: runtime.no_public_direct_rust_adapter_docs
harness:
  root: .
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
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
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
        - check_id
      - runtime.no_public_direct_rust_adapter_docs
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
