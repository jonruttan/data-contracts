```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
harness:
  type: unit.test
  profile: check
  config:
    check:
      profile: text.file
      config: {}
    use:
    - ref: "#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES"
      as: lib_path_normalize
      symbols:
      - path.normalize_slashes
    exports:
    - as: path.segments
      from: assert.function
      path: "/__export__path.matches"
      params:
      - path
      - pattern
      docs:
      - id: path.matches.doc.1
        summary: Evaluate whether path values satisfy the provided matcher rules.
        audience: implementer
        status: active
        description: |-
          Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - id: path.matches.doc.1.operator
        summary: Evaluate whether path values satisfy the provided matcher rules for operators.
        audience: operator
        status: active
        description: |-
          Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - id: path.matches.doc.1.integrator
        summary: Evaluate whether path values satisfy the provided matcher rules for integrations.
        audience: integrator
        status: active
        description: |-
          Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - id: path.matches.doc.1.maintainer
        summary: Evaluate whether path values satisfy the provided matcher rules for maintenance.
        audience: maintainer
        status: active
        description: |-
          Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - id: path.matches.doc.1.governance
        summary: Evaluate whether path values satisfy the provided matcher rules for governance.
        audience: governance
        status: active
        description: |-
          Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - id: path.matches.doc.1.reviewer
        summary: Evaluate whether path values satisfy the provided matcher rules for review.
        audience: reviewer
        status: active
        description: |-
          Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - id: path.matches.doc.1.auditor
        summary: Evaluate whether path values satisfy the provided matcher rules for audits.
        audience: auditor
        status: active
        description: |-
          Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
  - id: LIB-PATH-001-001-PATH-NORMALIZE-SLASHES
    docs:
    - summary: Case `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core
      module: path
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
    - summary: Case `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.operator
      module: path
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
    - summary: Case `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.integrator
      module: path
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
    - summary: Case `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.maintainer
      module: path
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
    - summary: Case `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.governance
      module: path
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
    - summary: Case `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.reviewer
      module: path
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
    - summary: Case `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      tags:
      - path
      id: path.path.core.auditor
      module: path
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
      - Use this as documented evidence for audit and policy review.
    asserts:
      checks:
      - id: __export__path.normalize_slashes
        assert:
          std.string.replace:
          - var: path
          - "\\"
          - "/"
      - id: __export__path.trim_dot
        assert:
          std.string.replace:
          - var: path
          - "./"
          - ''
      - id: __export__path.dirname
        assert:
          lit:
            let:
            - lit:
              - - segs
                - call:
                  - var: path.segments
                  - var: path
            - if:
              - std.logic.lte:
                - std.collection.len:
                  - var: segs
                - 1
              - ''
              - std.string.join:
                - std.collection.slice:
                  - 0
                  - std.math.sub:
                    - std.collection.len:
                      - var: segs
                    - 1
                  - var: segs
                - "/"
      - id: __export__path.has_extension
        assert:
          std.logic.eq:
          - call:
            - var: path.extension
            - var: path
          - var: ext
      - id: __export__path.is_under
        assert:
          std.string.starts_with:
          - call:
            - var: path.normalize_slashes
            - var: path
          - call:
            - var: path.normalize_slashes
            - var: prefix
      - id: __export__path.matches
        assert:
          std.string.regex_match:
          - call:
            - var: path.normalize_slashes
            - var: path
          - var: pattern
  - id: LIB-PATH-001-002-PATH-SEGMENTS
    docs:
    - summary: Case `LIB-PATH-001-002-PATH-SEGMENTS` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core
      module: path
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
    - summary: Case `LIB-PATH-001-002-PATH-SEGMENTS` for `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.operator
      module: path
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
    - summary: Case `LIB-PATH-001-002-PATH-SEGMENTS` for `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.integrator
      module: path
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
    - summary: Case `LIB-PATH-001-002-PATH-SEGMENTS` for `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.maintainer
      module: path
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
    - summary: Case `LIB-PATH-001-002-PATH-SEGMENTS` for `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.governance
      module: path
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
    - summary: Case `LIB-PATH-001-002-PATH-SEGMENTS` for `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.reviewer
      module: path
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
    - summary: Case `LIB-PATH-001-002-PATH-SEGMENTS` for `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      tags:
      - path
      id: path.path.core.auditor
      module: path
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
      - Use this as documented evidence for audit and policy review.
    asserts:
      checks:
      - id: __export__path.segments
        assert:
          std.string.split:
          - call:
            - var: path.normalize_slashes
            - var: path
          - "/"
      - id: __export__path.trim_dot
        assert:
          std.string.replace:
          - var: path
          - "./"
          - ''
      - id: __export__path.dirname
        assert:
          lit:
            let:
            - lit:
              - - segs
                - call:
                  - var: path.segments
                  - var: path
            - if:
              - std.logic.lte:
                - std.collection.len:
                  - var: segs
                - 1
              - ''
              - std.string.join:
                - std.collection.slice:
                  - 0
                  - std.math.sub:
                    - std.collection.len:
                      - var: segs
                    - 1
                  - var: segs
                - "/"
      - id: __export__path.has_extension
        assert:
          std.logic.eq:
          - call:
            - var: path.extension
            - var: path
          - var: ext
      - id: __export__path.is_under
        assert:
          std.string.starts_with:
          - call:
            - var: path.normalize_slashes
            - var: path
          - call:
            - var: path.normalize_slashes
            - var: prefix
      - id: __export__path.matches
        assert:
          std.string.regex_match:
          - call:
            - var: path.normalize_slashes
            - var: path
          - var: pattern
  - id: LIB-PATH-001-003-PATH-BASENAME
    docs:
    - summary: Case `LIB-PATH-001-003-PATH-BASENAME` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core
      module: path
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
    - summary: Case `LIB-PATH-001-003-PATH-BASENAME` for `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.operator
      module: path
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
    - summary: Case `LIB-PATH-001-003-PATH-BASENAME` for `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.integrator
      module: path
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
    - summary: Case `LIB-PATH-001-003-PATH-BASENAME` for `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.maintainer
      module: path
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
    - summary: Case `LIB-PATH-001-003-PATH-BASENAME` for `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.governance
      module: path
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
    - summary: Case `LIB-PATH-001-003-PATH-BASENAME` for `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.reviewer
      module: path
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
    - summary: Case `LIB-PATH-001-003-PATH-BASENAME` for `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      tags:
      - path
      id: path.path.core.auditor
      module: path
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
      - Use this as documented evidence for audit and policy review.
    asserts:
      checks:
      - id: __export__path.basename
        assert:
          lit:
            let:
            - lit:
              - - segs
                - call:
                  - var: path.segments
                  - var: path
            - if:
              - std.collection.is_empty:
                - var: segs
              - ''
              - std.object.get:
                - var: segs
                - std.math.sub:
                  - std.collection.len:
                    - var: segs
                  - 1
      - id: __export__path.trim_dot
        assert:
          std.string.replace:
          - var: path
          - "./"
          - ''
      - id: __export__path.dirname
        assert:
          lit:
            let:
            - lit:
              - - segs
                - call:
                  - var: path.segments
                  - var: path
            - if:
              - std.logic.lte:
                - std.collection.len:
                  - var: segs
                - 1
              - ''
              - std.string.join:
                - std.collection.slice:
                  - 0
                  - std.math.sub:
                    - std.collection.len:
                      - var: segs
                    - 1
                  - var: segs
                - "/"
      - id: __export__path.has_extension
        assert:
          std.logic.eq:
          - call:
            - var: path.extension
            - var: path
          - var: ext
      - id: __export__path.is_under
        assert:
          std.string.starts_with:
          - call:
            - var: path.normalize_slashes
            - var: path
          - call:
            - var: path.normalize_slashes
            - var: prefix
      - id: __export__path.matches
        assert:
          std.string.regex_match:
          - call:
            - var: path.normalize_slashes
            - var: path
          - var: pattern
  - id: LIB-PATH-001-004-PATH-EXTENSION
    docs:
    - summary: Case `LIB-PATH-001-004-PATH-EXTENSION` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core
      module: path
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
    - summary: Case `LIB-PATH-001-004-PATH-EXTENSION` for `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.operator
      module: path
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
    - summary: Case `LIB-PATH-001-004-PATH-EXTENSION` for `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.integrator
      module: path
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
    - summary: Case `LIB-PATH-001-004-PATH-EXTENSION` for `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.maintainer
      module: path
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
    - summary: Case `LIB-PATH-001-004-PATH-EXTENSION` for `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.governance
      module: path
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
    - summary: Case `LIB-PATH-001-004-PATH-EXTENSION` for `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.reviewer
      module: path
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
    - summary: Case `LIB-PATH-001-004-PATH-EXTENSION` for `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `path.matches` for this audience, including input contract, output contract, and failure modes.

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
      - path
      id: path.path.core.auditor
      module: path
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
      - Use this as documented evidence for audit and policy review.
    asserts:
      checks:
      - id: __export__path.extension
        assert:
          lit:
            let:
            - lit:
              - - base
                - call:
                  - var: path.basename
                  - var: path
            - let:
              - lit:
                - - parts
                  - split:
                    - var: base
                    - "."
              - if:
                - std.logic.lte:
                  - std.collection.len:
                    - var: parts
                  - 1
                - ''
                - std.object.get:
                  - var: parts
                  - std.math.sub:
                    - std.collection.len:
                      - var: parts
                    - 1
      - id: __export__path.trim_dot
        assert:
          std.string.replace:
          - var: path
          - "./"
          - ''
      - id: __export__path.dirname
        assert:
          lit:
            let:
            - lit:
              - - segs
                - call:
                  - var: path.segments
                  - var: path
            - if:
              - std.logic.lte:
                - std.collection.len:
                  - var: segs
                - 1
              - ''
              - std.string.join:
                - std.collection.slice:
                  - 0
                  - std.math.sub:
                    - std.collection.len:
                      - var: segs
                    - 1
                  - var: segs
                - "/"
      - id: __export__path.has_extension
        assert:
          std.logic.eq:
          - call:
            - var: path.extension
            - var: path
          - var: ext
      - id: __export__path.is_under
        assert:
          std.string.starts_with:
          - call:
            - var: path.normalize_slashes
            - var: path
          - call:
            - var: path.normalize_slashes
            - var: prefix
      - id: __export__path.matches
        assert:
          std.string.regex_match:
          - call:
            - var: path.normalize_slashes
            - var: path
          - var: pattern
  - id: LIB-PATH-001-900-PATH-SMOKE
    type: contract.check
    asserts:
      imports:
      - from: asset
        names:
        - text
      checks:
      - id: assert_1
        assert:
          std.logic.eq:
          - call:
            - var: path.normalize_slashes
            - a\b\c.txt
          - a/b/c.txt
