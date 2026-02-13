# Assertion Contract (v1)

## Tree Model

`assert` is an assertion tree with:

- list: implicit AND
- group mapping with exactly one of `must` / `can` / `cannot`
- leaf mapping with operator keys

## Group Semantics

- `must`: all children must pass
- `can`: at least one child must pass
- `cannot`: no child may pass
- group child lists must be non-empty

## Target Rules

- `target` is defined on group nodes.
- Leaf nodes inherit `target` from parent groups.
- Leaf nodes MUST NOT include `target`.
- A leaf without inherited `target` is invalid.

## Leaf Operators

Canonical operators:

- `contain`
- `regex`
- `json_type`
- `exists`

Operator values MUST be lists.

## Portable Regex Subset

`regex` patterns SHOULD stay within a portable subset across implementations.
Runners SHOULD emit assertion-health diagnostics for patterns that use
non-portable constructs, including:

- lookbehind (`(?<=...)`, `(?<!...)`)
- named capture groups / named backreferences
- inline flags (`(?i)`, `(?m:...)`, etc.)
- conditional groups
- atomic groups / possessive quantifiers

Canonical profile:

- `docs/spec/contract/03a_regex_portability_v1.md`

## Assertion Health Note

Redundant sibling branches within a group (for example duplicate `can` branch
expressions) are considered assertion-health diagnostics and may be surfaced as
warnings/errors depending on policy mode.
