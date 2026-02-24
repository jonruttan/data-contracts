```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
harness:
  type: unit.test
  profile: check
  config:
    exports:
    - as: std.string.contains
      from: assert.function
      path: "/__export__std.string.contains"
      params:
      - haystack
      - needle
      required: true
      docs:
      - id: std.string.contains.doc.1
        summary: Check whether a string contains a given substring.
        audience: implementer
        status: active
        description: Use deterministic substring search to decide whether a haystack string contains a required token.
        inputs:
        - haystack: Input text being searched.
        - needle: Search token; empty token is treated as present.
        returns:
        - Boolean true if token is found, false otherwise.
        errors:
        - Non-string arguments fail validation.
        usage_context:
        - Predicate logic inside contracts, assertions, and control-flow branches.
      - id: std.string.contains.doc.1.operator
        summary: Route operational checks using substring membership.
        audience: operator
        status: active
        description: Use deterministic string matching to drive runbook branching and incident classification.
        inputs:
        - haystack: Log/event payload text.
        - needle: Token to search in observability telemetry.
        returns:
        - Boolean membership result for runtime branching.
        errors:
        - Input shape/type mismatch errors are surfaced before branching.
        usage_context:
        - Incident triage, alert routing, and operational policy enforcement.
      - id: std.string.contains.doc.1.integrator
        summary: Compose text-matching predicates for external integrations.
        audience: integrator
        status: active
        description: Use substring semantics when integrating policy or orchestration pipelines.
        inputs:
        - haystack: Payload text supplied by upstream service.
        - needle: Match token owned by the consuming integration.
        returns:
        - Boolean indicating whether the token appears in payload.
        errors:
        - Missing/typed fields fail contract binding before invocation.
        usage_context:
        - Cross-service orchestration and contract composition.
      - id: std.string.contains.doc.1.maintainer
        summary: Track substring behavior through function lifecycle changes.
        audience: maintainer
        status: active
        description: Prefer stable, documented semantics when changing upstream runtimes or spec tooling.
        inputs:
        - haystack: Input payload expected by the function.
        - needle: Search token parameter.
        returns:
        - Boolean result and no side effects.
        errors:
        - Validation errors if input arity or typing changes.
        usage_context:
        - Release planning and compatibility review for text predicate behavior.
      - id: std.string.contains.doc.1.governance
        summary: Use deterministic predicate semantics for controls and policy gates.
        audience: governance
        status: active
        description: `contains` provides auditable boolean inputs for control checks requiring deterministic text checks.
        inputs:
        - haystack: Governed input text.
        - needle: Policy keyword.
        returns:
        - Boolean decision used in governance gates.
        errors:
        - Schema validation errors for malformed inputs.
        usage_context:
        - Access-control, policy enforcement, and compliance automation.
      - id: std.string.contains.doc.1.reviewer
        summary: Verify exact text-match behavior before release.
        audience: reviewer
        status: active
        description: Confirm positive/negative matching, empty token handling, and error behavior.
        inputs:
        - haystack: Source text under test.
        - needle: Required matching token.
        returns:
        - Boolean match result.
        errors:
        - Non-string input and missing argument errors.
        usage_context:
        - Contract review, change approval, and evidence verification.
      - id: std.string.contains.doc.1.auditor
        summary: Evidence-ready substring checks for audit records.
        audience: auditor
        status: active
        description: Deterministic predicate output is useful as an evidence source for compliance checks.
        inputs:
        - haystack: Logged source text.
        - needle: Required audit keyword.
        returns:
        - Boolean signal.
        errors:
        - Schema/type validation failures block reliable audit evidence.
        usage_context:
        - Compliance reporting and control effectiveness evidence.
    - as: std.string.starts_with
      from: assert.function
      path: "/__export__std.string.starts_with"
      params:
      - value
      - prefix
      required: true
      docs:
      - id: std.string.starts_with.doc.1
        summary: Check whether a string starts with a prefix.
        audience: implementer
        status: active
        description: Evaluate whether `value` has `prefix` at position zero.
        inputs:
        - value: Candidate string.
        - prefix: Prefix token.
        returns:
        - Boolean true when the match is exact at index zero.
        errors:
        - Non-string arguments fail schema validation.
        usage_context:
        - Validator and router implementation details for text prefixed checks.
      - id: std.string.starts_with.doc.1.operator
        summary: Use prefix checks to route structured operations.
        audience: operator
        status: active
        description: Deterministic string prefix checks suitable for run-path branching.
        inputs:
        - value: Runtime payload.
        - prefix: Prefix used for classification.
        returns:
        - Boolean classification for operator flow.
        errors:
        - Runtime validation errors on shape/type mismatch.
        usage_context:
        - Workflow routing and alert classification.
      - id: std.string.starts_with.doc.1.integrator
        summary: Compose prefix matching in integration chains.
        audience: integrator
        status: active
        description: Use as a stable predicate in interoperability and policy chains.
        inputs:
        - value: Upstream text value.
        - prefix: Expected prefix.
        returns:
        - Boolean true when prefixed.
        errors:
        - Invalid input type or arity fail early.
        usage_context:
        - Service composition and API contract mediation.
      - id: std.string.starts_with.doc.1.maintainer
        summary: Maintain stable prefix behavior across version upgrades.
        audience: maintainer
        status: active
        description: Keep contract and runtime assumptions around case and boundary behavior explicit.
        inputs:
        - value: Candidate input text.
        - prefix: Expected leading token.
        returns:
        - Boolean result.
        errors:
        - Validation failures for malformed inputs.
        usage_context:
        - Change management and backward-compatibility reviews.
      - id: std.string.starts_with.doc.1.governance
        summary: Use prefix checks in policy controls requiring deterministic matching.
        audience: governance
        status: active
        description: Prefix matching provides deterministic boolean outcomes suitable for control logic.
        inputs:
        - value: Controlled input.
        - prefix: Required prefix token.
        returns:
        - Boolean decision for control evaluation.
        errors:
        - Non-string and missing-field failures.
        usage_context:
        - Security/compliance control evaluation.
      - id: std.string.starts_with.doc.1.reviewer
        summary: Verify boundary and empty-prefix behavior.
        audience: reviewer
        status: active
        description: Review success/failure cases, including empty prefix and short input.
        inputs:
        - value: Candidate value string.
        - prefix: Prefix term.
        returns:
        - Boolean result.
        errors:
        - Validation errors and arity mismatches.
        usage_context:
        - Review and acceptance for text predicates.
      - id: std.string.starts_with.doc.1.auditor
        summary: Auditable prefix predicate for control evidence.
        audience: auditor
        status: active
        description: Track deterministic prefix semantics that feed policy and audit tooling.
        inputs:
        - value: Audited text.
        - prefix: Governing token.
        returns:
        - Boolean decision.
        errors:
        - Schema/type errors create non-deterministic audit inputs.
        usage_context:
        - Audit trail and control reporting.
    - as: std.string.ends_with
      from: assert.function
      path: "/__export__std.string.ends_with"
      params:
      - value
      - suffix
      required: true
      docs:
      - id: std.string.ends_with.doc.1
        summary: Check whether a string ends with a suffix.
        audience: implementer
        status: active
        description: Return true only when `value` ends with `suffix`.
        inputs:
        - value: Candidate string.
        - suffix: Expected trailing token.
        returns:
        - Boolean true when trailing text matches exactly.
        errors:
        - Type and shape violations fail validation.
        usage_context:
        - Implementation checks, validators, and routing predicates.
      - id: std.string.ends_with.doc.1.operator
        summary: Route operations by deterministic suffix checks.
        audience: operator
        status: active
        description: Use trailing token checks for incident and workflow branching.
        inputs:
        - value: Runtime payload.
        - suffix: Suffix token.
        returns:
        - Boolean classification output.
        errors:
        - Non-string values produce validation errors.
        usage_context:
        - Runbook logic and reliability controls.
      - id: std.string.ends_with.doc.1.integrator
        summary: Include suffix checks in interoperable integration logic.
        audience: integrator
        status: active
        description: Use deterministic suffix matching in policy and service chains.
        inputs:
        - value: Upstream string.
        - suffix: Suffix token.
        returns:
        - Boolean match result.
        errors:
        - Invalid payload shape or missing suffix.
        usage_context:
        - Cross-system validation and orchestration.
      - id: std.string.ends_with.doc.1.maintainer
        summary: Keep suffix semantics stable for support and maintenance.
        audience: maintainer
        status: active
        description: Ensure deterministic behavior and explicit compatibility notes during updates.
        inputs:
        - value: Input string.
        - suffix: Matching suffix.
        returns:
        - Boolean result.
        errors:
        - Validation failures from argument changes.
        usage_context:
        - Runtime lifecycle and support planning.
      - id: std.string.ends_with.doc.1.governance
        summary: Use suffix matching in deterministic governance checks.
        audience: governance
        status: active
        description: Deterministic trailing checks make this safe for policy assertions.
        inputs:
        - value: Governed text.
        - suffix: Control suffix token.
        returns:
        - Boolean gate signal.
        errors:
        - Type/shape validation failures.
        usage_context:
        - Enforcement rules and audit-oriented controls.
      - id: std.string.ends_with.doc.1.reviewer
        summary: Validate exact trailing-match behavior.
        audience: reviewer
        status: active
        description: Review normal and edge cases for suffix comparison logic.
        inputs:
        - value: Candidate text.
        - suffix: Expected suffix.
        returns:
        - Boolean.
        errors:
        - Missing argument or type errors.
        usage_context:
        - Review evidence and correctness checks.
      - id: std.string.ends_with.doc.1.auditor
        summary: Deterministic trailing predicate for evidence and attestations.
        audience: auditor
        status: active
        description: Use as a stable evidence-bearing predicate in control workflows.
        inputs:
        - value: Audited text.
        - suffix: Governing trailing term.
        returns:
        - Boolean result.
        errors:
        - Schema failures reduce audit certainty.
        usage_context:
        - Audit evidence collection.
```