adapters:
- type: beta.exports_as_path_normalize_slashes_from_assert_function_path_export_path_normalize_slashes_params_path_docs_id_path_normalize_slashes_doc_1_summary_contract_export_for_path_normalize_slashes_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_trim_dot_from_assert_function_path_export_path_trim_dot_params_path_docs_id_path_trim_dot_doc_1_summary_contract_export_for_path_trim_dot_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_dirname_from_assert_function_path_export_path_dirname_params_path_docs_id_path_dirname_doc_1_summary_contract_export_for_path_dirname_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_has_extension_from_assert_function_path_export_path_has_extension_params_path_ext_docs_id_path_has_extension_doc_1_summary_contract_export_for_path_has_extension_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_n_ext_ext_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_name_ext_n_type_any_n_required_true_n_description_input_parameter_ext_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_is_under_from_assert_function_path_export_path_is_under_params_path_prefix_docs_id_path_is_under_doc_1_summary_contract_export_for_path_is_under_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_n_prefix_prefix_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_name_prefix_n_type_any_n_required_true_n_description_input_parameter_prefix_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_matches_from_assert_function_path_export_path_matches_params_path_pattern_docs_id_path_matches_doc_1_summary_contract_export_for_path_matches_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_n_pattern_pattern_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_name_pattern_n_type_any_n_required_true_n_description_input_parameter_pattern_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.path.core.spec.1
    profile: default
