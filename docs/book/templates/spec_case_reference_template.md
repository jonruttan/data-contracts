## Generated Spec Case Reference

- case_count: {{catalog.summary.case_count}}
- type_count: {{catalog.summary.type_count}}
- domain_count: {{catalog.summary.domain_count}}
- source_root: `{{catalog.summary.source_root}}`

{{#catalog.domains}}
### Domain `{{domain}}` {#{{anchor}}}

- case_count: {{case_count}}
- types:
{{#types}}
  - `{{.}}`
{{/types}}

{{/catalog.domains}}

## Cases

{{#catalog.cases}}
### `{{case_id}}` {#{{anchor}}}

- Domain: `{{domain}}`
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


{{/catalog.cases}}
