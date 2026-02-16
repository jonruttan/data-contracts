## Generated Governance Check Catalog

- check_count: {{checks.summary.check_count}}
- checks_with_cases: {{checks.summary.checks_with_cases}}
- checks_without_cases: {{checks.summary.checks_without_cases}}

| check_id | case_count | has_case |
|---|---|---|
{{#checks.checks}}| `{{check_id}}` | {{case_count}} | {{has_case}} |
{{/checks.checks}}
