#!/usr/bin/env python3
import json
import pathlib
import re
from collections import defaultdict

root = pathlib.Path('.')
cases_dir = root / 'specs/governance/cases/core'
check_sets = root / 'specs/governance/check_sets_v1.yaml'
out_dir = root / '.artifacts'
out_dir.mkdir(parents=True, exist_ok=True)

check_re = re.compile(r'config:\s*\n\s*check:\s*([^\n]+)', re.MULTILINE)
profile_re = re.compile(r'^\s{2}([a-z_]+):\s*$')
set_re = re.compile(r'^\s{6}- id:\s*(\S+)\s*$')

active_profile = None
set_profiles = defaultdict(list)
for ln in check_sets.read_text(encoding='utf-8').splitlines():
    p = profile_re.match(ln)
    if p and p.group(1) in {'critical', 'full', 'optional'}:
        active_profile = p.group(1)
        continue
    m = set_re.match(ln)
    if m and active_profile:
        set_profiles[m.group(1)].append(active_profile)

optional_ids = sorted(k for k, v in set_profiles.items() if 'optional' in v)
case_by_check = defaultdict(list)
for p in sorted(cases_dir.glob('*.spec.md')):
    txt = p.read_text(encoding='utf-8')
    m = check_re.search(txt)
    if not m:
        continue
    chk = m.group(1).strip()
    case_by_check[chk].append(str(p))

optional = []
for chk in optional_ids:
    paths = case_by_check.get(chk, [])
    optional.append({'check_id': chk, 'case_count': len(paths), 'cases': paths})

unassigned_cases = []
for chk, paths in sorted(case_by_check.items()):
    profiles = set_profiles.get(chk, [])
    if profiles == ['optional']:
        continue
    if 'optional' not in profiles:
        continue
    unassigned_cases.append({'check_id': chk, 'profiles': profiles, 'cases': paths})

missing_cases = [row for row in optional if row['case_count'] == 0]

report = {
    'status': 'report-only',
    'optional_check_count': len(optional_ids),
    'optional_case_bound_count': len(optional_ids) - len(missing_cases),
    'optional_missing_case_count': len(missing_cases),
    'optional_missing_cases': missing_cases,
    'optional_profile_collisions': unassigned_cases,
    'optional_checks': optional,
}
(out_dir / 'governance-optional-report.json').write_text(json.dumps(report, indent=2))
with (out_dir / 'governance-optional-summary.md').open('w') as f:
    f.write('# Governance Optional Summary\n\n')
    f.write(f"- optional_check_count: `{len(optional_ids)}`\n")
    f.write(f"- optional_case_bound_count: `{len(optional_ids) - len(missing_cases)}`\n")
    f.write(f"- optional_missing_case_count: `{len(missing_cases)}`\n")
    for row in optional[:50]:
        f.write(f"- `{row['check_id']}` cases: `{row['case_count']}`\n")
    if missing_cases:
        f.write('\n## Missing Optional Case Bindings\n\n')
        for row in missing_cases[:50]:
            f.write(f"- `{row['check_id']}`\n")

print('OK: governance optional report written')
