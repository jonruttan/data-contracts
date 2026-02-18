# Assertion Contract (v1)

## Tree Model

`assert` is a list of assertion steps.

Each assertion step has:

- `id`
- `class` (`must` | `can` | `cannot`)
- optional `target`
- `checks` (non-empty list)

`checks` entries are assertion-tree nodes (group or leaf mappings).

## Group Semantics

- `must`: all `checks` must pass
- `can`: at least one check must pass
- `cannot`: no check may pass
- check lists must be non-empty

## Target Rules

- `target` is defined on assertion steps and may be refined by inner group nodes.
- Leaf nodes inherit `target` from the step/group chain.
- Leaf nodes MUST NOT include `target`.
- A leaf without inherited `target` is invalid.

## Leaf Operators

Canonical operators:

- universal core: `evaluate`

Operator values MUST be lists.

`evaluate` values are spec-lang v1 expressions encoded as operator-keyed mapping AST nodes within a YAML list.
Normative contract:

- `docs/spec/contract/03b_spec_lang_v1.md`

Internal execution model:

- runners compile external leaf operators into spec-lang predicate expressions
- evaluation executes compiled spec-lang predicates only
- compile mapping/invariants are documented in
  `docs/spec/contract/09_internal_representation.md`

## Naming Contract

- `evaluate` is the assertion leaf operator used under `assert`.
- Governance/orchestration decision obligations are encoded in `assert` blocks.
- `harness.policy_evaluate` and `harness.orchestration_policy.policy_evaluate`
  are forbidden in executable contracts.

## Governance Assertion Targets

For `type: governance.check`, assertion targets include:

- `text`: human-readable PASS/FAIL summary output
- `summary_json`: structured summary surface (available to `evaluate` as a
  mapping with `passed`, `check_id`, `case_id`, `violation_count`)
- `violation_count`: numeric violation count
- `context_json`: optional JSON subject profile envelope
- `meta_json`: runtime metadata envelope

## Core Surface Rule

- Assertion trees in `docs/spec/conformance/cases/**/*.spec.md` MUST use
  `evaluate` leaves only.
- Assertion trees in `docs/spec/governance/cases/**/*.spec.md` MUST use
  `evaluate` leaves only.
- Sugar operators remain compile-only schema forms for non-core surfaces.

## Spec-Lang-Primary Runtime Contract

- `evaluate` is the only universal assertion operator contract.
- Runtime decision semantics MUST execute as compiled spec-lang expressions.
- Implementations MUST NOT bypass the compiled spec-lang assertion engine.
- Target/type applicability is defined by subject availability and subject
  shape, not by per-type operator allowlists.
- Subject values consumed by spec-lang MUST be JSON-core values. Native runtime
  structures are projected by adapters into JSON profile envelopes.
- Regex portability guidance for spec-lang expressions is defined in
  `docs/spec/contract/03a_regex_portability_v1.md`.

## Assertion Health Note

Redundant sibling branches within a group (for example duplicate `can` branch
expressions) are considered assertion-health diagnostics and may be surfaced as
warnings/errors depending on policy mode.
