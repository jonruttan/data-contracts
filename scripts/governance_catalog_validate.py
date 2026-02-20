#!/usr/bin/env python3
import json
import pathlib
import re
import sys
from collections import defaultdict

root = pathlib.Path('.')
governance_cases_dir = root / 'specs/governance/cases/core'
check_sets = root / 'specs/governance/check_sets_v1.yaml'
out_dir = root / '.artifacts'
out_dir.mkdir(parents=True, exist_ok=True)

id_re = re.compile(r'^id:\s*(\S+)')
check_re = re.compile(r'config:\s*\n\s*check:\s*([^\n]+)', re.MULTILINE)
profile_re = re.compile(r'^\s{2}([a-z_]+):\s*$')
set_re = re.compile(r'^\s{6}- id:\s*(\S+)\s*$')

ids = defaultdict(list)
case_checks = []
for p in sorted((root / 'specs').rglob('*.spec.md')):
    txt = p.read_text(encoding='utf-8')
    for i, ln in enumerate(txt.splitlines(), 1):
        m = id_re.match(ln)
        if m:
            ids[m.group(1)].append({'path': str(p), 'line': i})

for p in sorted(governance_cases_dir.glob('*.spec.md')):
    txt = p.read_text(encoding='utf-8')
    m = check_re.search(txt)
    case_checks.append(
        {
            'path': str(p),
            'check_id': m.group(1).strip() if m else None,
        }
    )

set_profiles = defaultdict(list)
active_profile = None
for ln in check_sets.read_text(encoding='utf-8').splitlines():
    p = profile_re.match(ln)
    if p and p.group(1) in {'critical', 'full', 'optional'}:
        active_profile = p.group(1)
        continue
    m = set_re.match(ln)
    if m and active_profile:
        set_profiles[m.group(1)].append(active_profile)

duplicates = {k:v for k,v in ids.items() if len(v) > 1}
missing_check_field = [c for c in case_checks if not c['check_id']]
unmapped = [c for c in case_checks if c['check_id'] and c['check_id'] not in set_profiles]
multi_tier = [
    c
    for c in case_checks
    if c['check_id'] and len(set_profiles.get(c['check_id'], [])) != 1
]

summary = {
    'duplicate_case_id_count': len(duplicates),
    'missing_case_check_field_count': len(missing_check_field),
    'unmapped_case_check_count': len(unmapped),
    'multi_tier_case_check_count': len(multi_tier),
    'duplicates': duplicates,
    'missing_case_check_field': missing_check_field,
    'unmapped_case_checks': unmapped,
    'multi_tier_case_checks': multi_tier,
}
(out_dir / 'governance-catalog-validate.json').write_text(json.dumps(summary, indent=2))
(out_dir / 'governance-catalog-validate.md').write_text(
    '# Governance Catalog Validation\n\n'
    f"- duplicate_case_id_count: `{len(duplicates)}`\n"
    f"- missing_case_check_field_count: `{len(missing_check_field)}`\n"
    f"- unmapped_case_check_count: `{len(unmapped)}`\n"
    f"- multi_tier_case_check_count: `{len(multi_tier)}`\n"
)

if duplicates or missing_check_field or unmapped or multi_tier:
    print('ERROR: governance catalog validation failed', file=sys.stderr)
    print(
        json.dumps(
            {
                'duplicates': len(duplicates),
                'missing_case_check_field': len(missing_check_field),
                'unmapped': len(unmapped),
                'multi_tier': len(multi_tier),
            }
        ),
        file=sys.stderr,
    )
    sys.exit(1)

print('OK: governance catalog validation passed')
