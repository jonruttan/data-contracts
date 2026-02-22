```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'api_http': {'allowed_top_level_keys': ['id', 'type', 'title',
      'purpose', 'request', 'requests', 'assert', 'expect', 'requires', 'harness'],
      'allowed_assert_targets': ['status', 'headers', 'body_text', 'body_json', 'cors_json',
      'steps_json', 'context_json'], 'required_request_fields': ['method', 'url']},
      'check': {'profile': 'governance.scan', 'config': {'check': 'conformance.api_http_portable_shape'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
- type: legacy.root_api_http_allowed_top_level_keys_id_type_title_purpose_request_requests_assert_expect_requires_harness_allowed_assert_targets_status_headers_body_text_body_json_cors_json_steps_json_context_json_required_request_fields_method_url_check_profile_governance_scan_config_check_conformance_api_http_portable_shape_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  operations:
  - id: svc.root_api_http_allowed_top_level_keys_id_type_title_purpose_request_requests_assert_expect_requires_harness_allowed_assert_targets_status_headers_body_text_body_json_cors_json_steps_json_context_json_required_request_fields_method_url_check_profile_governance_scan_config_check_conformance_api_http_portable_shape_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCGOV-CONF-API-001
    title: api.http portable conformance cases use canonical shape
    purpose: Ensures api.http portable fixtures keep setup under harness and use only
      canonical behavior assertion targets.
    asserts:
      imports:
      - from: artifact
        names:
        - violation_count
      checks:
      - id: assert_1
        assert:
          call:
          - var: policy.assert.no_violations
          - std.object.assoc:
            - violation_count
            - var: violation_count
            - lit: {}
      - id: assert_2
        assert:
        - call:
          - var: policy.assert.summary_passed
          - std.object.assoc:
            - summary_json
            - var: summary_json
            - lit: {}
        - call:
          - var: policy.assert.summary_check_id
          - std.object.assoc:
            - summary_json
            - var: summary_json
            - lit: {}
          - conformance.api_http_portable_shape
        imports:
        - from: artifact
          names:
          - summary_json
```
