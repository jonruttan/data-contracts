## Generated Contract Policy Rule Catalog

- rule_count: {{policy.summary.rule_count}}
- must_count: {{policy.summary.must_count}}
- should_count: {{policy.summary.should_count}}
- must_not_count: {{policy.summary.must_not_count}}
- active_count: {{policy.summary.active_count}}
- deprecated_count: {{policy.summary.deprecated_count}}
- removed_count: {{policy.summary.removed_count}}

| id | norm | scope | applies_to | references | lifecycle |
|---|---|---|---|---|---|
{{#policy.rules}}| `{{id}}` | `{{norm}}` | `{{scope}}` | `{{applies_to}}` | {{reference_count}} | `{{lifecycle}}` |
{{/policy.rules}}
