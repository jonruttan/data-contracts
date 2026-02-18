from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    args = list(argv or [])
    if "--help" in args or "-h" in args:
        print("usage: conformance-fixture [--json]")
        return 0
    if "--json" in args:
        print(json.dumps({"ok": True, "source": "conformance-fixture"}))
        return 0
    print("conformance fixture ran")
    return 0


def codemod_smoke(argv: list[str] | None = None) -> int:
    args = list(argv or [])
    mode = args[0] if args else ""
    root = Path(__file__).resolve().parents[1]
    py = root / ".venv/bin/python"
    py_bin = str(py) if py.exists() else sys.executable

    with tempfile.TemporaryDirectory(prefix="sr-codemod-") as td:
        tmp = Path(td)
        if mode == "chain_export":
            legacy_key = "from" + "_" + "target"
            f = tmp / "x.spec.md"
            f.write_text(
                "\n".join(
                    [
                        "harness:",
                        "  chain:",
                        "    steps:",
                        "    - id: s1",
                        "      class: must",
                        "      ref: /a.spec.md#A",
                        "      exports:",
                        "      - as: x",
                        f"        {legacy_key}: text",
                        "        required: true",
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            cp = subprocess.run(
                [py_bin, "scripts/convert_chain_export_from_key.py", "--check", str(f)],
                cwd=root,
                check=False,
                capture_output=True,
                text=True,
            )
            if cp.returncode == 0:
                print("check_should_fail")
                return 1
            cp = subprocess.run(
                [py_bin, "scripts/convert_chain_export_from_key.py", "--write", str(f)],
                cwd=root,
                check=False,
                capture_output=True,
                text=True,
            )
            if cp.returncode != 0:
                print("write_failed")
                return 1
            updated = f.read_text(encoding="utf-8")
            if legacy_key in updated or "from: text" not in updated:
                print("rewrite_failed")
                return 1
            print("ok_chain_export")
            return 0

        if mode == "chain_ref":
            f = tmp / "x.spec.md"
            f.write_text(
                "\n".join(
                    [
                        "harness:",
                        "  chain:",
                        "    steps:",
                        "    - id: one",
                        "      class: must",
                        "      ref:",
                        "        path: /docs/spec/a.spec.md",
                        "        case_id: CASE-1",
                        "    - id: two",
                        "      class: must",
                        "      ref:",
                        "        case_id: CASE-2",
                        "    - id: three",
                        "      class: must",
                        "      ref:",
                        "        path: ../b.spec.md",
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            cp = subprocess.run(
                [py_bin, "scripts/convert_chain_ref_format.py", "--write", str(tmp)],
                cwd=root,
                check=False,
                capture_output=True,
                text=True,
            )
            if cp.returncode != 0:
                print("write_failed")
                return 1
            cp = subprocess.run(
                [py_bin, "scripts/convert_chain_ref_format.py", "--check", str(tmp)],
                cwd=root,
                check=False,
                capture_output=True,
                text=True,
            )
            if cp.returncode != 0:
                print("check_failed")
                return 1
            updated = f.read_text(encoding="utf-8")
            required = [
                "ref: /docs/spec/a.spec.md#CASE-1",
                "ref: #CASE-2",
                "ref: ../b.spec.md",
            ]
            if any(tok not in updated for tok in required):
                print("rewrite_failed")
                return 1
            print("ok_chain_ref")
            return 0

        if mode == "defines":
            f = tmp / "library.spec.md"
            f.write_text(
                "\n".join(
                    [
                        "# Sample",
                        "",
                        "```yaml contract-spec",
                        "id: LIB-1",
                        "type: spec_lang.export",
                        "definitions:",
                        "  public:",
                        "    keep:",
                        "      fn:",
                        "      - [x]",
                        "      - {var: x}",
                        "```",
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            cp = subprocess.run(
                [py_bin, "scripts/convert_definitions_to_defines.py", "--write", str(tmp)],
                cwd=root,
                check=False,
                capture_output=True,
                text=True,
            )
            if cp.returncode != 0:
                print("write_failed")
                return 1
            cp = subprocess.run(
                [py_bin, "scripts/convert_definitions_to_defines.py", "--check", str(tmp)],
                cwd=root,
                check=False,
                capture_output=True,
                text=True,
            )
            if cp.returncode != 0:
                print("check_failed")
                return 1
            updated = f.read_text(encoding="utf-8")
            if "definitions:" in updated or "defines:" not in updated:
                print("rewrite_failed")
                return 1
            print("ok_defines")
            return 0

    print("unknown_mode")
    return 2
