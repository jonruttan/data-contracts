# Assertion Contract (v1)

## Tree Model

`assert` is an assertion tree with:

- list: implicit AND
- group mapping with `must` / `can` / `cannot`
- leaf mapping with operator keys

## Group Semantics

- `must`: all children must pass
- `can`: at least one child must pass
- `cannot`: no child may pass

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
