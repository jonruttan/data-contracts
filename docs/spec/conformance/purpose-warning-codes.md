# Purpose Warning Codes

Stable warning codes emitted by `conformance_purpose_report.py`.

- `PUR001`: purpose duplicates title
  - hint: Rewrite purpose to explain intent or risk not already stated in title.
- `PUR002`: purpose word count below minimum
  - hint: Expand purpose to meet the configured minimum word count.
- `PUR003`: purpose contains placeholder token
  - hint: Replace placeholder tokens with concrete, implementation-neutral intent.
- `PUR004`: purpose lint configuration/policy error
  - hint: Fix purpose_lint settings or policy file shape/version before rerunning.
