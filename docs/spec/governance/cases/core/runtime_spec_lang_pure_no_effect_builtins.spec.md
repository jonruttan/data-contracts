# Governance Cases

## SRGOV-RUNTIME-SPECLANG-PURE-001

```yaml spec-test
id: SRGOV-RUNTIME-SPECLANG-PURE-001
title: spec-lang evaluators avoid side-effectful builtins
purpose: Enforces pure evaluation semantics by forbidding side-effectful probes in spec-lang
  implementations.
type: governance.check
check: runtime.spec_lang_pure_no_effect_builtins
harness:
  root: .
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  spec_lang_purity:
    files:
    - spec_runner/spec_lang.py
    - scripts/php/spec_runner.php
    - scripts/php/conformance_runner.php
    forbidden_tokens:
    - path_exists
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - runtime.spec_lang_pure_no_effect_builtins
```
