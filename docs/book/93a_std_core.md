# Stdlib Core Reference

```yaml doc-meta
doc_id: DOC-REF-931
title: Stdlib Core Reference
status: active
audience: reviewer
owns_tokens:
- appendix_std_core_reference
requires_tokens:
- appendix_spec_lang_builtin_catalog
commands:
- run: ./scripts/runner_adapter.sh docs-generate-check
  purpose: Verify generated std core reference content stays synchronized.
examples:
- id: EX-APP-STD-CORE-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide generated semantic reference for `std.core` and special forms.

## Inputs

- `/.artifacts/spec-lang-builtin-catalog.json`

## Outputs

- Generated symbol sections for core namespace.

## Failure Modes

- stale generated marker content
- missing builtin metadata

<!-- GENERATED:START spec_lang_namespace_core -->

## Generated Namespace Chapter: `std.core` and Special Forms

### `call`

- Signature: `call/var`
- Summary: Spec-lang special form `call` for expression control and binding.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `args` | `list` | true | Operator-defined argument list. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `call(...)`
  - result: Deterministic result per symbol contract.


### `fn`

- Signature: `fn/var`
- Summary: Spec-lang special form `fn` for expression control and binding.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `args` | `list` | true | Operator-defined argument list. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `fn(...)`
  - result: Deterministic result per symbol contract.


### `if`

- Signature: `if/var`
- Summary: Spec-lang special form `if` for expression control and binding.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `args` | `list` | true | Operator-defined argument list. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `if(...)`
  - result: Deterministic result per symbol contract.


### `let`

- Signature: `let/var`
- Summary: Spec-lang special form `let` for expression control and binding.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `args` | `list` | true | Operator-defined argument list. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `let(...)`
  - result: Deterministic result per symbol contract.


### `ops.fs.file.exists`

- Signature: `ops.fs.file.exists/1`
- Summary: Evaluates `exists` with arity 1.
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
  - expr: `ops.fs.file.exists(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.file.ext`

- Signature: `ops.fs.file.ext/1`
- Summary: Evaluates `ext` with arity 1.
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
  - expr: `ops.fs.file.ext(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.file.get`

- Signature: `ops.fs.file.get/3`
- Summary: Evaluates `get` with arity 3.
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
  - expr: `ops.fs.file.get(arg1, arg2, arg3)`
  - result: Deterministic result per symbol contract.


### `ops.fs.file.is_dir`

- Signature: `ops.fs.file.is_dir/1`
- Summary: Evaluates `is_dir` with arity 1.
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
  - expr: `ops.fs.file.is_dir(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.file.is_file`

- Signature: `ops.fs.file.is_file/1`
- Summary: Evaluates `is_file` with arity 1.
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
  - expr: `ops.fs.file.is_file(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.file.name`

- Signature: `ops.fs.file.name/1`
- Summary: Evaluates `name` with arity 1.
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
  - expr: `ops.fs.file.name(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.file.parent`

- Signature: `ops.fs.file.parent/1`
- Summary: Evaluates `parent` with arity 1.
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
  - expr: `ops.fs.file.parent(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.file.path`

- Signature: `ops.fs.file.path/1`
- Summary: Evaluates `path` with arity 1.
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
  - expr: `ops.fs.file.path(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.file.size_bytes`

- Signature: `ops.fs.file.size_bytes/1`
- Summary: Evaluates `size_bytes` with arity 1.
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
  - expr: `ops.fs.file.size_bytes(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.glob.all`

- Signature: `ops.fs.glob.all/2`
- Summary: Evaluates `all` with arity 2.
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
  - expr: `ops.fs.glob.all(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `ops.fs.glob.any`

- Signature: `ops.fs.glob.any/2`
- Summary: Evaluates `any` with arity 2.
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
  - expr: `ops.fs.glob.any(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `ops.fs.glob.filter`

- Signature: `ops.fs.glob.filter/2`
- Summary: Evaluates `filter` with arity 2.
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
  - expr: `ops.fs.glob.filter(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `ops.fs.glob.match`

- Signature: `ops.fs.glob.match/2`
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
  - expr: `ops.fs.glob.match(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `ops.fs.json.get`

- Signature: `ops.fs.json.get/2`
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
  - expr: `ops.fs.json.get(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `ops.fs.json.get_or`

- Signature: `ops.fs.json.get_or/3`
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
  - expr: `ops.fs.json.get_or(arg1, arg2, arg3)`
  - result: Deterministic result per symbol contract.


### `ops.fs.json.has_path`

- Signature: `ops.fs.json.has_path/2`
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
  - expr: `ops.fs.json.has_path(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `ops.fs.json.parse`

- Signature: `ops.fs.json.parse/1`
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
  - expr: `ops.fs.json.parse(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.path.basename`

- Signature: `ops.fs.path.basename/1`
- Summary: Evaluates `basename` with arity 1.
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
  - expr: `ops.fs.path.basename(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.path.change_ext`

- Signature: `ops.fs.path.change_ext/2`
- Summary: Evaluates `change_ext` with arity 2.
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
  - expr: `ops.fs.path.change_ext(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `ops.fs.path.dirname`

- Signature: `ops.fs.path.dirname/1`
- Summary: Evaluates `dirname` with arity 1.
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
  - expr: `ops.fs.path.dirname(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.path.extname`

- Signature: `ops.fs.path.extname/1`
- Summary: Evaluates `extname` with arity 1.
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
  - expr: `ops.fs.path.extname(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.path.has_ext`

- Signature: `ops.fs.path.has_ext/2`
- Summary: Evaluates `has_ext` with arity 2.
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
  - expr: `ops.fs.path.has_ext(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `ops.fs.path.is_abs`

- Signature: `ops.fs.path.is_abs/1`
- Summary: Evaluates `is_abs` with arity 1.
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
  - expr: `ops.fs.path.is_abs(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.path.join`

- Signature: `ops.fs.path.join/2`
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

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `ops.fs.path.join(arg1, arg2)`
  - result: Deterministic result per symbol contract.


### `ops.fs.path.normalize`

- Signature: `ops.fs.path.normalize/1`
- Summary: Evaluates `normalize` with arity 1.
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
  - expr: `ops.fs.path.normalize(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.path.split`

- Signature: `ops.fs.path.split/1`
- Summary: Evaluates `split` with arity 1.
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
  - expr: `ops.fs.path.split(arg1)`
  - result: Deterministic result per symbol contract.


### `ops.fs.path.stem`

- Signature: `ops.fs.path.stem/1`
- Summary: Evaluates `stem` with arity 1.
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
  - expr: `ops.fs.path.stem(arg1)`
  - result: Deterministic result per symbol contract.


### `std.core.subject`

- Signature: `std.core.subject/0`
- Summary: Returns the current assertion subject value.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `std.core.subject`
  - result: Deterministic result per symbol contract.


### `var`

- Signature: `var/var`
- Summary: Spec-lang special form `var` for expression control and binding.
- Since: v1
- Tags: `pure` `deterministic` 
- Parity: python=true, php=true, both=true

#### Parameters

| name | type | required | description |
|---|---|---|---|
| `args` | `list` | true | Operator-defined argument list. |


#### Returns

- Type: `json`
- Description: Deterministic pure return value.

#### Error Conditions

- `schema`: Unknown symbol, arity mismatch, or invalid argument types.


#### Examples

- **Basic usage**
  - expr: `var(...)`
  - result: Deterministic result per symbol contract.
<!-- GENERATED:END spec_lang_namespace_core -->
