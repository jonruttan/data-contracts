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
assert:
  - target: text
    must:
      - contain: ["PASS: docs.cli_flags_documented"]
```
