# Spec-Lang Stdlib Profile v1

This contract defines the complete fixed stdlib surface for spec-lang v1.

## Source Of Truth

- Profile file: `/docs/spec/schema/spec_lang_stdlib_profile_v1.yaml`
- The profile is normative for:
  - required symbols
  - category membership
  - declared arity
  - purity/determinism expectations
  - Python/PHP parity requirement

## Requirements

- All profile symbols MUST exist in Python and PHP implementations.
- All profile symbols with declared non-null arity MUST match Python declared arity.
- All profile symbols MUST remain pure and deterministic.
- Unknown schema-shape keys for `schema_match` / `schema_errors` MUST fail as `schema`.
- Governance MUST hard-fail on profile/implementation/docs/conformance drift.

## Schema Shape DSL Keys

Allowed keys:

- `type`
- `required`
- `properties`
- `allow_extra`
- `items`
- `min_items`
- `max_items`
- `min_length`
- `max_length`
- `pattern`
- `const`
- `enum`
- `all_of`
- `any_of`
- `not`
