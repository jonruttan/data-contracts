# Spec-Lang v1 Contract

## Scope

`spec-lang` is a pure, deterministic expression DSL used only through the
assertion leaf operator `evaluate`.

Expression encoding is YAML list S-expression form:

```yaml
["fn", arg1, arg2]
```

No string parser and no implementation-defined extension hooks are part of v1.

## Core Forms

Boolean:

- `and`
- `or`
- `not`

Value/text:

- `contains`
- `starts_with`
- `ends_with`
- `eq`
- `neq`
- `in`

JSON/value:

- `json_type`
- `has_key`
- `get`

Utility:

- `subject`
- `len`
- `trim`
- `lower`
- `upper`
- `var`
- `add`
- `sub`
- `json_parse`
- `path_exists`
- `regex_match`

Recursion/control:

- `let`
- `fn`
- `call`
- `if`

## Tail Position and TCO

Tail positions:

- the selected branch expression of `if`
- the body expression of `let`
- the body of `fn` when entered by `call`

Contract requirements:

- Evaluators MUST implement proper tail-call optimization for tail-position
  `call`.
- Tail-recursive programs MUST NOT fail due to host call-stack depth.
- Evaluators MUST execute with an explicit iterative state/trampoline model
  rather than host recursion for tail calls.

Non-tail recursion is not guaranteed stack-safe and may fail by evaluator
budget limits.

## Evaluator Budget Model

Evaluators MUST enforce all budgets:

- `max_steps`
- `max_nodes`
- `max_literal_bytes`
- optional `timeout_ms`

Budget failures are runtime failures and MUST identify the exceeded budget key:

- `steps`
- `nodes`
- `literal_size`
- `timeout`

## Error Semantics

- malformed expression, unknown symbol, arity/type error: `schema`
- expression evaluates false under `must`: `assertion`
- evaluator timeout/budget/internal execution fault: `runtime`

Diagnostics SHOULD include:

- case id
- assertion path
- failing symbol or form
- budget exceeded reason when applicable

## Harness Configuration

Runners MAY accept evaluator budget overrides in harness config:

```yaml
harness:
  spec_lang:
    max_steps: 20000
    max_nodes: 20000
    max_literal_bytes: 262144
    timeout_ms: 200
```

All values are integers; `timeout_ms` MAY be `0` to disable timeout enforcement.

## Canonical Authoring Format

For readability and deterministic diffs, implementations in this repo standardize
`evaluate` expression formatting to:

- one expression item per `evaluate` list entry
- flow-sequence S-expressions (`["symbol", ...]`)
- quoted string atoms in expressions (single-quote style in this repo tooling)
- wrapped lines with closing brackets preserved in flow style

Tooling:

- lint: `python scripts/evaluate_style.py --check docs/spec`
- format: `python scripts/evaluate_style.py --write docs/spec`
