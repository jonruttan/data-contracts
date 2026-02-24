This file is intentionally non-executable as a standalone conformance surface.
It provides producer cases referenced by conformance negative tests.


```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
harness:
  type: unit.test
  profile: check
  config:
    exports:
    - as: bad.path.symbol
      from: assert.function
      path: "/missing_step"
      params:
      - subject
      required: true
      docs:
      - id: bad.path.symbol.doc.1
        summary: Contract export for `bad.path.symbol`.
        audience: implementer
        status: active
        description: |-
          Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - id: bad.path.symbol.doc.1.operator
        summary: Contract export for `bad.path.symbol`. (operator)
        audience: operator
        status: active
        description: |-
          Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - id: bad.path.symbol.doc.1.integrator
        summary: Contract export for `bad.path.symbol`. (integrator)
        audience: integrator
        status: active
        description: |-
          Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - id: bad.path.symbol.doc.1.maintainer
        summary: Contract export for `bad.path.symbol`. (maintainer)
        audience: maintainer
        status: active
        description: |-
          Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - id: bad.path.symbol.doc.1.governance
        summary: Contract export for `bad.path.symbol`. (governance)
        audience: governance
        status: active
        description: |-
          Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - id: bad.path.symbol.doc.1.reviewer
        summary: Contract export for `bad.path.symbol`. (reviewer)
        audience: reviewer
        status: active
        description: |-
          Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      - id: bad.path.symbol.doc.1.auditor
        summary: Contract export for `bad.path.symbol`. (auditor)
        audience: auditor
        status: active
        description: |-
          Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
  - id: BAD-EXPORT-PATH
    docs:
    - summary: Case `BAD-EXPORT-PATH` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      id: conformance.chain.export.validation
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
    - summary: Case `BAD-EXPORT-PATH` for `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      id: conformance.chain.export.validation.operator
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
    - summary: Case `BAD-EXPORT-PATH` for `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      id: conformance.chain.export.validation.integrator
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
    - summary: Case `BAD-EXPORT-PATH` for `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      id: conformance.chain.export.validation.maintainer
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
    - summary: Case `BAD-EXPORT-PATH` for `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      id: conformance.chain.export.validation.governance
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
    - summary: Case `BAD-EXPORT-PATH` for `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      id: conformance.chain.export.validation.reviewer
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
    - summary: Case `BAD-EXPORT-PATH` for `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      id: conformance.chain.export.validation.auditor
      module: conformance
      stability: alpha
      owner: data-contracts
      checks:
      - id: valid_step
        assert:
          std.logic.eq:
          - var: subject
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
  - id: BAD-EXPORT-CLASS
    docs:
    - summary: Case `BAD-EXPORT-CLASS` for `contract.export`.
      audience: implementer
      status: active
      description: |-
        Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      id: conformance.chain.export.validation
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
    - summary: Case `BAD-EXPORT-CLASS` for `contract.export`. (operator)
      audience: operator
      status: active
      description: |-
        Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      id: conformance.chain.export.validation.operator
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
    - summary: Case `BAD-EXPORT-CLASS` for `contract.export`. (integrator)
      audience: integrator
      status: active
      description: |-
        Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      id: conformance.chain.export.validation.integrator
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
    - summary: Case `BAD-EXPORT-CLASS` for `contract.export`. (maintainer)
      audience: maintainer
      status: active
      description: |-
        Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      id: conformance.chain.export.validation.maintainer
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
    - summary: Case `BAD-EXPORT-CLASS` for `contract.export`. (governance)
      audience: governance
      status: active
      description: |-
        Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      id: conformance.chain.export.validation.governance
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
    - summary: Case `BAD-EXPORT-CLASS` for `contract.export`. (reviewer)
      audience: reviewer
      status: active
      description: |-
        Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      id: conformance.chain.export.validation.reviewer
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
    - summary: Case `BAD-EXPORT-CLASS` for `contract.export`. (auditor)
      audience: auditor
      status: active
      description: |-
        Purpose: This entry documents behavior for `bad.path.symbol` for the declared audience, including input expectations, output contracts, and failure modes.

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
      id: conformance.chain.export.validation.auditor
      module: conformance
      stability: alpha
      owner: data-contracts
      checks:
      - id: non_must_step
        required: false
        assert:
          std.logic.eq:
          - var: subject
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
- type: beta.exports_as_bad_path_symbol_from_assert_function_path_missing_step_params_subject_required_true_docs_id_bad_path_symbol_doc_1_summary_contract_export_for_bad_path_symbol_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.chain.export.validation.1
    profile: default
- type: beta.exports_as_bad_class_symbol_from_assert_function_path_non_must_step_params_subject_required_true_docs_id_bad_class_symbol_doc_1_summary_contract_export_for_bad_class_symbol_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nprior_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  actions:
  - id: act.lib.chain.export.validation.2
    profile: default
services:
- id: svc.lib.chain.export.validation.1
  consumes:
  - act.lib.chain.export.validation.1
- id: svc.lib.chain.export.validation.2
  consumes:
  - act.lib.chain.export.validation.2
```


