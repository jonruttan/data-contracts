```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-POLICY-REQ-002
  title: governance checks avoid check-level policy verdict branching
  purpose: Ensures check functions do not embed per-check policy verdict strings
    and rely on central governance policy evaluation.
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        std.logic.eq:
        - var: violation_count
        - 0
    - id: assert_2
      assert:
      - std.logic.eq:
        - std.object.get:
          - var: summary_json
          - passed
        - true
      - std.logic.eq:
        - std.object.get:
          - var: summary_json
          - check_id
        - governance.extractor_only_no_verdict_branching
      imports:
      - from: artifact
        names:
        - summary_json
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'extractor_policy': {'path': '/dc-runner-python', 'forbidden_tokens':
      ['spec.portability_metric evaluate returned false', 'spec.spec_lang_adoption_metric
      evaluate returned false', 'runtime.runner_independence_metric evaluate returned
      false', 'docs.operability_metric evaluate returned false', 'spec.contract_assertions_metric
      evaluate returned false', 'objective.scorecard_metric evaluate returned false']},
      'check': {'profile': 'governance.scan', 'config': {'check': 'governance.extractor_only_no_verdict_branching'}},
      'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.pass_when_no_violations']}]}"
services:
  entries:
  - id: 
      svc.root_extractor_policy_path_dc_runner_python_forbidden_tokens_spec_portability_metric_evaluate_returned_false_spec_spec_lang_adoption_metric_evaluate_returned_false_runtime_runner_independence_metric_evaluate_returned_false_docs_operability_metric_evaluate_returned_false_spec_contract_assertions_metric_evaluate_returned_false_objective_scorecard_metric_evaluate_returned_false_check_profile_governance_scan_config_check_governance_extractor_only_no_verdict_branching_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: 
      legacy.root_extractor_policy_path_dc_runner_python_forbidden_tokens_spec_portability_metric_evaluate_returned_false_spec_spec_lang_adoption_metric_evaluate_returned_false_runtime_runner_independence_metric_evaluate_returned_false_docs_operability_metric_evaluate_returned_false_spec_contract_assertions_metric_evaluate_returned_false_objective_scorecard_metric_evaluate_returned_false_check_profile_governance_scan_config_check_governance_extractor_only_no_verdict_branching_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
    config: {}
    default: true
```
