## Generated Library Symbol Reference

- module_count: {{catalog.summary.module_count}}
- symbol_count: {{catalog.summary.symbol_count}}
- source_root: `{{catalog.summary.library_root}}`

{{#catalog.modules}}
### Module `{{module}}` {#{{anchor}}}

- symbol_count: {{symbol_count}}
- libraries: {{#library_ids}}`{{.}}` {{/library_ids}}{{^library_ids}}-{{/library_ids}}

{{/catalog.modules}}

## Symbols

{{#catalog.symbols}}
### `{{symbol}}` {#{{anchor}}}

{{contract_badge}}

- Signature: `{{signature}}`
- Module: `{{module}}`
- Library: `{{library_id}}`
- Stability: `{{stability}}`
- Owner: `{{owner}}`
- Since: `{{since}}`
- Source: `{{source_doc}}#{{case_id}}`
- Export Path: `{{export_path}}`

#### Summary

{{summary}}

#### Description

{{description}}

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
{{#params}}| `{{name}}` | `{{type}}` | `{{required}}` | {{description}} | {{default}} |
{{/params}}

#### Returns

- type: `{{returns.type}}`
- description: {{returns.description}}

#### Errors

| code | category | when |
|---|---|---|
{{#errors}}| `{{code}}` | `{{category}}` | {{when}} |
{{/errors}}

#### Portability

- python: `{{portability.python}}`
- php: `{{portability.php}}`
- rust: `{{portability.rust}}`
- notes: {{portability.notes}}

#### Examples

{{#examples}}
- **{{title}}**
  - input: `{{input}}`
  - expected: `{{expected}}`
  - notes: {{notes}}
{{/examples}}

#### See Also

{{#see_also}}- `{{.}}`
{{/see_also}}{{^see_also}}- -
{{/see_also}}

{{#deprecated}}
#### Deprecated

- replacement: `{{replacement}}`
- reason: {{reason}}
{{/deprecated}}

{{/catalog.symbols}}

