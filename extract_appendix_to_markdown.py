#!/usr/bin/env python3
"""
Extract prose, code, and diagrams from appendix_original_html/ into
extracted/appendix/<manual>/original_markdown_**.md files.

These are the canonical English sources for appendix translation work
(same role as extracted/original_markdown_**.md for the main book).

Reuses the converter from extract_to_markdown.py (Scribble/Racket docs HTML).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

# Reuse HTDP/Scribble converter
from extract_to_markdown import Converter

ROOT = Path(__file__).resolve().parent
HTML_ROOT = ROOT / "appendix_original_html"
OUT_ROOT = ROOT / "extracted" / "appendix"

# Preferred ordering within a manual (TOC-like pages first).
PRIORITY_NAMES = [
    "index.html",
    "beginner.html",
    "beginner-abbr.html",
    "intermediate.html",
    "intermediate-lam.html",
    "advanced.html",
    "windowing-overview.html",
    "Widget_Gallery.html",
    "Windowing_Classes.html",
    "Windowing_Functions.html",
    "editor-overview.html",
    "Snip_and_Style_Classes.html",
    "Editor_Classes.html",
    "Editor_Functions.html",
    "WXME_Decoding.html",
    "mredprefs.html",
    "Dynamic_Loading.html",
    "Startup_Actions.html",
    "Init_Libraries.html",
    "libs.html",
    "doc-index.html",
]


def sort_html_files(files: list[Path]) -> list[Path]:
    prio = {name: i for i, name in enumerate(PRIORITY_NAMES)}

    def key(p: Path):
        name = p.name
        if name in prio:
            return (0, prio[name], name.lower())
        # class reference pages after overview
        return (1, name.lower())

    return sorted(files, key=key)


def process_manual(manual_dir: Path) -> list[Path]:
    html_files = sort_html_files(list(manual_dir.rglob("*.html")))
    if not html_files:
        print(f"  (no html in {manual_dir.name})")
        return []

    out_dir = OUT_ROOT / manual_dir.name
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    width = max(2, len(str(len(html_files) - 1)))
    for i, src in enumerate(html_files):
        rel = src.relative_to(manual_dir)
        # stable filename: original_markdown_00_index.md
        stem = src.stem
        # sanitize stem for filesystem
        safe = re.sub(r"[^\w.\-]+", "_", stem)
        out_name = f"original_markdown_{i:0{width}d}_{safe}.md"
        out_path = out_dir / out_name

        html = src.read_text(encoding="utf-8", errors="replace")
        soup = BeautifulSoup(html, "lxml")
        main = (
            soup.select_one("div.main")
            or soup.select_one("div.maincolumn")
            or soup.body
        )
        if main is None:
            print(f"  WARN: no main content in {rel}")
            continue

        source_label = f"appendix_original_html/{manual_dir.name}/{rel.as_posix()}"
        md = Converter(source_label).convert(main)
        # Prefix with appendix metadata
        header = (
            f"<!-- Appendix manual: {manual_dir.name} -->\n"
            f"<!-- Source URL path: /{manual_dir.name}/{rel.as_posix()} -->\n"
            f"<!-- Canonical English source for Japanese appendix translation -->\n\n"
        )
        # Converter already adds Extracted-from comments; keep both.
        out_path.write_text(header + md, encoding="utf-8")
        size = out_path.stat().st_size
        print(f"  [{i:0{width}d}] {out_name} <- {rel} ({size:,} bytes)")
        written.append(out_path)

    # Per-manual README
    lines = [
        f"# Appendix: `{manual_dir.name}` — original markdown (English source)",
        "",
        f"Extracted from `appendix_original_html/{manual_dir.name}/`.",
        "These files are the **canonical English source** for translating this appendix.",
        "",
        "| # | Source HTML | Extracted markdown |",
        "|---|-------------|--------------------|",
    ]
    for i, src in enumerate(html_files):
        stem = re.sub(r"[^\w.\-]+", "_", src.stem)
        out_name = f"original_markdown_{i:0{width}d}_{stem}.md"
        lines.append(
            f"| {i:0{width}d} | `{src.relative_to(manual_dir).as_posix()}` | `{out_name}` |"
        )
    lines.append("")
    (out_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return written


def main() -> int:
    if not HTML_ROOT.is_dir():
        print(
            f"ERROR: {HTML_ROOT} not found. Run download_appendix_docs.py first.",
            file=sys.stderr,
        )
        return 1

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    manuals = sorted(
        d for d in HTML_ROOT.iterdir() if d.is_dir() and any(d.rglob("*.html"))
    )
    if not manuals:
        print("ERROR: no manuals with HTML found.", file=sys.stderr)
        return 1

    all_written: list[Path] = []
    for manual in manuals:
        print(f"\n=== Extract {manual.name} ===")
        all_written.extend(process_manual(manual))

    # Top-level appendix index
    index_lines = [
        "# Appendix original markdown (English translation sources)",
        "",
        "Racket documentation manuals downloaded for use as **appendices**",
        "to the HTDP Japanese translation project.",
        "",
        "## Seeds",
        "",
        "- https://docs.racket-lang.org/quick/index.html",
        "- https://docs.racket-lang.org/htdp-langs/index.html",
        "- https://docs.racket-lang.org/racket-cheat/index.html",
        "- https://docs.racket-lang.org/gui/index.html",
        "",
        "## Workflow",
        "",
        "1. `appendix_original_html/<manual>/*.html` — downloaded originals",
        "2. **`extracted/appendix/<manual>/original_markdown_**.md`** — **translation source of truth**",
        "3. (future) Japanese appendix drafts under a agreed path, e.g. `appendix-ja/`",
        "",
        "Regenerate downloads:",
        "",
        "```bash",
        "python3 download_appendix_docs.py",
        "```",
        "",
        "Regenerate markdown extracts:",
        "",
        "```bash",
        "python3 extract_appendix_to_markdown.py",
        "```",
        "",
        "## Manuals",
        "",
    ]
    for manual in manuals:
        out_dir = OUT_ROOT / manual.name
        mds = sorted(out_dir.glob("original_markdown_*.md")) if out_dir.is_dir() else []
        index_lines.append(
            f"- **`{manual.name}/`** — {len(mds)} pages "
            f"(see [`{manual.name}/README.md`]({manual.name}/README.md))"
        )
    index_lines.append("")
    (OUT_ROOT / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    print(f"\nDone. Wrote {len(all_written)} markdown files under extracted/appendix/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