- type: beta.exports_as_path_segments_from_assert_function_path_export_path_segments_params_path_docs_id_path_segments_doc_1_summary_contract_export_for_path_segments_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_trim_dot_from_assert_function_path_export_path_trim_dot_params_path_docs_id_path_trim_dot_doc_1_summary_contract_export_for_path_trim_dot_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_dirname_from_assert_function_path_export_path_dirname_params_path_docs_id_path_dirname_doc_1_summary_contract_export_for_path_dirname_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_has_extension_from_assert_function_path_export_path_has_extension_params_path_ext_docs_id_path_has_extension_doc_1_summary_contract_export_for_path_has_extension_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_n_ext_ext_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_name_ext_n_type_any_n_required_true_n_description_input_parameter_ext_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_is_under_from_assert_function_path_export_path_is_under_params_path_prefix_docs_id_path_is_under_doc_1_summary_contract_export_for_path_is_under_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_n_prefix_prefix_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_name_prefix_n_type_any_n_required_true_n_description_input_parameter_prefix_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_matches_from_assert_function_path_export_path_matches_params_path_pattern_docs_id_path_matches_doc_1_summary_contract_export_for_path_matches_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_n_pattern_pattern_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_name_pattern_n_type_any_n_required_true_n_description_input_parameter_pattern_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.path.core.spec.2
    profile: default
