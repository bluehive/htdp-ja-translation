#!/usr/bin/env python3
"""
Extract prose, code, and diagrams from HtDP 2e original_html into
extracted/original_markdown_**.md files.

Diagrams / figures are rendered as ASCII art (or ASCII-framed text tables /
code). These files are the canonical English source for translation work.
"""

from __future__ import annotations

import html as html_lib
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parent
HTML_DIR = ROOT / "original_html"
OUT_DIR = ROOT / "extracted"

PAGES: list[tuple[str, str]] = [
    ("00", "index.html"),
    ("01", "part_preface.html"),
    ("02", "part_prologue.html"),
    ("03", "part_one.html"),
    ("04", "i1-2.html"),
    ("05", "part_two.html"),
    ("06", "i2-3.html"),
    ("07", "part_three.html"),
    ("08", "i3-4.html"),
    ("09", "part_four.html"),
    ("10", "i4-5.html"),
    ("11", "part_five.html"),
    ("12", "i5-6.html"),
    ("13", "part_six.html"),
    ("14", "part_epilogue.html"),
]

REMOVE_SELECTORS = (
    ".navsettop",
    ".navsetbottom",
    ".versionbox",
    ".tocset",
    ".button-group",
    "script",
    "style",
)


def nbsp_to_space(s: str) -> str:
    return s.replace("\xa0", " ").replace("\u200b", "")


def normalize_prose(text: str) -> str:
    text = html_lib.unescape(nbsp_to_space(text))
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def word_wrap(text: str, width: int = 78) -> list[str]:
    """Wrap text on word boundaries."""
    text = normalize_prose(text).replace("\n", " ")
    if not text:
        return [""]
    words = text.split(" ")
    lines: list[str] = []
    cur = ""
    for w in words:
        if not w:
            continue
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= width:
            cur = cur + " " + w
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def is_skip_inline(tag: Tag) -> bool:
    classes = set(tag.get("class") or [])
    if classes & {
        "refelem",
        "refcolumn",
        "refcontent",
        "refpara",
        "button-group",
        "heading-anchor",
    }:
        return True
    if tag.name in ("script", "style"):
        return True
    return False


def collect_margin_notes(node: Tag) -> list[str]:
    notes = []
    for el in node.select(".refcontent"):
        t = normalize_prose(el.get_text(" "))
        if t:
            notes.append(t)
    return notes


def racket_text(node: Tag) -> str:
    """Reconstruct Racket source from a node, preserving spaces/indentation."""

    def walk(n: Tag | NavigableString) -> str:
        if isinstance(n, NavigableString):
            return nbsp_to_space(str(n))
        if not isinstance(n, Tag):
            return ""
        if n.name in ("script", "style"):
            return ""
        if n.name == "br":
            return "\n"
        classes = set(n.get("class") or [])
        if "hspace" in classes:
            return nbsp_to_space(n.get_text()) or " "
        if n.name == "img":
            src = n.get("src") or "image"
            return f"[image:{src}]"
        return "".join(walk(c) for c in n.children)

    text = walk(node)
    lines = [ln.rstrip() for ln in text.split("\n")]
    return "\n".join(lines).rstrip()


def extract_code_block(node: Tag) -> str:
    table = (
        node
        if node.name == "table" and "RktBlk" in (node.get("class") or [])
        else node.find("table", class_="RktBlk")
    )
    if table is not None:
        lines: list[str] = []
        for tr in table.find_all("tr", recursive=False):
            tds = tr.find_all("td", recursive=False)
            if not tds:
                continue
            col_texts = [racket_text(td) for td in tds]
            # multi-column rare; join with two spaces
            line = "  ".join(col_texts)
            lines.append(line)
        return "\n".join(lines).rstrip()

    # Multiple <p> lines
    paragraphs = [p for p in node.find_all("p", recursive=False)] or node.find_all("p")
    if paragraphs:
        return "\n".join(racket_text(p) for p in paragraphs).rstrip()

    return racket_text(node).rstrip()


