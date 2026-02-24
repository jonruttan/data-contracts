```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
harness:
  type: unit.test
  profile: check
  config:
    exports:
    - as: domain.markdown.tokens_all_present
      from: assert.function
      path: "/__export__domain.markdown.tokens_all_present"
      params:
      - subject
      - tokens
      required: true
      docs:
      - id: domain.markdown.tokens_all_present.doc.1
        summary: Contract export for `domain.markdown.tokens_all_present`.
        audience: implementer
        status: active
        description: |-
          Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - id: domain.markdown.tokens_all_present.doc.1.operator
        summary: Contract export for `domain.markdown.tokens_all_present`. (operator)
        audience: operator
        status: active
        description: |-
          Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - id: domain.markdown.tokens_all_present.doc.1.integrator
        summary: Contract export for `domain.markdown.tokens_all_present`. (integrator)
        audience: integrator
        status: active
        description: |-
          Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - id: domain.markdown.tokens_all_present.doc.1.maintainer
        summary: Contract export for `domain.markdown.tokens_all_present`. (maintainer)
        audience: maintainer
        status: active
        description: |-
          Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - id: domain.markdown.tokens_all_present.doc.1.governance
        summary: Contract export for `domain.markdown.tokens_all_present`. (governance)
        audience: governance
        status: active
        description: |-
          Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - id: domain.markdown.tokens_all_present.doc.1.reviewer
        summary: Contract export for `domain.markdown.tokens_all_present`. (reviewer)
        audience: reviewer
        status: active
        description: |-
          Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - id: domain.markdown.tokens_all_present.doc.1.auditor
        summary: Contract export for `domain.markdown.tokens_all_present`. (auditor)
        audience: auditor
        status: active
        description: |-
          Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
  - id: LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING
    title: 'markdown projection helper functions: domain.markdown.has_heading'
    docs:
    - summary: Case `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core
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
    - summary: Case `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.operator
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
    - summary: Case `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.integrator
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
    - summary: Case `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.maintainer
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
    - summary: Case `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.governance
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
    - summary: Case `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.reviewer
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
    - summary: Case `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - domain
      id: domain.markdown.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.markdown.has_heading
        assert:
          std.logic.or:
          - std.collection.any:
            - std.collection.map:
              - fn:
                - - row
                - std.logic.eq:
                  - std.string.lower:
                    - std.object.get:
                      - var: row
                      - text
                  - std.string.lower:
                    - var: heading
              - call:
                - var: markdown._headings
                - var: subject
          - std.logic.or:
            - std.string.contains:
              - call:
                - var: markdown._text
                - var: subject
              - std.string.join:
                - std.collection.append:
                  - var: heading
                  - lit:
                    - "# "
                - ''
            - std.logic.or:
              - std.string.contains:
                - call:
                  - var: markdown._text
                  - var: subject
                - std.string.join:
                  - std.collection.append:
                    - var: heading
                    - lit:
                      - "## "
                  - ''
              - std.logic.or:
                - std.string.contains:
                  - call:
                    - var: markdown._text
                    - var: subject
                  - std.string.join:
                    - std.collection.append:
                      - var: heading
                      - lit:
                        - "### "
                    - ''
                - std.logic.or:
                  - std.string.contains:
                    - call:
                      - var: markdown._text
                      - var: subject
                    - std.string.join:
                      - std.collection.append:
                        - var: heading
                        - lit:
                          - "#### "
                      - ''
                  - std.logic.or:
                    - std.string.contains:
                      - call:
                        - var: markdown._text
                        - var: subject
                      - std.string.join:
                        - std.collection.append:
                          - var: heading
                          - lit:
                            - "##### "
                        - ''
                    - std.string.contains:
                      - call:
                        - var: markdown._text
                        - var: subject
                      - std.string.join:
                        - std.collection.append:
                          - var: heading
                          - lit:
                            - "###### "
                        - ''
      - id: __export__markdown._text
        assert:
          lit:
            if:
            - std.type.is_string:
              - var: subject
            - var: subject
            - std.null.default_to:
              - ''
              - std.object.get:
                - var: subject
                - value
      - id: __export__markdown._context
        assert:
          lit:
            if:
            - std.type.is_dict:
              - var: subject
            - std.null.default_to:
              - lit: {}
              - std.object.get:
                - var: subject
                - context
            - lit: {}
      - id: __export__markdown._headings
        assert:
          std.null.default_to:
          - lit: []
          - std.object.get:
            - call:
              - var: markdown._context
              - var: subject
            - headings
      - id: __export__markdown._links
        assert:
          std.null.default_to:
          - lit: []
          - std.object.get:
            - call:
              - var: markdown._context
              - var: subject
            - links
      - id: __export__markdown._tokens_map
        assert:
          std.null.default_to:
          - lit: {}
          - std.object.get:
            - call:
              - var: markdown._context
              - var: subject
            - tokens
      - id: __export__markdown._token_owners
        assert:
          std.null.default_to:
          - lit: {}
          - std.object.get:
            - call:
              - var: markdown._context
              - var: subject
            - token_owners
      - id: __export__markdown._token_dependencies
        assert:
          std.null.default_to:
          - lit: []
          - std.object.get:
            - call:
              - var: markdown._context
              - var: subject
            - token_dependencies
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
  - id: LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS
    title: 'markdown projection helper functions: domain.markdown.heading_level_exists'
    docs:
    - summary: Case `LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS` for
        `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core
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
    - summary: Case `LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS` for
        `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.operator
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
    - summary: Case `LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS` for
        `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.integrator
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
    - summary: Case `LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS` for
        `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.maintainer
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
    - summary: Case `LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS` for
        `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.governance
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
    - summary: Case `LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS` for
        `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.reviewer
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
    - summary: Case `LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS` for
        `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - domain
      id: domain.markdown.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.markdown.heading_level_exists
        assert:
          std.logic.or:
          - std.collection.any:
            - std.collection.map:
              - fn:
                - - row
                - std.logic.eq:
                  - std.object.get:
                    - var: row
                    - level
                  - var: level
              - call:
                - var: markdown._headings
                - var: subject
          - if:
            - std.logic.eq:
              - var: level
              - 1
            - std.string.regex_match:
              - call:
                - var: markdown._text
                - var: subject
              - "(?m)^#\\s+"
            - if:
              - std.logic.eq:
                - var: level
                - 2
              - std.string.regex_match:
                - call:
                  - var: markdown._text
                  - var: subject
                - "(?m)^##\\s+"
              - if:
                - std.logic.eq:
                  - var: level
                  - 3
                - std.string.regex_match:
                  - call:
                    - var: markdown._text
                    - var: subject
                  - "(?m)^###\\s+"
                - if:
                  - std.logic.eq:
                    - var: level
                    - 4
                  - std.string.regex_match:
                    - call:
                      - var: markdown._text
                      - var: subject
                    - "(?m)^####\\s+"
                  - if:
                    - std.logic.eq:
                      - var: level
                      - 5
                    - std.string.regex_match:
                      - call:
                        - var: markdown._text
                        - var: subject
                      - "(?m)^#####\\s+"
                    - if:
                      - std.logic.eq:
                        - var: level
                        - 6
                      - std.string.regex_match:
                        - call:
                          - var: markdown._text
                          - var: subject
                        - "(?m)^######\\s+"
                      - false
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
  - id: LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID
    title: 'markdown projection helper functions: domain.markdown.section_order_valid'
    docs:
    - summary: Case `LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID` for
        `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core
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
    - summary: Case `LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID` for
        `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.operator
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
    - summary: Case `LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID` for
        `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.integrator
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
    - summary: Case `LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID` for
        `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.maintainer
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
    - summary: Case `LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID` for
        `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.governance
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
    - summary: Case `LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID` for
        `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.reviewer
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
    - summary: Case `LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID` for
        `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - domain
      id: domain.markdown.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.markdown.section_order_valid
        assert:
          std.logic.and:
          - call:
            - var: domain.markdown.required_sections_present
            - var: subject
            - var: headings
          - if:
            - std.logic.lte:
              - std.collection.len:
                - var: headings
              - 1
            - true
            - std.logic.and:
              - std.logic.neq:
                - std.object.get:
                  - std.object.get:
                    - call:
                      - var: markdown._context
                      - var: subject
                    - heading_positions
                  - std.object.get:
                    - var: headings
                    - 0
              - std.logic.gt:
                - std.object.get:
                  - std.object.get:
                    - call:
                      - var: markdown._context
                      - var: subject
                    - heading_positions
                  - std.object.get:
                    - var: headings
                    - 1
                - std.object.get:
                  - std.object.get:
                    - call:
                      - var: markdown._context
                      - var: subject
                    - heading_positions
                  - std.object.get:
                    - var: headings
                    - 0
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
  - id: LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT
    title: 'markdown projection helper functions: domain.markdown.required_sections_present'
    docs:
    - summary: Case `LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT`
        for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core
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
    - summary: Case `LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT`
        for `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.operator
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
    - summary: Case `LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT`
        for `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.integrator
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
    - summary: Case `LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT`
        for `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.maintainer
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
    - summary: Case `LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT`
        for `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.governance
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
    - summary: Case `LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT`
        for `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.reviewer
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
    - summary: Case `LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT`
        for `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - domain
      id: domain.markdown.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.markdown.required_sections_present
        assert:
          std.collection.all:
          - std.collection.map:
            - fn:
              - - heading
              - call:
                - var: domain.markdown.has_heading
                - var: subject
                - var: heading
            - var: headings
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
  - id: LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE
    title: 'markdown projection helper functions: domain.markdown.link_targets_all_resolve'
    docs:
    - summary: Case `LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE`
        for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core
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
    - summary: Case `LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE`
        for `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.operator
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
    - summary: Case `LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE`
        for `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.integrator
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
    - summary: Case `LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE`
        for `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.maintainer
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
    - summary: Case `LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE`
        for `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.governance
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
    - summary: Case `LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE`
        for `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.reviewer
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
    - summary: Case `LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE`
        for `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - domain
      id: domain.markdown.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.markdown.link_targets_all_resolve
        assert:
          std.collection.all:
          - std.collection.map:
            - fn:
              - - row
              - std.logic.eq:
                - std.object.get:
                  - var: row
                  - resolved
                - true
            - call:
              - var: markdown._links
              - var: subject
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
  - id: LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS
    title: 'markdown projection helper functions: domain.markdown.has_broken_links'
    docs:
    - summary: Case `LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core
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
    - summary: Case `LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.operator
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
    - summary: Case `LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.integrator
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
    - summary: Case `LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.maintainer
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
    - summary: Case `LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.governance
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
    - summary: Case `LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.reviewer
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
    - summary: Case `LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - domain
      id: domain.markdown.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.markdown.has_broken_links
        assert:
          std.logic.not:
          - call:
            - var: domain.markdown.link_targets_all_resolve
            - var: subject
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
  - id: LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE
    title: 'markdown projection helper functions: domain.markdown.has_yaml_spec_test_fence'
    docs:
    - summary: Case `LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE`
        for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core
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
    - summary: Case `LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE`
        for `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.operator
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
    - summary: Case `LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE`
        for `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.integrator
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
    - summary: Case `LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE`
        for `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.maintainer
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
    - summary: Case `LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE`
        for `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.governance
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
    - summary: Case `LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE`
        for `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.reviewer
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
    - summary: Case `LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE`
        for `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - domain
      id: domain.markdown.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.markdown.has_yaml_spec_test_fence
        assert:
          std.logic.or:
          - std.string.contains:
            - call:
              - var: markdown._text
              - var: subject
            - "```yaml contract-spec"
          - std.string.contains:
            - call:
              - var: markdown._text
              - var: subject
            - "~~~yaml contract-spec"
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
  - id: LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS
    title: 'markdown projection helper functions: domain.markdown.code_fence_language_exists'
    docs:
    - summary: Case `LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS`
        for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core
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
    - summary: Case `LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS`
        for `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.operator
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
    - summary: Case `LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS`
        for `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.integrator
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
    - summary: Case `LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS`
        for `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.maintainer
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
    - summary: Case `LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS`
        for `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.governance
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
    - summary: Case `LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS`
        for `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.reviewer
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
    - summary: Case `LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS`
        for `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - domain
      id: domain.markdown.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.markdown.code_fence_language_exists
        assert:
          std.logic.or:
          - std.string.contains:
            - call:
              - var: markdown._text
              - var: subject
            - std.string.join:
              - std.collection.append:
                - var: language
                - lit:
                  - "```"
              - ''
          - std.string.contains:
            - call:
              - var: markdown._text
              - var: subject
            - std.string.join:
              - std.collection.append:
                - var: language
                - lit:
                  - "~~~"
              - ''
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
  - id: LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT
    title: 'markdown projection helper functions: domain.markdown.token_present'
    docs:
    - summary: Case `LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core
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
    - summary: Case `LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT` for `contract.export`.
        (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.operator
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
    - summary: Case `LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT` for `contract.export`.
        (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.integrator
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
    - summary: Case `LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT` for `contract.export`.
        (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.maintainer
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
    - summary: Case `LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT` for `contract.export`.
        (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.governance
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
    - summary: Case `LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT` for `contract.export`.
        (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.reviewer
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
    - summary: Case `LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT` for `contract.export`.
        (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - domain
      id: domain.markdown.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.markdown.token_present
        assert:
          std.logic.or:
          - std.object.has_key:
            - call:
              - var: markdown._tokens_map
              - var: subject
            - var: token
          - std.string.contains:
            - call:
              - var: markdown._text
              - var: subject
            - var: token
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
  - id: LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT
    title: 'markdown projection helper functions: domain.markdown.tokens_all_present'
    docs:
    - summary: Case `LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT` for
        `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core
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
    - summary: Case `LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT` for
        `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.operator
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
    - summary: Case `LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT` for
        `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.integrator
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
    - summary: Case `LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT` for
        `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.maintainer
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
    - summary: Case `LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT` for
        `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.governance
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
    - summary: Case `LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT` for
        `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.reviewer
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
    - summary: Case `LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT` for
        `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - domain
      id: domain.markdown.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.markdown.tokens_all_present
        assert:
          std.collection.all:
          - std.collection.map:
            - fn:
              - - token
              - call:
                - var: domain.markdown.token_present
                - var: subject
                - var: token
            - var: tokens
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
  - id: LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE
    title: 'markdown projection helper functions: domain.markdown.token_ownership_unique'
    docs:
    - summary: Case `LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE`
        for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core
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
    - summary: Case `LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE`
        for `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.operator
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
    - summary: Case `LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE`
        for `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.integrator
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
    - summary: Case `LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE`
        for `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.maintainer
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
    - summary: Case `LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE`
        for `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.governance
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
    - summary: Case `LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE`
        for `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.reviewer
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
    - summary: Case `LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE`
        for `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      - domain
      id: domain.markdown.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.markdown.token_ownership_unique
        assert:
          std.collection.all:
          - std.collection.map:
            - fn:
              - - owners
              - std.logic.eq:
                - std.collection.len:
                  - var: owners
                - 1
            - std.object.values:
              - call:
                - var: markdown._token_owners
                - var: subject
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
  - id: LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED
    title: 'markdown projection helper functions: domain.markdown.token_dependencies_resolved'
    docs:
    - summary: Case `LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED`
        for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core
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
    - summary: Case `LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED`
        for `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.operator
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
    - summary: Case `LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED`
        for `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.integrator
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
    - summary: Case `LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED`
        for `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.maintainer
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
    - summary: Case `LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED`
        for `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.governance
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
    - summary: Case `LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED`
        for `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.reviewer
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
    - summary: Case `LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED`
        for `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: Documents behavior for `domain.markdown.tokens_all_present` for this audience, including input contract, output contract, and failure modes.

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
      id: domain.markdown.core.auditor
      module: domain
      stability: alpha
      owner: data-contracts
      checks:
      - id: __export__domain.markdown.token_dependencies_resolved
        assert:
          std.collection.all:
          - std.collection.map:
            - fn:
              - - dep
              - std.logic.eq:
                - std.object.get:
                  - var: dep
                  - resolved
                - true
            - call:
              - var: markdown._token_dependencies
              - var: subject
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
- type: beta.exports_as_domain_markdown_has_heading_from_assert_function_path_export_domain_markdown_has_heading_params_subject_heading_required_true_docs_id_domain_markdown_has_heading_doc_1_summary_contract_export_for_domain_markdown_has_heading_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_heading_heading_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_heading_n_type_any_n_required_true_n_description_input_parameter_heading_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_markdown_text_from_assert_function_path_export_markdown_text_params_subject_required_true_docs_id_markdown_text_doc_1_summary_contract_export_for_markdown_text_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_markdown_context_from_assert_function_path_export_markdown_context_params_subject_required_true_docs_id_markdown_context_doc_1_summary_contract_export_for_markdown_context_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_markdown_headings_from_assert_function_path_export_markdown_headings_params_subject_required_true_docs_id_markdown_headings_doc_1_summary_contract_export_for_markdown_headings_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_markdown_links_from_assert_function_path_export_markdown_links_params_subject_required_true_docs_id_markdown_links_doc_1_summary_contract_export_for_markdown_links_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_markdown_tokens_map_from_assert_function_path_export_markdown_tokens_map_params_subject_required_true_docs_id_markdown_tokens_map_doc_1_summary_contract_export_for_markdown_tokens_map_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_markdown_token_owners_from_assert_function_path_export_markdown_token_owners_params_subject_required_true_docs_id_markdown_token_owners_doc_1_summary_contract_export_for_markdown_token_owners_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1_as_markdown_token_dependencies_from_assert_function_path_export_markdown_token_dependencies_params_subject_required_true_docs_id_markdown_token_dependencies_doc_1_summary_contract_export_for_markdown_token_dependencies_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.markdown.core.spec.1
  defaults:
    profile: default
