# Stdlib JSON / Schema / Fn / Null Reference

```yaml doc-meta
doc_id: DOC-REF-939
title: Stdlib JSON Schema Fn Null Reference
status: active
audience: reviewer
owns_tokens:
- appendix_std_json_schema_fn_null_reference
requires_tokens:
- appendix_spec_lang_builtin_catalog
commands:
- run: ./scripts/runner_adapter.sh docs-generate-check
  purpose: Verify generated std json/schema/fn/null reference content stays synchronized.
examples:
- id: EX-APP-STD-JSFN-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide generated semantic reference for `std.json`, `std.schema`, `std.fn`, and `std.null` symbols.

## Inputs

- `/.artifacts/spec-lang-builtin-catalog.json`

## Outputs

- Generated symbol sections for grouped namespaces.

## Failure Modes

- stale generated marker content
- missing builtin metadata

<!-- GENERATED:START spec_lang_namespace_json_schema_fn_null -->

## Generated Namespace Chapter: `std.json`, `std.schema`, `std.fn`, `std.null`

### `std.fn.always`

- Signature: `std.fn.always/2`
- Summary: Evaluates `always` with arity 2.
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
  - expr: `std.fn.always(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.fn.compose`

- Signature: `std.fn.compose/3`
- Summary: Evaluates `compose` with arity 3.
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
  - expr: `std.fn.compose(arg1, arg2, arg3)`
  - result: Deterministic result per symbol contract.


### `std.fn.identity`

- Signature: `std.fn.identity/1`
- Summary: Evaluates `identity` with arity 1.
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
  - expr: `std.fn.identity(arg1)`
  - result: Deterministic result per symbol contract.


### `std.fn.pipe`

- Signature: `std.fn.pipe/3`
- Summary: Evaluates `pipe` with arity 3.
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
  - expr: `std.fn.pipe(arg1, arg2, arg3)`
  - result: Deterministic result per symbol contract.


### `std.json.parse`

- Signature: `std.json.parse/1`
- Summary: Evaluates `parse` with arity 1.
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
  - expr: `std.json.parse(arg1)`
  - result: Deterministic result per symbol contract.


### `std.json.stringify`

- Signature: `std.json.stringify/1`
- Summary: Evaluates `stringify` with arity 1.
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
  - expr: `std.json.stringify(arg1)`
  - result: Deterministic result per symbol contract.


### `std.null.coalesce`

- Signature: `std.null.coalesce/2`
- Summary: Evaluates `coalesce` with arity 2.
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
  - expr: `std.null.coalesce(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.null.default_to`

- Signature: `std.null.default_to/2`
- Summary: Evaluates `default_to` with arity 2.
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
  - expr: `std.null.default_to(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.schema.errors`

- Signature: `std.schema.errors/2`
- Summary: Evaluates `errors` with arity 2.
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
  - expr: `std.schema.errors(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.schema.match`

- Signature: `std.schema.match/2`
- Summary: Evaluates `match` with arity 2.
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
  - expr: `std.schema.match(arg1, arg2)`
  - result: Deterministic result per symbol contract.
<!-- GENERATED:END spec_lang_namespace_json_schema_fn_null -->
