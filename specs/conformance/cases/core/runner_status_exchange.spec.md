# Runner Status Exchange Conformance Cases

## DCCONF-RSTAT-001

```yaml contract-spec
id: DCCONF-RSTAT-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: runner status report schema is declared
purpose: Ensures the producer-facing status report schema exists.
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
  use:
  - ref: /specs/libraries/policy/policy_text.spec.md
    as: lib_policy_text
    symbols:
    - policy.text.contains_pair
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - text
  steps:
  - id: assert_1
    assert:
    - call:
      - {var: policy.text.contains_pair}
      - {var: text}
      - runtime.runner_status_report
      - command_results
```

## DCCONF-RSTAT-002

```yaml contract-spec
id: DCCONF-RSTAT-002
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: runner status matrix schema is declared
purpose: Ensures the aggregate status matrix schema exists.
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
  use:
  - ref: /specs/libraries/policy/policy_text.spec.md
    as: lib_policy_text
    symbols:
    - policy.text.contains_pair
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - text
  steps:
  - id: assert_1
    assert:
    - call:
      - {var: policy.text.contains_pair}
      - {var: text}
      - runtime.runner_status_matrix
      - freshness_state
```

## DCCONF-RSTAT-003

```yaml contract-spec
id: DCCONF-RSTAT-003
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: ingest script enforces freshness threshold
purpose: Ensures ingest includes max-age controls and enforcement flag.
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
  use:
  - ref: /specs/libraries/policy/policy_text.spec.md
    as: lib_policy_text
    symbols:
    - policy.text.contains_pair
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - text
  steps:
  - id: assert_1
    assert:
    - call:
      - {var: policy.text.contains_pair}
      - {var: text}
      - --max-age-hours
      - --enforce-freshness
```

## DCCONF-RSTAT-004

```yaml contract-spec
id: DCCONF-RSTAT-004
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: ingest tracks missing compatibility status visibility
purpose: Ensures missing compatibility status is represented and policy-scored.
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
  use:
  - ref: /specs/libraries/policy/policy_text.spec.md
    as: lib_policy_text
    symbols:
    - policy.text.contains_pair
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - text
  steps:
  - id: assert_1
    assert:
    - call:
      - {var: policy.text.contains_pair}
      - {var: text}
      - freshness_state
      - non_blocking_fail
```

## DCCONF-RSTAT-005

```yaml contract-spec
id: DCCONF-RSTAT-005
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: required lane policy remains blocking
purpose: Ensures required lane status maps to blocking policy effect.
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
  use:
  - ref: /specs/libraries/policy/policy_text.spec.md
    as: lib_policy_text
    symbols:
    - policy.text.contains_pair
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - text
  steps:
  - id: assert_1
    assert:
    - call:
      - {var: policy.text.contains_pair}
      - {var: text}
      - lane_class
      - blocking_fail
```

