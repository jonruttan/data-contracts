## Generated Spec-Lang Builtin Catalog

- builtin_count: {{stdlib.summary.builtin_count}}
- parity_count: {{stdlib.summary.parity_count}}
- all_parity: {{stdlib.summary.all_parity}}

| symbol | arity | category | python | php | parity |
|---|---|---|---|---|---|
{{#stdlib.builtins}}| `{{symbol}}` | {{arity}} | `{{category}}` | {{python_supported}} | {{php_supported}} | {{parity}} |
{{/stdlib.builtins}}
