#!/usr/bin/env python3
import json
import pathlib
import re
import sys


ROOT = pathlib.Path(".")
OUT_DIR = ROOT / ".artifacts"
OUT_DIR.mkdir(parents=True, exist_ok=True)

TARGET_DIRS = [
    ROOT / "specs/conformance/cases",
    ROOT / "specs/governance/cases",
    ROOT / "specs/libraries",
]


def load_active_schema_map(catalog_path: pathlib.Path):
    lines = catalog_path.read_text(encoding="utf-8").splitlines()
    active = {}
    current = {}
    in_entry = False
    for raw in lines:
        line = raw.rstrip()
        if line.lstrip().startswith("- "):
            if in_entry and current.get("status") == "active":
                path = current.get("path")
                major = current.get("major")
                if path and major:
                    active[path] = int(major)
            in_entry = True
            current = {}
            m = re.match(r"^\s*-\s+schema_id:\s*(\S+)\s*$", line)
            if m:
                current["schema_id"] = m.group(1)
            continue
        if not in_entry:
            continue
        m = re.match(r"^\s*(schema_id|major|path|status):\s*(.+?)\s*$", line)
        if m:
            key = m.group(1)
            val = m.group(2).strip().strip('"').strip("'")
            current[key] = val
    if in_entry and current.get("status") == "active":
        path = current.get("path")
        major = current.get("major")
        if path and major:
            active[path] = int(major)
    return active


def collect_contract_spec_blocks(path: pathlib.Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks = []
    i = 0
    while i < len(lines):
        open_match = re.match(r"^(`{3,}|~{3,})yaml contract-spec\s*$", lines[i])
        if not open_match:
            i += 1
            continue
        fence = open_match.group(1)
        start = i + 1
        i += 1
        body = []
        while i < len(lines) and not re.match(rf"^{re.escape(fence)}\s*$", lines[i]):
            body.append(lines[i])
            i += 1
        blocks.append((start + 1, body))
        i += 1
    return blocks


def parse_header_field(lines, key):
    pat = re.compile(rf"^{re.escape(key)}\s*:\s*(.+?)\s*$")
    for ln in lines:
        m = pat.match(ln)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    return None


def main():
    catalog = ROOT / "specs/schema/schema_catalog_v1.yaml"
    if not catalog.exists():
        print(f"ERROR: missing schema catalog: {catalog}", file=sys.stderr)
        return 2

    active_schema_map = load_active_schema_map(catalog)

    missing_spec_version = []
    missing_schema_ref = []
    unknown_schema_ref = []
    mismatched_version = []

    files = []
    for d in TARGET_DIRS:
        if d.exists():
            files.extend(sorted(d.rglob("*.spec.md")))

    for path in files:
        for start_line, body in collect_contract_spec_blocks(path):
            spec_version = parse_header_field(body, "spec_version")
            schema_ref = parse_header_field(body, "schema_ref")

            if spec_version is None:
                missing_spec_version.append({"path": str(path), "line": start_line})
            if schema_ref is None:
                missing_schema_ref.append({"path": str(path), "line": start_line})

            if schema_ref is not None:
                expected = active_schema_map.get(schema_ref)
                if expected is None:
                    unknown_schema_ref.append(
                        {"path": str(path), "line": start_line, "schema_ref": schema_ref}
                    )
                else:
                    try:
                        case_major = int(spec_version) if spec_version is not None else None
                    except ValueError:
                        case_major = None
                    if case_major != expected:
                        mismatched_version.append(
                            {
                                "path": str(path),
                                "line": start_line,
                                "schema_ref": schema_ref,
                                "spec_version": spec_version,
                                "expected": expected,
                            }
                        )

    summary = {
        "missing_spec_version_count": len(missing_spec_version),
        "missing_schema_ref_count": len(missing_schema_ref),
        "unknown_schema_ref_count": len(unknown_schema_ref),
        "mismatched_version_count": len(mismatched_version),
        "active_schema_map": active_schema_map,
        "missing_spec_version": missing_spec_version,
        "missing_schema_ref": missing_schema_ref,
        "unknown_schema_ref": unknown_schema_ref,
        "mismatched_version": mismatched_version,
    }

    (OUT_DIR / "spec-schema-pin-validate.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    (OUT_DIR / "spec-schema-pin-validate.md").write_text(
        "# Spec Schema Pin Validation\n\n"
        f"- missing_spec_version_count: `{len(missing_spec_version)}`\n"
        f"- missing_schema_ref_count: `{len(missing_schema_ref)}`\n"
        f"- unknown_schema_ref_count: `{len(unknown_schema_ref)}`\n"
        f"- mismatched_version_count: `{len(mismatched_version)}`\n",
        encoding="utf-8",
    )

    if (
        missing_spec_version
        or missing_schema_ref
        or unknown_schema_ref
        or mismatched_version
    ):
        print("ERROR: schema pin validation failed", file=sys.stderr)
        return 1
    print("OK: schema pin validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
