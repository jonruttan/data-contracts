```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
harness:
  type: unit.test
  profile: check
  config:
    exports:
    - as: domain.contract_set.id
      from: assert.function
      path: "/__export__domain.contract_set.applies_to_runners"
      params:
      - manifest
      required: true
      docs:
      - id: domain.contract_set.applies_to_runners.doc.1
        summary: Contract export for `domain.contract_set.applies_to_runners`.
        audience: implementer
        status: active
        description: |-
          Purpose: Documents the runtime behavior and intent of `domain.contract_set.applies_to_runners` for this audience.

          Inputs:
          - Inputs come from the owning contract declaration and required fixture inputs for this symbol.
          - Runtime bindings and policy constraints are applied by the harness before execution. 

          Returns:
          - Returns the assertion or helper value produced by this symbol after all constraints apply.

          Errors/Caveats:
          - Input/shape mismatches are surfaced as validation failures. 
          - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
          - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

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
      - id: domain.contract_set.applies_to_runners.doc.1.operator
        summary: Contract export for `domain.contract_set.applies_to_runners`. (operator)
        audience: operator
        status: active
        description: |-
          Purpose: Documents the runtime behavior and intent of `domain.contract_set.applies_to_runners` for this audience.

          Inputs:
          - Inputs come from the owning contract declaration and required fixture inputs for this symbol.
          - Runtime bindings and policy constraints are applied by the harness before execution. 

          Returns:
          - Returns the assertion or helper value produced by this symbol after all constraints apply.

          Errors/Caveats:
          - Input/shape mismatches are surfaced as validation failures. 
          - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
          - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

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
      - id: domain.contract_set.applies_to_runners.doc.1.integrator
        summary: Contract export for `domain.contract_set.applies_to_runners`. (integrator)
        audience: integrator
        status: active
        description: |-
          Purpose: Documents the runtime behavior and intent of `domain.contract_set.applies_to_runners` for this audience.

          Inputs:
          - Inputs come from the owning contract declaration and required fixture inputs for this symbol.
          - Runtime bindings and policy constraints are applied by the harness before execution. 

          Returns:
          - Returns the assertion or helper value produced by this symbol after all constraints apply.

          Errors/Caveats:
          - Input/shape mismatches are surfaced as validation failures. 
          - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
          - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

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
      - id: domain.contract_set.applies_to_runners.doc.1.maintainer
        summary: Contract export for `domain.contract_set.applies_to_runners`. (maintainer)
        audience: maintainer
        status: active
        description: |-
          Purpose: Documents the runtime behavior and intent of `domain.contract_set.applies_to_runners` for this audience.

          Inputs:
          - Inputs come from the owning contract declaration and required fixture inputs for this symbol.
          - Runtime bindings and policy constraints are applied by the harness before execution. 

          Returns:
          - Returns the assertion or helper value produced by this symbol after all constraints apply.

          Errors/Caveats:
          - Input/shape mismatches are surfaced as validation failures. 
          - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
          - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

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
      - id: domain.contract_set.applies_to_runners.doc.1.governance
        summary: Contract export for `domain.contract_set.applies_to_runners`. (governance)
        audience: governance
        status: active
        description: |-
          Purpose: Documents the runtime behavior and intent of `domain.contract_set.applies_to_runners` for this audience.

          Inputs:
          - Inputs come from the owning contract declaration and required fixture inputs for this symbol.
          - Runtime bindings and policy constraints are applied by the harness before execution. 

          Returns:
          - Returns the assertion or helper value produced by this symbol after all constraints apply.

          Errors/Caveats:
          - Input/shape mismatches are surfaced as validation failures. 
          - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
          - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

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
      - id: domain.contract_set.applies_to_runners.doc.1.reviewer
        summary: Contract export for `domain.contract_set.applies_to_runners`. (reviewer)
        audience: reviewer
        status: active
        description: |-
          Purpose: Documents the runtime behavior and intent of `domain.contract_set.applies_to_runners` for this audience.

          Inputs:
          - Inputs come from the owning contract declaration and required fixture inputs for this symbol.
          - Runtime bindings and policy constraints are applied by the harness before execution. 

          Returns:
          - Returns the assertion or helper value produced by this symbol after all constraints apply.

          Errors/Caveats:
          - Input/shape mismatches are surfaced as validation failures. 
          - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
          - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

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
      - id: domain.contract_set.applies_to_runners.doc.1.auditor
        summary: Contract export for `domain.contract_set.applies_to_runners`. (auditor)
        audience: auditor
        status: active
        description: |-
          Purpose: Documents the runtime behavior and intent of `domain.contract_set.applies_to_runners` for this audience.

          Inputs:
          - Inputs come from the owning contract declaration and required fixture inputs for this symbol.
          - Runtime bindings and policy constraints are applied by the harness before execution. 

          Returns:
          - Returns the assertion or helper value produced by this symbol after all constraints apply.

          Errors/Caveats:
          - Input/shape mismatches are surfaced as validation failures. 
          - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
          - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

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
  - id: LIB-DOMAIN-CONTRACT-SET-001
    title: contract-set manifest projection helper functions
    docs:
    - summary: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.contract_set.applies_to_runners` for this audience.

        Inputs:
        - Inputs come from the owning contract declaration and required fixture inputs for this symbol.
        - Runtime bindings and policy constraints are applied by the harness before execution. 

        Returns:
        - Returns the assertion or helper value produced by this symbol after all constraints apply.

        Errors/Caveats:
        - Input/shape mismatches are surfaced as validation failures. 
        - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

        Usage context:
        - Use this for implementation work, local debugging, and runner-side behavior analysis.
      since: v1
      tags:
      - domain
      id: domain.contract_set.core
      module: domain
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
    - summary: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.contract_set.applies_to_runners` for this audience.

        Inputs:
        - Inputs come from the owning contract declaration and required fixture inputs for this symbol.
        - Runtime bindings and policy constraints are applied by the harness before execution. 

        Returns:
        - Returns the assertion or helper value produced by this symbol after all constraints apply.

        Errors/Caveats:
        - Input/shape mismatches are surfaced as validation failures. 
        - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

        Usage context:
        - Use this for observability, runbook readiness, and incident response.
      since: v1
      tags:
      - domain
      id: domain.contract_set.core.operator
      module: domain
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
    - summary: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.contract_set.applies_to_runners` for this audience.

        Inputs:
        - Inputs come from the owning contract declaration and required fixture inputs for this symbol.
        - Runtime bindings and policy constraints are applied by the harness before execution. 

        Returns:
        - Returns the assertion or helper value produced by this symbol after all constraints apply.

        Errors/Caveats:
        - Input/shape mismatches are surfaced as validation failures. 
        - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

        Usage context:
        - Use this for composing this contract in pipelines, services, and toolchains.
      since: v1
      tags:
      - domain
      id: domain.contract_set.core.integrator
      module: domain
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
    - summary: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.contract_set.applies_to_runners` for this audience.

        Inputs:
        - Inputs come from the owning contract declaration and required fixture inputs for this symbol.
        - Runtime bindings and policy constraints are applied by the harness before execution. 

        Returns:
        - Returns the assertion or helper value produced by this symbol after all constraints apply.

        Errors/Caveats:
        - Input/shape mismatches are surfaced as validation failures. 
        - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

        Usage context:
        - Use this for versioning, changelogs, and stability planning.
      since: v1
      tags:
      - domain
      id: domain.contract_set.core.maintainer
      module: domain
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
    - summary: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.contract_set.applies_to_runners` for this audience.

        Inputs:
        - Inputs come from the owning contract declaration and required fixture inputs for this symbol.
        - Runtime bindings and policy constraints are applied by the harness before execution. 

        Returns:
        - Returns the assertion or helper value produced by this symbol after all constraints apply.

        Errors/Caveats:
        - Input/shape mismatches are surfaced as validation failures. 
        - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

        Usage context:
        - Use this for policy gating, approval review, and compliance checks.
      since: v1
      tags:
      - domain
      id: domain.contract_set.core.governance
      module: domain
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
    - summary: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.contract_set.applies_to_runners` for this audience.

        Inputs:
        - Inputs come from the owning contract declaration and required fixture inputs for this symbol.
        - Runtime bindings and policy constraints are applied by the harness before execution. 

        Returns:
        - Returns the assertion or helper value produced by this symbol after all constraints apply.

        Errors/Caveats:
        - Input/shape mismatches are surfaced as validation failures. 
        - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

        Usage context:
        - Use this to verify correctness, completeness, and release readiness.
      since: v1
      tags:
      - domain
      id: domain.contract_set.core.reviewer
      module: domain
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
    - summary: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.contract_set.applies_to_runners` for this audience.

        Inputs:
        - Inputs come from the owning contract declaration and required fixture inputs for this symbol.
        - Runtime bindings and policy constraints are applied by the harness before execution. 

        Returns:
        - Returns the assertion or helper value produced by this symbol after all constraints apply.

        Errors/Caveats:
        - Input/shape mismatches are surfaced as validation failures. 
        - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

        Usage context:
        - Use this as documented evidence for audit and policy review.
      since: v1
      tags:
      - domain
      id: domain.contract_set.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.contract_set.id
        assert:
          std.object.get:
          - var: manifest
          - contract_set_id
      - id: __export__domain.contract_set.depends_on
        assert:
          std.object.get:
          - var: manifest
          - depends_on
      - id: __export__domain.contract_set.include_paths
        assert:
          std.object.get:
          - var: manifest
          - include_paths
      - id: __export__domain.contract_set.applies_to_runners
        assert:
          std.object.get:
          - var: manifest
          - applies_to_runners
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
- type: beta.exports_as_domain_contract_set_id_from_assert_function_path_export_domain_contract_set_id_params_manifest_required_true_docs_id_domain_contract_set_id_doc_1_summary_contract_export_for_domain_contract_set_id_audience_spec_authors_status_active_description_returns_manifest_contract_set_id_n_nprior_doc_fields_migrated_to_description_n_examples_title_read_id_ninput_n_manifest_n_contract_set_id_python_runner_contract_set_nexpected_python_runner_contract_set_n_params_name_manifest_n_type_any_n_required_true_n_description_contract_set_manifest_object_projection_n_returns_type_string_ndescription_manifest_contract_set_identifier_n_errors_code_schema_error_n_when_manifest_does_not_contain_the_required_field_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_portable_stdlib_projection_since_v1_as_domain_contract_set_depends_on_from_assert_function_path_export_domain_contract_set_depends_on_params_manifest_required_true_docs_id_domain_contract_set_depends_on_doc_1_summary_contract_export_for_domain_contract_set_depends_on_audience_spec_authors_status_active_description_returns_declared_dependency_list_from_manifest_n_nprior_doc_fields_migrated_to_description_n_examples_title_read_dependencies_ninput_n_manifest_n_depends_on_n_shared_makefile_help_contract_set_nexpected_n_shared_makefile_help_contract_set_n_params_name_manifest_n_type_any_n_required_true_n_description_contract_set_manifest_object_projection_n_returns_type_list_ndescription_manifest_dependency_contract_set_ids_n_errors_code_schema_error_n_when_manifest_does_not_contain_the_required_field_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_portable_stdlib_projection_since_v1_as_domain_contract_set_include_paths_from_assert_function_path_export_domain_contract_set_include_paths_params_manifest_required_true_docs_id_domain_contract_set_include_paths_doc_1_summary_contract_export_for_domain_contract_set_include_paths_audience_spec_authors_status_active_description_returns_include_path_glob_list_from_manifest_n_nprior_doc_fields_migrated_to_description_n_examples_title_read_include_paths_ninput_n_manifest_n_include_paths_n_specs_impl_python_nexpected_n_specs_impl_python_n_params_name_manifest_n_type_any_n_required_true_n_description_contract_set_manifest_object_projection_n_returns_type_list_ndescription_include_path_glob_list_n_errors_code_schema_error_n_when_manifest_does_not_contain_the_required_field_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_portable_stdlib_projection_since_v1_as_domain_contract_set_applies_to_runners_from_assert_function_path_export_domain_contract_set_applies_to_runners_params_manifest_required_true_docs_id_domain_contract_set_applies_to_runners_doc_1_summary_contract_export_for_domain_contract_set_applies_to_runners_audience_spec_authors_status_active_description_returns_optional_runner_applicability_list_n_nprior_doc_fields_migrated_to_description_n_examples_title_read_runner_filter_ninput_n_manifest_n_applies_to_runners_n_python_n_php_nexpected_n_python_n_php_n_params_name_manifest_n_type_any_n_required_true_n_description_contract_set_manifest_object_projection_n_returns_type_list_ndescription_runner_ids_list_or_null_empty_list_per_manifest_authoring_n_errors_code_schema_error_n_when_manifest_does_not_contain_expected_structure_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_portable_stdlib_projection_since_v1
  actions:
  - id: act.lib.contract.set.core.spec.1
    direction: bidirectional
    profile: default
services:
- id: svc.lib.contract.set.core.spec.1
  consumes:
  - act.lib.contract.set.core.spec.1
```
