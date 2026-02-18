# Governance Cases

## SRGOV-DOCS-REF-003

```yaml contract-spec
id: SRGOV-DOCS-REF-003
title: key reference chapters include required sections
purpose: Keeps the core reference pages structurally complete by requiring stable section
  tokens for author and implementer workflows.
type: contract.check
harness:
  root: .
  required_sections:
    docs/book/02_core_model.md:
    - '## Required Keys'
    - '## Discovery Model'
    - '## Type Model'
    - '## `harness` Namespace Rule'
    - '## Checklist'
    docs/book/03_assertions.md:
    - '## Step Shape'
    - '## Group Semantics'
    - '## Targets'
    - '## Operators'
    - '## Checklist'
    docs/book/07_spec_lang_reference.md:
    - '## 1) What `evaluate` Is'
    - '## 3) Core Forms'
    - '## 5) Budgets (`harness.spec_lang`)'
    - '## 6) Error Categories'
    - '## 9) Lint + Format'
    docs/book/reference_index.md:
    - '# Reference Index'
    - Canonical order for reference-manual chapters.
    - how to use
    docs/book/04_spec_lang_guide.md:
    - '## Mental Model'
    - '## Common Authoring Patterns'
    - '## Anti-Patterns'
    - '## Library Usage Patterns'
    - '## Debugging Evaluate Expressions'
    docs/book/05_howto.md:
    - '## Add A New Spec Case'
    - '## Add Or Reuse A Library Function'
    - '## Add A Governance Check'
    - '## Run Local Gate Subsets'
    docs/book/06_troubleshooting.md:
    - '## Triage Flow'
    - '## Check-ID To Cause Mapping'
    - '## Fast Recovery Playbook'
    - '## When To Escalate'
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
      check: docs.required_sections
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
    - docs.required_sections
  target: summary_json
```
