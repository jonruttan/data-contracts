## Generated Runner API Catalog

- command_count: {{runner.summary.command_count}}
- python_command_count: {{runner.summary.python_command_count}}
- rust_command_count: {{runner.summary.rust_command_count}}
- parity_command_count: {{runner.summary.parity_command_count}}
- all_commands_parity: {{runner.summary.all_commands_parity}}
- doc_quality_score: {{runner.quality.score}}

| command | group | python | rust | parity |
|---|---|---|---|---|
{{#runner.commands}}| `{{command}}` | `{{group}}` | {{python_supported}} | {{rust_supported}} | {{parity}} |
{{/runner.commands}}

### Command Semantics

{{#runner.commands}}#### `{{command}}`

- Summary: {{summary}}
- Details: {{details}}
- Defaults:
{{#defaults}}  - `{{name}}={{value}}`: {{description}}
{{/defaults}}{{^defaults}}  - -
{{/defaults}}
- Failure Modes:
{{#failure_modes}}  - {{.}}
{{/failure_modes}}{{^failure_modes}}  - -
{{/failure_modes}}
- Examples:
{{#examples}}  - `{{command}}`: {{description}}
{{/examples}}{{^examples}}  - -
{{/examples}}

{{/runner.commands}}
