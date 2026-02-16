## Generated Runner API Catalog

- command_count: {{runner.summary.command_count}}
- python_command_count: {{runner.summary.python_command_count}}
- rust_command_count: {{runner.summary.rust_command_count}}
- parity_command_count: {{runner.summary.parity_command_count}}
- all_commands_parity: {{runner.summary.all_commands_parity}}

| command | python | rust | parity |
|---|---|---|---|
{{#runner.commands}}| `{{command}}` | {{python_supported}} | {{rust_supported}} | {{parity}} |
{{/runner.commands}}
