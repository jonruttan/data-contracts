# Governance Cases

## SRGOV-STDLIB-002

```yaml spec-test
id: SRGOV-STDLIB-002
title: spec-lang stdlib symbols are parity-clean across python and php
purpose: Ensures no profile symbol is missing in either runtime implementation.
type: governance.check
check: spec_lang.stdlib_py_php_parity
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
```
