#!/usr/bin/env python3
"""
HtDP / Racket-doc figure assets for the Japanese translation.

Issue #9 (figures p0):
  - Download official PNG assets automatically (not hand-captioned).
  - Keep binaries out of git (assets/htdp-figures/ is gitignored).
  - Expand `[image: …]` placeholders to Markdown images at build time.

Usage:
  python3 tools/htdp_figures.py fetch [--force] [--report PATH]
  python3 tools/htdp_figures.py expand --in FILE --out FILE [--source book|quick|…]
  python3 tools/htdp_figures.py report [--out PATH]
  python3 tools/htdp_figures.py expand-tree   # rewrite each ??-*.md into build/expanded/
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets" / "htdp-figures"
BUILD = ROOT / "build"
HTML_BOOK = ROOT / "original_html"
HTML_APPENDIX = ROOT / "appendix_original_html"

# Prefer the edition already used by download_book.py
BOOK_BASE = "https://htdp.org/2026-5-28/Book/"
SOURCE_BASES: dict[str, str] = {
    "book": BOOK_BASE,
    "quick": "https://docs.racket-lang.org/quick/",
    "htdp-langs": "https://docs.racket-lang.org/htdp-langs/",
    "racket-cheat": "https://docs.racket-lang.org/racket-cheat/",
    "gui": "https://docs.racket-lang.org/gui/",
}

# `[image: pict_240.png]` or `[image:pict_240.png]` or with alt after em dash
PLACEHOLDER_RE = re.compile(
    r"\[image:\s*([^\]\s—]+)(?:\s*[—-]\s*([^\]]+))?\]"
)
IMG_SRC_RE = re.compile(
    r"""src\s*=\s*["']([^"']+\.(?:png|gif|jpe?g|svg))["']""",
    re.I,
)

USER_AGENT = "htdp-ja-translation-figures/1.0 (+https://github.com/bluehive/htdp-ja-translation)"


def source_for_md_name(name: str) -> str:
    """Map a Japanese draft filename to an image source bucket."""
    base = Path(name).name
    if "appendix-quick" in base:
        return "quick"
    if "appendix-htdp-langs" in base:
        return "htdp-langs"
    if "appendix-gui" in base:
        return "gui"
    if "appendix-racket-cheat" in base:
        return "racket-cheat"
    return "book"


def asset_rel(source: str, filename: str) -> str:
    """POSIX path relative to repo root (for Markdown + pandoc --resource-path)."""
    return f"assets/htdp-figures/{source}/{filename}"


def asset_path(source: str, filename: str) -> Path:
    return ASSETS / source / filename


def discover_html_index() -> dict[str, set[str]]:
    """filename -> set of sources that reference it in local HTML."""
    index: dict[str, set[str]] = defaultdict(set)

    def absorb(path: Path, source: str) -> None:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            return
        for src in IMG_SRC_RE.findall(text):
            index[Path(src).name].add(source)

    if HTML_BOOK.is_dir():
        for html in HTML_BOOK.glob("*.html"):
            absorb(html, "book")

    if HTML_APPENDIX.is_dir():
        for manual in SOURCE_BASES:
            if manual == "book":
                continue
            d = HTML_APPENDIX / manual
            if not d.is_dir():
                continue
            for html in d.rglob("*.html"):
                absorb(html, manual)

    return index


def collect_needed_from_markdown() -> dict[tuple[str, str], list[str]]:
    """
    (source, filename) -> list of referring draft basenames.
    Source is inferred from the draft filename (book vs appendix manual).
    """
    needed: dict[tuple[str, str], list[str]] = defaultdict(list)
    for md in sorted(ROOT.glob("??-*.md")):
        source = source_for_md_name(md.name)
        text = md.read_text(encoding="utf-8")
        for m in PLACEHOLDER_RE.finditer(text):
            filename = m.group(1).strip()
            needed[(source, filename)].append(md.name)
    return needed


def download_one(url: str, dest: Path, *, force: bool = False) -> tuple[str, str]:
    """
    Returns (status, detail) where status is:
      ok | skip | fail
    """
    if dest.exists() and dest.stat().st_size > 0 and not force:
        return "skip", f"exists ({dest.stat().st_size} bytes)"

    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = resp.read()
            ctype = (resp.headers.get("Content-Type") or "").lower()
    except urllib.error.HTTPError as e:
        return "fail", f"HTTP {e.code} {url}"
    except Exception as e:  # noqa: BLE001 — report any network failure
        return "fail", f"{type(e).__name__}: {e} ({url})"

    if not data:
        return "fail", f"empty body {url}"
    if "html" in ctype and not dest.suffix.lower() in {".html", ".htm"}:
        # soft 404 pages sometimes return 200 text/html
        head = data[:200].lstrip().lower()
        if head.startswith(b"<!doctype") or head.startswith(b"<html"):
            return "fail", f"got HTML instead of image ({url})"

    dest.write_bytes(data)
    return "ok", f"{len(data)} bytes -> {dest.relative_to(ROOT)}"


def resolve_url(source: str, filename: str, html_index: dict[str, set[str]]) -> list[str]:
    """Candidate download URLs, preferred source first then other known homes."""
    bases_order: list[str] = [source]
    for alt in html_index.get(filename, set()):
        if alt not in bases_order:
            bases_order.append(alt)
    for alt in SOURCE_BASES:
        if alt not in bases_order:
            bases_order.append(alt)

    urls: list[str] = []
    for s in bases_order:
        base = SOURCE_BASES.get(s)
        if not base:
            continue
        urls.append(base.rstrip("/") + "/" + filename)
    # de-dupe preserve order
    seen: set[str] = set()
    out: list[str] = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def cmd_fetch(args: argparse.Namespace) -> int:
    html_index = discover_html_index()
    needed = collect_needed_from_markdown()
    if not needed:
        print("No [image: …] placeholders found in ??-*.md", file=sys.stderr)
        return 1

    ok = skip = fail = 0
    failures: list[str] = []
    successes: list[str] = []

    items = sorted(needed.items(), key=lambda kv: (kv[0][0], kv[0][1]))
    print(f"Fetching {len(items)} unique (source, file) pairs into {ASSETS.relative_to(ROOT)}/")

    for (source, filename), refs in items:
        dest = asset_path(source, filename)
        urls = resolve_url(source, filename, html_index)
        status = "fail"
        detail = "no URL candidates"
        used_url = ""
        for url in urls:
            status, detail = download_one(url, dest, force=args.force)
            used_url = url
            if status in {"ok", "skip"}:
                break
            # try next URL on fail
        if status == "ok":
            ok += 1
            successes.append(f"OK   {source}/{filename}  {detail}")
        elif status == "skip":
            skip += 1
            successes.append(f"SKIP {source}/{filename}  {detail}")
        else:
            fail += 1
            ref_s = ", ".join(sorted(set(refs))[:5])
            failures.append(f"FAIL {source}/{filename}  {detail}  (refs: {ref_s})")
        # polite pacing only on network hits
        if status == "ok":
            time.sleep(args.sleep)

        if args.verbose and status != "skip":
            print(f"  [{status}] {source}/{filename} <- {used_url} ({detail})")

    report_lines = [
        "# HtDP figures fetch report",
        "",
        f"- needed pairs: **{len(items)}**",
        f"- downloaded: **{ok}**",
        f"- skipped (already present): **{skip}**",
        f"- failed: **{fail}**",
        f"- assets dir: `{ASSETS.relative_to(ROOT)}/` (gitignored)",
        "",
    ]
    if failures:
        report_lines.append("## Failures")
        report_lines.append("")
        report_lines.extend(f"- `{line}`" for line in failures)
        report_lines.append("")
    report_lines.append("## Notes")
    report_lines.append("")
    report_lines.append(
        "Images are intentionally not committed. Re-run "
        "`python3 tools/htdp_figures.py fetch` after clone."
    )
    report_lines.append("")

    report_path = Path(args.report) if args.report else BUILD / "figures-report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(f"Downloaded: {ok}, skipped: {skip}, failed: {fail}")
    print(f"Report -> {report_path}")
    if failures:
        print("Failures:", file=sys.stderr)
        for line in failures[:20]:
            print(f"  {line}", file=sys.stderr)
        if len(failures) > 20:
            print(f"  … and {len(failures) - 20} more", file=sys.stderr)
    # Non-zero only if everything failed; partial success is still usable
    return 0 if (ok + skip) > 0 else 1


def md_image(source: str, filename: str, alt: str | None) -> str:
    label = (alt or filename).strip() or filename
    # Escape rare brackets in alt
    label = label.replace("[", "\\[").replace("]", "\\]")
    return f"![{label}]({asset_rel(source, filename)})"


def _line_is_image_only(line: str) -> bool:
    """True if line is only placeholders (+ whitespace / table pipes / blockquote markers)."""
    # strip blockquote prefix repeatedly
    s = line.strip()
    while s.startswith(">"):
        s = s[1:].lstrip()
    # remove table pipes and spaces
    core = re.sub(r"[|\s]", "", s)
    if not core:
        return False
    # remove all placeholders; leftover should be empty
    leftover = PLACEHOLDER_RE.sub("", s)
    leftover = re.sub(r"[|\s>`]", "", leftover)
    return leftover == "" and PLACEHOLDER_RE.search(s) is not None


def expand_text(text: str, source: str, *, lift_fence_images: bool = True) -> tuple[str, int]:
    """
    Expand placeholders. Returns (new_text, replacement_count).

    Inside fenced code blocks, pure-image lines are lifted out of the fence
    so Pandoc/Typst can embed the PNG. Mixed code lines keep a short
    textual marker (filename) so Racket examples stay readable.
    """
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    count = 0
    in_fence = False
    fence_lang = ""
    pending_code: list[str] = []

    def close_code_if_open() -> None:
        if pending_code:
            out.append(f"```{fence_lang}\n")
            out.extend(pending_code)
            out.append("```\n")
            pending_code.clear()

    def fence_lang_of(line: str) -> str:
        return line.strip()[3:].strip()

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.lstrip("\ufeff")
        if stripped.startswith("```"):
            if not in_fence:
                in_fence = True
                fence_lang = fence_lang_of(stripped)
                pending_code = []
            else:
                close_code_if_open()
                in_fence = False
                fence_lang = ""
            i += 1
            continue

        if in_fence:
            if lift_fence_images and _line_is_image_only(line):
                if pending_code:
                    out.append(f"```{fence_lang}\n")
                    out.extend(pending_code)
                    out.append("```\n\n")
                    pending_code = []
                pieces: list[str] = []
                for m in PLACEHOLDER_RE.finditer(line):
                    count += 1
                    pieces.append(md_image(source, m.group(1).strip(), m.group(2)))
                out.append("\n\n".join(pieces) + "\n\n")
            else:

                def repl_code(m: re.Match[str]) -> str:
                    nonlocal count
                    count += 1
                    return f"<image:{m.group(1).strip()}>"

                pending_code.append(PLACEHOLDER_RE.sub(repl_code, line))
            i += 1
            continue

        def repl_out(m: re.Match[str]) -> str:
            nonlocal count
            count += 1
            return md_image(source, m.group(1).strip(), m.group(2))

        out.append(PLACEHOLDER_RE.sub(repl_out, line))
        i += 1

    if in_fence:
        close_code_if_open()

    return "".join(out), count


def cmd_expand(args: argparse.Namespace) -> int:
    in_path = Path(args.input)
    text = in_path.read_text(encoding="utf-8")
    source = args.source or source_for_md_name(in_path.name)
    new_text, n = expand_text(text, source, lift_fence_images=not args.no_lift)
    out_path = Path(args.output) if args.output else in_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(new_text, encoding="utf-8")
    print(f"Expanded {n} placeholders ({source}) -> {out_path}")
    return 0


def cmd_expand_tree(args: argparse.Namespace) -> int:
    """Expand each root ??-*.md into build/expanded/ for the build pipeline."""
    out_dir = Path(args.out_dir) if args.out_dir else BUILD / "expanded"
    out_dir.mkdir(parents=True, exist_ok=True)
    total = 0
    files = sorted(ROOT.glob("??-*.md"))
    for md in files:
        source = source_for_md_name(md.name)
        text = md.read_text(encoding="utf-8")
        new_text, n = expand_text(text, source, lift_fence_images=not args.no_lift)
        dest = out_dir / md.name
        dest.write_text(new_text, encoding="utf-8")
        total += n
        print(f"  {md.name}: {n} expansions -> {dest.relative_to(ROOT)}")
    print(f"Total expansions: {total}")
    # write list for shell
    list_path = out_dir / "filelist.txt"
    list_path.write_text("\n".join(str(out_dir / m.name) for m in files) + "\n", encoding="utf-8")
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    needed = collect_needed_from_markdown()
    present = missing = 0
    rows: list[str] = []
    for (source, filename), refs in sorted(needed.items()):
        p = asset_path(source, filename)
        if p.exists() and p.stat().st_size > 0:
            present += 1
            status = "ok"
        else:
            missing += 1
            status = "MISSING"
        rows.append(
            f"| `{source}/{filename}` | {status} | {len(set(refs))} | {', '.join(sorted(set(refs))[:3])} |"
        )

    bare = 0
    for md in ROOT.glob("??-*.md"):
        bare += len(PLACEHOLDER_RE.findall(md.read_text(encoding="utf-8")))

    lines = [
        "# HtDP figures inventory (report-only gate)",
        "",
        f"- placeholder occurrences in drafts: **{bare}**",
        f"- unique (source, file) pairs: **{len(needed)}**",
        f"- present on disk: **{present}**",
        f"- missing on disk: **{missing}**",
        "",
        "| asset | status | ref files | sample refs |",
        "|-------|--------|-----------|-------------|",
        *rows,
        "",
    ]
    out = Path(args.out) if args.out else BUILD / "figures-inventory.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Inventory -> {out} (present={present}, missing={missing}, bare_placeholders={bare})")
    if args.fail_on_missing and missing:
        return 2
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fetch", help="Download figure PNGs referenced by ??-*.md")
    f.add_argument("--force", action="store_true", help="Re-download even if present")
    f.add_argument("--sleep", type=float, default=0.15, help="Delay between successful downloads")
    f.add_argument("--report", type=str, default="", help="Report markdown path")
    f.add_argument("-v", "--verbose", action="store_true")
    f.set_defaults(func=cmd_fetch)

    e = sub.add_parser("expand", help="Expand placeholders in one markdown file")
    e.add_argument("--in", dest="input", required=True)
    e.add_argument("--out", dest="output", default="")
    e.add_argument("--source", default="", help="Override source bucket (book/quick/…)")
    e.add_argument("--no-lift", action="store_true", help="Do not lift pure-image lines out of fences")
    e.set_defaults(func=cmd_expand)

    t = sub.add_parser("expand-tree", help="Expand all root ??-*.md into build/expanded/")
    t.add_argument("--out-dir", default="")
    t.add_argument("--no-lift", action="store_true")
    t.set_defaults(func=cmd_expand_tree)

    r = sub.add_parser("report", help="Write inventory of placeholders vs downloaded assets")
    r.add_argument("--out", default="")
    r.add_argument("--fail-on-missing", action="store_true")
    r.set_defaults(func=cmd_report)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
