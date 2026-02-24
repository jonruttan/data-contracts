```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
harness:
  type: unit.test
  profile: check
  config:
    exports:
    - as: domain.repo.walk_matching
      from: assert.function
      path: "/__export__domain.repo.walk_matching"
      params:
      - root
      - pattern
      required: true
      docs:
      - id: domain.repo.walk_matching.doc.1
        summary: Contract export for `domain.repo.walk_matching`.
        audience: implementer
        status: active
        description: |-
          Purpose: Documents behavior for `domain.repo.walk_matching` for this audience, including input contract, output contract, and failure modes.

          Inputs:
          - Inputs are the fixture inputs bound to this docs-bearing symbol as declared in the owning export or case entry.
          - Runtime bindings and policy constraints are applied by the harness before execution. 

          Returns:
          - Returns the assertion/helper value emitted by this symbol after bindings and policy checks execute.

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
      - id: domain.repo.walk_matching.doc.1.operator
        summary: Contract export for `domain.repo.walk_matching`. (operator)
        audience: operator
        status: active
        description: |-
          Purpose: Documents behavior for `domain.repo.walk_matching` for this audience, including input contract, output contract, and failure modes.

          Inputs:
          - Inputs are the fixture inputs bound to this docs-bearing symbol as declared in the owning export or case entry.
          - Runtime bindings and policy constraints are applied by the harness before execution. 

          Returns:
          - Returns the assertion/helper value emitted by this symbol after bindings and policy checks execute.

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
      - id: domain.repo.walk_matching.doc.1.integrator
        summary: Contract export for `domain.repo.walk_matching`. (integrator)
        audience: integrator
        status: active
        description: |-
          Purpose: Documents behavior for `domain.repo.walk_matching` for this audience, including input contract, output contract, and failure modes.

          Inputs:
          - Inputs are the fixture inputs bound to this docs-bearing symbol as declared in the owning export or case entry.
          - Runtime bindings and policy constraints are applied by the harness before execution. 

          Returns:
          - Returns the assertion/helper value emitted by this symbol after bindings and policy checks execute.

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
      - id: domain.repo.walk_matching.doc.1.maintainer
        summary: Contract export for `domain.repo.walk_matching`. (maintainer)
        audience: maintainer
        status: active
        description: |-
          Purpose: Documents behavior for `domain.repo.walk_matching` for this audience, including input contract, output contract, and failure modes.

          Inputs:
          - Inputs are the fixture inputs bound to this docs-bearing symbol as declared in the owning export or case entry.
          - Runtime bindings and policy constraints are applied by the harness before execution. 

          Returns:
          - Returns the assertion/helper value emitted by this symbol after bindings and policy checks execute.

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
      - id: domain.repo.walk_matching.doc.1.governance
        summary: Contract export for `domain.repo.walk_matching`. (governance)
        audience: governance
        status: active
        description: |-
          Purpose: Documents behavior for `domain.repo.walk_matching` for this audience, including input contract, output contract, and failure modes.

          Inputs:
          - Inputs are the fixture inputs bound to this docs-bearing symbol as declared in the owning export or case entry.
          - Runtime bindings and policy constraints are applied by the harness before execution. 

          Returns:
          - Returns the assertion/helper value emitted by this symbol after bindings and policy checks execute.

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
      - id: domain.repo.walk_matching.doc.1.reviewer
        summary: Contract export for `domain.repo.walk_matching`. (reviewer)
        audience: reviewer
        status: active
        description: |-
          Purpose: Documents behavior for `domain.repo.walk_matching` for this audience, including input contract, output contract, and failure modes.

          Inputs:
          - Inputs are the fixture inputs bound to this docs-bearing symbol as declared in the owning export or case entry.
          - Runtime bindings and policy constraints are applied by the harness before execution. 

          Returns:
          - Returns the assertion/helper value emitted by this symbol after bindings and policy checks execute.

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
      - id: domain.repo.walk_matching.doc.1.auditor
        summary: Contract export for `domain.repo.walk_matching`. (auditor)
        audience: auditor
        status: active
        description: |-
          Purpose: Documents behavior for `domain.repo.walk_matching` for this audience, including input contract, output contract, and failure modes.

          Inputs:
          - Inputs are the fixture inputs bound to this docs-bearing symbol as declared in the owning export or case entry.
          - Runtime bindings and policy constraints are applied by the harness before execution. 

          Returns:
          - Returns the assertion/helper value emitted by this symbol after bindings and policy checks execute.

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
  - id: LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING
    docs:
    - summary: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.repo.walk_matching` for this audience, including input contract, output contract, and failure modes.

        Inputs:
        - Inputs are the fixture inputs bound to this docs-bearing symbol as declared in the owning export or case entry.
        - Runtime bindings and policy constraints are applied by the harness before execution. 

        Returns:
        - Returns the assertion/helper value emitted by this symbol after bindings and policy checks execute.

        Errors/Caveats:
        - Input/shape mismatches are surfaced as validation failures. 
        - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

        Usage context:
        - Use this for implementation work, local debugging, and runner-side behavior analysis.
      since: v1
      tags:
      - domain
      id: domain.repo.core
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
    - summary: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.repo.walk_matching` for this audience, including input contract, output contract, and failure modes.

        Inputs:
        - Inputs are the fixture inputs bound to this docs-bearing symbol as declared in the owning export or case entry.
        - Runtime bindings and policy constraints are applied by the harness before execution. 

        Returns:
        - Returns the assertion/helper value emitted by this symbol after bindings and policy checks execute.

        Errors/Caveats:
        - Input/shape mismatches are surfaced as validation failures. 
        - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

        Usage context:
        - Use this for observability, runbook readiness, and incident response.
      since: v1
      tags:
      - domain
      id: domain.repo.core.operator
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
    - summary: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.repo.walk_matching` for this audience, including input contract, output contract, and failure modes.

        Inputs:
        - Inputs are the fixture inputs bound to this docs-bearing symbol as declared in the owning export or case entry.
        - Runtime bindings and policy constraints are applied by the harness before execution. 

        Returns:
        - Returns the assertion/helper value emitted by this symbol after bindings and policy checks execute.

        Errors/Caveats:
        - Input/shape mismatches are surfaced as validation failures. 
        - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

        Usage context:
        - Use this for composing this contract in pipelines, services, and toolchains.
      since: v1
      tags:
      - domain
      id: domain.repo.core.integrator
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
    - summary: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.repo.walk_matching` for this audience, including input contract, output contract, and failure modes.

        Inputs:
        - Inputs are the fixture inputs bound to this docs-bearing symbol as declared in the owning export or case entry.
        - Runtime bindings and policy constraints are applied by the harness before execution. 

        Returns:
        - Returns the assertion/helper value emitted by this symbol after bindings and policy checks execute.

        Errors/Caveats:
        - Input/shape mismatches are surfaced as validation failures. 
        - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

        Usage context:
        - Use this for versioning, changelogs, and stability planning.
      since: v1
      tags:
      - domain
      id: domain.repo.core.maintainer
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
    - summary: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `domain.repo.walk_matching` for this audience, including input contract, output contract, and failure modes.

        Inputs:
        - Inputs are the fixture inputs bound to this docs-bearing symbol as declared in the owning export or case entry.
        - Runtime bindings and policy constraints are applied by the harness before execution. 

        Returns:
        - Returns the assertion/helper value emitted by this symbol after bindings and policy checks execute.

        Errors/Caveats:
        - Input/shape mismatches are surfaced as validation failures. 
        - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

        Usage context:
        - Use this for policy gating, approval review, and compliance checks.
      since: v1
      tags:
      - domain
      id: domain.repo.core.governance
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
    - summary: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.repo.walk_matching` for this audience, including input contract, output contract, and failure modes.

        Inputs:
        - Inputs are the fixture inputs bound to this docs-bearing symbol as declared in the owning export or case entry.
        - Runtime bindings and policy constraints are applied by the harness before execution. 

        Returns:
        - Returns the assertion/helper value emitted by this symbol after bindings and policy checks execute.

        Errors/Caveats:
        - Input/shape mismatches are surfaced as validation failures. 
        - Schema, runtime binding, or environment mismatches are surfaced as runtime or validation failures.
        - Policy and validation failures are surfaced through contract evaluation, including policy assertions and policy checks.

        Usage context:
        - Use this to verify correctness, completeness, and release readiness.
      since: v1
      tags:
      - domain
      id: domain.repo.core.reviewer
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
    - summary: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `domain.repo.walk_matching` for this audience, including input contract, output contract, and failure modes.

        Inputs:
        - Inputs are the fixture inputs bound to this docs-bearing symbol as declared in the owning export or case entry.
        - Runtime bindings and policy constraints are applied by the harness before execution. 

        Returns:
        - Returns the assertion/helper value emitted by this symbol after bindings and policy checks execute.

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
      id: domain.repo.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.repo.walk_matching
        assert:
          ops.fs.walk:
          - var: root
          - lit:
              pattern:
                var: pattern
              include_dirs: false
              relative: true
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
- type: beta.exports_as_domain_repo_walk_matching_from_assert_function_path_export_domain_repo_walk_matching_params_root_pattern_required_true_docs_id_domain_repo_walk_matching_doc_1_summary_contract_export_for_domain_repo_walk_matching_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_root_root_n_pattern_pattern_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_root_n_type_any_n_required_true_n_description_input_parameter_root_n_name_pattern_n_type_any_n_required_true_n_description_input_parameter_pattern_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.repo.core.spec.1
    direction: bidirectional
    profile: default
services:
- id: svc.lib.repo.core.spec.1
  consumes:
  - act.lib.repo.core.spec.1
```
