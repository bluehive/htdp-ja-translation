#!/usr/bin/env python3
"""
Restore broken ASCII Figure boxes in Japanese drafts using official HTML RktBlk code.

Only rewrites fenced blocks whose body contains a classic +--- box AND a Figure/図 N
caption. Dual RktBlk figures become dual ```racket fences (86/87 style).

Usage:
  python3 tools/fix_ascii_figures.py              # Part III+ book chapters (07–14)
  python3 tools/fix_ascii_figures.py --report-only
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from bs4 import BeautifulSoup  # noqa: E402
from extract_to_markdown import extract_code_block  # noqa: E402

HTML_FOR_MD_PREFIX = {
    range(7, 8): "part_three.html",  # 07
}


def html_for_md(md_name: str) -> str | None:
    n = int(md_name[:2])
    return {
        7: "part_three.html",
        8: "i3-4.html",
        10: "i4-5.html",
        12: "i5-6.html",
    }.get(n)


def pretty_racket(s: str) -> str:
    s = s.strip()
    if s.count("\n") >= 3:
        return s
    s = re.sub(r";\s*;\s*", "\n; ", s)
    s = re.sub(r"\)\s*;\s*", ")\n; ", s)
    s = re.sub(r"(?<!\n)\(define\s*\(", "\n(define (", s)
    s = re.sub(r"(?<!\n)\(define-struct\s+", "\n(define-struct ", s)
    s = re.sub(r"(?<!\n)\(check-expect\s+", "\n(check-expect ", s)
    s = re.sub(r"\s+\[\(empty\?", "\n  [(empty?", s)
    s = re.sub(r"\s+\[else\b", "\n  [else", s)
    return "\n".join(ln.rstrip() for ln in s.splitlines() if ln.strip())


def load_figures(html_name: str) -> dict[int, dict]:
    path = ROOT / "original_html" / html_name
    soup = BeautifulSoup(path.read_text(encoding="utf-8", errors="ignore"), "html.parser")
    figs: dict[int, dict] = {}
    for leg in soup.select(".Legend"):
        text = leg.get_text(" ", strip=True)
        m = re.search(r"Figure[\s\xa0]*(\d+)", text)
        if not m:
            continue
        n = int(m.group(1))
        fig = leg
        FIGURE_CLASSES = {
            "Figure",
            "Herefigure",
            "Centerfigure",
            "Leftfigure",
            "Rightfigure",
        }
        for _ in range(12):
            if fig is None:
                break
            if set(fig.get("class") or []) & FIGURE_CLASSES:
                break
            fig = fig.parent
        # If we walked out without hitting a figure class, skip
        if fig is None or not (set(fig.get("class") or []) & FIGURE_CLASSES):
            continue
        inside = fig.select_one(".FigureInside") or fig
        codes: list[str] = []
        for b in inside.select("table.RktBlk"):
            parent = b.find_parent("table", class_="RktBlk")
            if parent is not None and parent is not b:
                continue
            c = extract_code_block(b)
            if c.strip():
                codes.append(pretty_racket(c))
        imgs = []
        for im in inside.find_all("img"):
            src = (im.get("src") or "").strip()
            if src:
                imgs.append(Path(src).name)
        # Grammar / notation tables (e.g. for loops, match)
        prose = ""
        if not codes and not imgs:
            tplain = inside.get_text("\n", strip=True)
            # drop legend echo
            tplain = re.sub(r"^Figure[\s\xa0]*\d+\s*:\s*[^\n]*\n?", "", tplain)
            if tplain.strip():
                prose = tplain.strip()
        if codes or imgs or prose:
            figs[n] = {"title": text, "codes": codes, "images": imgs, "prose": prose}
    return figs


def build_md(n: int, info: dict) -> str:
    title = re.sub(r"^Figure[\s\xa0]*\d+\s*:\s*", "", info["title"], flags=re.I).strip()
    codes = info.get("codes") or []
    images = info.get("images") or []
    prose = info.get("prose") or ""
    out = [f"> **図{n}: {title}**"]
    if len(codes) >= 2:
        out.append("> 左右対比（崩れた ASCII 枠を二重 fence に復元。コードは公式 HTML の RktBlk より）。")
        out.append("")
        labs = ["左", "右"] + [f"ブロック{i+1}" for i in range(2, 20)]
        for i, c in enumerate(codes):
            out.extend([f"**{labs[i]}**", "", "```racket", c.rstrip(), "```", ""])
    elif len(codes) == 1:
        out.extend(["", "```racket", codes[0].rstrip(), "```", ""])
    if images:
        out.append("")
        out.append("> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:")
        for name in images:
            out.append(">")
            out.append(f"> [image: {name}]")
        out.append("")
    if prose and not codes:
        out.append("")
        out.append("```")
        out.append(prose)
        out.append("```")
        out.append("")
    if not codes and not images and not prose:
        out.append("")
        out.append("> （原本 Figure の構造化に失敗。HTML を参照。）")
        out.append("")
    return "\n".join(out).rstrip() + "\n\n"


def is_broken_ascii_figure_fence(body: str) -> int | None:
    """Return figure number if this fence body is a broken +--- Figure box."""
    if "+---" not in body:
        return None
    m = re.search(r"Figure\s*(\d+)|図\s*(\d+)", body)
    if not m:
        return None
    # Prefer caption line inside the box
    return int(m.group(1) or m.group(2))


def is_fence_open(line: str) -> bool:
    s = line.strip()
    return s.startswith("```")


def is_fence_close(line: str) -> bool:
    return line.strip() == "```"


def fix_markdown(md_path: Path, figs: dict[int, dict], *, dry: bool) -> list[str]:
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    report: list[str] = []
    while i < len(lines):
        if is_fence_open(lines[i]):
            open_line = lines[i]
            j = i + 1
            body_lines: list[str] = []
            while j < len(lines) and not is_fence_close(lines[j]):
                body_lines.append(lines[j])
                j += 1
            body = "".join(body_lines)
            num = is_broken_ascii_figure_fence(body)
            # Only bare ``` openers that start with an ASCII figure box
            if (
                open_line.strip() == "```"
                and num is not None
                and num in figs
                and j < len(lines)
            ):
                first = next((ln.strip() for ln in body_lines if ln.strip()), "")
                if first.startswith("+---") or first.startswith("| Figure") or first.startswith("| 図"):
                    rep = build_md(num, figs[num])
                    out.append(rep)
                    report.append(
                        f"{md_path.name}: Figure {num} ({len(figs[num]['codes'])} code block(s))"
                    )
                    i = j + 1
                    continue
            out.append(open_line)
            out.extend(body_lines)
            if j < len(lines):
                out.append(lines[j])
            i = j + 1
            continue
        out.append(lines[i])
        i += 1
    if report and not dry:
        md_path.write_text("".join(out), encoding="utf-8")
    return report


def inventory(md_path: Path) -> list[str]:
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    hits = []
    i = 0
    while i < len(lines):
        if is_fence_open(lines[i]):
            open_line = lines[i]
            j = i + 1
            body: list[str] = []
            while j < len(lines) and not is_fence_close(lines[j]):
                body.append(lines[j])
                j += 1
            b = "\n".join(body)
            num = is_broken_ascii_figure_fence(b)
            if open_line.strip() == "```" and num is not None:
                first = next((ln.strip() for ln in body if ln.strip()), "")
                if first.startswith("+---") or first.startswith("|"):
                    hits.append(f"{md_path.name}:{i+1} Figure {num}")
            i = j + 1
        else:
            i += 1
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--report-only", action="store_true")
    ap.add_argument("--all-translated", action="store_true", help="Also scan 00-46 (still only broken +--- figures)")
    args = ap.parse_args()

    if args.all_translated:
        md_files = sorted(ROOT.glob("??-*.md"))
    else:
        md_files = [
            f
            for f in sorted(ROOT.glob("??-*.md"))
            if f.name[:2].isdigit() and 7 <= int(f.name[:2]) <= 14
        ]

    if args.report_only:
        all_hits = []
        for md in md_files:
            all_hits.extend(inventory(md))
        print(f"Broken ASCII figure fences: {len(all_hits)}")
        for h in all_hits:
            print(h)
        return 0

    cache: dict[str, dict[int, dict]] = {}
    all_report: list[str] = []
    for md in md_files:
        html = html_for_md(md.name)
        if not html:
            continue
        if html not in cache:
            cache[html] = load_figures(html)
            print(f"loaded {html}: {len(cache[html])} figures with code")
        rep = fix_markdown(md, cache[html], dry=False)
        all_report.extend(rep)
        if rep:
            print(f"wrote {md.name} ({len(rep)} fixes)")

    out = ROOT / "build" / "ascii-figures-fix-report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        "# ASCII figure fix report\n\n"
        f"- fixes: **{len(all_report)}**\n\n"
        + "\n".join(f"- {r}" for r in all_report)
        + "\n",
        encoding="utf-8",
    )
    print(f"Total fixes: {len(all_report)}")
    print(f"Report -> {out}")

    # leftover inventory
    left = []
    for md in md_files:
        left.extend(inventory(md))
    print(f"Remaining broken ASCII figures in scope: {len(left)}")
    for h in left:
        print("  still:", h)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
