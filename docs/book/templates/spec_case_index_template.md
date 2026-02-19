## Generated Spec Case Index

| type | case_count |
|---|---|
{{#catalog.types}}| `{{type}}` | {{case_count}} |
{{/catalog.types}}

## Case Anchors

| case_id | type | reference |
|---|---|---|
{{#catalog.cases}}| `{{case_id}}` | `{{type}}` | [jump](/docs/book/93l_spec_case_reference.md#{{anchor}}) |
{{/catalog.cases}}
