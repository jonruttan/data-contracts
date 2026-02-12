# Conformance Contract (v1)

Implementations are conformant when equivalent fixture sets produce equivalent:

- pass/fail status per case id
- failure category per case id

Stack traces and language-specific exception classes need not match.

## Expected Outcomes DSL

Conformance cases define expected outcomes directly in case records using:

- `expect.portable`: shared expectations for all implementations
- `expect.impl.<name>`: implementation-specific overrides (for example
  `python`, `php`)

Expected keys:

- `status`: `pass`, `fail`, or `skip`
- `category`: `schema` / `assertion` / `runtime` / `null`
- `message_tokens`: optional list of tokens expected in failure messages

Resolution order:

1. Start from `expect.portable`.
2. If `expect.impl.<implementation>` exists, overlay its keys.

`expect` is required for conformance fixture cases.

## Capability Requirements

Cases may declare capability requirements under `requires`:

- `capabilities`: list of required capability strings
- `when_missing`: `skip` or `fail` (default `fail`)
- capability names are implementation-defined strings (for example `cli.run`)

Execution behavior:

- if all required capabilities are present: evaluate the case normally
- if required capabilities are missing and `when_missing=skip`: result is `skip`
- if required capabilities are missing and `when_missing=fail`: result is `fail`
  with category `runtime`
