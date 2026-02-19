## Generated Spec Case Reference

- case_count: {{catalog.summary.case_count}}
- type_count: {{catalog.summary.type_count}}
- source_root: `{{catalog.summary.source_root}}`

{{#catalog.types}}
### Type `{{type}}` {#{{anchor}}}

- case_count: {{case_count}}

{{/catalog.types}}

## Cases

{{#catalog.cases}}
### `{{case_id}}` {#{{anchor}}}

- Type: `{{type}}`
- Title: {{title}}
- Audience: `{{audience}}`
- Since: `{{since}}`
- Source: `{{source_doc}}#{{case_id}}`

#### Summary

{{summary}}

#### Description

{{description}}

{{#tags}}
- Tag: `{{.}}`
{{/tags}}

{{#see_also}}
- See Also: `{{.}}`
{{/see_also}}

{{#deprecated}}
- Deprecated: `true`
- Replacement: `{{replacement}}`
- Reason: {{reason}}
{{/deprecated}}

{{/catalog.cases}}
