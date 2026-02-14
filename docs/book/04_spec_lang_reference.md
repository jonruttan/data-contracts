# Chapter 4: Spec-Lang Reference (`evaluate`)

This chapter is the practical reference for the `evaluate` assertion leaf.

## 1) What `evaluate` Is

`evaluate` runs a spec-lang expression against the assertion target subject.
The expression must be YAML list S-expression form.

Example:

```yaml
assert:
  - target: text
    must:
      - evaluate:
          - ["contains", "hello"]
```

Each `evaluate` item is one expression. The expression result is coerced to
boolean for assertion pass/fail.

## 2) Expression Shape

Valid form:

```yaml
['symbol', arg1, arg2, ...]
```

Invalid forms:

- mapping root (`{...}`)
- empty list (`[]`)
- non-string head (`[123, ...]`)

## 3) Core Forms

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
- `any`
- `all`
- `none`
- `var`
- `add`
- `sub`
- `lt`
- `lte`
- `gt`
- `gte`
- `matches`

Control/recursion:

- `if`
- `let`
- `fn`
- `call`

## 4) Common Patterns

Text + boolean composition:

```yaml
- evaluate:
    - ["and",
       ["contains", "WARN"],
       ["not", ["contains", "ERROR"]]]
```

JSON field check (for `target: body_json`):

```yaml
- evaluate:
    - ["and",
       ["has_key", "items"],
       ["eq", ["json_type", ["get", ["subject"], "items"]], true]]
```

Tail recursion (stack-safe by contract):

```yaml
- evaluate:
    - ["let",
       [["loop",
            ["fn",
                ["n", "acc"],
                ["if",
                     ["eq", ["var", "n"], 0],
                     ["var", "acc"],
                     ["call",
                           ["var", "loop"],
                           ["sub", ["var", "n"], 1],
                           ["add", ["var", "acc"], 1]]]]]],
       ["eq", ["call", ["var", "loop"], 1000, 0], 1000]]
```

## 5) Budgets (`harness.spec_lang`)

Optional per-case evaluator limits:

```yaml
harness:
  spec_lang:
    max_steps: 20000
    max_nodes: 20000
    max_literal_bytes: 262144
    timeout_ms: 200
```

Rules:

- all values are integers
- `max_steps`, `max_nodes`, `max_literal_bytes` must be `>= 1`
- `timeout_ms` must be `>= 0` (`0` disables timeout)

## 6) Error Categories

- malformed form / unknown symbol / arity/type issues: `schema`
- expression returns false in `must`: `assertion`
- budget/timeout/execution faults: `runtime`

Typical diagnostics include:

- `case_id=...`
- `assert_path=...`
- `target=...`
- `op=evaluate`

## 7) When To Use `contain` vs `evaluate`

Use `contain` / `regex` when simple string checks are enough.
Use `evaluate` when you need:

- composable boolean logic
- value/JSON-aware checks
- deterministic recursive logic in the spec itself

## 8) Cross-References

- `docs/spec/schema/schema_v1.md`
- `docs/spec/contract/03_assertions.md`
- `docs/spec/contract/03b_spec_lang_v1.md`
- `docs/spec/contract/14_spec_lang_libraries.md`
- `docs/spec/conformance/cases/spec_lang.spec.md`

## 9) Lint + Format

Use the repo tool to keep `evaluate` layout canonical:

```sh
python scripts/evaluate_style.py --check docs/spec
python scripts/evaluate_style.py --write docs/spec
```
