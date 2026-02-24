```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
harness:
  type: unit.test
  profile: check
  config:
    exports:
    - as: domain.path.sorted
      from: assert.function
      path: "/__export__domain.path.sorted"
      params:
      - paths
      required: true
      docs:
      - id: domain.path.sorted.doc.1
        summary: Contract export for `domain.path.sorted`.
        audience: implementer
        status: active
        description: |-
          Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      - id: domain.path.sorted.doc.1.operator
        summary: Contract export for `domain.path.sorted`. (operator)
        audience: operator
        status: active
        description: |-
          Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      - id: domain.path.sorted.doc.1.integrator
        summary: Contract export for `domain.path.sorted`. (integrator)
        audience: integrator
        status: active
        description: |-
          Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      - id: domain.path.sorted.doc.1.maintainer
        summary: Contract export for `domain.path.sorted`. (maintainer)
        audience: maintainer
        status: active
        description: |-
          Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      - id: domain.path.sorted.doc.1.governance
        summary: Contract export for `domain.path.sorted`. (governance)
        audience: governance
        status: active
        description: |-
          Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      - id: domain.path.sorted.doc.1.reviewer
        summary: Contract export for `domain.path.sorted`. (reviewer)
        audience: reviewer
        status: active
        description: |-
          Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      - id: domain.path.sorted.doc.1.auditor
        summary: Contract export for `domain.path.sorted`. (auditor)
        audience: auditor
        status: active
        description: |-
          Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
  - id: LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE
    docs:
    - summary: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core
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
    - summary: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.operator
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
    - summary: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.integrator
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
    - summary: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.maintainer
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
    - summary: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.governance
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
    - summary: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.reviewer
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
    - summary: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.path.normalize
        assert:
          ops.fs.path.normalize:
          - var: path
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
  - id: LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ
    docs:
    - summary: Case `LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core
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
    - summary: Case `LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.operator
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
    - summary: Case `LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.integrator
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
    - summary: Case `LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.maintainer
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
    - summary: Case `LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.governance
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
    - summary: Case `LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.reviewer
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
    - summary: Case `LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.path.eq
        assert:
          std.logic.eq:
          - ops.fs.path.normalize:
            - var: left
          - ops.fs.path.normalize:
            - var: right
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
  - id: LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD
    docs:
    - summary: Case `LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core
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
    - summary: Case `LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.operator
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
    - summary: Case `LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.integrator
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
    - summary: Case `LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.maintainer
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
    - summary: Case `LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.governance
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
    - summary: Case `LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.reviewer
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
    - summary: Case `LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.path.is_spec_md
        assert:
          std.string.ends_with:
          - ops.fs.path.normalize:
            - var: path
          - ".spec.md"
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
  - id: LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS
    docs:
    - summary: Case `LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core
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
    - summary: Case `LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.operator
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
    - summary: Case `LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.integrator
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
    - summary: Case `LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.maintainer
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
    - summary: Case `LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.governance
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
    - summary: Case `LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.reviewer
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
    - summary: Case `LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.path.is_in_docs
        assert:
          ops.fs.path.within:
          - "/docs"
          - ops.fs.path.normalize:
            - var: path
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
  - id: LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED
    docs:
    - summary: Case `LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core
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
    - summary: Case `LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.operator
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
    - summary: Case `LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.integrator
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
    - summary: Case `LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.maintainer
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
    - summary: Case `LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.governance
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
    - summary: Case `LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.reviewer
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
    - summary: Case `LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.path.sorted
        assert:
          ops.fs.path.sort:
          - var: paths
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
  - id: LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE
    docs:
    - summary: Case `LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core
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
    - summary: Case `LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.operator
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
    - summary: Case `LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.integrator
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
    - summary: Case `LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.maintainer
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
    - summary: Case `LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.governance
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
    - summary: Case `LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.reviewer
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
    - summary: Case `LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.file.is_existing_file
        assert:
          std.logic.and:
          - ops.fs.file.exists:
            - var: meta
          - ops.fs.file.is_file:
            - var: meta
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
  - id: LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR
    docs:
    - summary: Case `LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core
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
    - summary: Case `LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.operator
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
    - summary: Case `LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.integrator
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
    - summary: Case `LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.maintainer
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
    - summary: Case `LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.governance
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
    - summary: Case `LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.reviewer
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
    - summary: Case `LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.file.is_existing_dir
        assert:
          std.logic.and:
          - ops.fs.file.exists:
            - var: meta
          - ops.fs.file.is_dir:
            - var: meta
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
  - id: LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT
    docs:
    - summary: Case `LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core
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
    - summary: Case `LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.operator
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
    - summary: Case `LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.integrator
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
    - summary: Case `LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.maintainer
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
    - summary: Case `LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.governance
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
    - summary: Case `LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.reviewer
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
    - summary: Case `LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.file.has_ext
        assert:
          ops.fs.path.has_ext:
          - ops.fs.file.path:
            - var: meta
          - var: ext
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
  - id: LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME
    docs:
    - summary: Case `LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core
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
    - summary: Case `LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.operator
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
    - summary: Case `LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.integrator
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
    - summary: Case `LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.maintainer
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
    - summary: Case `LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.governance
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
    - summary: Case `LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.reviewer
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
    - summary: Case `LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior of `domain.path.sorted` for this audience, including expected inputs, return shape, failure modes, and practical use cases.

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
      id: domain.path.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.file.name
        assert:
          ops.fs.file.name:
          - var: meta
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
- type: beta.exports_as_domain_path_normalize_from_assert_function_path_export_domain_path_normalize_params_path_required_true_docs_id_domain_path_normalize_doc_1_summary_contract_export_for_domain_path_normalize_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.path.core.spec.1
    profile: default
- type: beta.exports_as_domain_path_eq_from_assert_function_path_export_domain_path_eq_params_left_right_required_true_docs_id_domain_path_eq_doc_1_summary_contract_export_for_domain_path_eq_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_left_left_n_right_right_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_left_n_type_any_n_required_true_n_description_input_parameter_left_n_name_right_n_type_any_n_required_true_n_description_input_parameter_right_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.path.core.spec.2
    profile: default
- type: beta.exports_as_domain_path_is_spec_md_from_assert_function_path_export_domain_path_is_spec_md_params_path_required_true_docs_id_domain_path_is_spec_md_doc_1_summary_contract_export_for_domain_path_is_spec_md_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.path.core.spec.3
    profile: default
- type: beta.exports_as_domain_path_is_in_docs_from_assert_function_path_export_domain_path_is_in_docs_params_path_required_true_docs_id_domain_path_is_in_docs_doc_1_summary_contract_export_for_domain_path_is_in_docs_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.path.core.spec.4
    profile: default
- type: beta.exports_as_domain_path_sorted_from_assert_function_path_export_domain_path_sorted_params_paths_required_true_docs_id_domain_path_sorted_doc_1_summary_contract_export_for_domain_path_sorted_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_paths_paths_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_paths_n_type_any_n_required_true_n_description_input_parameter_paths_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.path.core.spec.5
    profile: default
- type: beta.exports_as_domain_file_is_existing_file_from_assert_function_path_export_domain_file_is_existing_file_params_meta_required_true_docs_id_domain_file_is_existing_file_doc_1_summary_contract_export_for_domain_file_is_existing_file_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_meta_meta_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_meta_n_type_any_n_required_true_n_description_input_parameter_meta_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.path.core.spec.6
    profile: default
- type: beta.exports_as_domain_file_is_existing_dir_from_assert_function_path_export_domain_file_is_existing_dir_params_meta_required_true_docs_id_domain_file_is_existing_dir_doc_1_summary_contract_export_for_domain_file_is_existing_dir_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_meta_meta_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_meta_n_type_any_n_required_true_n_description_input_parameter_meta_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.path.core.spec.7
    profile: default
- type: beta.exports_as_domain_file_has_ext_from_assert_function_path_export_domain_file_has_ext_params_meta_ext_required_true_docs_id_domain_file_has_ext_doc_1_summary_contract_export_for_domain_file_has_ext_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_meta_meta_n_ext_ext_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_meta_n_type_any_n_required_true_n_description_input_parameter_meta_n_name_ext_n_type_any_n_required_true_n_description_input_parameter_ext_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.path.core.spec.8
    profile: default
- type: beta.exports_as_domain_file_name_from_assert_function_path_export_domain_file_name_params_meta_required_true_docs_id_domain_file_name_doc_1_summary_contract_export_for_domain_file_name_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_meta_meta_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_meta_n_type_any_n_required_true_n_description_input_parameter_meta_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.path.core.spec.9
    profile: default
services:
- id: svc.lib.path.core.spec.1
  consumes:
  - act.lib.path.core.spec.1
- id: svc.lib.path.core.spec.2
  consumes:
  - act.lib.path.core.spec.2
- id: svc.lib.path.core.spec.3
  consumes:
  - act.lib.path.core.spec.3
- id: svc.lib.path.core.spec.4
  consumes:
  - act.lib.path.core.spec.4
- id: svc.lib.path.core.spec.5
  consumes:
  - act.lib.path.core.spec.5
- id: svc.lib.path.core.spec.6
  consumes:
  - act.lib.path.core.spec.6
- id: svc.lib.path.core.spec.7
  consumes:
  - act.lib.path.core.spec.7
- id: svc.lib.path.core.spec.8
  consumes:
  - act.lib.path.core.spec.8
- id: svc.lib.path.core.spec.9
  consumes:
  - act.lib.path.core.spec.9
```








