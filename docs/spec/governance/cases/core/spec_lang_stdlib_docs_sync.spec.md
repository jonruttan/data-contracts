# Governance Cases

## SRGOV-STDLIB-003

```yaml spec-test
id: SRGOV-STDLIB-003
title: stdlib profile references are synchronized in schema contract and book docs
purpose: Ensures core docs reference the canonical stdlib profile artifacts.
type: governance.check
check: spec_lang.stdlib_docs_sync
harness:
  root: .
  policy_evaluate:
  - {call: [{var: policy.pass_when_no_violations}, {var: subject}]}
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{var: subject}, 0]}
```
