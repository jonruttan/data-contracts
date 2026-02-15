# Governance Cases

## SRGOV-DOC-CURRENT-001

```yaml spec-test
id: SRGOV-DOC-CURRENT-001
title: current-spec-only contract forbids prior-schema references and shims
purpose: Ensures pre-v1 docs and parser paths stay focused on current schema only, without prior-spec wording or compatibility rewrites.
type: governance.check
check: docs.current_spec_only_contract
harness:
  root: .
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - {call: [{var: policy.pass_when_no_violations}, {var: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{var: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{var: subject}, passed]}
      - true
    - eq:
      - {get: [{var: subject}, check_id]}
      - docs.current_spec_only_contract
```
