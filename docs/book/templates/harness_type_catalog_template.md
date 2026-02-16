## Generated Harness Type Catalog

- type_profile_count: {{harness.summary.type_profile_count}}
- total_type_field_count: {{harness.summary.total_type_field_count}}

| case_type | field_count | required_top_level | allowed_top_level_extra |
|---|---|---|---|
{{#harness.type_profiles}}| `{{case_type}}` | {{field_count}} | {{required_top_level_md}} | {{allowed_top_level_extra_md}} |
{{/harness.type_profiles}}
