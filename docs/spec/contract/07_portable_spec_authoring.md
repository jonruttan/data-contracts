# Portable Spec Authoring Contract (v1)

Goal: keep one high-quality executable spec set that is deterministic and
implementation-independent.

## Canonical Spec Set

- The canonical cross-implementation behavior set lives in:
  - `docs/spec/conformance/cases/*.spec.md`
- New portable behavior coverage SHOULD be added to this canonical set first.
- Implementation-specific suites (for example `docs/spec/impl/php/cases/`) are
  for runner-local coverage and MUST NOT replace portable conformance coverage.

## Expected Outcome Shape

- Portable expectations MUST be expressed in `expect.portable`.
- Implementation deltas MUST be expressed only via `expect.impl.<runtime>`
  overlays.
- Portable semantics should not be duplicated in per-runtime case copies.

## Determinism Requirements

Portable conformance cases SHOULD be deterministic by construction:

- No ambient-time assumptions (`now`, current date/time, timezone-dependent
  expectations) unless the value is injected explicitly as case input.
- No ambient-randomness assumptions unless deterministic seed/input is
  explicitly provided.
- No network dependency in portable cases.
- No ambient environment dependency unless declared via case-level inputs
  (`harness.*`, explicit fixture files, or explicit capability requirements).

Governance enforcement:

- `conformance.no_ambient_assumptions` rejects common ambient
  environment/time/random dependency tokens in portable case content.

## Portability Boundaries

- Portable case IDs use `SRCONF-*`.
- Runtime/implementation-specific behavior should be represented via:
  - `requires.capabilities`
  - `expect.impl.<runtime>`
- Portable case text SHOULD avoid language/runtime branding unless the case is
  explicitly testing portability deltas.

## API Extension Authoring Rule

For `type: api.http` portable cases:

- transport/setup details MUST live under `harness`
- HTTP behavior assertions MUST live under canonical `assert` targets
- portable assertion targets are: `status`, `headers`, `body_text`, `body_json`
