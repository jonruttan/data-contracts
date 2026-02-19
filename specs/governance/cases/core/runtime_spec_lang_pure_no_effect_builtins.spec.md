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
    - runners/python/spec_runner/spec_lang.py
    - runners/php/spec_runner.php
    - runners/php/conformance_runner.php
    forbidden_tokens:
    - path_exists
  check:
    profile: governance.scan
    config:
      check: runtime.spec_lang_pure_no_effect_builtins
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    assert:
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
    imports:
      subject:
        from: artifact
        key: summary_json
```