- type: beta.exports_as_path_basename_from_assert_function_path_export_path_basename_params_path_docs_id_path_basename_doc_1_summary_contract_export_for_path_basename_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_trim_dot_from_assert_function_path_export_path_trim_dot_params_path_docs_id_path_trim_dot_doc_1_summary_contract_export_for_path_trim_dot_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_dirname_from_assert_function_path_export_path_dirname_params_path_docs_id_path_dirname_doc_1_summary_contract_export_for_path_dirname_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_has_extension_from_assert_function_path_export_path_has_extension_params_path_ext_docs_id_path_has_extension_doc_1_summary_contract_export_for_path_has_extension_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_n_ext_ext_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_name_ext_n_type_any_n_required_true_n_description_input_parameter_ext_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_is_under_from_assert_function_path_export_path_is_under_params_path_prefix_docs_id_path_is_under_doc_1_summary_contract_export_for_path_is_under_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_n_prefix_prefix_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_name_prefix_n_type_any_n_required_true_n_description_input_parameter_prefix_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_matches_from_assert_function_path_export_path_matches_params_path_pattern_docs_id_path_matches_doc_1_summary_contract_export_for_path_matches_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_n_pattern_pattern_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_name_pattern_n_type_any_n_required_true_n_description_input_parameter_pattern_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.path.core.spec.3
    profile: default
- type: beta.exports_as_path_extension_from_assert_function_path_export_path_extension_params_path_docs_id_path_extension_doc_1_summary_contract_export_for_path_extension_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_trim_dot_from_assert_function_path_export_path_trim_dot_params_path_docs_id_path_trim_dot_doc_1_summary_contract_export_for_path_trim_dot_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_dirname_from_assert_function_path_export_path_dirname_params_path_docs_id_path_dirname_doc_1_summary_contract_export_for_path_dirname_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_has_extension_from_assert_function_path_export_path_has_extension_params_path_ext_docs_id_path_has_extension_doc_1_summary_contract_export_for_path_has_extension_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_n_ext_ext_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_name_ext_n_type_any_n_required_true_n_description_input_parameter_ext_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_is_under_from_assert_function_path_export_path_is_under_params_path_prefix_docs_id_path_is_under_doc_1_summary_contract_export_for_path_is_under_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_n_prefix_prefix_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_name_prefix_n_type_any_n_required_true_n_description_input_parameter_prefix_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_path_matches_from_assert_function_path_export_path_matches_params_path_pattern_docs_id_path_matches_doc_1_summary_contract_export_for_path_matches_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_n_pattern_pattern_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_name_pattern_n_type_any_n_required_true_n_description_input_parameter_pattern_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.path.core.spec.4
    profile: default
- type: beta.check_profile_text_file_config_use_ref_lib_path_001_001_path_normalize_slashes_as_lib_path_normalize_symbols_path_normalize_slashes
  actions:
  - id: act.lib.path.core.spec.5
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
```



