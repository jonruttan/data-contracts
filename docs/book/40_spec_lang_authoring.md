# Chapter 40: Spec-Lang Authoring

```yaml doc-meta
doc_id: DOC-REF-140
title: Chapter 40 Spec-Lang Authoring
status: active
audience: author
owns_tokens:
- mapping_ast_authoring_patterns
requires_tokens:
- explicit_assert_imports_v1
commands:
- run: ./scripts/control_plane.sh spec-lang-format --check --cases specs
  purpose: Verify canonical expression formatting.
- run: ./scripts/control_plane.sh spec-lang-lint --cases specs
  purpose: Verify pedantic expression and schema hygiene.
examples:
- id: EX-SPECLANG-AUTH-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide practical patterns for writing readable, deterministic mapping-AST assertions.

## Inputs

- imported symbols from `contract.imports` / `steps[].imports`
- operator set defined by stdlib profile and runtime capabilities

## Outputs

- composable expressions with stable behavior
- reduced duplication via library exports

## Failure Modes

- malformed AST shape (multi-key expression mapping)
- over-nested expressions that obscure intent
- duplicated logic better expressed in shared libraries

## Mapping-AST Rules

- each expression mapping has exactly one operator key
- operator args are list-valued
- literals use `lit` when needed for disambiguation
- variables are explicit (`{var: symbol}`)

## Readability Patterns

- keep small predicates inline
- split complex expressions into staged `std.logic.and` clauses
- prefer library calls for repeated policy logic

Example:

```yaml
assert:
  std.logic.and:
  - std.type.is_dict:
    - {var: summary_json}
  - std.object.has_key:
    - {var: summary_json}
    - passed
  - std.logic.eq:
    - std.object.get:
      - {var: summary_json}
      - passed
    - true
```

## Anti-Patterns

- encoding final decision logic in harness adapters
- mixing prior syntax with canonical forms
- using ambiguous aliases when direct import names are clearer

## Library-Backed Reuse

Use `harness.use` to import shared symbols and call them in assertions.

Normative references:

- `specs/contract/03b_spec_lang_v1.md`
- `specs/contract/14_spec_lang_libraries.md`
- `specs/schema/spec_lang_stdlib_profile_v1.yaml`
