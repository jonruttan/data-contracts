# Governance Cases

## SRGOV-CONF-STYLE-001

```yaml spec-test
id: SRGOV-CONF-STYLE-001
title: conformance case documents satisfy style and purpose lint rules
purpose: Ensures conformance fixtures remain readable, deterministic, and policy-compliant.
type: governance.check
check: conformance.case_doc_style_guard
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
      - conformance.case_doc_style_guard
```
