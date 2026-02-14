# Governance Cases

## SRGOV-DOCS-REF-007

```yaml spec-test
id: SRGOV-DOCS-REF-007
title: docs use canonical make command entrypoints
purpose: Keeps contributor docs aligned on the canonical make-based command entrypoints for verification and gate execution.
type: governance.check
check: docs.make_commands_sync
harness:
  root: .
  make_commands:
    files:
      - README.md
      - docs/development.md
    required_tokens:
      - make verify-docs
      - make check
assert:
  - target: text
    must:
      - contain: ["PASS: docs.make_commands_sync"]
```
