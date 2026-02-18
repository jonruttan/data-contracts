# Governance Cases

## SRGOV-DOCS-REF-005

```yaml contract-spec
id: SRGOV-DOCS-REF-005
title: runner cli flags are documented in development and impl docs
purpose: Prevents CLI contract drift by requiring script flags to be documented in
  the development guide and implementation reference pages.
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
- id: assert_2
  class: MUST
  asserts:
  - MUST:
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