def inline_md(node: Tag | NavigableString | None, *, skip_notes: bool = True) -> str:
    if node is None:
        return ""
    if isinstance(node, NavigableString):
        return nbsp_to_space(str(node))

    assert isinstance(node, Tag)
    if skip_notes and is_skip_inline(node):
        return ""
    name = (node.name or "").lower()
    classes = set(node.get("class") or [])

    if name in ("script", "style"):
        return ""
    if "button-group" in classes or "heading-anchor" in classes:
        return ""
    if name == "br":
        return "\n"
    if "hspace" in classes:
        return nbsp_to_space(node.get_text()) or " "
    if name == "img":
        src = node.get("src") or "image"
        alt = (node.get("alt") or "").strip()
        if alt and alt.lower() != "image":
            return f"[image: {src} — {alt}]"
        return f"[image: {src}]"

    if name in ("em", "i") or "emph" in classes:
        inner = "".join(inline_md(c, skip_notes=skip_notes) for c in node.children).strip()
        return f"*{inner}*" if inner else ""

    style = node.get("style") or ""
    if name in ("strong", "b") or "font-weight: bold" in style.replace(" ", ""):
        inner = "".join(inline_md(c, skip_notes=skip_notes) for c in node.children).strip()
        return f"**{inner}**" if inner else ""

    if name == "a":
        return "".join(inline_md(c, skip_notes=skip_notes) for c in node.children)

    if name == "code" or "stt" in classes:
        inner = "".join(inline_md(c, skip_notes=skip_notes) for c in node.children)
        inner = inner.strip()
        if inner and "\n" not in inner and "`" not in inner:
            return f"`{inner}`"
        return inner

    # Racket tokens inline
    if classes & {
        "RktPn",
        "RktSym",
        "RktVal",
        "RktValLink",
        "RktStxLink",
        "RktCmt",
        "RktRes",
        "RktVar",
        "RktErr",
        "RktOut",
        "RktIn",
        "RktInBG",
        "RktMeta",
    }:
        return racket_text(node)

    return "".join(inline_md(c, skip_notes=skip_notes) for c in node.children)


def ascii_box(title: str, body_lines: list[str], width: int = 78) -> str:
    content: list[str] = []
    if title:
        content.extend(word_wrap(title, width))
        content.append("")
    for line in body_lines:
        if line == "":
            content.append("")
        elif line.startswith(" ") or line.startswith("|") or line.startswith("+") or line.startswith("*") or re.match(r"^\d+\.", line):
            # preserve preformatted / list-ish lines; hard-wrap only if very long
            if len(line) <= width:
                content.append(line)
            else:
                content.extend(word_wrap(line, width))
        else:
            content.extend(word_wrap(line, width))

    while content and content[-1] == "":
        content.pop()
    w = min(max((len(x) for x in content), default=20), width)
    w = max(w, 20)
    top = "+" + "-" * (w + 2) + "+"
    out = [top]
    for line in content:
        if len(line) <= w:
            out.append(f"| {line.ljust(w)} |")
        else:
            out.append(f"| {line[:w]} |")
    out.append(top)
    return "\n".join(out)


def html_table_to_ascii(table: Tag, max_col: int = 36) -> list[str]:
    rows: list[list[str]] = []
    for tr in table.find_all("tr"):
        cells = tr.find_all(["td", "th"], recursive=False)
        if not cells:
            continue
        row = []
        for cell in cells:
            rkt = cell.find("table", class_="RktBlk")
            scode = cell.find(class_="SCodeFlow")
            if rkt is not None:
                txt = extract_code_block(rkt)
            elif scode is not None or cell.find(class_="RktPn"):
                txt = racket_text(cell)
            else:
                # avoid nested table double-count: take shallow text
                parts = []
                for c in cell.children:
                    if isinstance(c, Tag) and c.name == "table":
                        continue
                    parts.append(inline_md(c) if isinstance(c, Tag) else nbsp_to_space(str(c)))
                txt = normalize_prose("".join(parts))
            txt = re.sub(r"\s*\n\s*", " ⏎ ", txt)
            row.append(txt)
        if any(c.strip() for c in row):
            rows.append(row)

    if not rows:
        return []

    ncols = max(len(r) for r in rows)
    for r in rows:
        while len(r) < ncols:
            r.append("")

    cap = max_col if ncols > 2 else min(48, max_col + 12)
    col_w = [0] * ncols
    for r in rows:
        for i, c in enumerate(r):
            col_w[i] = min(max(col_w[i], len(c)), cap)

    def fmt(r: list[str]) -> str:
        parts = []
        for i, c in enumerate(r):
            if len(c) > col_w[i]:
                c = c[: max(0, col_w[i] - 1)] + "…"
            parts.append(c.ljust(col_w[i]))
        return "| " + " | ".join(parts) + " |"

    sep = "+-" + "-+-".join("-" * w for w in col_w) + "-+"
    out = [sep]
    for i, r in enumerate(rows):
        out.append(fmt(r))
        if i == 0:
            out.append(sep)
    out.append(sep)
    return out


