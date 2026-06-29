#!/usr/bin/env python3
"""
Local UX scorecard runner for ux-interaction-skill.

Usage:
  Generate template:  python ux_scorecard.py --template > my-screen.json
  Run score (json):   python ux_scorecard.py my-screen.json
  Run score (md):     python ux_scorecard.py --format md my-screen.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

TEMPLATE: dict = {
    "screen": "Screen or feature name",
    "context": "Brief description of the user scenario",
    "dimensions": {
        "useful": {
            "score": 0,
            "strengths": [],
            "issues": [],
            "recommendations": []
        },
        "usable": {
            "score": 0,
            "strengths": [],
            "issues": [],
            "recommendations": []
        },
        "equitable": {
            "score": 0,
            "strengths": [],
            "issues": [],
            "recommendations": []
        },
        "enjoyable": {
            "score": 0,
            "strengths": [],
            "issues": [],
            "recommendations": []
        }
    },
    "anti_patterns_found": [],
    "multi_path_gaps": [],
    "summary_zh": "",
    "summary_en": "",
    "top_priority_fix": ""
}

STAR_MAP = {0: "☆☆☆☆☆", 1: "⭐☆☆☆☆", 2: "⭐⭐☆☆☆", 3: "⭐⭐⭐☆☆", 4: "⭐⭐⭐⭐☆", 5: "⭐⭐⭐⭐⭐"}
LABEL = {"useful": "Useful 有用", "usable": "Usable 可用", "equitable": "Equitable 公平", "enjoyable": "Enjoyable 愉悦"}


def render_json(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def render_md(data: dict) -> str:
    lines = []
    screen = data.get("screen", "Unknown screen")
    context = data.get("context", "")
    lines.append(f"# UX Scorecard — {screen}\n")
    if context:
        lines.append(f"> {context}\n")

    dims = data.get("dimensions", {})
    scores = []
    for key in ("useful", "usable", "equitable", "enjoyable"):
        dim = dims.get(key, {})
        score = int(dim.get("score", 0))
        scores.append(score)
        stars = STAR_MAP.get(score, "?")
        lines.append(f"## {LABEL[key]}　{stars} {score}/5\n")
        strengths = dim.get("strengths", [])
        if strengths:
            lines.append("**做得好的地方 / Strengths**")
            for s in strengths:
                lines.append(f"- {s}")
            lines.append("")
        issues = dim.get("issues", [])
        if issues:
            lines.append("**问题 / Issues**")
            for i in issues:
                lines.append(f"- {i}")
            lines.append("")
        recs = dim.get("recommendations", [])
        if recs:
            lines.append("**改进建议 / Recommendations**")
            for r in recs:
                lines.append(f"- {r}")
            lines.append("")

    avg = sum(scores) / len(scores) if scores else 0
    lines.append(f"---\n\n**综合评分 / Overall**：{avg:.1f} / 5\n")

    aps = data.get("anti_patterns_found", [])
    if aps:
        lines.append("**发现反模式 / Anti-patterns**")
        for ap in aps:
            lines.append(f"- {ap}")
        lines.append("")

    gaps = data.get("multi_path_gaps", [])
    if gaps:
        lines.append("**多路径缺口 / Multi-path gaps**")
        for g in gaps:
            lines.append(f"- {g}")
        lines.append("")

    zh = data.get("summary_zh", "")
    en = data.get("summary_en", "")
    fix = data.get("top_priority_fix", "")
    if zh or en or fix:
        lines.append("---\n\n### 总结 · Summary\n")
        if zh:
            lines.append(f"**中文版**\n> {zh}\n")
        if en:
            lines.append(f"**English**\n> {en}\n")
        if fix:
            lines.append(f"**最高优先级改进 / Top Priority Fix**: {fix}")

    return "\n".join(lines)


def main() -> None:
    args = sys.argv[1:]
    fmt = "json"
    paths = []
    template_mode = False
    i = 0
    while i < len(args):
        if args[i] == "--template":
            template_mode = True
        elif args[i] == "--format" and i + 1 < len(args):
            fmt = args[i + 1]
            i += 1
        else:
            paths.append(args[i])
        i += 1

    if template_mode:
        print(render_json(TEMPLATE))
        return

    if not paths:
        print("Usage: ux_scorecard.py [--template] [--format json|md] <file.json>", file=sys.stderr)
        raise SystemExit(1)

    path = Path(paths[0])
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    data = json.loads(path.read_text(encoding="utf-8"))
    if fmt == "md":
        print(render_md(data))
    else:
        print(render_json(data))


if __name__ == "__main__":
    main()
