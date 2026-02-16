# SPEC-OPT-OUT: Harness-side file IO and docs registry wiring behavior are not yet safely representable as stable .spec.md fixtures.
from __future__ import annotations

from pathlib import Path

from spec_runner.dispatcher import SpecRunContext, run_case
from spec_runner.doc_parser import SpecDocTest
from spec_runner.runtime_context import MiniCapsys, MiniMonkeyPatch


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_docs_generate_harness_updates_marker_block(tmp_path: Path) -> None:
    _write(tmp_path / ".git/keep", "")
    _write(
        tmp_path / "docs/spec/schema/docs_generator_registry_v1.yaml",
        """version: 1
surfaces:
- surface_id: test_surface
  source_type: code_scan
  inputs: [/docs]
  outputs: [/docs/out.md]
  generator: test_generator
  check_mode_supported: true
  owner_contract_docs: [/docs/spec/contract/10_docs_quality.md]
  determinism_hash_fields: [outputs]
  read_only_sections: [/docs/out.md]
  template_path: /docs/tpl.mustache
  output_mode: markers
  marker_surface_id: test_surface
  data_sources:
  - id: payload
    source_type: generated_artifact
    path: /.artifacts/payload.json
""",
    )
    _write(tmp_path / "docs/spec/contract/10_docs_quality.md", "# docs")
    _write(tmp_path / "docs/tpl.mustache", "value={{payload.value}}\n")
    _write(tmp_path / ".artifacts/payload.json", '{"value": "ok"}\n')
    _write(
        tmp_path / "docs/out.md",
        "# Out\n\n<!-- GENERATED:START test_surface -->\nold\n<!-- GENERATED:END test_surface -->\n",
    )
    _write(tmp_path / "docs/spec/impl/docs_generate/cases/case.spec.md", "# case")

    case = SpecDocTest(
        doc_path=tmp_path / "docs/spec/impl/docs_generate/cases/case.spec.md",
        test={
            "id": "SRDOCGEN-TMP-001",
            "type": "docs.generate",
            "harness": {
                "docs_generate": {
                    "surface_id": "test_surface",
                    "mode": "write",
                    "output_mode": "markers",
                    "template_path": "/docs/tpl.mustache",
                    "output_path": "/docs/out.md",
                    "marker_surface_id": "test_surface",
                    "legacy_generator": False,
                    "data_sources": [
                        {
                            "id": "payload",
                            "source_type": "generated_artifact",
                            "path": "/.artifacts/payload.json",
                        }
                    ],
                }
            },
            "assert": [
                {
                    "target": "context_json",
                    "must": [
                        {
                            "evaluate": [
                                {
                                    "std.logic.eq": [
                                        True,
                                        True,
                                    ]
                                }
                            ]
                        }
                    ],
                }
            ],
        },
    )

    ctx = SpecRunContext(tmp_path=tmp_path / ".tmp", patcher=MiniMonkeyPatch(), capture=MiniCapsys())
    run_case(case, ctx=ctx)

    text = (tmp_path / "docs/out.md").read_text(encoding="utf-8")
    assert "value=ok" in text
