# Assertion Contract (v1)

## Tree Model

`contract` uses mapping form:

- `defaults` (optional mapping)
- `steps` (required non-empty list)

Each step has:

- `id` (string)
- `class` (`MUST` | `MAY` | `MUST_NOT`, default `MUST`)
- `imports` (optional mapping)
- `assert` (non-empty expression mapping or list)

Legacy forms are forbidden:

- top-level list `contract: [...]`
- step key `asserts`
- step keys `target` / `on`

## Explicit Import Bindings

Assertions must consume explicitly imported values.

Import binding shape:

- `imports.<name>.from`: `artifact | symbol | literal`
- `imports.<name>.key`: required when `from` is `artifact` or `symbol`
- `imports.<name>.value`: required when `from` is `literal`

Import merge semantics:

- effective imports = `contract.defaults.imports` + `contract.steps[].imports`
- step imports override same-name defaults

`{var: subject}` is valid only when `subject` is imported explicitly.

## Group Semantics

- `MUST`: all assertions in the step must pass
- `MAY`: at least one assertion in the step must pass
- `MUST_NOT`: no assertion in the step may pass

## Governance Artifact Keys

For `type: contract.check` with governance profile, common artifact imports include:

- `text`
- `summary_json`
- `violation_count`
- `meta_json`

Example:

```yaml
contract:
  defaults:
    class: MUST
    imports:
      subject:
        from: artifact
        key: violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```

## Leaf Operators

Runtime decision semantics are evaluate-only through spec-lang mapping AST expressions.

Normative references:

- `specs/contract/03b_spec_lang_v1.md`
- `specs/contract/09_internal_representation.md`
