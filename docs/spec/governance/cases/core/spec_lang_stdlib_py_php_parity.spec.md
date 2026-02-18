# Governance Cases

## SRGOV-STDLIB-002

```yaml contract-spec
id: SRGOV-STDLIB-002
title: spec-lang stdlib symbols are parity-clean across python and php
purpose: Ensures no profile symbol is missing in either runtime implementation.
type: contract.check
harness:
  root: .
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
      check: spec_lang.stdlib_py_php_parity
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.logic.eq:
            - {var: subject}
            - 0
  target: violation_count
```
