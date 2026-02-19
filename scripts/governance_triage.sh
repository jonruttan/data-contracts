#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

mkdir -p .artifacts
./scripts/control_plane.sh governance

cat > .artifacts/governance-triage-summary.md <<'MD'
# Governance Triage

- mode: control-plane
- result: pass
- note: runtime execution triage is externalized to runner repositories.
MD

jq -n '{status:"pass", mode:"control-plane", notes:["runtime execution triage is externalized"]}' > .artifacts/governance-triage.json

echo "governance triage: pass"
