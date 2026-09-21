#!/usr/bin/env python3
"""
check_markdown.py — structural sanity checks for the tri-lingual READMEs.

Catches the failure modes that a link checker cannot see:
  * in-page anchors (#-foo) that don't resolve to a real heading
  * malformed table rows (inconsistent column counts inside one table)
  * unbalanced markdown link/bracket syntax on list entries
  * unclosed code fences

Exit code 1 if any problem is found.
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ["README.md", "README.zh-CN.md", "README.ja.md"]

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
LINK_RE = re.compile(r"\[(?:[^\[\]]|\[[^\]]*\])*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def slugify(text: str) -> str:
    """Approximate GitHub's heading -> anchor algorithm."""
    s = text.strip().lower()
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)  # links -> label
    s = re.sub(r"[*_~]", "", s)
    out = []
    for ch in s:
        if ch.isalnum() or ch in "-_":
            out.append(ch)
        elif ch.isspace():
            out.append("-")
        elif unicodedata.category(ch).startswith("M"):
            out.append(ch)
        # everything else (punctuation, emoji) is dropped
    return "".join(out)


def check(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").split("\n")
    problems = 0

    # ---- collect anchors
    anchors: set[str] = set()
    fence = False
    for l in lines:
        if l.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        m = HEADING_RE.match(l)
        if m:
            base = slugify(m.group(2))
            candidate = base
            suffix = 0
            while candidate in anchors:
                suffix += 1
                candidate = f"{base}-{suffix}"
            anchors.add(candidate)
    if fence:
        print(f"  [FENCE] unclosed code fence in {path.name}")
        problems += 1

    # ---- in-page anchor targets
    fence = False
    bad_anchors = []
    for i, l in enumerate(lines, 1):
        if l.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        for url in LINK_RE.findall(l):
            if not url.startswith("#"):
                continue
            target = url[1:]
            if target and target not in anchors:
                bad_anchors.append((i, url))
    if bad_anchors:
        print(f"  [ANCHOR] {len(bad_anchors)} unresolved in-page anchor(s)")
        for i, u in bad_anchors[:12]:
            print(f"    L{i}: {u}")
        problems += len(bad_anchors)

    # ---- table column consistency
    fence = False
    table: list[tuple[int, int]] = []
    bad_tables = []

    def flush(tbl):
        if len(tbl) < 2:
            return
        counts = {}
        for ln, c in tbl:
            counts.setdefault(c, []).append(ln)
        if len(counts) > 1:
            majority = max(counts, key=lambda k: len(counts[k]))
            for c, lns in counts.items():
                if c == majority:
                    continue
                for ln in lns:
                    bad_tables.append((ln, c, majority))

    for i, l in enumerate(lines, 1):
        if l.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        if l.startswith("|") and l.rstrip().endswith("|"):
            table.append((i, l.count("|")))
        else:
            flush(table)
            table = []
    flush(table)
    if bad_tables:
        print(f"  [TABLE] {len(bad_tables)} row(s) with off column counts")
        for ln, c, exp in bad_tables[:12]:
            print(f"    L{ln}: {c - 1} cells (table mostly {exp - 1})")
        problems += len(bad_tables)

    # ---- entry syntax
    bad_entries = []
    fence = False
    for i, l in enumerate(lines, 1):
        if l.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        if not l.startswith("- ["):
            continue
        if l.count("[") != l.count("]") or l.count("(") != l.count(")"):
            bad_entries.append((i, "unbalanced brackets/parens"))
            continue
        if not LINK_RE.search(l):
            bad_entries.append((i, "no parseable markdown link"))
    if bad_entries:
        print(f"  [ENTRY] {len(bad_entries)} malformed entr(ies)")
        for ln, why in bad_entries[:12]:
            print(f"    L{ln}: {why} -> {lines[ln - 1][:88]}")
        problems += len(bad_entries)

    if problems == 0:
        print("  clean")
    return problems


def main() -> int:
    total = 0
    for name in FILES:
        p = ROOT / name
        print("=" * 66)
        print(name)
        print("=" * 66)
        total += check(p)
    print("=" * 66)
    if total:
        print(f"RESULT: {total} markdown problem(s)")
        return 1
    print("RESULT: markdown structurally clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
