# Governance Cases

## SRGOV-POLICY-REQ-001

```yaml spec-test
id: SRGOV-POLICY-REQ-001
title: governance checks require policy_evaluate contract
purpose: Ensures governance decision contracts include explicit policy_evaluate expressions in harness config.
type: governance.check
check: governance.policy_evaluate_required
harness:
  root: .
  policy_requirements:
    cases_path: docs/spec/governance/cases
    case_file_pattern: "*.spec.md"
    required_checks:
      - conformance.portable_determinism_guard
      - conformance.no_ambient_assumptions
      - conformance.spec_lang_preferred
      - spec.portability_metric
      - spec.spec_lang_adoption_metric
      - runtime.runner_independence_metric
      - docs.operability_metric
      - spec.contract_assertions_metric
      - objective.scorecard_metric
      - runtime.orchestration_policy_via_spec_lang
    ignore_checks:
      - governance.policy_evaluate_required
      - governance.extractor_only_no_verdict_branching
      - runtime.rust_adapter_no_python_exec
  policy_evaluate:
    - ["eq", true, true]
assert:
  - target: text
    must:
      - contain: ["PASS: governance.policy_evaluate_required"]
```
