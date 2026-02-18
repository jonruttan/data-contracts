# Governance Cases

## SRGOV-RUNTIME-POLICY-FORBID-001

```yaml contract-spec
id: SRGOV-RUNTIME-POLICY-FORBID-001
title: governance cases forbid policy_evaluate decision fields
purpose: Ensures governance contracts do not declare harness.policy_evaluate or
  harness.orchestration_policy.policy_evaluate.
type: governance.check
check: runtime.policy_evaluate_forbidden
harness:
  root: .
  policy_forbidden:
    cases_path: /docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
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
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - passed
    - true
  target: summary_json
```
