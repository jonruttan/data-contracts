# Governance Cases

## SRGOV-DOCS-QUAL-009

```yaml spec-test
id: SRGOV-DOCS-QUAL-009
title: release contract forbids manual sequential checklist choreography
purpose: Ensures release guidance uses executable gate entrypoints and codifies that manual do-X-then-inspect-Y sequences are an anti-pattern.
type: governance.check
check: docs.release_contract_automation_policy
harness:
  root: .
  release_contract:
    files:
    - docs/release_checklist.md
    required_tokens:
    - Release readiness is defined by executable gates, not manual checklists.
    - make ci-smoke
    - ./scripts/ci_gate.sh
    - convert it into an executable
    forbidden_patterns:
    - (?m)^##\s+[0-9]+\)
    - (?m)^\s*[0-9]+\.\s+(Run|Then|Check|Inspect)\b
  policy_evaluate:
  - is_empty:
    - {get: [{subject: []}, violations]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - docs.release_contract_automation_policy
```
