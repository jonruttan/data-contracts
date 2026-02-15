# Governance Cases

## SRGOV-POLICY-REQ-002

```yaml spec-test
id: SRGOV-POLICY-REQ-002
title: governance checks avoid check-level policy verdict branching
purpose: Ensures check functions do not embed per-check policy verdict strings and rely on central governance policy evaluation.
type: governance.check
check: governance.extractor_only_no_verdict_branching
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  extractor_policy:
    path: scripts/run_governance_specs.py
    forbidden_tokens:
    - spec.portability_metric policy_evaluate returned false
    - spec.spec_lang_adoption_metric policy_evaluate returned false
    - runtime.runner_independence_metric policy_evaluate returned false
    - docs.operability_metric policy_evaluate returned false
    - spec.contract_assertions_metric policy_evaluate returned false
    - objective.scorecard_metric policy_evaluate returned false
  policy_evaluate:
  - {eq: [true, true]}
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
      - governance.extractor_only_no_verdict_branching
```
