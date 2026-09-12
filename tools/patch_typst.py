#!/usr/bin/env python3
"""Patch Pandoc Typst output: 目次 title, ja, gothic after conf()."""

from pathlib import Path
import sys

p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")
t = t.replace("title: auto,", "title: [目次],", 1)

conf_call = t.find("#show: doc => conf(")
if conf_call < 0:
    raise SystemExit("conf() call not found")
# Inject lang: "ja" into this conf() call only.
call_end = t.find("\n)", conf_call)
if call_end < 0:
    raise SystemExit("conf() call end not found")
call = t[conf_call:call_end]
if 'lang: "ja"' not in call:
    t = t[:call_end] + '\n  lang: "ja",' + t[call_end:]

outline = t.find("#outline(")
if outline < 0:
    raise SystemExit("#outline not found")
extra = """
#set text(font: "Noto Sans CJK JP", lang: "ja")
#show raw: set text(font: "Noto Sans Mono CJK JP", size: 9pt)
#show heading: set text(font: "Noto Sans CJK JP", weight: "bold")

"""
if extra.strip() not in t[outline - 400 : outline]:
    t = t[:outline] + extra + t[outline:]

p.write_text(t, encoding="utf-8")
print(f"  patched Typst outline title + gothic shows -> {p}")
