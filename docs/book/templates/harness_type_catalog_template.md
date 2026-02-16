## Generated Harness Type Catalog

- type_profile_count: {{harness.summary.type_profile_count}}
- total_type_field_count: {{harness.summary.total_type_field_count}}
- doc_quality_score: {{harness.quality.score}}

| case_type | field_count | required_top_level | allowed_top_level_extra |
|---|---|---|---|
{{#harness.type_profiles}}| `{{case_type}}` | {{field_count}} | {{required_top_level_md}} | {{allowed_top_level_extra_md}} |
{{/harness.type_profiles}}

### Type Semantics

{{#harness.type_profiles}}#### `{{case_type}}`

- Summary: {{summary}}
- Defaults:
{{#defaults}}  - {{.}}
{{/defaults}}{{^defaults}}  - -
{{/defaults}}
- Failure Modes:
{{#failure_modes}}  - {{.}}
{{/failure_modes}}{{^failure_modes}}  - -
{{/failure_modes}}
- Examples:
{{#examples}}  - `{{snippet}}`
{{/examples}}{{^examples}}  - -
{{/examples}}

{{/harness.type_profiles}}
