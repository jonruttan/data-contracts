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
    - runners/python/spec_runner/python_conformance_runner.py
    php_scripts:
    - runners/php/conformance_runner.php
    - runners/php/spec_runner.php
    python_docs:
    - docs/development.md
    - specs/impl/python.md
    php_docs:
    - docs/development.md
    - specs/impl/php.md
  check:
    profile: governance.scan
    config:
      check: docs.cli_flags_documented
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
  - id: assert_2
    target: summary_json
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
      - docs.cli_flags_documented
```
