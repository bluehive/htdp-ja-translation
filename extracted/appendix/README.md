# Appendix original markdown (English translation sources)

Racket documentation manuals downloaded for use as **appendices**
to the HTDP Japanese translation project.

## Seeds

- https://docs.racket-lang.org/quick/index.html
- https://docs.racket-lang.org/htdp-langs/index.html
- https://docs.racket-lang.org/racket-cheat/index.html
- https://docs.racket-lang.org/gui/index.html

## Workflow

1. `appendix_original_html/<manual>/*.html` — downloaded originals
2. **`extracted/appendix/<manual>/original_markdown_**.md`** — **translation source of truth**
3. (future) Japanese appendix drafts under a agreed path, e.g. `appendix-ja/`

Regenerate downloads:

```bash
python3 download_appendix_docs.py
```

Regenerate markdown extracts:

```bash
python3 extract_appendix_to_markdown.py
```

## Manuals

- **`gui/`** — 100 pages (see [`gui/README.md`](gui/README.md))
- **`htdp-langs/`** — 6 pages (see [`htdp-langs/README.md`](htdp-langs/README.md))
- **`quick/`** — 1 pages (see [`quick/README.md`](quick/README.md))
- **`racket-cheat/`** — 1 pages (see [`racket-cheat/README.md`](racket-cheat/README.md))

