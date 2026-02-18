# Governance Cases

## SRGOV-RUNTIME-PREPUSH-005

```yaml contract-spec
id: SRGOV-RUNTIME-PREPUSH-005
title: local ci parity entrypoint is documented for contributors
purpose: Ensures contributor docs cover parity-default prepush, fast opt-out, and
  hook installation.
type: governance.check
check: runtime.local_ci_parity_entrypoint_documented
harness:
  root: .
  local_ci_parity_docs:
    files:
    - /README.md
    - /docs/development.md
    - /docs/book/05_howto.md
    - /docs/book/06_troubleshooting.md
    required_tokens:
    - make prepush
    - make prepush-fast
    - make hooks-install
    - SPEC_PREPUSH_BYPASS=1
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