- type: beta.exports_as_domain_markdown_heading_level_exists_from_assert_function_path_export_domain_markdown_heading_level_exists_params_subject_level_required_true_docs_id_domain_markdown_heading_level_exists_doc_1_summary_contract_export_for_domain_markdown_heading_level_exists_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_level_level_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_level_n_type_any_n_required_true_n_description_input_parameter_level_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.markdown.core.spec.2
  defaults:
    profile: default
- type: beta.exports_as_domain_markdown_section_order_valid_from_assert_function_path_export_domain_markdown_section_order_valid_params_subject_headings_required_true_docs_id_domain_markdown_section_order_valid_doc_1_summary_contract_export_for_domain_markdown_section_order_valid_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_headings_headings_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_headings_n_type_any_n_required_true_n_description_input_parameter_headings_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.markdown.core.spec.3
  defaults:
    profile: default
- type: beta.exports_as_domain_markdown_required_sections_present_from_assert_function_path_export_domain_markdown_required_sections_present_params_subject_headings_required_true_docs_id_domain_markdown_required_sections_present_doc_1_summary_contract_export_for_domain_markdown_required_sections_present_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_headings_headings_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_headings_n_type_any_n_required_true_n_description_input_parameter_headings_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.markdown.core.spec.4
  defaults:
    profile: default