def figure_to_ascii(fig: Tag) -> str:
    legend_el = fig.find(class_="Legend")
    legend = normalize_prose(legend_el.get_text(" ")) if legend_el else "Figure"
    inside = fig.find(class_="FigureInside") or fig

    body: list[str] = []

    # Images first
    for img in inside.find_all("img"):
        src = img.get("src") or "image"
        alt = (img.get("alt") or "").strip()
        if alt and alt.lower() != "image":
            body.append(f"[image: {src} — {alt}]")
        else:
            body.append(f"[image: {src}]")

    # Non-RktBlk tables
    seen_tables: set[int] = set()
    for table in inside.find_all("table"):
        if "RktBlk" in (table.get("class") or []):
            continue
        # top-level-ish within figure
        parent_table = table.find_parent("table")
        if parent_table is not None and parent_table in inside.find_all("table"):
            # still allow if parent is layout without content - keep all top-level
            if parent_table.find_parent(class_="FigureInside") or parent_table.find_parent(class_="Figure"):
                # skip nested
                if id(parent_table) in seen_tables or parent_table is not table:
                    if table.find_parent("table") is not None:
                        # only skip deeply nested duplicates
                        pass
        # Prefer outermost tables only
        if table.find_parent("table") is not None:
            continue
        seen_tables.add(id(table))
        rows = html_table_to_ascii(table)
        if rows:
            if body and body[-1] != "":
                body.append("")
            body.extend(rows)
            body.append("")

    # Code blocks
    for code in inside.select("blockquote.SCodeFlow, table.RktBlk"):
        if code.name == "table" and code.find_parent(class_="SCodeFlow"):
            continue
        if code.find_parent("table") and "RktBlk" in (code.get("class") or []):
            # may be inside larger layout table already rendered
            outer = code.find_parent("table")
            if outer is not None and "RktBlk" not in (outer.get("class") or []):
                # already part of table ascii if outer was rendered
                if id(outer) in seen_tables:
                    continue
        ctext = extract_code_block(code)
        if ctext:
            if body and body[-1] != "":
                body.append("")
            body.extend(ctext.split("\n"))
            body.append("")

    # Lists (design recipes)
    for lst in inside.find_all(["ol", "ul"]):
        if lst.find_parent(["ol", "ul"]) is not None:
            continue
        if lst.find_parent("table") is not None:
            continue
        if body and body[-1] != "":
            body.append("")
        items = lst.find_all("li", recursive=False)
        for i, li in enumerate(items, 1):
            ps = li.find_all("p", recursive=False) or li.find_all("p")
            if ps:
                head = normalize_prose(inline_md(ps[0]))
                prefix = f"{i}. " if lst.name == "ol" else "* "
                body.append(prefix + head)
                for p in ps[1:]:
                    for ln in word_wrap(normalize_prose(inline_md(p)), 72):
                        body.append("   " + ln)
            else:
                t = normalize_prose(inline_md(li))
                prefix = f"{i}. " if lst.name == "ol" else "* "
                body.append(prefix + t)
        body.append("")

    # Plain paragraphs if still sparse
    if len([ln for ln in body if ln.strip() and not ln.startswith("[image:")]) == 0:
        for p in inside.find_all("p"):
            if p.find_parent(class_="Legend"):
                continue
            if legend_el and (p in legend_el.descendants or p == legend_el):
                continue
            if p.find_parent(["ol", "ul", "table"]):
                continue
            t = normalize_prose(inline_md(p))
            if t:
                body.append(t)

    while body and body[-1] == "":
        body.pop()
    if not body:
        body = ["(diagram — content is graphical in the original; see HTML figure)"]

    boxed = ascii_box(legend, body, width=78)
    return "\n```\n" + boxed + "\n```\n"


def heading_text(tag: Tag) -> str:
    t = normalize_prose(inline_md(tag))
    t = t.replace("🔗", "").strip()
    # Scribble often glues section numbers to titles: "1Ready..." -> "1 Ready..."
    t = re.sub(r"^(\d+(?:\.\d+)*)([A-Za-z“\"])", r"\1 \2", t)
    t = t.replace("ℹ", "").strip()
    return t


