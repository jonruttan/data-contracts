# Spec Case Shape Reference

This page is machine-generated from the schema registry type and field profiles.

<!-- GENERATED:START spec_schema_field_catalog -->

## Generated Spec Schema Field Catalog

- top_level_field_count: 10
- type_profile_count: 6
- total_type_field_count: 7

### Top-Level Fields

| key | type | required | since |
|---|---|---|---|
| `assert` | `list` | false | `v1` |
| `assert_health` | `mapping` | false | `v1` |
| `expect` | `mapping` | false | `v1` |
| `harness` | `mapping` | false | `v1` |
| `id` | `string` | true | `v1` |
| `path` | `string` | false | `v1` |
| `purpose` | `string` | false | `v1` |
| `requires` | `mapping` | false | `v1` |
| `title` | `string` | false | `v1` |
| `type` | `string` | true | `v1` |

### Type Profiles

| case_type | field_count | required_top_level |
|---|---|---|
| `api.http` | 1 | `request` |
| `cli.run` | 2 | - |
| `governance.check` | 1 | `check` |
| `orchestration.run` | 0 | - |
| `spec_lang.library` | 2 | `definitions` |
| `text.file` | 1 | - |
<!-- GENERATED:END spec_schema_field_catalog -->
