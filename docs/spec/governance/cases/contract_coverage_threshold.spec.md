# Governance Cases

## SRGOV-CONTRACT-002

```yaml spec-test
id: SRGOV-CONTRACT-002
title: contract must-rule coverage stays complete
purpose: Ensures all MUST policy rules remain covered by traceability evidence and keeps overall contract coverage above a minimum baseline.
type: governance.check
check: contract.coverage_threshold
harness:
  root: .
  contract_coverage:
    require_all_must_covered: true
    min_coverage_ratio: 0.50
assert:
  - target: text
    must:
      - contain: ["PASS: contract.coverage_threshold"]
```
