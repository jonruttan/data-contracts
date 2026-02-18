# Stdlib String Reference

```yaml doc-meta
doc_id: DOC-REF-934
title: Stdlib String Reference
status: active
audience: reviewer
owns_tokens:
- appendix_std_string_reference
requires_tokens:
- appendix_spec_lang_builtin_catalog
commands:
- run: ./runners/public/runner_adapter.sh docs-generate-check
  purpose: Verify generated std string reference content stays synchronized.
examples:
- id: EX-APP-STD-STRING-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide generated semantic reference for `std.string` symbols.

## Inputs

- `/.artifacts/spec-lang-builtin-catalog.json`

## Outputs

- Generated symbol sections for string namespace.

## Failure Modes

- stale generated marker content
- missing builtin metadata

<!-- GENERATED:START spec_lang_namespace_string -->

## Generated Namespace Chapter: `std.string`

### `std.string.contains`

- Signature: `std.string.contains/2`
- Summary: Evaluates `contains` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `string`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.string.contains(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.string.ends_with`

- Signature: `std.string.ends_with/2`
- Summary: Evaluates `ends_with` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `string`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.string.ends_with(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.string.join`

- Signature: `std.string.join/2`
- Summary: Evaluates `join` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `string`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.string.join(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.string.lower`

- Signature: `std.string.lower/1`
- Summary: Evaluates `lower` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `string`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.string.lower(arg1)`
  - result: Deterministic result per symbol contract.


### `std.string.matches`

- Signature: `std.string.matches/2`
- Summary: Evaluates `matches` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `string`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.string.matches(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.string.matches_all`

- Signature: `std.string.matches_all/2`
- Summary: Evaluates `matches_all` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `string`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.string.matches_all(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.string.pad_left`

- Signature: `std.string.pad_left/3`
- Summary: Evaluates `pad_left` with arity 3.
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

- Type: `string`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.string.pad_left(arg1, arg2, arg3)`
  - result: Deterministic result per symbol contract.


### `std.string.pad_right`

- Signature: `std.string.pad_right/3`
- Summary: Evaluates `pad_right` with arity 3.
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

- Type: `string`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.string.pad_right(arg1, arg2, arg3)`
  - result: Deterministic result per symbol contract.


### `std.string.regex_match`

- Signature: `std.string.regex_match/2`
- Summary: Evaluates `regex_match` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `string`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.string.regex_match(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.string.replace`

- Signature: `std.string.replace/3`
- Summary: Evaluates `replace` with arity 3.
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

- Type: `string`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.string.replace(arg1, arg2, arg3)`
  - result: Deterministic result per symbol contract.


### `std.string.split`

- Signature: `std.string.split/2`
- Summary: Evaluates `split` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `string`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.string.split(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.string.starts_with`

- Signature: `std.string.starts_with/2`
- Summary: Evaluates `starts_with` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `string`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.string.starts_with(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.string.trim`

- Signature: `std.string.trim/1`
- Summary: Evaluates `trim` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `string`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.string.trim(arg1)`
  - result: Deterministic result per symbol contract.


### `std.string.upper`

- Signature: `std.string.upper/1`
- Summary: Evaluates `upper` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `string`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.string.upper(arg1)`
  - result: Deterministic result per symbol contract.
<!-- GENERATED:END spec_lang_namespace_string -->
