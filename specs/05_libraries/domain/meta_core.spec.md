```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
harness:
  type: unit.test
  profile: check
  config:
    exports:
    - as: domain.meta.has_artifact_target
      from: assert.function
      path: "/__export__domain.meta.has_artifact_target"
      params:
      - meta
      - target_name
      required: true
      docs:
      - id: domain.meta.has_artifact_target.doc.1
        summary: Contract export for `domain.meta.has_artifact_target`.
        audience: implementer
        status: active
        description: |-
          Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      - id: domain.meta.has_artifact_target.doc.1.operator
        summary: Contract export for `domain.meta.has_artifact_target`. (operator)
        audience: operator
        status: active
        description: |-
          Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      - id: domain.meta.has_artifact_target.doc.1.integrator
        summary: Contract export for `domain.meta.has_artifact_target`. (integrator)
        audience: integrator
        status: active
        description: |-
          Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      - id: domain.meta.has_artifact_target.doc.1.maintainer
        summary: Contract export for `domain.meta.has_artifact_target`. (maintainer)
        audience: maintainer
        status: active
        description: |-
          Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      - id: domain.meta.has_artifact_target.doc.1.governance
        summary: Contract export for `domain.meta.has_artifact_target`. (governance)
        audience: governance
        status: active
        description: |-
          Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      - id: domain.meta.has_artifact_target.doc.1.reviewer
        summary: Contract export for `domain.meta.has_artifact_target`. (reviewer)
        audience: reviewer
        status: active
        description: |-
          Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      - id: domain.meta.has_artifact_target.doc.1.auditor
        summary: Contract export for `domain.meta.has_artifact_target`. (auditor)
        audience: auditor
        status: active
        description: |-
          Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
  - id: LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ
    docs:
    - summary: Case `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      id: domain.meta.core
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
    - summary: Case `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      id: domain.meta.core.operator
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
    - summary: Case `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      id: domain.meta.core.integrator
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
    - summary: Case `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      id: domain.meta.core.maintainer
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
    - summary: Case `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      id: domain.meta.core.governance
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
    - summary: Case `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      id: domain.meta.core.reviewer
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
    - summary: Case `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      id: domain.meta.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.meta.case_id_eq
        assert:
          std.logic.eq:
          - std.object.get:
            - std.object.get:
              - var: meta
              - case
            - id
          - var: case_id
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
  - id: LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET
    docs:
    - summary: Case `LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET` for
        `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      id: domain.meta.core
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
    - summary: Case `LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET` for
        `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      id: domain.meta.core.operator
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
    - summary: Case `LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET` for
        `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      id: domain.meta.core.integrator
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
    - summary: Case `LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET` for
        `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      id: domain.meta.core.maintainer
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
    - summary: Case `LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET` for
        `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      id: domain.meta.core.governance
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
    - summary: Case `LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET` for
        `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      id: domain.meta.core.reviewer
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
    - summary: Case `LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET` for
        `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents the runtime behavior and intent of `domain.meta.has_artifact_target` for this audience.

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
      id: domain.meta.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.meta.has_artifact_target
        assert:
          std.collection.includes:
          - std.object.get:
            - std.object.get:
              - var: meta
              - artifacts
            - target_keys
          - var: target_name
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
- type: beta.exports_as_domain_meta_case_id_eq_from_assert_function_path_export_domain_meta_case_id_eq_params_meta_case_id_required_true_docs_id_domain_meta_case_id_eq_doc_1_summary_contract_export_for_domain_meta_case_id_eq_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_meta_meta_n_case_id_case_id_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_meta_n_type_any_n_required_true_n_description_input_parameter_meta_n_name_case_id_n_type_any_n_required_true_n_description_input_parameter_case_id_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.meta.core.spec.1
    profile: default
- type: beta.exports_as_domain_meta_has_artifact_target_from_assert_function_path_export_domain_meta_has_artifact_target_params_meta_target_name_required_true_docs_id_domain_meta_has_artifact_target_doc_1_summary_contract_export_for_domain_meta_has_artifact_target_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_meta_meta_n_target_name_target_name_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_meta_n_type_any_n_required_true_n_description_input_parameter_meta_n_name_target_name_n_type_any_n_required_true_n_description_input_parameter_target_name_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.meta.core.spec.2
    profile: default
services:
- id: svc.lib.meta.core.spec.1
  consumes:
  - act.lib.meta.core.spec.1
- id: svc.lib.meta.core.spec.2
  consumes:
  - act.lib.meta.core.spec.2
```

