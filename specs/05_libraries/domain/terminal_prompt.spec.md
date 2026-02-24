```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
harness:
  type: unit.test
  profile: check
  config:
    spec_lang:
      capabilities:
      - ops.terminal
    exports:
    - as: domain.terminal.prompt
      from: assert.function
      path: "/__export__domain.terminal.prompt"
      params:
      - message
      - mode
      required: true
    docs:
      - id: domain.terminal.prompt.doc.1
        summary: Prompt the user in terminal and return raw input.
        audience: implementer
        status: active
        description: |-
          Purpose: Prompt the user with `message` and return the text read from
          stdin without trimming or normalization.

          Inputs:
          - `message` (string, required): Prompt text to display.
          - `mode` (string, optional): `plain` or `rich` display mode. `plain`
            is the default (`default: plain`).

          Returns:
          - Raw input text as a string.

          Errors:
          - Return a direct actionable error when terminal input is unavailable
            (for example non-interactive/no-stdin runs) and no fallback mode is
            available.
            Recovery suggestion should point to interactive terminal execution or
            a non-interactive input source that satisfies the runner contract.
          - `mode` must be `plain` or `rich`; unsupported modes must fail with
            a direct runtime error.
        since: v1
        errors:
        - Invalid input shape or unsupported mode.
        - Non-interactive/no-stdin environments; use interactive terminal mode or
          supported non-interactive input source.
```
