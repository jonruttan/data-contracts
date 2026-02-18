# Governance Cases

## SRGOV-DOCS-REF-005

```yaml contract-spec
id: SRGOV-DOCS-REF-005
title: runner cli flags are documented in development and impl docs
purpose: Prevents CLI contract drift by requiring script flags to be documented in the development
  guide and implementation reference pages.
type: contract.check
harness:
  root: .
  cli_docs:
    python_scripts:
    - spec_runner/python_conformance_runner.py
    php_scripts:
    - runners/php/conformance_runner.php
    - runners/php/spec_runner.php
    python_docs:
    - docs/development.md
    - specs/impl/python.md
    php_docs:
    - docs/development.md
    - specs/impl/php.md
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: docs.cli_flags_documented
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - passed
    - true
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - docs.cli_flags_documented
  target: summary_json
```
