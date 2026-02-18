# Stdlib Set Reference

```yaml doc-meta
doc_id: DOC-REF-938
title: Stdlib Set Reference
status: active
audience: reviewer
owns_tokens:
- appendix_std_set_reference
requires_tokens:
- appendix_spec_lang_builtin_catalog
commands:
- run: ./runners/public/runner_adapter.sh docs-generate-check
  purpose: Verify generated std set reference content stays synchronized.
examples:
- id: EX-APP-STD-SET-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide generated semantic reference for `std.set` symbols.

## Inputs

- `/.artifacts/spec-lang-builtin-catalog.json`

## Outputs

- Generated symbol sections for set namespace.

## Failure Modes

- stale generated marker content
- missing builtin metadata

<!-- GENERATED:START spec_lang_namespace_set -->

## Generated Namespace Chapter: `std.set`

### `std.set.difference`

- Signature: `std.set.difference/2`
- Summary: Evaluates `difference` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.set.difference(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.set.intersection`

- Signature: `std.set.intersection/2`
- Summary: Evaluates `intersection` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.set.intersection(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.set.is_subset`

- Signature: `std.set.is_subset/2`
- Summary: Evaluates `is_subset` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.set.is_subset(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.set.is_superset`

- Signature: `std.set.is_superset/2`
- Summary: Evaluates `is_superset` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.set.is_superset(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.set.set_equals`

- Signature: `std.set.set_equals/2`
- Summary: Evaluates `set_equals` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.set.set_equals(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.set.symmetric_difference`

- Signature: `std.set.symmetric_difference/2`
- Summary: Evaluates `symmetric_difference` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.set.symmetric_difference(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.set.union`

- Signature: `std.set.union/2`
- Summary: Evaluates `union` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.set.union(arg1, arg2)`
  - result: Deterministic result per symbol contract.
<!-- GENERATED:END spec_lang_namespace_set -->
