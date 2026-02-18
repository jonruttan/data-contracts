# Governance Cases

## SRGOV-DOCS-QUAL-009

```yaml contract-spec
id: SRGOV-DOCS-QUAL-009
title: release contract forbids manual sequential checklist choreography
purpose: Ensures release guidance uses executable gate entrypoints and codifies that manual
  do-X-then-inspect-Y sequences are an anti-pattern.
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
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  asserts:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.release_contract_automation_policy
  target: summary_json
```
