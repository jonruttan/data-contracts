# Stdlib Math Reference

```yaml doc-meta
doc_id: DOC-REF-933
title: Stdlib Math Reference
status: active
audience: reviewer
owns_tokens:
- appendix_std_math_reference
requires_tokens:
- appendix_spec_lang_builtin_catalog
commands:
- run: ./runners/public/runner_adapter.sh docs-generate-check
  purpose: Verify generated std math reference content stays synchronized.
examples:
- id: EX-APP-STD-MATH-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide generated semantic reference for `std.math` symbols.

## Inputs

- `/.artifacts/spec-lang-builtin-catalog.json`

## Outputs

- Generated symbol sections for math namespace.

## Failure Modes

- stale generated marker content
- missing builtin metadata

<!-- GENERATED:START spec_lang_namespace_math -->

## Generated Namespace Chapter: `std.math`

### `std.math.abs`

- Signature: `std.math.abs/1`
- Summary: Evaluates `abs` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.abs(arg1)`
  - result: Deterministic result per symbol contract.


### `std.math.add`

- Signature: `std.math.add/2`
- Summary: Evaluates `add` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.add(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.math.ceil`

- Signature: `std.math.ceil/1`
- Summary: Evaluates `ceil` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.ceil(arg1)`
  - result: Deterministic result per symbol contract.


### `std.math.clamp`

- Signature: `std.math.clamp/3`
- Summary: Evaluates `clamp` with arity 3.
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

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.clamp(arg1, arg2, arg3)`
  - result: Deterministic result per symbol contract.


### `std.math.dec`

- Signature: `std.math.dec/1`
- Summary: Evaluates `dec` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.dec(arg1)`
  - result: Deterministic result per symbol contract.


### `std.math.div`

- Signature: `std.math.div/2`
- Summary: Evaluates `div` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.div(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.math.floor`

- Signature: `std.math.floor/1`
- Summary: Evaluates `floor` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.floor(arg1)`
  - result: Deterministic result per symbol contract.


### `std.math.inc`

- Signature: `std.math.inc/1`
- Summary: Evaluates `inc` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.inc(arg1)`
  - result: Deterministic result per symbol contract.


### `std.math.max`

- Signature: `std.math.max/1`
- Summary: Evaluates `max` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.max(arg1)`
  - result: Deterministic result per symbol contract.


### `std.math.min`

- Signature: `std.math.min/1`
- Summary: Evaluates `min` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.min(arg1)`
  - result: Deterministic result per symbol contract.


### `std.math.mod`

- Signature: `std.math.mod/2`
- Summary: Evaluates `mod` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.mod(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.math.mul`

- Signature: `std.math.mul/2`
- Summary: Evaluates `mul` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.mul(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.math.negate`

- Signature: `std.math.negate/1`
- Summary: Evaluates `negate` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.negate(arg1)`
  - result: Deterministic result per symbol contract.


### `std.math.pow`

- Signature: `std.math.pow/2`
- Summary: Evaluates `pow` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.pow(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.math.range`

- Signature: `std.math.range/2`
- Summary: Evaluates `range` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.range(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.math.round`

- Signature: `std.math.round/1`
- Summary: Evaluates `round` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.round(arg1)`
  - result: Deterministic result per symbol contract.


### `std.math.sub`

- Signature: `std.math.sub/2`
- Summary: Evaluates `sub` with arity 2.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |
| `arg2` | `json` | true | Positional argument 2. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.sub(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `std.math.sum`

- Signature: `std.math.sum/1`
- Summary: Evaluates `sum` with arity 1.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `arg1` | `json` | true | Positional argument 1. |


#### Returns

- Type: `number`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.math.sum(arg1)`
  - result: Deterministic result per symbol contract.
<!-- GENERATED:END spec_lang_namespace_math -->
