## Generated Spec Schema Field Catalog

- top_level_field_count: {{schema.summary.top_level_field_count}}
- type_profile_count: {{schema.summary.type_profile_count}}
- total_type_field_count: {{schema.summary.total_type_field_count}}

### Top-Level Fields

| key | type | required | since |
|---|---|---|---|
{{#schema.top_level_fields}}| `{{key}}` | `{{type}}` | {{required}} | `{{since}}` |
{{/schema.top_level_fields}}

### Type Profiles

| case_type | field_count | required_top_level |
|---|---|---|
{{#schema.type_profiles}}| `{{case_type}}` | {{field_count}} | {{required_top_level_md}} |
{{/schema.type_profiles}}
