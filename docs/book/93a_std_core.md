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