- type: beta.exports_as_domain_markdown_link_targets_all_resolve_from_assert_function_path_export_domain_markdown_link_targets_all_resolve_params_subject_required_true_docs_id_domain_markdown_link_targets_all_resolve_doc_1_summary_contract_export_for_domain_markdown_link_targets_all_resolve_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.markdown.core.spec.5
  defaults:
    profile: default
- type: beta.exports_as_domain_markdown_has_broken_links_from_assert_function_path_export_domain_markdown_has_broken_links_params_subject_required_true_docs_id_domain_markdown_has_broken_links_doc_1_summary_contract_export_for_domain_markdown_has_broken_links_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.markdown.core.spec.6
  defaults:
    profile: default
- type: beta.exports_as_domain_markdown_has_yaml_spec_test_fence_from_assert_function_path_export_domain_markdown_has_yaml_spec_test_fence_params_subject_required_true_docs_id_domain_markdown_has_yaml_spec_test_fence_doc_1_summary_contract_export_for_domain_markdown_has_yaml_spec_test_fence_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.markdown.core.spec.7
  defaults:
    profile: default
- type: beta.exports_as_domain_markdown_code_fence_language_exists_from_assert_function_path_export_domain_markdown_code_fence_language_exists_params_subject_language_required_true_docs_id_domain_markdown_code_fence_language_exists_doc_1_summary_contract_export_for_domain_markdown_code_fence_language_exists_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_language_language_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_language_n_type_any_n_required_true_n_description_input_parameter_language_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.markdown.core.spec.8
  defaults:
    profile: default
