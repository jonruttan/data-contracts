# Governance Cases

## SRGOV-DOCS-REF-003

```yaml spec-test
id: SRGOV-DOCS-REF-003
title: key reference chapters include required sections
purpose: Keeps the core reference pages structurally complete by requiring stable section
  tokens for author and implementer workflows.
type: governance.check
check: docs.required_sections
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  required_sections:
    docs/book/02_core_model.md:
    - '## Required Keys'
    - '## Discovery Model'
    - '## Type Model'
    - '## `harness` Namespace Rule'
    - '## Checklist'
    docs/book/03_assertions.md:
    - '## Tree Shape'
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
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - docs.required_sections
```
