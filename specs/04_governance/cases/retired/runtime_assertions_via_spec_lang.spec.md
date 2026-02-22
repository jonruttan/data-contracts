```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
defaults:
  type: contract.check
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - '{''root'': ''.'', ''assert_engine'': {''files'': [{''path'': ''/dc-runner-php'', ''required_tokens'': [''compileAssertionLeafExpr('', ''assertLeafPredicate('', ''specLangEvalPredicate(''], ''forbidden_tokens'': [''strpos($subject, $v)'', "preg_match(''/'' . str_replace(''/'', ''\\/'', $v) . ''/u'', $subject)"]}, {''path'': ''/dc-runner-php'', ''required_tokens'': [''compileAssertionLeafExpr('', ''assertLeafPredicate('', ''specLangEvalPredicate(''], ''forbidden_tokens'': [''strpos($subject, $v)'', "preg_match(''/'' . str_replace(''/'', ''\\/'', $v) . ''/u'', $subject)"]}, {''path'': ''/dc-runner-python'', ''required_tokens'': [''eval_predicate(''], ''forbidden_tokens'': [''assert_text_op('']}, {''path'': ''/dc-runner-python'', ''required_tokens'': [''evaluate_internal_assert_tree('', ''eval_predicate(''], ''forbidden_tokens'': [''def assert_text_op('']}, {''path'': ''/dc-runner-python'', ''required_tokens'': [''run_assertions_with_context(''], ''forbidden_tokens'': [''contain assertion failed'']}, {''path'': ''/dc-runner-python'', ''required_tokens'': [''run_assertions_with_context(''], ''forbidden_tokens'': [''contain assertion failed'']}, {''path'': ''/dc-runner-python'', ''required_tokens'': [''run_assertions_with_context(''], ''forbidden_tokens'': [''contain assertion failed'']}]}, ''check'': {''profile'': ''governance.scan'', ''config'': {''check'': ''runtime.assertions_via_spec_lang''}}, ''use'': [{''ref'': ''/specs/05_libraries/policy/policy_core.spec.md'', ''as'': ''lib_policy_core_spec'', ''symbols'': [''policy.pass_when_no_violations'']}]}'
services:
  actions:
  - id: svc.root_assert_engine_files_path_dc_runner_php_required_tokens_compileassertionleafexpr_assertleafpredicate_speclangevalpredicate_forbidden_tokens_strpos_subject_v_preg_match_str_replace_v_u_subject_path_dc_runner_php_required_tokens_compileassertionleafexpr_assertleafpredicate_speclangevalpredicate_forbidden_tokens_strpos_subject_v_preg_match_str_replace_v_u_subject_path_dc_runner_python_required_tokens_eval_predicate_forbidden_tokens_assert_text_op_path_dc_runner_python_required_tokens_evaluate_internal_assert_tree_eval_predicate_forbidden_tokens_def_assert_text_op_path_dc_runner_python_required_tokens_run_assertions_with_context_forbidden_tokens_contain_assertion_failed_path_dc_runner_python_required_tokens_run_assertions_with_context_forbidden_tokens_contain_assertion_failed_path_dc_runner_python_required_tokens_run_assertions_with_context_forbidden_tokens_contain_assertion_failed_check_profile_governance_scan_config_check_runtime_assertions_via_spec_lang_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_assert_engine_files_path_dc_runner_php_required_tokens_compileassertionleafexpr_assertleafpredicate_speclangevalpredicate_forbidden_tokens_strpos_subject_v_preg_match_str_replace_v_u_subject_path_dc_runner_php_required_tokens_compileassertionleafexpr_assertleafpredicate_speclangevalpredicate_forbidden_tokens_strpos_subject_v_preg_match_str_replace_v_u_subject_path_dc_runner_python_required_tokens_eval_predicate_forbidden_tokens_assert_text_op_path_dc_runner_python_required_tokens_evaluate_internal_assert_tree_eval_predicate_forbidden_tokens_def_assert_text_op_path_dc_runner_python_required_tokens_run_assertions_with_context_forbidden_tokens_contain_assertion_failed_path_dc_runner_python_required_tokens_run_assertions_with_context_forbidden_tokens_contain_assertion_failed_path_dc_runner_python_required_tokens_run_assertions_with_context_forbidden_tokens_contain_assertion_failed_check_profile_governance_scan_config_check_runtime_assertions_via_spec_lang_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-ASSERT-001
  title: runtime assertion paths compile and evaluate through spec-lang
  purpose: Enforces that runner assertion semantics route through spec-lang expression evaluation and avoid direct ad-hoc contain or regex execution paths.
  clauses:
    imports:
    - artifact:
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
        - runtime.assertions_via_spec_lang
      imports:
      - artifact:
        - summary_json
```
