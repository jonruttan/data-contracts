```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
harness:
  type: unit.test
  profile: check
  config:
    spec_lang:
      capabilities:
      - ops.helper
    exports:
    - as: domain.job.scan_bundle_has_result
      from: assert.function
      path: "/__export__domain.job.scan_bundle_has_result"
      params:
      - scan_path
      - pattern
      docs:
      - id: domain.job.scan_bundle_has_result.doc.1
        summary: Contract export for `domain.job.scan_bundle_has_result`.
        audience: implementer
        status: active
        description: |-
          Purpose: Documents behavior of `domain.job.scan_bundle_has_result` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
        outputs:
        - The normalized output produced by this symbol in the owning execution context.
        caveats:
        - Invocation defaults and ordering must match contract expectations for deterministic behavior.
        - Environment-sensitive references can change runtime outcome if not explicitly provided.
        examples:
        - Test the symbol with known-valid data and a representative invalid input to verify both pass/fail behavior.
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
      - id: domain.job.scan_bundle_has_result.doc.1.operator
        summary: Contract export for `domain.job.scan_bundle_has_result`. (operator)
        audience: operator
        status: active
        description: |-
          Purpose: Documents behavior of `domain.job.scan_bundle_has_result` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
        outputs:
        - The normalized output produced by this symbol in the owning execution context.
        caveats:
        - Invocation defaults and ordering must match contract expectations for deterministic behavior.
        - Environment-sensitive references can change runtime outcome if not explicitly provided.
        examples:
        - Test the symbol with known-valid data and a representative invalid input to verify both pass/fail behavior.
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
      - id: domain.job.scan_bundle_has_result.doc.1.integrator
        summary: Contract export for `domain.job.scan_bundle_has_result`. (integrator)
        audience: integrator
        status: active
        description: |-
          Purpose: Documents behavior of `domain.job.scan_bundle_has_result` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
        outputs:
        - The normalized output produced by this symbol in the owning execution context.
        caveats:
        - Invocation defaults and ordering must match contract expectations for deterministic behavior.
        - Environment-sensitive references can change runtime outcome if not explicitly provided.
        examples:
        - Test the symbol with known-valid data and a representative invalid input to verify both pass/fail behavior.
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
      - id: domain.job.scan_bundle_has_result.doc.1.maintainer
        summary: Contract export for `domain.job.scan_bundle_has_result`. (maintainer)
        audience: maintainer
        status: active
        description: |-
          Purpose: Documents behavior of `domain.job.scan_bundle_has_result` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
        outputs:
        - The normalized output produced by this symbol in the owning execution context.
        caveats:
        - Invocation defaults and ordering must match contract expectations for deterministic behavior.
        - Environment-sensitive references can change runtime outcome if not explicitly provided.
        examples:
        - Test the symbol with known-valid data and a representative invalid input to verify both pass/fail behavior.
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
      - id: domain.job.scan_bundle_has_result.doc.1.governance
        summary: Contract export for `domain.job.scan_bundle_has_result`. (governance)
        audience: governance
        status: active
        description: |-
          Purpose: Documents behavior of `domain.job.scan_bundle_has_result` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
        outputs:
        - The normalized output produced by this symbol in the owning execution context.
        caveats:
        - Invocation defaults and ordering must match contract expectations for deterministic behavior.
        - Environment-sensitive references can change runtime outcome if not explicitly provided.
        examples:
        - Test the symbol with known-valid data and a representative invalid input to verify both pass/fail behavior.
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
      - id: domain.job.scan_bundle_has_result.doc.1.reviewer
        summary: Contract export for `domain.job.scan_bundle_has_result`. (reviewer)
        audience: reviewer
        status: active
        description: |-
          Purpose: Documents behavior of `domain.job.scan_bundle_has_result` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
        outputs:
        - The normalized output produced by this symbol in the owning execution context.
        caveats:
        - Invocation defaults and ordering must match contract expectations for deterministic behavior.
        - Environment-sensitive references can change runtime outcome if not explicitly provided.
        examples:
        - Test the symbol with known-valid data and a representative invalid input to verify both pass/fail behavior.
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
      - id: domain.job.scan_bundle_has_result.doc.1.auditor
        summary: Contract export for `domain.job.scan_bundle_has_result`. (auditor)
        audience: auditor
        status: active
        description: |-
          Purpose: Documents behavior of `domain.job.scan_bundle_has_result` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
        outputs:
        - The normalized output produced by this symbol in the owning execution context.
        caveats:
        - Invocation defaults and ordering must match contract expectations for deterministic behavior.
        - Environment-sensitive references can change runtime outcome if not explicitly provided.
        examples:
        - Test the symbol with known-valid data and a representative invalid input to verify both pass/fail behavior.
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
  - id: LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT
    title: domain.job.scan_bundle_has_result
    purpose: Reusable helper-backed predicate for contract.job governance scan helper
      output.
    docs:
    - summary: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for
        `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.job.scan_bundle_has_result` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.job.core
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
    - summary: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for
        `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.job.scan_bundle_has_result` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.job.core.operator
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
    - summary: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for
        `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.job.scan_bundle_has_result` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.job.core.integrator
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
    - summary: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for
        `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.job.scan_bundle_has_result` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.job.core.maintainer
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
    - summary: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for
        `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior of `domain.job.scan_bundle_has_result` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.job.core.governance
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
    - summary: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for
        `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.job.scan_bundle_has_result` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.job.core.reviewer
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
    - summary: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for
        `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior of `domain.job.scan_bundle_has_result` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      outputs:
      - The normalized output produced by this docs-bearing symbol for the owning suite context.
      caveats:
      - Invocation order and default arguments may influence determinism if not explicitly controlled.
      - Environment-sensitive paths/services can produce different output on non-equivalent runner setups.
      examples:
      - Use this export in its owning fixture case to verify expected pass/fail behavior on representative success and validation-failure inputs.
      since: v1
      tags:
      - domain
      id: domain.job.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      imports:
      - from: asset
        names:
        - subject
      checks:
      - id: __export__domain.job.scan_bundle_has_result
        assert:
          std.logic.neq:
          - std.object.get:
            - ops.helper.call:
              - lit: helper.governance.scan_bundle
              - lit:
                  path:
                    var: scan_path
                  patterns:
                  - var: pattern
            - scanned_files
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
- type: beta.spec_lang_capabilities_ops_helper_exports_as_domain_job_scan_bundle_has_result_from_assert_function_path_export_domain_job_scan_bundle_has_result_params_scan_path_pattern_docs_id_domain_job_scan_bundle_has_result_doc_1_summary_contract_export_for_domain_job_scan_bundle_has_result_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_scan_path_scan_path_n_pattern_pattern_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_scan_path_n_type_any_n_required_true_n_description_input_parameter_scan_path_n_name_pattern_n_type_any_n_required_true_n_description_input_parameter_pattern_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.job.core.spec.1
    direction: bidirectional
    profile: default
services:
- id: svc.lib.job.core.spec.1
  consumes:
  - act.lib.job.core.spec.1
```

