# Governance Cases

## SRGOV-STDLIB-004

```yaml spec-test
id: SRGOV-STDLIB-004
title: stdlib conformance coverage files are present
purpose: Ensures canonical stdlib conformance fixtures are present and discoverable.
type: governance.check
check: spec_lang.stdlib_conformance_coverage
harness:
  root: .
  stdlib_conformance:
    required_paths:
    - /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
    - /docs/spec/conformance/cases/core/spec_lang_schema.spec.md
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
