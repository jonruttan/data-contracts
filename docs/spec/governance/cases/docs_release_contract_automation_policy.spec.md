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
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
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
      - docs.release_contract_automation_policy
```
