## Generated Spec Case Index

| domain | case_count |
|---|---|
{{#catalog.domains}}| `{{domain}}` | {{case_count}} |
{{/catalog.domains}}

## Type Summary

| type | case_count |
|---|---|
{{#catalog.types}}| `{{type}}` | {{case_count}} |
{{/catalog.types}}

## Case Anchors

| case_id | domain | type | reference |
|---|---|---|---|
{{#catalog.cases}}| `{{case_id}}` | `{{domain}}` | `{{type}}` | [jump](/docs/book/93l_spec_case_reference.md#{{anchor}}) |
{{/catalog.cases}}
