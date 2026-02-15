# Governance Cases

## SRGOV-REF-SYMBOLS-004

```yaml spec-test
id: SRGOV-REF-SYMBOLS-004
title: private library symbols are not referenced externally
purpose: Ensures conformance/governance/impl cases do not reference functions.private symbols from library docs.
type: governance.check
check: reference.private_symbols_forbidden
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
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{var: subject}, check_id]}
      - reference.private_symbols_forbidden
```
