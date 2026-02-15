# Spec-Lang v1 Contract

## Scope

`spec-lang` is a pure, deterministic expression DSL used only through the
assertion leaf operator `evaluate`.

Expression encoding is YAML list S-expression form:

```yaml
- fn
- arg1
- arg2
```

No string parser and no implementation-defined extension hooks are part of v1.

Purity requirement:

- Evaluation MUST remain pure and deterministic.
- Evaluation MUST NOT perform filesystem, network, process, clock, random, or
  environment side effects.
- Implementations MUST perform side effects in adapters/harnesses and pass
  normalized subjects into spec-lang.

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
- `count`
- `first`
- `rest`
- `trim`
- `lower`
- `upper`
- `split`
- `join`
- `map`
- `filter`
- `reject`
- `find`
- `reduce`
- `partition`
- `group_by`
- `uniq_by`
- `flatten`
- `concat`
- `append`
- `prepend`
- `take`
- `drop`
- `any`
- `all`
- `none`
- `sum`
- `min`
- `max`
- `sort_by`
- `pluck`
- `distinct`
- `is_empty`
- `coalesce`
- `matches_all`
- `var`
- `add`
- `sub`
- `json_parse`
- `regex_match`
- `matches`
- `lt`
- `lte`
- `gt`
- `gte`
- `equals`
- `includes`
- `union`
- `intersection`
- `difference`
- `symmetric_difference`
- `is_subset`
- `is_superset`
- `set_equals`

Recursion/control:

- `let`
- `fn`
- `call`
- `if`

## Equality + Set Algebra Semantics

- `equals` uses deep structural equality:
  - scalars compare by strict type+value
  - lists compare by length + ordered pairwise equality
  - maps compare by key-set equality + per-key value equality
- set operators (`union`, `intersection`, `difference`,
  `symmetric_difference`) require list inputs.
- set outputs are deterministic and preserve stable left-first encounter order.
- `includes` performs list membership using deep equality.
- `set_equals` compares de-duplicated deep-equality sets (order-insensitive).
- `is_subset` / `is_superset` apply the same de-duplicated deep-equality model.

## Currying Contract

- Builtins MUST support automatic currying by declared arity.
- Supplying fewer args than arity MUST return a callable builtin function value.
- Supplying exactly arity args MUST evaluate the builtin.
- Supplying extra args MUST:
  - evaluate first arity args
  - apply remaining args only if the intermediate result is callable
  - otherwise fail as `schema` with deterministic over-application diagnostics
- Function values MUST be usable via `call` and as inputs to collection forms
  (for example `map`, `filter`, `reduce`).

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

Library configuration (optional):

```yaml
harness:
  spec_lang:
    library_paths:
    - docs/spec/libraries/common.spec.md
    exports:
    - is_portable_case
```

Library contract details:

- `docs/spec/contract/14_spec_lang_libraries.md`

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
