#!/usr/bin/env python3
"""Combine HTDP JA drafts in book order (本文 → 付録). See ../BUILD.md."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BODY_AFTER_FRONT = [
    "01-preface.md",
    "02-prologue.md",
    "03-part1-fixed-size-data.md",
    "04-intermezzo1.md",
]

PART2_CHAPTERS = [
    "05-part2-08.md",
    "05-part2-09.md",
    "05-part2-10.md",
    "05-part2-11.md",
    "05-part2-12.md",
    "05-part2-13.md",
]

BODY_AFTER_PART2 = [
    "06-intermezzo2.md",
    "07-part3-abstraction.md",
    "08-intermezzo3.md",
    "09-part4-intertwined-data.md",
    "10-intermezzo4.md",
    "11-part5-generative-recursion.md",
    "12-intermezzo5.md",
    "13-part6-accumulators.md",
    "14-epilogue.md",
]

APPENDIX = [
    "15-appendix-quick.md",
    "16-appendix-htdp-langs-00-index.md",
    "17-appendix-htdp-langs-01-beginner.md",
    "18-appendix-htdp-langs-02-beginner-abbr.md",
    "19-appendix-htdp-langs-03-intermediate.md",
    "20-appendix-htdp-langs-04-intermediate-lam.md",
    "21-appendix-htdp-langs-05-advanced.md",
]

SKIP = {
    "05-part2-arbitrarily-large-data.md",  # stub H1; injected once before ch.8
}

PART2_HEADING = "# II 任意サイズのデータ (Arbitrarily Large Data)\n"


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.is_file():
        raise SystemExit(f"missing {rel}")
    return path.read_text(encoding="utf-8")


def front_matter_only(text: str) -> str:
    cut = text.find("\n# 目次")
    if cut < 0:
        cut = text.find("# 目次")
    if cut < 0:
        raise SystemExit("00-toc-and-front.md: '# 目次' not found")
    return text[:cut].rstrip() + "\n\n"


def normalize_appendix(text: str, rel: str) -> str:
    """First 付録 heading becomes H1 so each appendix file is one unit."""
    lines = text.splitlines(keepends=True)
    if not lines:
        return text
    # Promote the first markdown heading if it names an appendix.
    for i, line in enumerate(lines):
        m = re.match(r"^(#{1,6})\s+(.*付録.*)$", line.rstrip("\n"))
        if m:
            title = m.group(2).strip()
            lines[i] = f"# {title}\n"
            break
    text = "".join(lines)
    if rel == "16-appendix-htdp-langs-00-index.md":
        # Extra H1 would reset 本文/付録 detection and duplicate the TOC.
        text = text.replace(
            "# How to Design Programs 言語\n",
            "## How to Design Programs 言語\n",
            1,
        )
    return text


def combine() -> str:
    parts: list[str] = []
    log: list[str] = []

    def add(rel: str, body: str) -> None:
        parts.append(body.rstrip() + "\n\n")
        log.append(f"  + {rel}")

    add("00-toc-and-front.md (title only)", front_matter_only(read("00-toc-and-front.md")))
    for rel in BODY_AFTER_FRONT:
        add(rel, read(rel))
    add("[heading] II 任意サイズのデータ", PART2_HEADING)
    for rel in PART2_CHAPTERS:
        add(rel, read(rel))
    for rel in BODY_AFTER_PART2:
        add(rel, read(rel))
    log.append("  -- appendix --")
    for rel in APPENDIX:
        add(rel, normalize_appendix(read(rel), rel))

    stray = sorted(
        p.name
        for p in ROOT.glob("??-*.md")
        if p.name not in SKIP
        and p.name != "00-toc-and-front.md"
        and p.name not in BODY_AFTER_FRONT
        and p.name not in PART2_CHAPTERS
        and p.name not in BODY_AFTER_PART2
        and p.name not in APPENDIX
    )
    if stray:
        raise SystemExit("unlisted ??-*.md (add to combine_book.py or SKIP): " + ", ".join(stray))

    sys.stderr.write("=== combine order (本文 → 付録) ===\n")
    sys.stderr.write("\n".join(log) + "\n")
    return "".join(parts)


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("-")
    text = combine()
    if str(out) == "-":
        sys.stdout.write(text)
    else:
        out.parent.mkdir(parents=True, exist_ok=True)
        tmp = out.with_suffix(out.suffix + ".partial")
        tmp.write_text(text, encoding="utf-8")
        tmp.replace(out)
        sys.stderr.write(f"Combined -> {out} ({out.stat().st_size} bytes)\n")


if __name__ == "__main__":
    main()