- type: beta.exports_as_domain_markdown_token_present_from_assert_function_path_export_domain_markdown_token_present_params_subject_token_required_true_docs_id_domain_markdown_token_present_doc_1_summary_contract_export_for_domain_markdown_token_present_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_token_token_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_token_n_type_any_n_required_true_n_description_input_parameter_token_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.markdown.core.spec.9
  defaults:
    profile: default
- type: beta.exports_as_domain_markdown_tokens_all_present_from_assert_function_path_export_domain_markdown_tokens_all_present_params_subject_tokens_required_true_docs_id_domain_markdown_tokens_all_present_doc_1_summary_contract_export_for_domain_markdown_tokens_all_present_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_tokens_tokens_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_tokens_n_type_any_n_required_true_n_description_input_parameter_tokens_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.markdown.core.spec.10
  defaults:
    profile: default
- type: beta.exports_as_domain_markdown_token_ownership_unique_from_assert_function_path_export_domain_markdown_token_ownership_unique_params_subject_required_true_docs_id_domain_markdown_token_ownership_unique_doc_1_summary_contract_export_for_domain_markdown_token_ownership_unique_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.markdown.core.spec.11
  defaults:
    profile: default
- type: beta.exports_as_domain_markdown_token_dependencies_resolved_from_assert_function_path_export_domain_markdown_token_dependencies_resolved_params_subject_required_true_docs_id_domain_markdown_token_dependencies_resolved_doc_1_summary_contract_export_for_domain_markdown_token_dependencies_resolved_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.markdown.core.spec.12
  defaults:
    profile: default
