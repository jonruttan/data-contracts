from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal


@dataclass(frozen=True)
class PredicateLeaf:
    target: str
    subject_key: str
    op: str
    expr: Any
    assert_path: str


@dataclass(frozen=True)
class GroupNode:
    op: Literal["must", "can", "cannot"]
    target: str | None
    children: list["InternalAssertNode"]
    assert_path: str


InternalAssertNode = GroupNode | PredicateLeaf


@dataclass(frozen=True)
class InternalSpecCase:
    id: str
    type: str
    title: str | None
    doc_path: Path
    harness: dict[str, Any]
    metadata: dict[str, Any]
    raw_case: dict[str, Any]
    assert_tree: InternalAssertNode
