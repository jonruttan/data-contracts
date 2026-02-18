# Stdlib Object Reference

```yaml doc-meta
doc_id: DOC-REF-936
title: Stdlib Object Reference
status: active
audience: reviewer
owns_tokens:
- appendix_std_object_reference
requires_tokens:
- appendix_spec_lang_builtin_catalog
commands:
- run: ./runners/public/runner_adapter.sh docs-generate-check
  purpose: Verify generated std object reference content stays synchronized.
examples:
- id: EX-APP-STD-OBJECT-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide generated semantic reference for `std.object` symbols.

## Inputs

- `/.artifacts/spec-lang-builtin-catalog.json`

## Outputs

- Generated symbol sections for object namespace.

## Failure Modes

- stale generated marker content
- missing builtin metadata

<!-- GENERATED:START spec_lang_namespace_object -->

## Generated Namespace Chapter: `std.object`

### `std.object.assoc`

- Signature: `std.object.assoc/3`
- Summary: Evaluates `assoc` with arity 3.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |
| `arg3` | `json` | true | Positional argument 3. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.assoc(arg1, arg2, arg3)`
  - result: Deterministic result per symbol contract.


### `std.object.dissoc`

- Signature: `std.object.dissoc/2`
- Summary: Evaluates `dissoc` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.dissoc(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.object.entries`

- Signature: `std.object.entries/1`
- Summary: Evaluates `entries` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.entries(arg1)`
  - result: Deterministic result per symbol contract.


### `std.object.get`

- Signature: `std.object.get/2`
- Summary: Evaluates `get` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.get(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.object.get_in`

- Signature: `std.object.get_in/2`
- Summary: Evaluates `get_in` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.get_in(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.object.get_or`

- Signature: `std.object.get_or/3`
- Summary: Evaluates `get_or` with arity 3.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |
| `arg3` | `json` | true | Positional argument 3. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.get_or(arg1, arg2, arg3)`
  - result: Deterministic result per symbol contract.


### `std.object.has_key`

- Signature: `std.object.has_key/2`
- Summary: Evaluates `has_key` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.has_key(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.object.has_path`

- Signature: `std.object.has_path/2`
- Summary: Evaluates `has_path` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.has_path(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.object.keys`

- Signature: `std.object.keys/1`
- Summary: Evaluates `keys` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.keys(arg1)`
  - result: Deterministic result per symbol contract.


### `std.object.keys_exact`

- Signature: `std.object.keys_exact/2`
- Summary: Evaluates `keys_exact` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.keys_exact(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.object.keys_exclude`

- Signature: `std.object.keys_exclude/2`
- Summary: Evaluates `keys_exclude` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.keys_exclude(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.object.keys_include`

- Signature: `std.object.keys_include/2`
- Summary: Evaluates `keys_include` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.keys_include(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.object.merge`

- Signature: `std.object.merge/2`
- Summary: Evaluates `merge` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.merge(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.object.merge_deep`

- Signature: `std.object.merge_deep/2`
- Summary: Evaluates `merge_deep` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.merge_deep(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.object.omit`

- Signature: `std.object.omit/2`
- Summary: Evaluates `omit` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.omit(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.object.pick`

- Signature: `std.object.pick/2`
- Summary: Evaluates `pick` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.pick(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.object.pluck`

- Signature: `std.object.pluck/2`
- Summary: Evaluates `pluck` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.pluck(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.object.prop_eq`

- Signature: `std.object.prop_eq/3`
- Summary: Evaluates `prop_eq` with arity 3.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |
| `arg3` | `json` | true | Positional argument 3. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.prop_eq(arg1, arg2, arg3)`
  - result: Deterministic result per symbol contract.


### `std.object.values`

- Signature: `std.object.values/1`
- Summary: Evaluates `values` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.values(arg1)`
  - result: Deterministic result per symbol contract.


### `std.object.where`

- Signature: `std.object.where/2`
- Summary: Evaluates `where` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.object.where(arg1, arg2)`
  - result: Deterministic result per symbol contract.
<!-- GENERATED:END spec_lang_namespace_object -->