def definition_box_to_md(box: Tag) -> str:
    """Convert Scribble SVInsetFlow / boxed definition tables to markdown."""
    label_el = box.select_one(".RBackgroundLabelInner")
    label = normalize_prose(label_el.get_text(" ")) if label_el else "def"

    lines: list[str] = []
    # Signature row(s): RForeground first, then argument rows
    foreground = box.select_one("p.RForeground")
    if foreground is not None:
        sig = normalize_prose(racket_text(foreground))
        if sig:
            lines.append(sig)
    else:
        # fallback: first non-label cell text
        for tr in box.select("table.boxed tr, table.RBoxed tr"):
            cell = tr.find("td")
            if not cell:
                continue
            if cell.select_one(".RBackgroundLabel"):
                # still may have RForeground inside
                fg = cell.select_one("p.RForeground")
                if fg:
                    sig = normalize_prose(racket_text(fg))
                    if sig:
                        lines.append(sig)
                continue
            row_txt = normalize_prose(racket_text(cell))
            if row_txt:
                lines.append(row_txt)

    # Remaining table rows (contract args) not already covered
    if foreground is not None:
        for tr in box.select("table.boxed tr, table.RBoxed tr"):
            cell = tr.find("td")
            if not cell or cell.select_one("p.RForeground"):
                continue
            row_txt = normalize_prose(racket_text(cell))
            if row_txt:
                lines.append(row_txt)

    # Nested code examples inside the box
    for code in box.select("blockquote.SCodeFlow, table.RktBlk"):
        if code.name == "table" and code.find_parent(class_="SCodeFlow"):
            continue
        ctext = extract_code_block(code)
        if ctext:
            lines.append("")
            lines.append("```racket")
            lines.extend(ctext.split("\n"))
            lines.append("```")

    body = "\n".join(lines).strip()
    if not body:
        body = normalize_prose(inline_md(box))

    # ASCII-framed definition for translation source stability
    header = f"[{label}]"
    framed = ascii_box(header, body.split("\n") if body else ["(empty definition)"])
    return "\n```\n" + framed + "\n```\n"


