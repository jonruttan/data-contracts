# Appendix: Cheatsheet

## Minimal `text.file`

```yaml
id: CHEAT-001
type: text.file
assert:
  - target: text
    must:
      - contain: ["hello"]
```

## Minimal `cli.run`

```yaml
id: CHEAT-002
type: cli.run
argv: ["hello"]
exit_code: 0
harness:
  entrypoint: /bin/echo
assert:
  - target: stdout
    must:
      - contain: ["hello"]
```

## Minimal `evaluate`

```yaml
id: CHEAT-003
type: text.file
assert:
  - target: text
    must:
      - evaluate:
          - ["contains", "CHEAT-003"]
```

## Group Semantics

- `must`: AND
- `can`: OR
- `cannot`: NONE

## Frequent Schema Rules

- `id` and `type` required
- runner-only keys must be under `harness:`
- operator values are lists
- leaf nodes do not carry `target`
- `evaluate` expression roots are YAML lists (`["symbol", ...]`)

## Common Error -> Fix

- `unsupported harness key(s)` -> move/rename unsupported keys
- `text.file path must be relative` -> remove absolute path
- `text.file path escapes contract root` -> use safe in-root relative path
- `unsupported op` -> use canonical operators
- `assert_health.mode must be one of` -> use `ignore`, `warn`, or `error`