services:
- id: svc.lib.markdown.core.spec.1
  consumes:
  - act.lib.markdown.core.spec.1
- id: svc.lib.markdown.core.spec.2
  consumes:
  - act.lib.markdown.core.spec.2
- id: svc.lib.markdown.core.spec.3
  consumes:
  - act.lib.markdown.core.spec.3
- id: svc.lib.markdown.core.spec.4
  consumes:
  - act.lib.markdown.core.spec.4
- id: svc.lib.markdown.core.spec.5
  consumes:
  - act.lib.markdown.core.spec.5
- id: svc.lib.markdown.core.spec.6
  consumes:
  - act.lib.markdown.core.spec.6
- id: svc.lib.markdown.core.spec.7
  consumes:
  - act.lib.markdown.core.spec.7
- id: svc.lib.markdown.core.spec.8
  consumes:
  - act.lib.markdown.core.spec.8
- id: svc.lib.markdown.core.spec.9
  consumes:
  - act.lib.markdown.core.spec.9
- id: svc.lib.markdown.core.spec.10
  consumes:
  - act.lib.markdown.core.spec.10
- id: svc.lib.markdown.core.spec.11
  consumes:
  - act.lib.markdown.core.spec.11
- id: svc.lib.markdown.core.spec.12
  consumes:
  - act.lib.markdown.core.spec.12
```


































