# Governance Cases

## SRGOV-DOCS-REF-004

```yaml spec-test
id: SRGOV-DOCS-REF-004
title: reference examples parse or are explicitly opted out
purpose: Ensures reference examples are trustworthy by requiring parseable or statically valid fenced examples unless explicitly opted out.
type: governance.check
check: docs.examples_runnable
harness:
  root: .
  docs_examples:
    files:
    - docs/book/01_quickstart.md
    - docs/book/02_core_model.md
    - docs/book/03_assertions.md
    - docs/book/04_spec_lang_reference.md
    - docs/development.md
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: docs.examples_runnable'
```
