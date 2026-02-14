# Governance Cases

## SRGOV-DOCS-REF-003

```yaml spec-test
id: SRGOV-DOCS-REF-003
title: key reference chapters include required sections
purpose: Keeps the core reference pages structurally complete by requiring stable section tokens for author and implementer workflows.
type: governance.check
check: docs.required_sections
harness:
  root: .
  required_sections:
    docs/book/02_core_model.md:
      - "## Required Keys"
      - "## Discovery Model"
      - "## Type Model"
      - "## `harness` Namespace Rule"
      - "## Checklist"
    docs/book/03_assertions.md:
      - "## Tree Shape"
      - "## Group Semantics"
      - "## Targets"
      - "## Operators"
      - "## Checklist"
    docs/book/04_spec_lang_reference.md:
      - "## 1) What `evaluate` Is"
      - "## 3) Core Forms"
      - "## 5) Budgets (`harness.spec_lang`)"
      - "## 6) Error Categories"
      - "## 9) Lint + Format"
    docs/book/reference_index.md:
      - "# Reference Index"
      - "Canonical order for reference-manual chapters."
      - "how to use"
assert:
  - target: text
    must:
      - contain: ["PASS: docs.required_sections"]
```