class Converter:
    def __init__(self, source_name: str):
        self.source_name = source_name
        self.out: list[str] = []
        self.seen: set[int] = set()

    def emit(self, s: str = "") -> None:
        self.out.append(s)

    def mark_tree(self, tag: Tag) -> None:
        self.seen.add(id(tag))
        for d in tag.descendants:
            if isinstance(d, Tag):
                self.seen.add(id(d))

    def marked(self, tag: Tag) -> bool:
        return id(tag) in self.seen

    def emit_notes(self, notes: list[str]) -> None:
        for n in notes:
            self.emit(f"\n> **Note:** {n}\n")

    def convert_block(self, node: Tag) -> None:
        if not isinstance(node, Tag) or self.marked(node):
            return
        name = (node.name or "").lower()
        classes = set(node.get("class") or [])

        # Headings
        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            text = heading_text(node)
            if text:
                lvl = int(name[1])
                self.emit(f"\n{'#' * lvl} {text}\n")
            self.mark_tree(node)
            return

        # Top-level Figure
        if name == "blockquote" and "Figure" in classes:
            self.emit(figure_to_ascii(node))
            self.mark_tree(node)
            return

        if classes & {"Centerfigure", "Leftfigure", "Rightfigure", "Herefigure"}:
            if node.find_parent(class_="Figure") is not None:
                return
            self.emit(figure_to_ascii(node))
            self.mark_tree(node)
            return

        # Scribble API definition boxes (htdp-langs, gui, etc.)
        if name == "blockquote" and (
            "SVInsetFlow" in classes
            or node.select_one("table.boxed, table.RBoxed, .RBackgroundLabel")
        ):
            # Avoid treating plain SCodeFlow as def box
            if "SCodeFlow" not in classes:
                self.emit(definition_box_to_md(node))
                self.mark_tree(node)
                return

        # Code
        if "SCodeFlow" in classes:
            if node.find_parent(class_="Figure"):
                return
            code = extract_code_block(node)
            if code:
                self.emit(f"\n```racket\n{code}\n```\n")
            self.mark_tree(node)
            return

        if name == "table" and "RktBlk" in classes:
            if node.find_parent(class_="SCodeFlow") or node.find_parent(class_="Figure"):
                return
            code = extract_code_block(node)
            if code:
                self.emit(f"\n```racket\n{code}\n```\n")
            self.mark_tree(node)
            return

        # Margin note blocks
        if "refpara" in classes:
            text = normalize_prose(node.get_text(" "))
            if text:
                self.emit(f"\n> **Note:** {text}\n")
            self.mark_tree(node)
            return

        # Standalone images
        if name == "img":
            if node.find_parent(class_="Figure"):
                return
            src = node.get("src") or "image"
            alt = (node.get("alt") or "").strip()
            note = f"[image: {src}" + (f" — {alt}" if alt and alt.lower() != "image" else "") + "]"
            self.emit("\n```\n" + ascii_box("Illustration", [note]) + "\n```\n")
            self.mark_tree(node)
            return

        # SIntrapara may hold exercises or mixed content
        if "SIntrapara" in classes:
            self.convert_sintrapara(node)
            return

        # Paragraph
        if name == "p":
            if node.find_parent(class_="Figure"):
                return
            if node.find_parent(class_="SCodeFlow"):
                return
            if node.find_parent(class_="refpara"):
                return
            notes = collect_margin_notes(node)
            text = normalize_prose(inline_md(node))
            if text:
                self.emit(f"\n{text}\n")
            self.emit_notes(notes)
            self.mark_tree(node)
            return

        # Lists
        if name in ("ol", "ul"):
            if node.find_parent(class_="Figure"):
                return
            if node.find_parent(["ol", "ul"]) is not None:
                return
            self.emit("")
            for i, li in enumerate(node.find_all("li", recursive=False), 1):
                notes = collect_margin_notes(li)
                t = normalize_prose(inline_md(li))
                if not t:
                    continue
                if name == "ol":
                    self.emit(f"{i}. {t}")
                else:
                    self.emit(f"- {t}")
                for n in notes:
                    self.emit(f"  > **Note:** {n}")
            self.emit("")
            self.mark_tree(node)
            return

        # Tables
        if name == "table" and "RktBlk" not in classes:
            if node.find_parent(class_="Figure"):
                return
            if node.find_parent("table") is not None:
                return
            links = node.select("a.toclink")
            if links:
                self.emit("\n### Contents\n")
                for a in links:
                    t = normalize_prose(a.get_text(" "))
                    if t:
                        self.emit(f"- {t}")
                self.emit("")
                self.mark_tree(node)
                return
            rows = html_table_to_ascii(node)
            if rows:
                self.emit("\n```\n" + "\n".join(rows) + "\n```\n")
                self.mark_tree(node)
                return

        # Generic blockquote
        if name == "blockquote":
            if classes & FIGURE_LIKE:
                return
            text = normalize_prose(inline_md(node))
            if text:
                for line in text.split("\n"):
                    self.emit(f"> {line}")
                self.emit("")
            self.mark_tree(node)
            return

        # Section wrappers: recurse into children
        if name in ("section", "div", "blockquote", "span") or "SsectionLevel" in "".join(classes):
            for child in list(node.children):
                if isinstance(child, Tag):
                    self.convert_block(child)
            return

        # Fallback: recurse
        for child in list(node.children):
            if isinstance(child, Tag):
                self.convert_block(child)

    def convert_sintrapara(self, node: Tag) -> None:
        if self.marked(node):
            return
        # Exercise detection
        raw = node.get_text(" ", strip=False)
        bold_spans = node.find_all(style=re.compile(r"font-weight:\s*bold", re.I))
        is_exercise = any(normalize_prose(b.get_text()) == "Exercise" for b in bold_spans)

        # Contains figure?
        fig = node.find(class_="Figure")
        if fig and fig.find_parent(class_="SIntrapara") == node:
            # process mixed: notes/text around figure via children
            for child in list(node.children):
                if isinstance(child, Tag):
                    self.convert_block(child)
                elif isinstance(child, NavigableString):
                    t = normalize_prose(str(child))
                    if t:
                        self.emit(f"\n{t}\n")
            self.mark_tree(node)
            return

        # Code only?
        scode = node.find(class_="SCodeFlow")
        if scode and normalize_prose(inline_md(node)).strip() == "":
            self.convert_block(scode)
            self.mark_tree(node)
            return

        notes = collect_margin_notes(node)

        if is_exercise:
            text = normalize_prose(inline_md(node))
            # Prefer **Exercise N. ...**
            self.emit(f"\n**{text}**\n")
            # Also include nested code/blocks after the header line
            for child in list(node.children):
                if isinstance(child, Tag) and (
                    "SCodeFlow" in (child.get("class") or [])
                    or child.name in ("blockquote", "table", "ol", "ul")
                    or "Figure" in (child.get("class") or [])
                ):
                    self.convert_block(child)
            self.emit_notes(notes)
            self.mark_tree(node)
            return

        # Mixed content: walk children in order
        has_block = any(
            isinstance(c, Tag)
            and (
                c.name in ("blockquote", "table", "ol", "ul", "pre", "div")
                or set(c.get("class") or [])
                & {
                    "SCodeFlow",
                    "Figure",
                    "Centerfigure",
                    "RktBlk",
                    "SCentered",
                    "SVInsetFlow",
                    "boxed",
                    "RBoxed",
                }
            )
            for c in node.children
        )

        if has_block:
            buf = []
            for child in list(node.children):
                if isinstance(child, NavigableString):
                    buf.append(nbsp_to_space(str(child)))
                elif isinstance(child, Tag):
                    classes = set(child.get("class") or [])
                    if is_skip_inline(child):
                        continue
                    if (
                        child.name in ("blockquote", "table", "ol", "ul", "pre", "div")
                        or classes
                        & {
                            "SCodeFlow",
                            "Figure",
                            "Centerfigure",
                            "RktBlk",
                            "SCentered",
                            "SVInsetFlow",
                            "boxed",
                            "RBoxed",
                        }
                    ):
                        prose = normalize_prose("".join(buf))
                        if prose:
                            self.emit(f"\n{prose}\n")
                        buf = []
                        self.convert_block(child)
                    else:
                        buf.append(inline_md(child))
            prose = normalize_prose("".join(buf))
            if prose:
                self.emit(f"\n{prose}\n")
            self.emit_notes(notes)
            self.mark_tree(node)
            return

        text = normalize_prose(inline_md(node))
        if text:
            self.emit(f"\n{text}\n")
        self.emit_notes(notes)
        self.mark_tree(node)

    def convert(self, main: Tag) -> str:
        self.emit(f"<!-- Extracted from {self.source_name} -->")
        self.emit("<!-- Canonical English source for Japanese translation -->")
        self.emit("")

        for sel in REMOVE_SELECTORS:
            for el in main.select(sel):
                el.decompose()

        # Process top-level children of main
        for child in list(main.children):
            if isinstance(child, Tag):
                self.convert_block(child)
            elif isinstance(child, NavigableString):
                t = normalize_prose(str(child))
                if t:
                    self.emit(f"\n{t}\n")

        text = "\n".join(self.out)
        text = re.sub(r"\n{3,}", "\n\n", text)
        # Fix spaces before punctuation from removed notes
        text = re.sub(r" +([,.;:!?])", r"\1", text)
        text = re.sub(r" +\n", "\n", text)
        return text.strip() + "\n"


