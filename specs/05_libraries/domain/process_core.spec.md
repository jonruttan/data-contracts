```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
harness:
  type: unit.test
  profile: check
  config:
    spec_lang:
      capabilities:
      - ops.os
    exports:
    - as: domain.process.exec_capture_ex_code
      from: assert.function
      path: "/__export__domain.process.exec_capture_ex_code"
      params:
      - command
      - options
      required: true
      docs:
      - id: domain.process.exec_capture_ex_code.doc.1
        summary: Contract export for `domain.process.exec_capture_ex_code`.
        audience: implementer
        status: active
        description: |-
          Purpose: This entry documents behavior for `domain.process.exec_capture_ex_code` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - id: domain.process.exec_capture_ex_code.doc.1.operator
        summary: Contract export for `domain.process.exec_capture_ex_code`. (operator)
        audience: operator
        status: active
        description: |-
          Purpose: This entry documents behavior for `domain.process.exec_capture_ex_code` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - id: domain.process.exec_capture_ex_code.doc.1.integrator
        summary: Contract export for `domain.process.exec_capture_ex_code`. (integrator)
        audience: integrator
        status: active
        description: |-
          Purpose: This entry documents behavior for `domain.process.exec_capture_ex_code` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - id: domain.process.exec_capture_ex_code.doc.1.maintainer
        summary: Contract export for `domain.process.exec_capture_ex_code`. (maintainer)
        audience: maintainer
        status: active
        description: |-
          Purpose: This entry documents behavior for `domain.process.exec_capture_ex_code` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - id: domain.process.exec_capture_ex_code.doc.1.governance
        summary: Contract export for `domain.process.exec_capture_ex_code`. (governance)
        audience: governance
        status: active
        description: |-
          Purpose: This entry documents behavior for `domain.process.exec_capture_ex_code` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - id: domain.process.exec_capture_ex_code.doc.1.reviewer
        summary: Contract export for `domain.process.exec_capture_ex_code`. (reviewer)
        audience: reviewer
        status: active
        description: |-
          Purpose: This entry documents behavior for `domain.process.exec_capture_ex_code` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - id: domain.process.exec_capture_ex_code.doc.1.auditor
        summary: Contract export for `domain.process.exec_capture_ex_code`. (auditor)
        audience: auditor
        status: active
        description: |-
          Purpose: This entry documents behavior for `domain.process.exec_capture_ex_code` for the declared audience, including input expectations, output contracts, and failure modes.

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
  - id: LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE
    docs:
    - summary: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE`
        for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: This entry documents behavior for `domain.process.exec_capture_ex_code` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - domain
      id: domain.process.core
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
    - summary: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE`
        for `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: This entry documents behavior for `domain.process.exec_capture_ex_code` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - domain
      id: domain.process.core.operator
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
    - summary: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE`
        for `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: This entry documents behavior for `domain.process.exec_capture_ex_code` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - domain
      id: domain.process.core.integrator
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
    - summary: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE`
        for `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: This entry documents behavior for `domain.process.exec_capture_ex_code` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - domain
      id: domain.process.core.maintainer
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
    - summary: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE`
        for `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: This entry documents behavior for `domain.process.exec_capture_ex_code` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - domain
      id: domain.process.core.governance
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
    - summary: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE`
        for `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: This entry documents behavior for `domain.process.exec_capture_ex_code` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - domain
      id: domain.process.core.reviewer
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
    - summary: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE`
        for `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: This entry documents behavior for `domain.process.exec_capture_ex_code` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - domain
      id: domain.process.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.process.exec_capture_ex_code
        assert:
          std.object.get:
          - ops.os.exec_capture_ex:
            - var: command
            - var: options
          - code
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
- type: beta.spec_lang_capabilities_ops_os_exports_as_domain_process_exec_capture_ex_code_from_assert_function_path_export_domain_process_exec_capture_ex_code_params_command_options_required_true_docs_id_domain_process_exec_capture_ex_code_doc_1_summary_contract_export_for_domain_process_exec_capture_ex_code_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_command_command_n_options_options_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_command_n_type_any_n_required_true_n_description_input_parameter_command_n_name_options_n_type_any_n_required_true_n_description_input_parameter_options_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.process.core.spec.1
    direction: bidirectional
    profile: default
services:
- id: svc.lib.process.core.spec.1
  consumes:
  - act.lib.process.core.spec.1
```
