# Governance Cases

## SRGOV-RUNTIME-PREPUSH-005

```yaml contract-spec
id: SRGOV-RUNTIME-PREPUSH-005
title: local ci parity entrypoint is documented for contributors
purpose: Ensures contributor docs cover parity-default prepush, fast opt-out, and hook installation.
type: contract.check
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
  check:
    profile: governance.scan
    config:
      check: runtime.local_ci_parity_entrypoint_documented
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
