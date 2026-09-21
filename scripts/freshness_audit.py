#!/usr/bin/env python3
"""
freshness_audit.py — catch STALE MODEL RECOMMENDATIONS.

Motivation
----------
`sync_audit.py` catches structural drift between en/zh/ja.
`check_markdown.py` catches broken anchors/tables/syntax.
Neither catches the failure mode that actually degrades this list fastest:

    the *advice* sections silently keep recommending superseded models.

On 2026-07-30 the Model Selection section still opened with

    "I need the smartest model for complex multi-step reasoning
     - Claude Opus 4.7 (/think xhigh) ...
     - Gemini 2.5 Pro — 2M context ..."

while Opus 5 / Fable 5 had shipped, and Gemini 2.5 Pro's context window is
1M, not 2M. Every link in those lines returned HTTP 200, so no existing check
complained.

Historical entries are supposed to name old models — the Timeline says
"Apr 16, 2026 | Claude Opus 4.7 released" and that must stay. So this script
only audits ADVISORY ZONES (the sections that tell a reader what to pick
today), and it treats everything above them as archival.

Usage
-----
    python3 scripts/freshness_audit.py            # audit all three READMEs
    python3 scripts/freshness_audit.py --list     # print the model registry

Exit code 1 if any superseded model is recommended in an advisory zone.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ["README.md", "README.zh-CN.md", "README.ja.md"]

# ---------------------------------------------------------------------------
# Advisory zones.
#
# Identified positionally, because headings are translated. The advisory block
# starts at the "Compare — side-by-side tables" heading (the first section that
# makes present-tense recommendations) and ends at the "Notable projects"
# heading (after which everything is retrospective again).
#
# Matched on the leading emoji, which IS stable across translations.
# ---------------------------------------------------------------------------
ADVISORY_START_EMOJI = "📝"   # Compare — Side-by-Side Tables
ADVISORY_END_EMOJI = "🌟"     # Notable Agent Projects of 2026

# ---------------------------------------------------------------------------
# Model registry.
#
# "superseded" = a model that should no longer appear as a *recommendation*.
# It may still legitimately appear in the Foundation Models catalogue (which is
# a historical record of what was released) and in the Timeline.
#
# Keep `replacement` short and actionable — it is printed verbatim to whoever
# runs the audit, and it is the whole point of the tool.
#
# `allow_regex` carves out phrasings that are legitimately about the old model,
# e.g. an Anti-Pick row explaining why NOT to use it, or an explicit
# "legacy option" note.
# ---------------------------------------------------------------------------
SUPERSEDED: dict[str, dict] = {
    # --- Anthropic -------------------------------------------------------
    "Claude Opus 4.7": {
        "replacement": "Claude Opus 5 (Jul 24, 2026 — $5/$25, 1M ctx) "
                       "or Claude Fable 5 for Mythos-class work",
        "since": "2026-07-24",
    },
    "Claude Opus 4.6": {
        "replacement": "Claude Opus 5",
        "since": "2026-05-28",
    },
    "Claude Sonnet 4.6": {
        "replacement": "Claude Sonnet 5; consult the current official pricing table",
        "since": "2026-06-30",
    },
    # --- OpenAI ----------------------------------------------------------
    "GPT-4o": {
        "replacement": "GPT-5.6 Terra (balanced) or GPT-5.6 Luna (cheap/fast)",
        "since": "2026-02-01",
        # GPT-4o is legitimately named in Anti-Picks and as the retired-but-
        # still-on-API legacy tier.
        "allow_regex": r"legacy|retired|deprecat|Anti-Pick|❌|不推荐|非推奨",
    },
    "GPT-4o-mini": {
        "replacement": "GPT-5.6 Luna",
        "since": "2026-02-01",
        "allow_regex": r"legacy|retired|deprecat|❌|不推奨|遗留|レガシー",
    },
    "GPT-5.5": {
        "replacement": "GPT-5.6 (Sol / Terra / Luna)",
        "since": "2026-07-09",
    },
    # --- Google ----------------------------------------------------------
    "Gemini 2.5 Pro": {
        "replacement": "Gemini 3.1 Pro (flagship) — and note 2.5 Pro is 1M ctx, never 2M",
        "since": "2026-02-01",
    },
    "Gemini 2.5 Flash": {
        "replacement": "Gemini 3.8 Flash; check current access and promotional pricing",
        "since": "2026-05-19",
    },
    "Gemini 2.5 Flash-Lite": {
        "replacement": "Gemini 3.5 Flash-Lite; consult the official model catalogue",
        "since": "2026-05-08",
    },
    # --- DeepSeek --------------------------------------------------------
    "DeepSeek V3.2": {
        "replacement": "DeepSeek V4-Flash or V4-Pro; consult current peak/off-peak pricing",
        "since": "2026-04-24",
        "allow_regex": r"deprecat|退役|廃止|superseded",
    },
}

# ---------------------------------------------------------------------------
# Factual claims that keep getting re-introduced.
# Pattern -> why it is wrong. Checked across the WHOLE file, not just advisory
# zones, because a wrong number is wrong everywhere.
# ---------------------------------------------------------------------------
FACT_TRAPS: list[tuple[str, str]] = [
    (
        r"Gemini 2\.5 Pro[^|\n]{0,80}?2M",
        "Gemini 2.5 Pro has a 1M-token context window. Do not attribute a "
        "different model's context capacity to 2.5 Pro.",
    ),
    (
        r"Claude Opus 4\.7[^|\n]{0,40}?200K",
        "Claude Opus 4.7 shipped with a 1M-token context window, not 200K.",
    ),
    (
        r"Opus 4\.7[^|\n]{0,60}?\$15\s*/\s*\$75",
        "Opus-class pricing is $5/$25 per 1M tokens, not $15/$75.",
    ),
]


# ---------------------------------------------------------------------------
# Not every line in the advisory zone is advice.
#
#  * Inventory tables (API cost, local deployment, head-to-head specs) exist to
#    document what is purchasable today, legacy tiers included. Listing
#    "Claude Opus 4.8 — 📦 Legacy" there is correct and must not fail the build.
#  * Anti-Picks rows NAME the thing to avoid in column 1. Flagging "GPT-4o
#    Vision for OCR" in a table whose whole purpose is to say "don't" would be
#    backwards — but the "Use Instead" column is a real recommendation and does
#    get checked.
#
# Both are recognised from the table's header row, so the rule travels with the
# table rather than being pinned to line numbers that shift on every edit.
# ---------------------------------------------------------------------------
INVENTORY_HEADER_SIGNS = (
    "Input $", "入力 $", "输入 $",
    "Min VRAM", "HF repo",
    "Context Window", "上下文窗口", "コンテキストウィンドウ",
)
ANTIPICK_HEADER_SIGNS = (
    "Use Instead", "使用替代", "代わりに使う", "✅ Use", "✅ 改用",
)


def classify_tables(lines: list[str]) -> dict[int, str]:
    """Map line index -> 'inventory' | 'antipick' for rows inside such tables."""
    kinds: dict[int, str] = {}
    current: str | None = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("|"):
            current = None
            continue
        # A header row is followed by a |---|---| separator; detect the header
        # by looking at whether THIS line declares the columns.
        if any(sign in line for sign in ANTIPICK_HEADER_SIGNS):
            current = "antipick"
        elif any(sign in line for sign in INVENTORY_HEADER_SIGNS):
            current = "inventory"
        if current:
            kinds[i] = current
    return kinds


def antipick_recommendation_part(line: str) -> str:
    """Return only the columns of an Anti-Picks row that carry a recommendation.

    Layout is: | don't use | for this | USE INSTEAD | why |
    Column 1 naming a dead model is the point of the row; column 3 must be
    current. Column 4 ("why") explains the deprecation and may name it too.
    """
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return cells[2] if len(cells) >= 3 else ""


def find_advisory_zone(lines: list[str]) -> tuple[int, int]:
    """Return (start, end) line indices of the advisory zone."""
    start = end = None
    for i, line in enumerate(lines):
        if not line.startswith("## "):
            continue
        if start is None and ADVISORY_START_EMOJI in line:
            start = i
        elif start is not None and ADVISORY_END_EMOJI in line:
            end = i
            break
    if start is None:
        return (0, 0)
    return (start, end if end is not None else len(lines))


def audit_file(path: Path) -> list[str]:
    problems: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    start, end = find_advisory_zone(lines)

    if start == end == 0:
        problems.append(
            f"  could not locate advisory zone (no '## ...{ADVISORY_START_EMOJI}...' heading)"
        )
        return problems

    table_kinds = classify_tables(lines)

    # --- superseded models inside advisory zone --------------------------
    for i in range(start, end):
        line = lines[i]
        kind = table_kinds.get(i)

        if kind == "inventory":
            # Documents what exists, legacy included. Not a recommendation.
            continue
        if kind == "antipick":
            haystack = antipick_recommendation_part(line)
        else:
            haystack = line

        if not haystack:
            continue

        for model, meta in SUPERSEDED.items():
            if model not in haystack:
                continue
            allow = meta.get("allow_regex")
            if allow and re.search(allow, line, re.IGNORECASE):
                continue
            problems.append(
                f"  L{i+1}: recommends superseded '{model}' "
                f"(superseded {meta['since']})\n"
                f"        → use: {meta['replacement']}\n"
                f"        {line.strip()[:140]}"
            )

    # --- factual traps, whole file ---------------------------------------
    for pattern, why in FACT_TRAPS:
        for m in re.finditer(pattern, text):
            line_no = text[: m.start()].count("\n") + 1
            problems.append(f"  L{line_no}: FACT — {why}\n        matched: {m.group(0)[:120]}")

    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true", help="print the model registry and exit")
    args = ap.parse_args()

    if args.list:
        print("Superseded models (must not appear as recommendations):\n")
        for model, meta in SUPERSEDED.items():
            print(f"  {model:22s} superseded {meta['since']}  →  {meta['replacement']}")
        print("\nFactual traps checked across the whole file:\n")
        for pattern, why in FACT_TRAPS:
            print(f"  /{pattern}/\n      {why}\n")
        return 0

    total = 0
    for name in FILES:
        path = ROOT / name
        if not path.exists():
            print(f"missing file: {name}")
            total += 1
            continue
        print("=" * 66)
        print(name)
        print("=" * 66)
        problems = audit_file(path)
        if problems:
            total += len(problems)
            for p in problems:
                print(p)
        else:
            print("  clean")

    print("=" * 66)
    if total:
        print(f"RESULT: {total} freshness problem(s) — advisory sections are stale")
        return 1
    print("RESULT: no known stale recommendations found in the maintained registry")
    return 0


if __name__ == "__main__":
    sys.exit(main())
