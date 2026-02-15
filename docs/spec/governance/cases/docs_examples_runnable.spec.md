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
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  docs_examples:
    files:
    - docs/book/01_quickstart.md
    - docs/book/02_core_model.md
    - docs/book/03_assertions.md
    - docs/book/04_spec_lang_reference.md
    - docs/development.md
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
      - docs.examples_runnable
```
