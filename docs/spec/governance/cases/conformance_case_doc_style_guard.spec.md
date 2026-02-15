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
  policy_evaluate:
    - ["is_empty", ["get", ["subject"], "violations"]]
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.case_doc_style_guard"]
```
