# Governance Cases

## SRGOV-DOCS-REF-004

```yaml contract-spec
id: SRGOV-DOCS-REF-004
title: reference examples parse or are explicitly opted out
purpose: Ensures reference examples are trustworthy by requiring parseable or statically
  valid fenced examples unless explicitly opted out.
type: governance.check
check: docs.examples_runnable
harness:
  root: .
  docs_examples:
    files:
    - docs/book/01_quickstart.md
    - docs/book/02_core_model.md
    - docs/book/03_assertions.md
    - docs/book/04_spec_lang_guide.md
    - docs/book/05_howto.md
    - docs/book/06_troubleshooting.md
    - docs/book/07_spec_lang_reference.md
    - docs/development.md
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
      - docs.examples_runnable
  target: summary_json
```
