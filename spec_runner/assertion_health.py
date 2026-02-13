from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any


@dataclass(frozen=True)
class AssertionHealthDiagnostic:
    code: str
    message: str
    path: str


_ALWAYS_TRUE_REGEX = {".*", "^.*$", r"\A.*\Z"}
_VALID_MODES = {"ignore", "warn", "error"}
_NON_PORTABLE_REGEX_TOKENS: tuple[tuple[str, str], ...] = (
    (r"\(\?<=|\(\?<!", "lookbehind"),
    (r"\(\?P<|\(\?<([A-Za-z_][A-Za-z0-9_]*)>", "named capture group"),
    (r"\\k<", "named backreference"),
    (r"\(\?\(", "conditional group"),
    (r"\(\?[aiLmsux-]+:|\(\?[aiLmsux-]+\)", "inline flags"),
    (r"\(\?>", "atomic group"),
    (r"(?<!\\)(?:\\\\)*[+*?]\+", "possessive quantifier"),
)


def resolve_assert_health_mode(test: dict[str, Any], *, env: dict[str, str]) -> str:
    mode = str(env.get("SPEC_RUNNER_ASSERT_HEALTH", "ignore")).strip().lower() or "ignore"
    cfg = test.get("assert_health")
    if cfg is not None:
        if not isinstance(cfg, dict):
            raise TypeError("assert_health must be a mapping when provided")
        if "mode" in cfg:
            mode = str(cfg.get("mode", "")).strip().lower()
    if mode not in _VALID_MODES:
        raise ValueError("assert_health.mode must be one of: ignore, warn, error")
    return mode


def lint_assert_tree(assert_spec: Any) -> list[AssertionHealthDiagnostic]:
    out: list[AssertionHealthDiagnostic] = []

    def _walk(node: Any, *, path: str, group_ctx: str | None) -> None:
        if node is None:
            return
        if isinstance(node, list):
            for i, child in enumerate(node):
                _walk(child, path=f"{path}[{i}]", group_ctx=group_ctx)
            return
        if not isinstance(node, dict):
            return

        group_key = None
        for k in ("must", "can", "cannot"):
            if k in node:
                group_key = k
                break
        if group_key:
            children = node.get(group_key)
            if isinstance(children, list):
                seen: set[str] = set()
                for child in children:
                    try:
                        import json

                        key = json.dumps(child, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
                    except (TypeError, ValueError):
                        key = repr(child)
                    if key in seen:
                        out.append(
                            AssertionHealthDiagnostic(
                                code="AH004",
                                message=f"redundant sibling assertion branch in '{group_key}'",
                                path=f"{path}.{group_key}",
                            )
                        )
                        break
                    seen.add(key)
            _walk(children, path=f"{path}.{group_key}", group_ctx=group_key)
            return

        for op in ("contain", "regex"):
            if op not in node:
                continue
            raw = node.get(op)
            if not isinstance(raw, list):
                continue
            vals = [str(v) for v in raw]
            if len(vals) != len(set(vals)):
                out.append(
                    AssertionHealthDiagnostic(
                        code="AH003",
                        message=f"duplicate values in '{op}' list can hide intent drift",
                        path=f"{path}.{op}",
                    )
                )
            if op == "contain" and "" in vals:
                code = "AH001"
                msg = "contain with empty string is always true"
                if group_ctx == "cannot":
                    msg = "cannot(contain:'') is always false"
                out.append(AssertionHealthDiagnostic(code=code, message=msg, path=f"{path}.contain"))
            if op == "regex":
                for v in vals:
                    if v in _ALWAYS_TRUE_REGEX:
                        code = "AH002"
                        msg = "regex pattern is trivially always true"
                        if group_ctx == "cannot":
                            msg = "cannot(regex always-true) is always false"
                        out.append(AssertionHealthDiagnostic(code=code, message=msg, path=f"{path}.regex"))
                    for pattern, reason in _NON_PORTABLE_REGEX_TOKENS:
                        if re.search(pattern, v):
                            out.append(
                                AssertionHealthDiagnostic(
                                    code="AH005",
                                    message=f"regex uses non-portable construct ({reason})",
                                    path=f"{path}.regex",
                                )
                            )
                            break

    _walk(assert_spec, path="assert", group_ctx=None)
    return out


def format_assertion_health_warning(d: AssertionHealthDiagnostic) -> str:
    return f"WARN: ASSERT_HEALTH {d.code} at {d.path}: {d.message}"


def format_assertion_health_error(diags: list[AssertionHealthDiagnostic]) -> str:
    details = "; ".join(f"{d.code}@{d.path}" for d in diags)
    return f"assertion health check failed ({len(diags)} issue(s)): {details}"
