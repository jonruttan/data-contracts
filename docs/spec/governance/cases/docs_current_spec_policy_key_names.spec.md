# Governance Cases

## SRGOV-DOCS-CURRENT-KEYS-001

```yaml spec-test
id: SRGOV-DOCS-CURRENT-KEYS-001
title: current spec policy key names stay canonical
purpose: Enforces policy expression naming consistency by allowing only `policy_evaluate` in `.spec.md` cases.
type: governance.check
check: docs.current_spec_policy_key_names
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
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
      - docs.current_spec_policy_key_names
```
