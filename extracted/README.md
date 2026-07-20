# Extracted original markdown (English source)

These files are extracted from `original_html/` and are the **canonical
English source** for Japanese translation work in this repository.

## Main book (HTDP 2e)

Workflow:

1. `original_html/*.html` — downloaded HtDP 2e pages
2. `extracted/original_markdown_**.md` — **translation source of truth**
   (prose + Racket code + ASCII-art diagrams)
3. Root `??-*.md` — Japanese translation drafts
4. `build_translation.sh` / `build_translation.ps1` — build EPUB/PDF from translations

Regenerate extracts with:

```bash
python3 extract_to_markdown.py
```

## Appendices (Racket docs)

See **[`appendix/README.md`](appendix/README.md)**.

| Manual | HTML | Markdown originals |
|--------|------|--------------------|
| quick | `appendix_original_html/quick/` | `appendix/quick/` |
| htdp-langs | `appendix_original_html/htdp-langs/` | `appendix/htdp-langs/` |
| racket-cheat | `appendix_original_html/racket-cheat/` | `appendix/racket-cheat/` |
| gui | `appendix_original_html/gui/` | `appendix/gui/` |

```bash
python3 download_appendix_docs.py      # recursive crawl from TOC seeds
python3 extract_appendix_to_markdown.py
```


| # | Source HTML | Extracted markdown |
|---|-------------|--------------------|
| 00 | `index.html` | `original_markdown_00_index.md` |
| 01 | `part_preface.html` | `original_markdown_01_part_preface.md` |
| 02 | `part_prologue.html` | `original_markdown_02_part_prologue.md` |
| 03 | `part_one.html` | `original_markdown_03_part_one.md` |
| 04 | `i1-2.html` | `original_markdown_04_i1-2.md` |
| 05 | `part_two.html` | `original_markdown_05_part_two.md` |
| 06 | `i2-3.html` | `original_markdown_06_i2-3.md` |
| 07 | `part_three.html` | `original_markdown_07_part_three.md` |
| 08 | `i3-4.html` | `original_markdown_08_i3-4.md` |
| 09 | `part_four.html` | `original_markdown_09_part_four.md` |
| 10 | `i4-5.html` | `original_markdown_10_i4-5.md` |
| 11 | `part_five.html` | `original_markdown_11_part_five.md` |
| 12 | `i5-6.html` | `original_markdown_12_i5-6.md` |
| 13 | `part_six.html` | `original_markdown_13_part_six.md` |
| 14 | `part_epilogue.html` | `original_markdown_14_part_epilogue.md` |

