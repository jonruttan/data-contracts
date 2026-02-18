# Governance Cases

## SRGOV-RUNTIME-SPECLANG-PURE-001

```yaml contract-spec
id: SRGOV-RUNTIME-SPECLANG-PURE-001
title: spec-lang evaluators avoid side-effectful builtins
purpose: Enforces pure evaluation semantics by forbidding side-effectful probes in spec-lang
  implementations.
type: contract.check
harness:
  root: .
  spec_lang_purity:
    files:
    - spec_runner/spec_lang.py
    - scripts/php/spec_runner.php
    - scripts/php/conformance_runner.php
    forbidden_tokens:
    - path_exists
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
      check: runtime.spec_lang_pure_no_effect_builtins
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          MUST:
          - std.logic.eq:
            - std.object.get:
              - {var: subject}
              - passed
            - true
          - std.logic.eq:
            - std.object.get:
              - {var: subject}
              - check_id
            - runtime.spec_lang_pure_no_effect_builtins
  target: summary_json
```
