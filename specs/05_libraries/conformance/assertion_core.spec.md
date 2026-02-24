```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
harness:
  type: unit.test
  profile: check
  config:
    exports:
    - as: conf.pass_when_text_contains
      from: assert.function
      path: "/__export__conf.json_type_is"
      params:
      - subject
      - type_name
      required: true
      docs:
      - id: conf.json_type_is.doc.1
        summary: Contract export for `conf.json_type_is`.
        audience: implementer
        status: active
        description: |-
          Purpose: This entry documents behavior for `conf.json_type_is` for the declared audience, including input expectations, output contracts, and failure modes.

          Inputs:
          - Inputs come from the declared contract and export bindings for this symbol.
          - Runtime bindings and policy constraints are applied by the harness before evaluation.

          Returns:
          - The assertion or helper return value produced by this symbol.

          Errors/Caveats:
          - Malformed inputs and shape mismatches are surfaced as validation failures.
          - Schema/runtime binding or environment mismatches are surfaced as runtime or validation failures.
          - Policy and validation failures are surfaced through contract evaluation, including policy assertions.

          Usage context:
          - Use this for implementation work, local debugging, and runner-side behavior analysis.
        since: v1
        inputs:
        - Contract parameters and required case inputs associated with this docs-bearing
          symbol.
        - Any runtime symbols declared through harness/config bindings for the owning
          execution path.
        returns:
        - Structured evaluation result as defined by the owning assert/export symbol.
        errors:
        - Validation failures for malformed inputs and invalid bindings.
        - Runtime environment and policy compatibility errors.
        usage_context:
        - Use this for implementation work, local debugging, and runner-side behavior
          analysis.
      - id: conf.json_type_is.doc.1.operator
        summary: Contract export for `conf.json_type_is`. (operator)
        audience: operator
        status: active
        description: |-
          Purpose: This entry documents behavior for `conf.json_type_is` for the declared audience, including input expectations, output contracts, and failure modes.

          Inputs:
          - Inputs come from the declared contract and export bindings for this symbol.
          - Runtime bindings and policy constraints are applied by the harness before evaluation.

          Returns:
          - The assertion or helper return value produced by this symbol.

          Errors/Caveats:
          - Malformed inputs and shape mismatches are surfaced as validation failures.
          - Schema/runtime binding or environment mismatches are surfaced as runtime or validation failures.
          - Policy and validation failures are surfaced through contract evaluation, including policy assertions.

          Usage context:
          - Use this for observability, runbook readiness, and incident response.
        since: v1
        inputs:
        - Contract parameters and required case inputs associated with this docs-bearing
          symbol.
        - Any runtime symbols declared through harness/config bindings for the owning
          execution path.
        returns:
        - Structured evaluation result as defined by the owning assert/export symbol.
        errors:
        - Validation failures for malformed inputs and invalid bindings.
        - Runtime environment and policy compatibility errors.
        usage_context:
        - Use this for observability, runbook readiness, and incident response.
      - id: conf.json_type_is.doc.1.integrator
        summary: Contract export for `conf.json_type_is`. (integrator)
        audience: integrator
        status: active
        description: |-
          Purpose: This entry documents behavior for `conf.json_type_is` for the declared audience, including input expectations, output contracts, and failure modes.

          Inputs:
          - Inputs come from the declared contract and export bindings for this symbol.
          - Runtime bindings and policy constraints are applied by the harness before evaluation.

          Returns:
          - The assertion or helper return value produced by this symbol.

          Errors/Caveats:
          - Malformed inputs and shape mismatches are surfaced as validation failures.
          - Schema/runtime binding or environment mismatches are surfaced as runtime or validation failures.
          - Policy and validation failures are surfaced through contract evaluation, including policy assertions.

          Usage context:
          - Use this for composing this contract in pipelines, services, and toolchains.
        since: v1
        inputs:
        - Contract parameters and required case inputs associated with this docs-bearing
          symbol.
        - Any runtime symbols declared through harness/config bindings for the owning
          execution path.
        returns:
        - Structured evaluation result as defined by the owning assert/export symbol.
        errors:
        - Validation failures for malformed inputs and invalid bindings.
        - Runtime environment and policy compatibility errors.
        usage_context:
        - Use this for composing this contract in pipelines, services, and toolchains.
      - id: conf.json_type_is.doc.1.maintainer
        summary: Contract export for `conf.json_type_is`. (maintainer)
        audience: maintainer
        status: active
        description: |-
          Purpose: This entry documents behavior for `conf.json_type_is` for the declared audience, including input expectations, output contracts, and failure modes.

          Inputs:
          - Inputs come from the declared contract and export bindings for this symbol.
          - Runtime bindings and policy constraints are applied by the harness before evaluation.

          Returns:
          - The assertion or helper return value produced by this symbol.

          Errors/Caveats:
          - Malformed inputs and shape mismatches are surfaced as validation failures.
          - Schema/runtime binding or environment mismatches are surfaced as runtime or validation failures.
          - Policy and validation failures are surfaced through contract evaluation, including policy assertions.

          Usage context:
          - Use this for versioning, changelogs, and stability planning.
        since: v1
        inputs:
        - Contract parameters and required case inputs associated with this docs-bearing
          symbol.
        - Any runtime symbols declared through harness/config bindings for the owning
          execution path.
        returns:
        - Structured evaluation result as defined by the owning assert/export symbol.
        errors:
        - Validation failures for malformed inputs and invalid bindings.
        - Runtime environment and policy compatibility errors.
        usage_context:
        - Use this for versioning, changelogs, and stability planning.
      - id: conf.json_type_is.doc.1.governance
        summary: Contract export for `conf.json_type_is`. (governance)
        audience: governance
        status: active
        description: |-
          Purpose: This entry documents behavior for `conf.json_type_is` for the declared audience, including input expectations, output contracts, and failure modes.

          Inputs:
          - Inputs come from the declared contract and export bindings for this symbol.
          - Runtime bindings and policy constraints are applied by the harness before evaluation.

          Returns:
          - The assertion or helper return value produced by this symbol.

          Errors/Caveats:
          - Malformed inputs and shape mismatches are surfaced as validation failures.
          - Schema/runtime binding or environment mismatches are surfaced as runtime or validation failures.
          - Policy and validation failures are surfaced through contract evaluation, including policy assertions.

          Usage context:
          - Use this for policy gating, approval review, and compliance checks.
        since: v1
        inputs:
        - Contract parameters and required case inputs associated with this docs-bearing
          symbol.
        - Any runtime symbols declared through harness/config bindings for the owning
          execution path.
        returns:
        - Structured evaluation result as defined by the owning assert/export symbol.
        errors:
        - Validation failures for malformed inputs and invalid bindings.
        - Runtime environment and policy compatibility errors.
        usage_context:
        - Use this for policy gating, approval review, and compliance checks.
      - id: conf.json_type_is.doc.1.reviewer
        summary: Contract export for `conf.json_type_is`. (reviewer)
        audience: reviewer
        status: active
        description: |-
          Purpose: This entry documents behavior for `conf.json_type_is` for the declared audience, including input expectations, output contracts, and failure modes.

          Inputs:
          - Inputs come from the declared contract and export bindings for this symbol.
          - Runtime bindings and policy constraints are applied by the harness before evaluation.

          Returns:
          - The assertion or helper return value produced by this symbol.

          Errors/Caveats:
          - Malformed inputs and shape mismatches are surfaced as validation failures.
          - Schema/runtime binding or environment mismatches are surfaced as runtime or validation failures.
          - Policy and validation failures are surfaced through contract evaluation, including policy assertions.

          Usage context:
          - Use this to verify correctness, completeness, and release readiness.
        since: v1
        inputs:
        - Contract parameters and required case inputs associated with this docs-bearing
          symbol.
        - Any runtime symbols declared through harness/config bindings for the owning
          execution path.
        returns:
        - Structured evaluation result as defined by the owning assert/export symbol.
        errors:
        - Validation failures for malformed inputs and invalid bindings.
        - Runtime environment and policy compatibility errors.
        usage_context:
        - Use this to verify correctness, completeness, and release readiness.
      - id: conf.json_type_is.doc.1.auditor
        summary: Contract export for `conf.json_type_is`. (auditor)
        audience: auditor
        status: active
        description: |-
          Purpose: This entry documents behavior for `conf.json_type_is` for the declared audience, including input expectations, output contracts, and failure modes.

          Inputs:
          - Inputs come from the declared contract and export bindings for this symbol.
          - Runtime bindings and policy constraints are applied by the harness before evaluation.

          Returns:
          - The assertion or helper return value produced by this symbol.

          Errors/Caveats:
          - Malformed inputs and shape mismatches are surfaced as validation failures.
          - Schema/runtime binding or environment mismatches are surfaced as runtime or validation failures.
          - Policy and validation failures are surfaced through contract evaluation, including policy assertions.

          Usage context:
          - Use this as documented evidence for audit and policy review.
        since: v1
        inputs:
        - Contract parameters and required case inputs associated with this docs-bearing
          symbol.
        - Any runtime symbols declared through harness/config bindings for the owning
          execution path.
        returns:
        - Structured evaluation result as defined by the owning assert/export symbol.
        errors:
        - Validation failures for malformed inputs and invalid bindings.
        - Runtime environment and policy compatibility errors.
        usage_context:
        - Use this as documented evidence for audit and policy review.
  clauses:
  - id: LIB-CONF-ASSERT-001
    title: reusable conformance assertion helper functions
    docs:
    - summary: Case `LIB-CONF-ASSERT-001` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: This entry documents behavior for `conf.json_type_is` for the declared audience, including input expectations, output contracts, and failure modes.

        Inputs:
        - Inputs come from the declared contract and export bindings for this symbol.
        - Runtime bindings and policy constraints are applied by the harness before evaluation.

        Returns:
        - The assertion or helper return value produced by this symbol.

        Errors/Caveats:
        - Malformed inputs and shape mismatches are surfaced as validation failures.
        - Schema/runtime binding or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions.

        Usage context:
        - Use this for implementation work, local debugging, and runner-side behavior analysis.
      since: v1
      tags:
      - conformance
      id: conformance.assertion.core
      module: conformance
      stability: alpha
      owner: data-contracts
      inputs:
      - Contract parameters and required case inputs associated with this docs-bearing
        symbol.
      - Any runtime symbols declared through harness/config bindings for the owning
        execution path.
      returns:
      - Structured evaluation result as defined by the owning assert/export symbol.
      errors:
      - Validation failures for malformed inputs and invalid bindings.
      - Runtime environment and policy compatibility errors.
      usage_context:
      - Use this for implementation work, local debugging, and runner-side behavior
        analysis.
    - summary: Case `LIB-CONF-ASSERT-001` for `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: This entry documents behavior for `conf.json_type_is` for the declared audience, including input expectations, output contracts, and failure modes.

        Inputs:
        - Inputs come from the declared contract and export bindings for this symbol.
        - Runtime bindings and policy constraints are applied by the harness before evaluation.

        Returns:
        - The assertion or helper return value produced by this symbol.

        Errors/Caveats:
        - Malformed inputs and shape mismatches are surfaced as validation failures.
        - Schema/runtime binding or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions.

        Usage context:
        - Use this for observability, runbook readiness, and incident response.
      since: v1
      tags:
      - conformance
      id: conformance.assertion.core.operator
      module: conformance
      stability: alpha
      owner: data-contracts
      inputs:
      - Contract parameters and required case inputs associated with this docs-bearing
        symbol.
      - Any runtime symbols declared through harness/config bindings for the owning
        execution path.
      returns:
      - Structured evaluation result as defined by the owning assert/export symbol.
      errors:
      - Validation failures for malformed inputs and invalid bindings.
      - Runtime environment and policy compatibility errors.
      usage_context:
      - Use this for observability, runbook readiness, and incident response.
    - summary: Case `LIB-CONF-ASSERT-001` for `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: This entry documents behavior for `conf.json_type_is` for the declared audience, including input expectations, output contracts, and failure modes.

        Inputs:
        - Inputs come from the declared contract and export bindings for this symbol.
        - Runtime bindings and policy constraints are applied by the harness before evaluation.

        Returns:
        - The assertion or helper return value produced by this symbol.

        Errors/Caveats:
        - Malformed inputs and shape mismatches are surfaced as validation failures.
        - Schema/runtime binding or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions.

        Usage context:
        - Use this for composing this contract in pipelines, services, and toolchains.
      since: v1
      tags:
      - conformance
      id: conformance.assertion.core.integrator
      module: conformance
      stability: alpha
      owner: data-contracts
      inputs:
      - Contract parameters and required case inputs associated with this docs-bearing
        symbol.
      - Any runtime symbols declared through harness/config bindings for the owning
        execution path.
      returns:
      - Structured evaluation result as defined by the owning assert/export symbol.
      errors:
      - Validation failures for malformed inputs and invalid bindings.
      - Runtime environment and policy compatibility errors.
      usage_context:
      - Use this for composing this contract in pipelines, services, and toolchains.
    - summary: Case `LIB-CONF-ASSERT-001` for `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: This entry documents behavior for `conf.json_type_is` for the declared audience, including input expectations, output contracts, and failure modes.

        Inputs:
        - Inputs come from the declared contract and export bindings for this symbol.
        - Runtime bindings and policy constraints are applied by the harness before evaluation.

        Returns:
        - The assertion or helper return value produced by this symbol.

        Errors/Caveats:
        - Malformed inputs and shape mismatches are surfaced as validation failures.
        - Schema/runtime binding or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions.

        Usage context:
        - Use this for versioning, changelogs, and stability planning.
      since: v1
      tags:
      - conformance
      id: conformance.assertion.core.maintainer
      module: conformance
      stability: alpha
      owner: data-contracts
      inputs:
      - Contract parameters and required case inputs associated with this docs-bearing
        symbol.
      - Any runtime symbols declared through harness/config bindings for the owning
        execution path.
      returns:
      - Structured evaluation result as defined by the owning assert/export symbol.
      errors:
      - Validation failures for malformed inputs and invalid bindings.
      - Runtime environment and policy compatibility errors.
      usage_context:
      - Use this for versioning, changelogs, and stability planning.
    - summary: Case `LIB-CONF-ASSERT-001` for `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: This entry documents behavior for `conf.json_type_is` for the declared audience, including input expectations, output contracts, and failure modes.

        Inputs:
        - Inputs come from the declared contract and export bindings for this symbol.
        - Runtime bindings and policy constraints are applied by the harness before evaluation.

        Returns:
        - The assertion or helper return value produced by this symbol.

        Errors/Caveats:
        - Malformed inputs and shape mismatches are surfaced as validation failures.
        - Schema/runtime binding or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions.

        Usage context:
        - Use this for policy gating, approval review, and compliance checks.
      since: v1
      tags:
      - conformance
      id: conformance.assertion.core.governance
      module: conformance
      stability: alpha
      owner: data-contracts
      inputs:
      - Contract parameters and required case inputs associated with this docs-bearing
        symbol.
      - Any runtime symbols declared through harness/config bindings for the owning
        execution path.
      returns:
      - Structured evaluation result as defined by the owning assert/export symbol.
      errors:
      - Validation failures for malformed inputs and invalid bindings.
      - Runtime environment and policy compatibility errors.
      usage_context:
      - Use this for policy gating, approval review, and compliance checks.
    - summary: Case `LIB-CONF-ASSERT-001` for `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: This entry documents behavior for `conf.json_type_is` for the declared audience, including input expectations, output contracts, and failure modes.

        Inputs:
        - Inputs come from the declared contract and export bindings for this symbol.
        - Runtime bindings and policy constraints are applied by the harness before evaluation.

        Returns:
        - The assertion or helper return value produced by this symbol.

        Errors/Caveats:
        - Malformed inputs and shape mismatches are surfaced as validation failures.
        - Schema/runtime binding or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions.

        Usage context:
        - Use this to verify correctness, completeness, and release readiness.
      since: v1
      tags:
      - conformance
      id: conformance.assertion.core.reviewer
      module: conformance
      stability: alpha
      owner: data-contracts
      inputs:
      - Contract parameters and required case inputs associated with this docs-bearing
        symbol.
      - Any runtime symbols declared through harness/config bindings for the owning
        execution path.
      returns:
      - Structured evaluation result as defined by the owning assert/export symbol.
      errors:
      - Validation failures for malformed inputs and invalid bindings.
      - Runtime environment and policy compatibility errors.
      usage_context:
      - Use this to verify correctness, completeness, and release readiness.
    - summary: Case `LIB-CONF-ASSERT-001` for `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: This entry documents behavior for `conf.json_type_is` for the declared audience, including input expectations, output contracts, and failure modes.

        Inputs:
        - Inputs come from the declared contract and export bindings for this symbol.
        - Runtime bindings and policy constraints are applied by the harness before evaluation.

        Returns:
        - The assertion or helper return value produced by this symbol.

        Errors/Caveats:
        - Malformed inputs and shape mismatches are surfaced as validation failures.
        - Schema/runtime binding or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions.

        Usage context:
        - Use this as documented evidence for audit and policy review.
      since: v1
      tags:
      - conformance
      id: conformance.assertion.core.auditor
      module: conformance
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__conf.pass_when_text_contains
        assert:
          std.string.contains:
          - var: subject
          - var: token
      - id: __export__conf.pass_when_text_regex
        assert:
          std.string.regex_match:
          - var: subject
          - var: pattern
      - id: __export__conf.eq
        assert:
          std.logic.eq:
          - var: subject
          - var: value
      - id: __export__conf.has_error_category
        assert:
          std.string.contains:
          - var: subject
          - var: category
      - id: __export__conf.json_type_is
        assert:
          std.type.json_type:
          - var: subject
          - var: type_name
      inputs:
      - Contract parameters and required case inputs associated with this docs-bearing
        symbol.
      - Any runtime symbols declared through harness/config bindings for the owning
        execution path.
      returns:
      - Structured evaluation result as defined by the owning assert/export symbol.
      errors:
      - Validation failures for malformed inputs and invalid bindings.
      - Runtime environment and policy compatibility errors.
      usage_context:
      - Use this as documented evidence for audit and policy review.
adapters:
- type: beta.exports_as_conf_pass_when_text_contains_from_assert_function_path_export_conf_pass_when_text_contains_params_subject_token_required_true_docs_id_conf_pass_when_text_contains_doc_1_summary_contract_export_for_conf_pass_when_text_contains_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_token_token_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_token_n_type_any_n_required_true_n_description_input_parameter_token_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_conf_pass_when_text_regex_from_assert_function_path_export_conf_pass_when_text_regex_params_subject_pattern_required_true_docs_id_conf_pass_when_text_regex_doc_1_summary_contract_export_for_conf_pass_when_text_regex_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_pattern_pattern_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_pattern_n_type_any_n_required_true_n_description_input_parameter_pattern_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_conf_eq_from_assert_function_path_export_conf_eq_params_subject_value_required_true_docs_id_conf_eq_doc_1_summary_contract_export_for_conf_eq_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_value_value_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_value_n_type_any_n_required_true_n_description_input_parameter_value_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_conf_has_error_category_from_assert_function_path_export_conf_has_error_category_params_subject_category_required_true_docs_id_conf_has_error_category_doc_1_summary_contract_export_for_conf_has_error_category_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_category_category_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_category_n_type_any_n_required_true_n_description_input_parameter_category_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_conf_json_type_is_from_assert_function_path_export_conf_json_type_is_params_subject_type_name_required_true_docs_id_conf_json_type_is_doc_1_summary_contract_export_for_conf_json_type_is_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_type_name_type_name_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_type_name_n_type_any_n_required_true_n_description_input_parameter_type_name_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.assertion.core.spec.1
    direction: bidirectional
    profile: default
services:
- id: svc.lib.assertion.core.spec.1
  consumes:
  - act.lib.assertion.core.spec.1
```
