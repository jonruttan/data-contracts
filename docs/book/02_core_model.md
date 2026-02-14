# Chapter 2: Core Model

```yaml doc-meta
doc_id: DOC-REF-003
title: Chapter 2 Core Model
status: active
audience: maintainer
owns_tokens: ["core_case_model", "harness_namespace_rule", "discovery_model"]
requires_tokens: ["must"]
commands:
  - run: "python scripts/run_governance_specs.py"
    purpose: Validate core contract and governance assumptions.
examples:
  - id: EX-COREMODEL-001
    runnable: true
sections_required:
  - "## Purpose"
  - "## Inputs"
  - "## Outputs"
  - "## Failure Modes"
```

The `yaml spec-test` syntax is a case model with strict structure.

## Purpose

Define the stable structural model for executable spec cases.

## Inputs

- markdown docs containing `yaml spec-test` fenced blocks

## Outputs

- validated case model ready for type dispatch and harness execution

## Failure Modes

- missing required keys (`id`, `type`)
- runner keys placed outside `harness:`
- invalid path constraints for `text.file`

## Required Keys

- `id` (string)
- `type` (string)

Typical optional keys:

- `title`
- `assert`
- `harness`
- `assert_health`
- `expect` (for conformance fixtures)
- `requires` (capability metadata)

## Discovery Model

- Runners scan Markdown files matching case-file pattern (default `*.spec.md`).
- They parse fenced blocks tagged with both:
  - `spec-test`
  - `yaml` or `yml`
- Discovery is non-recursive for the provided directory.
- `type` is required.

## Type Model

Core types currently used in this repo:

- `text.file`
- `cli.run`

### `text.file`

- Default subject: containing spec document.
- Optional `path` overrides subject file.
- `path` must be relative and must stay inside contract root.

### `cli.run`

- Executes entrypoint command/function with `argv`.
- Asserts against `stdout`, `stderr`, `stdout_path`, or `stdout_path_text`.
- Runner-specific setup belongs under `harness:`.

## `harness` Namespace Rule

Always put runner-only inputs under `harness:`.

Good:

```yaml
id: BK-CM-001
type: cli.run
harness:
  entrypoint: /bin/echo
```

Bad:

```yaml
id: BK-CM-002
type: cli.run
entrypoint: /bin/echo
```

## Conformance Metadata

Fixture cases can include `expect`:

```yaml
expect:
  portable:
    status: pass
    category: null
  impl:
    php:
      status: skip
      category: null
```

## Capability Metadata

Use `requires` to express feature prerequisites:

```yaml
requires:
  capabilities: ["cli.run"]
  when_missing: skip
```

## Checklist

- `id` and `type` present.
- Type-specific fields are valid for that type.
- Runner-only keys only under `harness:`.
- If using `path`, it is relative and safe.
- If using `expect`, include `expect.portable.status`.
- If using feature-gated behavior, declare `requires.capabilities`.