FIGURE_LIKE = {"Figure", "Centerfigure", "Leftfigure", "Rightfigure", "Herefigure", "FigureInside"}


def process_page(num: str, filename: str) -> Path:
    src = HTML_DIR / filename
    if not src.exists():
        raise FileNotFoundError(src)
    html = src.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")
    main = soup.select_one("div.main") or soup.select_one("div.maincolumn") or soup.body
    if main is None:
        raise RuntimeError(f"No main content in {filename}")

    md = Converter(filename).convert(main)
    stem = Path(filename).stem
    out_name = f"original_markdown_{num}_{stem}.md"
    out_path = OUT_DIR / out_name
    out_path.write_text(md, encoding="utf-8")
    return out_path


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for num, filename in PAGES:
        path = process_page(num, filename)
        size = path.stat().st_size
        print(f"Wrote {path.relative_to(ROOT)} ({size:,} bytes)")
        written.append(path)

    index_lines = [
        "# Extracted original markdown (English source)",
        "",
        "These files are extracted from `original_html/` and are the **canonical",
        "English source** for Japanese translation work in this repository.",
        "",
        "Workflow:",
        "",
        "1. `original_html/*.html` — downloaded HtDP 2e pages",
        "2. `extracted/original_markdown_**.md` — **translation source of truth**",
        "   (prose + Racket code + ASCII-art diagrams)",
        "3. Root `??-*.md` — Japanese translation drafts",
        "4. `build_translation.sh` / `build_translation.ps1` — build EPUB/PDF from translations",
        "",
        "Regenerate extracts with:",
        "",
        "```bash",
        "python3 extract_to_markdown.py",
        "```",
        "",
        "| # | Source HTML | Extracted markdown |",
        "|---|-------------|--------------------|",
    ]
    for num, filename in PAGES:
        stem = Path(filename).stem
        out_name = f"original_markdown_{num}_{stem}.md"
        index_lines.append(f"| {num} | `{filename}` | `{out_name}` |")
    index_lines.append("")
    (OUT_DIR / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"Wrote extracted/README.md ({len(written)} pages)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
