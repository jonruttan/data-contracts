# Governance Cases

## SRGOV-DOCS-REF-005

```yaml spec-test
id: SRGOV-DOCS-REF-005
title: runner cli flags are documented in development and impl docs
purpose: Prevents CLI contract drift by requiring script flags to be documented in the development
  guide and implementation reference pages.
type: governance.check
check: docs.cli_flags_documented
harness:
  root: .
  cli_docs:
    python_scripts:
    - scripts/python/conformance_runner.py
    php_scripts:
    - scripts/php/conformance_runner.php
    - scripts/php/spec_runner.php
    python_docs:
    - docs/development.md
    - docs/spec/impl/python.md
    php_docs:
    - docs/development.md
    - docs/spec/impl/php.md
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
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.cli_flags_documented
  target: summary_json
```
