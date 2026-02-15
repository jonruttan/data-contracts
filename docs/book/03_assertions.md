# Chapter 3: Assertions

```yaml doc-meta
doc_id: DOC-REF-004
title: Chapter 3 Assertions
status: active
audience: author
owns_tokens: ["must", "can", "cannot", "evaluate"]
requires_tokens: ["spec-lang"]
commands:
  - run: "python scripts/evaluate_style.py --check docs/spec"
    purpose: Validate canonical evaluate formatting.
examples:
  - id: EX-ASSERTIONS-001
    runnable: true
sections_required:
  - "## Purpose"
  - "## Inputs"
  - "## Outputs"
  - "## Failure Modes"
```

Assertions are an expression tree with explicit group semantics.

## Purpose

Define assertion-tree semantics and canonical leaf operator usage.

## Inputs

- `assert` trees with group nodes and leaf operators

## Outputs

- deterministic assertion evaluation semantics across runners

## Failure Modes

- leaf `target` misuse
- non-list operator values
- invalid `evaluate` expression roots

## Tree Shape

`assert` supports:

- list: implicit AND over children
- group mapping: exactly one of `must` / `can` / `cannot`
- leaf mapping: operator lists

## Group Semantics

- `must`: all children must pass
- `can`: at least one child must pass
- `cannot`: no child may pass

## Targets

Target is set on a group node and inherited by leaves.

Valid:

```yaml
assert:
  - target: stdout
    must:
      - contain: ["ok"]
```

Invalid:

```yaml
assert:
  - must:
      - target: stdout
        contain: ["ok"]
```

Why invalid:

- leaf nodes must not include `target`.

## Operators

Canonical operators:

- `contain`
- `regex`
- `json_type`
- `exists`
- `evaluate`

All operator values are lists.

Authoring policy:

- Use sugar operators by default (`contain`, `regex`, `json_type`, `exists`).
- Use `evaluate` only when case intent requires expression composition or
  value/collection logic that sugar cannot express clearly.
- `evaluate` includes deep-equality set algebra and collection transforms,
  with automatic builtin currying by arity for function-style composition.

`evaluate` uses spec-lang v1 YAML list S-expressions:

```yaml
assert:
  - target: text
    must:
      - evaluate:
          - ["and",
             ["contains", "version"],
             ["starts_with", ["subject"], "#"]]
```

Reference:

- `docs/book/04_spec_lang_reference.md`
- `docs/spec/contract/03b_spec_lang_v1.md`

Tail-recursive example:

```yaml
assert:
  - target: text
    must:
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
             ["eq", ["call", ["var", "loop"], 100, 0], 100]]
```

## Example: Mixed Assertions

```yaml
assert:
  - target: stderr
    cannot:
      - contain: ["ERROR:"]
  - target: stdout
    can:
      - json_type: ["list"]
      - contain: ["[]"]
```

## `stdout_path` / `stdout_path_text`

For `cli.run`:

- `stdout_path` uses first non-empty line of stdout as a path.
- Adapter code resolves existence; spec-lang receives a normalized boolean.
- `stdout_path.exists` only supports `true` (or `null`) values.
- `stdout_path_text` reads that file content and applies text assertions.

## Assertion Health

`assert_health.mode` controls diagnostics:

- `ignore`
- `warn`
- `error`

Common diagnostic examples:

- `AH001`: empty `contain` (always true)
- `AH002`: always-true regex
- `AH003`: duplicate operator values
- `AH004`: redundant sibling branches
- `AH005`: non-portable regex constructs

## Troubleshooting Patterns

Symptom: `unsupported op: ...`

- Cause: non-canonical operator key.
- Fix: use one of the supported operators.

Symptom: `assertion leaf requires inherited target`

- Cause: leaf exists without parent target.
- Fix: move `target` to the containing group node.

Symptom: `assert group must include exactly one key`

- Cause: multiple group keys in one node.
- Fix: split into separate group nodes.

## Checklist

- Every leaf has an inherited target.
- Every operator value is a list.
- Group nodes use exactly one of `must/can/cannot`.
- Sugar is the default authoring form unless `evaluate` is required.
- Portable regex subset is used when cross-runtime parity matters.
