# Stdlib Type Reference

```yaml doc-meta
doc_id: DOC-REF-937
title: Stdlib Type Reference
status: active
audience: reviewer
owns_tokens:
- appendix_std_type_reference
requires_tokens:
- appendix_spec_lang_builtin_catalog
commands:
- run: ./runners/public/runner_adapter.sh docs-generate-check
  purpose: Verify generated std type reference content stays synchronized.
examples:
- id: EX-APP-STD-TYPE-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide generated semantic reference for `std.type` symbols.

## Inputs

- `/.artifacts/spec-lang-builtin-catalog.json`

## Outputs

- Generated symbol sections for type namespace.

## Failure Modes

- stale generated marker content
- missing builtin metadata

<!-- GENERATED:START spec_lang_namespace_type -->

## Generated Namespace Chapter: `std.type`

### `std.type.is_array`

- Signature: `std.type.is_array/1`
- Summary: Evaluates `is_array` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.type.is_array(arg1)`
  - result: Deterministic result per symbol contract.


### `std.type.is_bool`

- Signature: `std.type.is_bool/1`
- Summary: Evaluates `is_bool` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.type.is_bool(arg1)`
  - result: Deterministic result per symbol contract.


### `std.type.is_boolean`

- Signature: `std.type.is_boolean/1`
- Summary: Evaluates `is_boolean` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.type.is_boolean(arg1)`
  - result: Deterministic result per symbol contract.


### `std.type.is_dict`

- Signature: `std.type.is_dict/1`
- Summary: Evaluates `is_dict` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.type.is_dict(arg1)`
  - result: Deterministic result per symbol contract.


### `std.type.is_integer`

- Signature: `std.type.is_integer/1`
- Summary: Evaluates `is_integer` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.type.is_integer(arg1)`
  - result: Deterministic result per symbol contract.


### `std.type.is_list`

- Signature: `std.type.is_list/1`
- Summary: Evaluates `is_list` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.type.is_list(arg1)`
  - result: Deterministic result per symbol contract.


### `std.type.is_null`

- Signature: `std.type.is_null/1`
- Summary: Evaluates `is_null` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.type.is_null(arg1)`
  - result: Deterministic result per symbol contract.


### `std.type.is_number`

- Signature: `std.type.is_number/1`
- Summary: Evaluates `is_number` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.type.is_number(arg1)`
  - result: Deterministic result per symbol contract.


### `std.type.is_object`

- Signature: `std.type.is_object/1`
- Summary: Evaluates `is_object` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.type.is_object(arg1)`
  - result: Deterministic result per symbol contract.


### `std.type.is_string`

- Signature: `std.type.is_string/1`
- Summary: Evaluates `is_string` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `bool`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.type.is_string(arg1)`
  - result: Deterministic result per symbol contract.


### `std.type.json_type`

- Signature: `std.type.json_type/2`
- Summary: Evaluates `json_type` with arity 2.
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
  - expr: `std.type.json_type(arg1, arg2)`
  - result: Deterministic result per symbol contract.
<!-- GENERATED:END spec_lang_namespace_type -->
