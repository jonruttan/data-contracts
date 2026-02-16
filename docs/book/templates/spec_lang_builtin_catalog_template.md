## Generated Spec-Lang Builtin Catalog

- builtin_count: {{stdlib.summary.builtin_count}}
- namespace_count: {{stdlib.summary.namespace_count}}
- parity_count: {{stdlib.summary.parity_count}}
- all_parity: {{stdlib.summary.all_parity}}
- doc_quality_score: {{stdlib.quality.score}}

| namespace | chapter | symbols |
|---|---|---|
{{#stdlib.chapters}}| `{{key}}` | `{{path}}` | {{symbol_count}} |
{{/stdlib.chapters}}
