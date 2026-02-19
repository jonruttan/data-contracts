# SPEC-OPT-OUT: Verifies orchestration.run harness registry dispatch and capability validation behavior.
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pytest

from spec_runner.harnesses.orchestration_run import run
from spec_runner.internal_model import GroupNode
from spec_runner.internal_model import InternalSpecCase
from spec_runner.internal_model import PredicateLeaf


@dataclass
class _Ctx:
    tmp_path: Path
    env: dict[str, str] | None = None


def _case(doc_path: Path, *, harness: dict[str, Any]) -> InternalSpecCase:
    return InternalSpecCase(
        id="ORCH-001",
        type="orchestration.run",
        title=None,
        doc_path=doc_path,
        harness=harness,
        metadata={},
        raw_case={"id": "ORCH-001", "type": "orchestration.run", "harness": harness},
        assert_tree=GroupNode(
            op="must",
            target="result_json",
            assert_path="assert",
            children=[
                PredicateLeaf(
                    target="result_json",
                    subject_key="result_json",
                    op="evaluate",
                    expr=["eq", ["get", ["var", "subject"], "tool_id"], "governance.run"],
                    assert_path="assert.must[0]",
                )
            ],
        ),
    )


def test_orchestration_harness_validates_required_capability(tmp_path: Path) -> None:
    tools_dir = tmp_path / "specs/governance/tools/python"
    tools_dir.mkdir(parents=True, exist_ok=True)
    (tools_dir / "tools_v1.yaml").write_text(
        """
version: 1
implementation: python
tools:
- tool_id: governance.run
  effect_symbol: ops.proc.command.exec
  capability_id: orchestration.tool.governance.run
  input_schema_ref: /specs/schema/orchestration_result_v1.yaml#tool_input
  output_schema_ref: /specs/schema/orchestration_result_v1.yaml#tool_output
  stability: stable
  since: v1
  adapter_subcommand: governance
""".strip()
        + "\n",
        encoding="utf-8",
    )
    (tmp_path / ".git").mkdir(parents=True, exist_ok=True)

    case = _case(
        tmp_path / "specs/orchestration/cases/core/sample.spec.md",
        harness={
            "orchestration": {
                "impl": "python",
                "tool_id": "governance.run",
                "capabilities": [],
            }
        },
    )
    with pytest.raises(ValueError, match="missing required capability"):
        run(case, ctx=_Ctx(tmp_path=tmp_path))


def test_orchestration_harness_rejects_unknown_tool(tmp_path: Path) -> None:
    tools_dir = tmp_path / "specs/governance/tools/python"
    tools_dir.mkdir(parents=True, exist_ok=True)
    (tools_dir / "tools_v1.yaml").write_text(
        "version: 1\nimplementation: python\ntools: []\n",
        encoding="utf-8",
    )
    (tmp_path / ".git").mkdir(parents=True, exist_ok=True)
    case = _case(
        tmp_path / "specs/orchestration/cases/core/sample.spec.md",
        harness={
            "orchestration": {
                "impl": "python",
                "tool_id": "governance.run",
                "capabilities": ["orchestration.tool.governance.run"],
            }
        },
    )
    with pytest.raises(ValueError, match="unknown orchestration tool_id"):
        run(case, ctx=_Ctx(tmp_path=tmp_path))
