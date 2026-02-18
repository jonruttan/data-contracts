# Governance Cases

## SRGOV-POLICY-REQ-002

```yaml contract-spec
id: SRGOV-POLICY-REQ-002
title: governance checks avoid check-level policy verdict branching
purpose: Ensures check functions do not embed per-check policy verdict strings and
  rely on central governance policy evaluation.
type: governance.check
check: governance.extractor_only_no_verdict_branching
harness:
  root: .
  extractor_policy:
    path: /scripts/run_governance_specs.py
    forbidden_tokens:
    - spec.portability_metric policy_evaluate returned false
    - spec.spec_lang_adoption_metric policy_evaluate returned false
    - runtime.runner_independence_metric policy_evaluate returned false
    - docs.operability_metric policy_evaluate returned false
    - spec.contract_assertions_metric policy_evaluate returned false
    - objective.scorecard_metric policy_evaluate returned false
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
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - governance.extractor_only_no_verdict_branching
  target: summary_json
```
