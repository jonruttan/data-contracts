# Internal Representation Contract (v1)

## Purpose

`spec_runner` decouples external case authoring formats from execution by
compiling cases into a single internal representation before dispatch/runtime
evaluation.

## Internal Model

Each compiled case contains:

- `id`
- `type`
- `title` (optional)
- `doc_path` (source location)
- `harness` (runner-only config mapping)
- `raw_case` (original external mapping for compatibility/tooling)
- `metadata` (expect/requires/assert_health/source)
- `assert_tree` (compiled internal assertion tree)

Internal assertion node forms:

- group node:
  - `op`: `must` | `can` | `cannot`
  - `target`: optional inherited target
  - `children`: child internal nodes
  - `assert_path`: stable path for diagnostics
- predicate leaf:
  - `target`
  - `subject_key` (adapter-provided subject lookup key)
  - `op` (original external op token for diagnostics)
  - `expr` (spec-lang expression)
  - `assert_path`

## External -> Internal Compile Rules

- `contain` -> `["contains", ["subject"], <value>]`
- `regex` -> `["regex_match", ["subject"], <pattern>]`
- `json_type` -> normalized to `["json_type", <subject_expr>, <kind>]`
  - where `<subject_expr>` is either `["subject"]` (already-JSON targets) or
    `["json_parse", ["subject"]]` (text targets)
- `exists` on `stdout_path` -> `subject_key: "stdout_path.exists"` with
  expression `["eq", ["subject"], true]`
- `evaluate` -> pass-through spec-lang expression

List-valued leaf ops compile to conjunction semantics (same as current v1
external behavior).

## Discovery and Codec Rules

Default discovery remains `.spec.md` only.

Opt-in external formats:

- `.spec.yaml` / `.spec.yml`
- `.spec.json`

The compile contract is semantic-lossless:

- case ids must remain stable
- pass/fail/category behavior must remain equivalent
- formatting/comments are not guaranteed to round-trip

## Compatibility Rules

- Canonical authoring for docs/spec fixtures remains `.spec.md`.
- External codecs are adapters; they must not change runtime semantics.
- Non-core custom runners may still receive external-case objects for
  compatibility; core runner types execute compiled internal cases.

## Assertion Execution Invariant

MUST:

- runtime assertion execution MUST evaluate compiled spec-lang predicates.
- external leaf operators (`contain`, `regex`, `json_type`, `exists`,
  `evaluate`) MUST be compiled to spec-lang expression form before execution.
- runners MUST NOT introduce direct ad-hoc leaf-op execution branches that
  bypass the spec-lang evaluator.
- spec-lang evaluator MUST remain pure; side-effectful probes are adapter
  responsibilities that produce normalized subject values.
