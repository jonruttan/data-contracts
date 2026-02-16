## Generated Traceability Catalog

- link_count: {{trace.summary.link_count}}
- rules_with_conformance_cases: {{trace.summary.rules_with_conformance_cases}}
- rules_with_unit_tests: {{trace.summary.rules_with_unit_tests}}
- rules_with_implementation_refs: {{trace.summary.rules_with_implementation_refs}}

| rule_id | policy_ref | contract_refs | schema_refs | conformance_cases | unit_tests | implementation_refs |
|---|---|---|---|---|---|---|
{{#trace.links}}| `{{rule_id}}` | `{{policy_ref}}` | {{contract_ref_count}} | {{schema_ref_count}} | {{conformance_case_count}} | {{unit_test_ref_count}} | {{implementation_ref_count}} |
{{/trace.links}}
