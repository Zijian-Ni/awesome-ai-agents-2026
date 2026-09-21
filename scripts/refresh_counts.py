#!/usr/bin/env python3
"""
refresh_counts.py — keep the advertised counts honest.

The Quick Navigation table, the header badges, and the footer blurb all quote
counts ("80+", "Resources-780+", "56 curated scenarios"). Those numbers are
written by hand and then never revisited, so they drift downward-wrong: on
2026-07-30 the nav table claimed "23+" agent frameworks while the section held
43, and "16+" security tools against an actual 33.

Nobody notices, because an undercount looks plausible and no checker reads it.

This script recomputes every count from the file itself and can rewrite them.

    python3 scripts/refresh_counts.py            # report drift, exit 1 if any
    python3 scripts/refresh_counts.py --write    # fix the numbers in place

Counting rules
--------------
* A section's entry count is the number of top-level `- [...]` list items
  between its `## ` heading and the next `## ` heading. Nested/indented bullets
  and prose bullets are excluded, matching how sync_audit.py counts entries.
* Nav rows are matched to sections by ANCHOR, not by label text, because the
  nav label is often shortened relative to the heading ("🧠 Foundation Models"
  vs "## 🧠 Foundation Models 2026") and both are translated in zh/ja.
* Counts are rendered as "N+" rounded DOWN to the nearest 5 for values >= 10,
  so the number stays true after a couple of additions and does not need a
  commit every time a single entry lands.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from check_markdown import slugify as heading_slug
from sync_audit import ENTRY_RE, is_anchor

ROOT = Path(__file__).resolve().parent.parent
FILES = ["README.md", "README.zh-CN.md", "README.ja.md"]

NAV_ROW_RE = re.compile(r"^\|\s*\[([^\]]+)\]\(#([^)]+)\)\s*\|(.*)\|\s*([^|]*?)\s*\|\s*$")


def slugify(heading: str) -> str:
    """GitHub's anchor algorithm, close enough for our heading set."""
    return heading_slug(re.sub(r"^#+\s*", "", heading.strip()))


def section_counts(lines: list[str]) -> dict[str, int]:
    """anchor -> number of top-level entries in that H2 section."""
    counts: dict[str, int] = {}
    current: str | None = None
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("## "):
            current = slugify(line)
            counts[current] = 0
        elif current is not None and (entry := ENTRY_RE.match(line)) and not is_anchor(entry.group("url")):
            counts[current] += 1
    return counts


def render(n: int) -> str:
    """Render a count as a stable, slightly-conservative '<N>+' string."""
    if n < 10:
        return f"{n}+"
    return f"{(n // 5) * 5}+"


def advisory_counts(lines: list[str]) -> dict[str, int]:
    """Count scenario prompts and recipe/anti-pick rows, excluding headers."""
    counts: dict[str, int] = {}
    current = None
    kind = None
    for line in lines:
        if line.startswith("## "):
            current = slugify(line)
            kind = next((e for e in ("🗺", "📋", "⚠") if e in line), None)
            if kind:
                counts[current] = 0
        elif kind == "🗺" and line.startswith("**"):
            counts[current] += 1
        elif kind in ("📋", "⚠") and line.startswith("|") and not re.match(r"^\|\s*[-:]", line):
            counts[current] += 1
    for key in counts:
        if any(slugify(h) == key and any(e in h for e in ("📋", "⚠")) for h in lines if h.startswith("## ")):
            counts[key] = max(0, counts[key] - 1)
    return counts


def process(path: Path, write: bool) -> list[str]:
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    counts = section_counts(lines)
    # Scenario questions and recipe/anti-pick tables are navigation aids,
    # not catalogue resources. Count them separately for their nav cells.
    nav_counts = dict(counts)
    nav_counts.update(advisory_counts(lines))
    notes: list[str] = []

    # ---- Quick Navigation table -----------------------------------------
    for i, line in enumerate(lines):
        m = NAV_ROW_RE.match(line)
        if not m:
            continue
        label, anchor, middle, claimed = m.groups()
        claimed = claimed.strip()
        # only touch rows whose count cell looks like a count
        if not re.fullmatch(r"\d+\+?|—|-", claimed):
            continue
        actual = nav_counts.get(anchor)
        if actual is None:
            # nav label may be shorter than the heading; try prefix match
            cands = [a for a in nav_counts if a.startswith(anchor) or anchor.startswith(a)]
            if len(cands) == 1:
                actual = nav_counts[cands[0]]
        if actual is None or actual == 0:
            continue
        want = str(actual) if any(e in label for e in ("🗺", "📋", "⚠")) else render(actual)
        if claimed == want:
            continue
        notes.append(f"  nav '{label.strip()}': claimed {claimed} → actual {actual} (write {want})")
        if write:
            lines[i] = f"| [{label}](#{anchor}) |{middle}| {want} |"

    # ---- header Resources badge -----------------------------------------
    total = sum(counts.values())
    badge_re = re.compile(r"(Resources-)(\d+)(%2B-orange)")
    for i, line in enumerate(lines):
        m = badge_re.search(line)
        if not m:
            continue
        claimed_total = int(m.group(2))
        want_total = (total // 10) * 10
        if claimed_total != want_total:
            notes.append(f"  badge Resources: claimed {claimed_total}+ → actual {total} (write {want_total}+)")
            if write:
                lines[i] = badge_re.sub(rf"\g<1>{want_total}\g<3>", line)

    # ---- footer blurb ---------------------------------------------------
    foot_re = re.compile(r"(\*)(\d+)(\+ (?:resources|个资源|リソース))")
    for i, line in enumerate(lines):
        m = foot_re.search(line)
        if not m:
            continue
        claimed_total = int(m.group(2))
        want_total = (total // 10) * 10
        if claimed_total != want_total:
            notes.append(f"  footer: claimed {claimed_total}+ → actual {total} (write {want_total}+)")
            if write:
                lines[i] = foot_re.sub(rf"\g<1>{want_total}\g<3>", line)

    if write and notes:
        path.write_text("\n".join(lines), encoding="utf-8")

    return notes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="rewrite the counts in place")
    args = ap.parse_args()

    drift = 0
    for name in FILES:
        path = ROOT / name
        print("=" * 66)
        print(name)
        print("=" * 66)
        notes = process(path, args.write)
        if notes:
            drift += len(notes)
            print("\n".join(notes))
        else:
            print("  counts accurate")

    print("=" * 66)
    if drift and not args.write:
        print(f"RESULT: {drift} stale count(s) — run with --write to fix")
        return 1
    if drift:
        print(f"RESULT: rewrote {drift} count(s)")
        return 0
    print("RESULT: all advertised counts match reality")
    return 0


if __name__ == "__main__":
    sys.exit(main())
