# Governance Cases

## SRGOV-DOCS-REF-005

```yaml spec-test
id: SRGOV-DOCS-REF-005
title: runner cli flags are documented in development and impl docs
purpose: Prevents CLI contract drift by requiring script flags to be documented in the development guide and implementation reference pages.
type: governance.check
check: docs.cli_flags_documented
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
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
  - {call: [{var: [policy.pass_when_no_violations]}, {ref: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{ref: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{ref: subject}, passed]}
      - true
    - eq:
      - {get: [{ref: subject}, check_id]}
      - docs.cli_flags_documented
```
