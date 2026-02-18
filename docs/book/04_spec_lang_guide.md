# Chapter 4: Spec-Lang Guide (Learn By Composition)

```yaml doc-meta
doc_id: DOC-REF-005
title: Chapter 4 Spec-Lang Guide
status: active
audience: author
owns_tokens:
- spec_lang_guide_patterns
- spec_lang_debug_patterns
requires_tokens:
- must
commands:
- run: ./scripts/runner_adapter.sh normalize-check
  purpose: Validate canonical spec-lang formatting and normalization.
examples:
- id: EX-SPECLANG-GUIDE-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide practical authoring patterns for spec-lang `evaluate` expressions.

## Inputs

- assertion subjects (`text`, JSON targets, governance summaries)
- mapping-AST expression nodes
- executable symbol reuse via chain-loaded library symbols (`harness.chain`)

## Outputs

- readable, reusable, and deterministic policy/assertion logic

## Failure Modes

- over-inline expressions that reduce readability
- duplicated expression fragments instead of shared library calls
- type-shape assumptions that do not match target subject profiles

## Mental Model

- Keep extractors/adapters focused on producing deterministic JSON subject data.
- Keep decisions in `evaluate` using pure spec-lang expressions.
- Prefer library-backed predicates for repeated logic.

## Common Authoring Patterns

Use staged boolean guards:

```yaml
- evaluate:
  - std.logic.and:
    - std.type.is_dict:
      - var: subject
    - std.object.has_key:
      - var: subject
      - violations
    - std.logic.eq:
      - std.collection.count:
        - std.object.get:
          - var: subject
          - violations
      - 0
```

Use `let` for intermediate values when expressions repeat.

Use `fn` + `call` for local composable logic.

## Anti-Patterns

- Writing deep expression trees as dense inline flow nodes.
- Encoding decision logic in adapter scripts when the value is derivable in spec-lang.
- Repeating the same policy expression across many cases without library extraction.

## Library Usage Patterns

Load shared libraries in harness and call exported symbols:

```yaml
harness:
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
evaluate:
- call:
  - var: policy.pass_when_no_violations
  - var: subject
```

## Debugging Evaluate Expressions

1. Validate shape first: run `normalize-check`.
2. Confirm subject shape using assertion targets (for example `summary_json`).
3. Reduce expression to minimal failing predicate, then expand.
4. Move stable repeated logic into library defines.

## Cross-References

- `/docs/book/03_assertions.md`
- `/docs/book/07_spec_lang_reference.md`
- `/docs/spec/contract/03b_spec_lang_v1.md`
- `/docs/spec/libraries/`
