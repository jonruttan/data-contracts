```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - '{''exports'': [{''as'': ''domain.http.auth_is_oauth'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.auth_is_oauth'', ''params'': [''subject''], ''docs'': [{''id'': ''domain.http.auth_is_oauth.doc.1'', ''summary'': ''Contract export for `domain.http.auth_is_oauth`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\ n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.body_json'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.body_json'', ''params'': [''subject''], ''docs'': [{''id'': ''domain.http.body_json.doc.1'', ''summary'': ''Contract export for `domain.http.body_json`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\ n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\ nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.body_json_has_key'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.body_json_has_key'', ''params'': [''subject'', ''key''], ''docs'': [{''id'': ''domain.http.body_json_has_key.doc.1'', ''summary'': ''Contract export for `domain.http.body_json_has_key`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\n  key: "<key>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: key\n  type: any\n  required: true\n  description: Input parameter `key`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\ nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.body_json_type_is'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.body_json_type_is'', ''params'': [''subject'', ''expected_type''], ''docs'': [{''id'': ''domain.http.body_json_type_is.doc.1'', ''summary'': ''Contract export for `domain.http.body_json_type_is`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\n  expected_type: "<expected_type>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: expected_type\n  type: any\n  required: true\n  description: Input parameter `expected_type`.\n- returns: type: any\ ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.body_text'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.body_text'', ''params'': [''subject''], ''docs'': [{''id'': ''domain.http.body_text.doc.1'', ''summary'': ''Contract export for `domain.http.body_text`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\ n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\ nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.cors_allow_origin'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.cors_allow_origin'', ''params'': [''subject''], ''docs'': [{''id'': ''domain.http.cors_allow_origin.doc.1'', ''summary'': ''Contract export for `domain.http.cors_allow_origin`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.cors_allows_header'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.cors_allows_header'', ''params'': [''subject'', ''header_name''], ''docs'': [{''id'': ''domain.http.cors_allows_header.doc.1'', ''summary'': ''Contract export for `domain.http.cors_allows_header`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\n  header_name: "<header_name>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: header_name\n  type: any\n  required: true\n  description: Input parameter `header_name`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.cors_allows_method'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.cors_allows_method'', ''params'': [''subject'', ''method_name''], ''docs'': [{''id'': ''domain.http.cors_allows_method.doc.1'', ''summary'': ''Contract export for `domain.http.cors_allows_method`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\n  method_name: "<method_name>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: method_name\n  type: any\n  required: true\n  description: Input parameter `method_name`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.cors_credentials_enabled'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.cors_credentials_enabled'', ''params'': [''subject''], ''docs'': [{''id'': ''domain.http.cors_credentials_enabled.doc.1'', ''summary'': ''Contract export for `domain.http.cors_credentials_enabled`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\ n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\ nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.cors_max_age_gte'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.cors_max_age_gte'', ''params'': [''subject'', ''min_age''], ''docs'': [{''id'': ''domain.http.cors_max_age_gte.doc.1'', ''summary'': ''Contract export for `domain.http.cors_max_age_gte`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\n  min_age: "<min_age>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: min_age\n  type: any\n  required: true\n  description: Input parameter `min_age`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.has_bearer_header'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.has_bearer_header'', ''params'': [''subject''], ''docs'': [{''id'': ''domain.http.has_bearer_header.doc.1'', ''summary'': ''Contract export for `domain.http.has_bearer_header`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.header_contains'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.header_contains'', ''params'': [''subject'', ''key'', ''token''], ''docs'': [{''id'': ''domain.http.header_contains.doc.1'', ''summary'': ''Contract export for `domain.http.header_contains`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\n  key: "<key>"\n  token: "<token>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: key\n  type: any\n  required: true\n  description: Input parameter `key`.\n- name: token\n  type: any\n  required: true\n  description: Input parameter `token`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\ n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.header_get'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.header_get'', ''params'': [''subject'', ''key''], ''docs'': [{''id'': ''domain.http.header_get.doc.1'', ''summary'': ''Contract export for `domain.http.header_get`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\n  key: "<key>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: key\n  type: any\n  required: true\n  description: Input parameter `key`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.is_preflight_step'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.is_preflight_step'', ''params'': [''step''], ''docs'': [{''id'': ''domain.http.is_preflight_step.doc.1'', ''summary'': ''Contract export for `domain.http.is_preflight_step`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  step: "<step>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: step\n  type: any\n  required: true\n  description: Input parameter `step`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.oauth_scope_requested'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.oauth_scope_requested'', ''params'': [''subject''], ''docs'': [{''id'': ''domain.http.oauth_scope_requested.doc.1'', ''summary'': ''Contract export for `domain.http.oauth_scope_requested`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\ n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\ nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.oauth_token_source_is'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.oauth_token_source_is'', ''params'': [''subject'', ''expected''], ''docs'': [{''id'': ''domain.http.oauth_token_source_is.doc.1'', ''summary'': ''Contract export for `domain.http.oauth_token_source_is`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\n  expected: "<expected>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\ n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: expected\n  type: any\n  required: true\n  description: Input parameter `expected`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\ n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.ok_2xx'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.ok_2xx'', ''params'': [''subject''], ''docs'': [{''id'': ''domain.http.ok_2xx.doc.1'', ''summary'': ''Contract export for `domain.http.ok_2xx`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\ n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\ nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.status'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.status'', ''params'': [''subject''], ''docs'': [{''id'': ''domain.http.status.doc.1'', ''summary'': ''Contract export for `domain.http.status`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\ n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\ nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.status_in'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.status_in'', ''params'': [''subject'', ''allowed''], ''docs'': [{''id'': ''domain.http.status_in.doc.1'', ''summary'': ''Contract export for `domain.http.status_in`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\n  allowed: "<allowed>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: allowed\n  type: any\n  required: true\n  description: Input parameter `allowed`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\ nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.status_is'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.status_is'', ''params'': [''subject'', ''expected''], ''docs'': [{''id'': ''domain.http.status_is.doc.1'', ''summary'': ''Contract export for `domain.http.status_is`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\n  expected: "<expected>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: expected\n  type: any\n  required: true\n  description: Input parameter `expected`.\ n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\ nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.status_is_forbidden'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.status_is_forbidden'', ''params'': [''subject''], ''docs'': [{''id'': ''domain.http.status_is_forbidden.doc.1'', ''summary'': ''Contract export for `domain.http.status_is_forbidden`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\ n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\ nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.status_is_unauthorized'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.status_is_unauthorized'', ''params'': [''subject''], ''docs'': [{''id'': ''domain.http.status_is_unauthorized.doc.1'', ''summary'': ''Contract export for `domain.http.status_is_unauthorized`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: "<subject>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\ n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\ nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.step_body_json_get'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.step_body_json_get'', ''params'': [''steps'', ''step_id'', ''field''], ''docs'': [{''id'': ''domain.http.step_body_json_get.doc.1'', ''summary'': ''Contract export for `domain.http.step_body_json_get`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  steps: "<steps>"\n  step_id: "<step_id>"\n  field: "<field>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: steps\n  type: any\n  required: true\n  description: Input parameter `steps`.\n- name: step_id\n  type: any\n  required: true\n  description: Input parameter `step_id`.\n- name: field\n  type: any\n  required: true\n  description: Input parameter `field`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\ nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.step_by_id'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.step_by_id'', ''params'': [''steps'', ''step_id''], ''docs'': [{''id'': ''domain.http.step_by_id.doc.1'', ''summary'': ''Contract export for `domain.http.step_by_id`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  steps: "<steps>"\n  step_id: "<step_id>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: steps\n  type: any\n  required: true\n  description: Input parameter `steps`.\n- name: step_id\n  type: any\n  required: true\n  description: Input parameter `step_id`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.http.step_status_is'', ''from'': ''assert.function'', ''path'': ''/__export__domain.http.step_status_is'', ''params'': [''steps'', ''step_id'', ''expected''], ''docs'': [{''id'': ''domain.http.step_status_is.doc.1'', ''summary'': ''Contract export for `domain.http.step_status_is`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  steps: "<steps>"\n  step_id: "<step_id>"\n  expected: "<expected>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: steps\n  type: any\n  required: true\n  description: Input parameter `steps`.\n- name: step_id\n  type: any\n  required: true\n  description: Input parameter `step_id`.\ n- name: expected\n  type: any\n  required: true\n  description: Input parameter `expected`.\n- returns: type: any\ndescription: Result payload for this symbol.\ n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
services:
  defaults:
    profile: default
    config: {}
  entries:
  - id: svc.exports_as_domain_http_status_from_assert_function_path_export_domain_http_status_params_subject_docs_id_domain_http_status_doc_1_summary_contract_export_for_domain_http_status_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_status_from_assert_function_path_export_domain_http_status_params_subject_docs_id_domain_http_status_doc_1_summary_contract_export_for_domain_http_status_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_status_in_from_assert_function_path_export_domain_http_status_in_params_subject_allowed_docs_id_domain_http_status_in_doc_1_summary_contract_export_for_domain_http_status_in_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_allowed_allowed_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_allowed_n_type_any_n_required_true_n_description_input_parameter_allowed_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_status_in_from_assert_function_path_export_domain_http_status_in_params_subject_allowed_docs_id_domain_http_status_in_doc_1_summary_contract_export_for_domain_http_status_in_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_allowed_allowed_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_allowed_n_type_any_n_required_true_n_description_input_parameter_allowed_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_status_is_from_assert_function_path_export_domain_http_status_is_params_subject_expected_docs_id_domain_http_status_is_doc_1_summary_contract_export_for_domain_http_status_is_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_expected_expected_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_expected_n_type_any_n_required_true_n_description_input_parameter_expected_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_status_is_from_assert_function_path_export_domain_http_status_is_params_subject_expected_docs_id_domain_http_status_is_doc_1_summary_contract_export_for_domain_http_status_is_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_expected_expected_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_expected_n_type_any_n_required_true_n_description_input_parameter_expected_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_status_is_unauthorized_from_assert_function_path_export_domain_http_status_is_unauthorized_params_subject_docs_id_domain_http_status_is_unauthorized_doc_1_summary_contract_export_for_domain_http_status_is_unauthorized_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_status_is_unauthorized_from_assert_function_path_export_domain_http_status_is_unauthorized_params_subject_docs_id_domain_http_status_is_unauthorized_doc_1_summary_contract_export_for_domain_http_status_is_unauthorized_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_status_is_forbidden_from_assert_function_path_export_domain_http_status_is_forbidden_params_subject_docs_id_domain_http_status_is_forbidden_doc_1_summary_contract_export_for_domain_http_status_is_forbidden_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_status_is_forbidden_from_assert_function_path_export_domain_http_status_is_forbidden_params_subject_docs_id_domain_http_status_is_forbidden_doc_1_summary_contract_export_for_domain_http_status_is_forbidden_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_ok_2xx_from_assert_function_path_export_domain_http_ok_2xx_params_subject_docs_id_domain_http_ok_2xx_doc_1_summary_contract_export_for_domain_http_ok_2xx_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_ok_2xx_from_assert_function_path_export_domain_http_ok_2xx_params_subject_docs_id_domain_http_ok_2xx_doc_1_summary_contract_export_for_domain_http_ok_2xx_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_header_get_from_assert_function_path_export_domain_http_header_get_params_subject_key_docs_id_domain_http_header_get_doc_1_summary_contract_export_for_domain_http_header_get_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_key_key_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_key_n_type_any_n_required_true_n_description_input_parameter_key_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_header_get_from_assert_function_path_export_domain_http_header_get_params_subject_key_docs_id_domain_http_header_get_doc_1_summary_contract_export_for_domain_http_header_get_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_key_key_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_key_n_type_any_n_required_true_n_description_input_parameter_key_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_header_contains_from_assert_function_path_export_domain_http_header_contains_params_subject_key_token_docs_id_domain_http_header_contains_doc_1_summary_contract_export_for_domain_http_header_contains_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_key_key_n_token_token_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_key_n_type_any_n_required_true_n_description_input_parameter_key_n_name_token_n_type_any_n_required_true_n_description_input_parameter_token_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_header_contains_from_assert_function_path_export_domain_http_header_contains_params_subject_key_token_docs_id_domain_http_header_contains_doc_1_summary_contract_export_for_domain_http_header_contains_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_key_key_n_token_token_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_key_n_type_any_n_required_true_n_description_input_parameter_key_n_name_token_n_type_any_n_required_true_n_description_input_parameter_token_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_body_text_from_assert_function_path_export_domain_http_body_text_params_subject_docs_id_domain_http_body_text_doc_1_summary_contract_export_for_domain_http_body_text_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_body_text_from_assert_function_path_export_domain_http_body_text_params_subject_docs_id_domain_http_body_text_doc_1_summary_contract_export_for_domain_http_body_text_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_body_json_from_assert_function_path_export_domain_http_body_json_params_subject_docs_id_domain_http_body_json_doc_1_summary_contract_export_for_domain_http_body_json_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_body_json_from_assert_function_path_export_domain_http_body_json_params_subject_docs_id_domain_http_body_json_doc_1_summary_contract_export_for_domain_http_body_json_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_body_json_type_is_from_assert_function_path_export_domain_http_body_json_type_is_params_subject_expected_type_docs_id_domain_http_body_json_type_is_doc_1_summary_contract_export_for_domain_http_body_json_type_is_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_expected_type_expected_type_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_expected_type_n_type_any_n_required_true_n_description_input_parameter_expected_type_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_body_json_type_is_from_assert_function_path_export_domain_http_body_json_type_is_params_subject_expected_type_docs_id_domain_http_body_json_type_is_doc_1_summary_contract_export_for_domain_http_body_json_type_is_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_expected_type_expected_type_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_expected_type_n_type_any_n_required_true_n_description_input_parameter_expected_type_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_body_json_has_key_from_assert_function_path_export_domain_http_body_json_has_key_params_subject_key_docs_id_domain_http_body_json_has_key_doc_1_summary_contract_export_for_domain_http_body_json_has_key_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_key_key_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_key_n_type_any_n_required_true_n_description_input_parameter_key_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_body_json_has_key_from_assert_function_path_export_domain_http_body_json_has_key_params_subject_key_docs_id_domain_http_body_json_has_key_doc_1_summary_contract_export_for_domain_http_body_json_has_key_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_key_key_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_key_n_type_any_n_required_true_n_description_input_parameter_key_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_auth_is_oauth_from_assert_function_path_export_domain_http_auth_is_oauth_params_subject_docs_id_domain_http_auth_is_oauth_doc_1_summary_contract_export_for_domain_http_auth_is_oauth_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_auth_is_oauth_from_assert_function_path_export_domain_http_auth_is_oauth_params_subject_docs_id_domain_http_auth_is_oauth_doc_1_summary_contract_export_for_domain_http_auth_is_oauth_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_oauth_token_source_is_from_assert_function_path_export_domain_http_oauth_token_source_is_params_subject_expected_docs_id_domain_http_oauth_token_source_is_doc_1_summary_contract_export_for_domain_http_oauth_token_source_is_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_expected_expected_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_expected_n_type_any_n_required_true_n_description_input_parameter_expected_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_oauth_token_source_is_from_assert_function_path_export_domain_http_oauth_token_source_is_params_subject_expected_docs_id_domain_http_oauth_token_source_is_doc_1_summary_contract_export_for_domain_http_oauth_token_source_is_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_expected_expected_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_expected_n_type_any_n_required_true_n_description_input_parameter_expected_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_has_bearer_header_from_assert_function_path_export_domain_http_has_bearer_header_params_subject_docs_id_domain_http_has_bearer_header_doc_1_summary_contract_export_for_domain_http_has_bearer_header_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_has_bearer_header_from_assert_function_path_export_domain_http_has_bearer_header_params_subject_docs_id_domain_http_has_bearer_header_doc_1_summary_contract_export_for_domain_http_has_bearer_header_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_oauth_scope_requested_from_assert_function_path_export_domain_http_oauth_scope_requested_params_subject_docs_id_domain_http_oauth_scope_requested_doc_1_summary_contract_export_for_domain_http_oauth_scope_requested_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_oauth_scope_requested_from_assert_function_path_export_domain_http_oauth_scope_requested_params_subject_docs_id_domain_http_oauth_scope_requested_doc_1_summary_contract_export_for_domain_http_oauth_scope_requested_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_cors_allow_origin_from_assert_function_path_export_domain_http_cors_allow_origin_params_subject_docs_id_domain_http_cors_allow_origin_doc_1_summary_contract_export_for_domain_http_cors_allow_origin_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_cors_allow_origin_from_assert_function_path_export_domain_http_cors_allow_origin_params_subject_docs_id_domain_http_cors_allow_origin_doc_1_summary_contract_export_for_domain_http_cors_allow_origin_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_cors_allows_method_from_assert_function_path_export_domain_http_cors_allows_method_params_subject_method_name_docs_id_domain_http_cors_allows_method_doc_1_summary_contract_export_for_domain_http_cors_allows_method_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_method_name_method_name_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_method_name_n_type_any_n_required_true_n_description_input_parameter_method_name_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_cors_allows_method_from_assert_function_path_export_domain_http_cors_allows_method_params_subject_method_name_docs_id_domain_http_cors_allows_method_doc_1_summary_contract_export_for_domain_http_cors_allows_method_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_method_name_method_name_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_method_name_n_type_any_n_required_true_n_description_input_parameter_method_name_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_cors_allows_header_from_assert_function_path_export_domain_http_cors_allows_header_params_subject_header_name_docs_id_domain_http_cors_allows_header_doc_1_summary_contract_export_for_domain_http_cors_allows_header_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_header_name_header_name_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_header_name_n_type_any_n_required_true_n_description_input_parameter_header_name_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_cors_allows_header_from_assert_function_path_export_domain_http_cors_allows_header_params_subject_header_name_docs_id_domain_http_cors_allows_header_doc_1_summary_contract_export_for_domain_http_cors_allows_header_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_header_name_header_name_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_header_name_n_type_any_n_required_true_n_description_input_parameter_header_name_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_cors_credentials_enabled_from_assert_function_path_export_domain_http_cors_credentials_enabled_params_subject_docs_id_domain_http_cors_credentials_enabled_doc_1_summary_contract_export_for_domain_http_cors_credentials_enabled_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_cors_credentials_enabled_from_assert_function_path_export_domain_http_cors_credentials_enabled_params_subject_docs_id_domain_http_cors_credentials_enabled_doc_1_summary_contract_export_for_domain_http_cors_credentials_enabled_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_cors_max_age_gte_from_assert_function_path_export_domain_http_cors_max_age_gte_params_subject_min_age_docs_id_domain_http_cors_max_age_gte_doc_1_summary_contract_export_for_domain_http_cors_max_age_gte_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_min_age_min_age_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_min_age_n_type_any_n_required_true_n_description_input_parameter_min_age_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_cors_max_age_gte_from_assert_function_path_export_domain_http_cors_max_age_gte_params_subject_min_age_docs_id_domain_http_cors_max_age_gte_doc_1_summary_contract_export_for_domain_http_cors_max_age_gte_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_subject_subject_n_min_age_min_age_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_subject_n_type_any_n_required_true_n_description_input_parameter_subject_n_name_min_age_n_type_any_n_required_true_n_description_input_parameter_min_age_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_is_preflight_step_from_assert_function_path_export_domain_http_is_preflight_step_params_step_docs_id_domain_http_is_preflight_step_doc_1_summary_contract_export_for_domain_http_is_preflight_step_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_step_step_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_step_n_type_any_n_required_true_n_description_input_parameter_step_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_is_preflight_step_from_assert_function_path_export_domain_http_is_preflight_step_params_step_docs_id_domain_http_is_preflight_step_doc_1_summary_contract_export_for_domain_http_is_preflight_step_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_step_step_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_step_n_type_any_n_required_true_n_description_input_parameter_step_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_step_by_id_from_assert_function_path_export_domain_http_step_by_id_params_steps_step_id_docs_id_domain_http_step_by_id_doc_1_summary_contract_export_for_domain_http_step_by_id_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_steps_steps_n_step_id_step_id_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_steps_n_type_any_n_required_true_n_description_input_parameter_steps_n_name_step_id_n_type_any_n_required_true_n_description_input_parameter_step_id_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_step_by_id_from_assert_function_path_export_domain_http_step_by_id_params_steps_step_id_docs_id_domain_http_step_by_id_doc_1_summary_contract_export_for_domain_http_step_by_id_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_steps_steps_n_step_id_step_id_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_steps_n_type_any_n_required_true_n_description_input_parameter_steps_n_name_step_id_n_type_any_n_required_true_n_description_input_parameter_step_id_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_step_status_is_from_assert_function_path_export_domain_http_step_status_is_params_steps_step_id_expected_docs_id_domain_http_step_status_is_doc_1_summary_contract_export_for_domain_http_step_status_is_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_steps_steps_n_step_id_step_id_n_expected_expected_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_steps_n_type_any_n_required_true_n_description_input_parameter_steps_n_name_step_id_n_type_any_n_required_true_n_description_input_parameter_step_id_n_name_expected_n_type_any_n_required_true_n_description_input_parameter_expected_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_step_status_is_from_assert_function_path_export_domain_http_step_status_is_params_steps_step_id_expected_docs_id_domain_http_step_status_is_doc_1_summary_contract_export_for_domain_http_step_status_is_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_steps_steps_n_step_id_step_id_n_expected_expected_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_steps_n_type_any_n_required_true_n_description_input_parameter_steps_n_name_step_id_n_type_any_n_required_true_n_description_input_parameter_step_id_n_name_expected_n_type_any_n_required_true_n_description_input_parameter_expected_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_http_step_body_json_get_from_assert_function_path_export_domain_http_step_body_json_get_params_steps_step_id_field_docs_id_domain_http_step_body_json_get_doc_1_summary_contract_export_for_domain_http_step_body_json_get_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_steps_steps_n_step_id_step_id_n_field_field_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_steps_n_type_any_n_required_true_n_description_input_parameter_steps_n_name_step_id_n_type_any_n_required_true_n_description_input_parameter_step_id_n_name_field_n_type_any_n_required_true_n_description_input_parameter_field_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_http_step_body_json_get_from_assert_function_path_export_domain_http_step_body_json_get_params_steps_step_id_field_docs_id_domain_http_step_body_json_get_doc_1_summary_contract_export_for_domain_http_step_body_json_get_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_steps_steps_n_step_id_step_id_n_field_field_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_steps_n_type_any_n_required_true_n_description_input_parameter_steps_n_name_step_id_n_type_any_n_required_true_n_description_input_parameter_step_id_n_name_field_n_type_any_n_required_true_n_description_input_parameter_field_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
contracts:
- id: LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS
  docs:
  - id: LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.status
      assert:
        std.object.get:
        - std.object.get:
          - var: subject
          - value
        - status
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-002-DOMAIN-HTTP-STATUS-IN
  docs:
  - id: LIB-DOMAIN-HTTP-001-002-DOMAIN-HTTP-STATUS-IN.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-002-DOMAIN-HTTP-STATUS-IN` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.status_in
      assert:
        std.collection.in:
        - std.object.get:
          - std.object.get:
            - var: subject
            - value
          - status
        - var: allowed
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-003-DOMAIN-HTTP-STATUS-IS
  docs:
  - id: LIB-DOMAIN-HTTP-001-003-DOMAIN-HTTP-STATUS-IS.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-003-DOMAIN-HTTP-STATUS-IS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.status_is
      assert:
        std.logic.eq:
        - std.object.get:
          - std.object.get:
            - var: subject
            - value
          - status
        - var: expected
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-004-DOMAIN-HTTP-STATUS-IS-UNAUTHORIZED
  docs:
  - id: LIB-DOMAIN-HTTP-001-004-DOMAIN-HTTP-STATUS-IS-UNAUTHORIZED.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-004-DOMAIN-HTTP-STATUS-IS-UNAUTHORIZED` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.status_is_unauthorized
      assert:
        lit:
          call:
          - var: domain.http.status_is
          - var: subject
          - 401
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-005-DOMAIN-HTTP-STATUS-IS-FORBIDDEN
  docs:
  - id: LIB-DOMAIN-HTTP-001-005-DOMAIN-HTTP-STATUS-IS-FORBIDDEN.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-005-DOMAIN-HTTP-STATUS-IS-FORBIDDEN` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.status_is_forbidden
      assert:
        lit:
          call:
          - var: domain.http.status_is
          - var: subject
          - 403
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-006-DOMAIN-HTTP-OK-2XX
  docs:
  - id: LIB-DOMAIN-HTTP-001-006-DOMAIN-HTTP-OK-2XX.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-006-DOMAIN-HTTP-OK-2XX` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.ok_2xx
      assert:
        std.logic.and:
        - std.logic.gte:
          - std.object.get:
            - std.object.get:
              - var: subject
              - value
            - status
          - 200
        - std.logic.lt:
          - std.object.get:
            - std.object.get:
              - var: subject
              - value
            - status
          - 300
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-007-DOMAIN-HTTP-HEADER-GET
  docs:
  - id: LIB-DOMAIN-HTTP-001-007-DOMAIN-HTTP-HEADER-GET.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-007-DOMAIN-HTTP-HEADER-GET` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.header_get
      assert:
        std.object.get:
        - std.object.get:
          - std.object.get:
            - var: subject
            - value
          - headers
        - var: key
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-008-DOMAIN-HTTP-HEADER-CONTAINS
  docs:
  - id: LIB-DOMAIN-HTTP-001-008-DOMAIN-HTTP-HEADER-CONTAINS.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-008-DOMAIN-HTTP-HEADER-CONTAINS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.header_contains
      assert:
        std.string.contains:
        - std.object.get:
          - std.object.get:
            - std.object.get:
              - var: subject
              - value
            - headers
          - var: key
        - var: token
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-009-DOMAIN-HTTP-BODY-TEXT
  docs:
  - id: LIB-DOMAIN-HTTP-001-009-DOMAIN-HTTP-BODY-TEXT.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-009-DOMAIN-HTTP-BODY-TEXT` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.body_text
      assert:
        std.object.get:
        - std.object.get:
          - var: subject
          - value
        - body_text
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-010-DOMAIN-HTTP-BODY-JSON
  docs:
  - id: LIB-DOMAIN-HTTP-001-010-DOMAIN-HTTP-BODY-JSON.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-010-DOMAIN-HTTP-BODY-JSON` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.body_json
      assert:
        std.object.get:
        - std.object.get:
          - var: subject
          - value
        - body_json
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-011-DOMAIN-HTTP-BODY-JSON-TYPE-IS
  docs:
  - id: LIB-DOMAIN-HTTP-001-011-DOMAIN-HTTP-BODY-JSON-TYPE-IS.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-011-DOMAIN-HTTP-BODY-JSON-TYPE-IS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.body_json_type_is
      assert:
        std.type.json_type:
        - std.object.get:
          - std.object.get:
            - var: subject
            - value
          - body_json
        - var: expected_type
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-012-DOMAIN-HTTP-BODY-JSON-HAS-KEY
  docs:
  - id: LIB-DOMAIN-HTTP-001-012-DOMAIN-HTTP-BODY-JSON-HAS-KEY.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-012-DOMAIN-HTTP-BODY-JSON-HAS-KEY` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.body_json_has_key
      assert:
        std.object.has_key:
        - std.object.get:
          - std.object.get:
            - var: subject
            - value
          - body_json
        - var: key
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-013-DOMAIN-HTTP-AUTH-IS-OAUTH
  docs:
  - id: LIB-DOMAIN-HTTP-001-013-DOMAIN-HTTP-AUTH-IS-OAUTH.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-013-DOMAIN-HTTP-AUTH-IS-OAUTH` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.auth_is_oauth
      assert:
        std.logic.eq:
        - std.object.get:
          - std.object.get:
            - var: subject
            - meta
          - auth_mode
        - oauth
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-014-DOMAIN-HTTP-OAUTH-TOKEN-SOURCE-IS
  docs:
  - id: LIB-DOMAIN-HTTP-001-014-DOMAIN-HTTP-OAUTH-TOKEN-SOURCE-IS.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-014-DOMAIN-HTTP-OAUTH-TOKEN-SOURCE-IS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.oauth_token_source_is
      assert:
        std.logic.eq:
        - std.object.get:
          - std.object.get:
            - var: subject
            - meta
          - oauth_token_source
        - var: expected
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-HAS-BEARER-HEADER
  docs:
  - id: LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-HAS-BEARER-HEADER.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-HAS-BEARER-HEADER` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.has_bearer_header
      assert:
        std.string.starts_with:
        - std.object.get:
          - std.object.get:
            - std.object.get:
              - var: subject
              - value
            - headers
          - Authorization
        - 'Bearer '
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-OAUTH-SCOPE-REQUESTED
  docs:
  - id: LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-OAUTH-SCOPE-REQUESTED.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-OAUTH-SCOPE-REQUESTED` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.oauth_scope_requested
      assert:
        std.logic.neq:
        - std.object.get:
          - std.object.get:
            - std.object.get:
              - var: subject
              - context
            - oauth
          - scope_requested
        -
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-016-DOMAIN-HTTP-CORS-ALLOW-ORIGIN
  docs:
  - id: LIB-DOMAIN-HTTP-001-016-DOMAIN-HTTP-CORS-ALLOW-ORIGIN.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-016-DOMAIN-HTTP-CORS-ALLOW-ORIGIN` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.cors_allow_origin
      assert:
        std.object.get:
        - std.object.get:
          - std.object.get:
            - var: subject
            - value
          - cors
        - allow_origin
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-017-DOMAIN-HTTP-CORS-ALLOWS-METHOD
  docs:
  - id: LIB-DOMAIN-HTTP-001-017-DOMAIN-HTTP-CORS-ALLOWS-METHOD.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-017-DOMAIN-HTTP-CORS-ALLOWS-METHOD` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.cors_allows_method
      assert:
        std.collection.includes:
        - std.object.get:
          - std.object.get:
            - std.object.get:
              - var: subject
              - value
            - cors
          - allow_methods
        - var: method_name
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-018-DOMAIN-HTTP-CORS-ALLOWS-HEADER
  docs:
  - id: LIB-DOMAIN-HTTP-001-018-DOMAIN-HTTP-CORS-ALLOWS-HEADER.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-018-DOMAIN-HTTP-CORS-ALLOWS-HEADER` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.cors_allows_header
      assert:
        std.collection.includes:
        - std.object.get:
          - std.object.get:
            - std.object.get:
              - var: subject
              - value
            - cors
          - allow_headers
        - var: header_name
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-019-DOMAIN-HTTP-CORS-CREDENTIALS-ENABLED
  docs:
  - id: LIB-DOMAIN-HTTP-001-019-DOMAIN-HTTP-CORS-CREDENTIALS-ENABLED.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-019-DOMAIN-HTTP-CORS-CREDENTIALS-ENABLED` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.cors_credentials_enabled
      assert:
        std.logic.eq:
        - std.object.get:
          - std.object.get:
            - std.object.get:
              - var: subject
              - value
            - cors
          - allow_credentials
        - true
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-020-DOMAIN-HTTP-CORS-MAX-AGE-GTE
  docs:
  - id: LIB-DOMAIN-HTTP-001-020-DOMAIN-HTTP-CORS-MAX-AGE-GTE.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-020-DOMAIN-HTTP-CORS-MAX-AGE-GTE` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.cors_max_age_gte
      assert:
        std.logic.gte:
        - std.object.get:
          - std.object.get:
            - std.object.get:
              - var: subject
              - value
            - cors
          - max_age
        - var: min_age
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-021-DOMAIN-HTTP-IS-PREFLIGHT-STEP
  docs:
  - id: LIB-DOMAIN-HTTP-001-021-DOMAIN-HTTP-IS-PREFLIGHT-STEP.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-021-DOMAIN-HTTP-IS-PREFLIGHT-STEP` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.is_preflight_step
      assert:
        std.logic.eq:
        - std.object.get:
          - var: step
          - method
        - OPTIONS
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-022-DOMAIN-HTTP-STEP-BY-ID
  docs:
  - id: LIB-DOMAIN-HTTP-001-022-DOMAIN-HTTP-STEP-BY-ID.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-022-DOMAIN-HTTP-STEP-BY-ID` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.step_by_id
      assert:
        std.collection.find:
        - fn:
          - - row
          - std.logic.eq:
            - std.object.get:
              - var: row
              - id
            - var: step_id
        - var: steps
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-023-DOMAIN-HTTP-STEP-STATUS-IS
  docs:
  - id: LIB-DOMAIN-HTTP-001-023-DOMAIN-HTTP-STEP-STATUS-IS.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-023-DOMAIN-HTTP-STEP-STATUS-IS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.step_status_is
      assert:
        std.logic.eq:
        - std.object.get:
          - call:
            - var: domain.http.step_by_id
            - var: steps
            - var: step_id
          - status
        - var: expected
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-HTTP-001-024-DOMAIN-HTTP-STEP-BODY-JSON-GET
  docs:
  - id: LIB-DOMAIN-HTTP-001-024-DOMAIN-HTTP-STEP-BODY-JSON-GET.doc.1
    summary: Case `LIB-DOMAIN-HTTP-001-024-DOMAIN-HTTP-STEP-BODY-JSON-GET` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.http.step_body_json_get
      assert:
        std.object.get:
        - std.object.get:
          - call:
            - var: domain.http.step_by_id
            - var: steps
            - var: step_id
          - body_json
        - var: field
  library:
    id: domain.http.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
```
























