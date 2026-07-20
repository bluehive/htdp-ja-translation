## Summary

Commit 8b1d8b0 successfully wires a download → extract → translate → build pipeline for Racket appendix docs, and the Japanese root files `15-`…`21-appendix-*.md` are actually included in EPUB/PDF (confirmed: built PDF ends in Advanced Student §5.24–5.26 and grew from ~2.5 MB to ~13 MB). Code fidelity is largely solid where it matters—htdp-langs beginner keeps 220 `` ```racket `` fences matching the English extract, and Quick preserves example bodies while improving a few fenced blocks that extraction left inline. The serious product risk is not the build wiring: `tools/translate_htdp_langs_appendix.py` produces large volumes of unreadable EN/JA word-salad that is now published in the book, and the repo commits a heavy HTML + markdown mirror (especially full `gui/`) plus binary PDF without corresponding hygiene/CI guards.

## Issues

### Issue 1 -- Severity: bug
- File: `/home/mevius/my-project/htdp-ja-translation/tools/translate_htdp_langs_appendix.py:231-363` (glossary pass); outputs e.g. `/home/mevius/my-project/htdp-ja-translation/17-appendix-htdp-langs-01-beginner.md:196-241`, `:319-343`
- Description: The “translation” for htdp-langs is often not Japanese prose. Token-level glossary substitution (`to`→`へ`, `that`→`という`, `cannot`→`できない`, etc.) yields unreadable mixes such as:
  - `An alternate way へ defining 関数s. name は name の 関数, であり できない be same として という の another 関数 または 変数.`
  - `関数 named name must defined before it できる be called. 数 の 引数 式s でなければならない same として 数 の 引数s expected によって 関数.`
  - Sentence fragments like `that the first expression evaluates to the same value as the expected-expression を検査します。`
  The same patterns appear across `18`–`21` as well. Short API one-liners that match phrase rules are OK; multi-sentence syntax/check docs and many procedure blurbs are not. Shipping this as an “appendix translation” misrepresents quality relative to the hand-done Quick appendix and the rest of the book.
- Suggestion: Treat current htdp-langs JA files as machine draft only: (1) stop regenerating over hand-fixed text without a quality gate; (2) prefer leave-English-prose + JA headings/labels, or true LLM/human translation with post-check; (3) expand `CORE_EXACT`/`long_map` for shared syntax sections and ban the glossary pass for any line that still has >N Latin word tokens after substitution; (4) mark `17`–`21` as “draft / needs human pass” in README and front matter until fixed.
- Status: open

### Issue 2 -- Severity: bug
- File: PDF rendering of appendix definition boxes / REPL examples (source OK: e.g. `17-appendix-htdp-langs-01-beginner.md:2272-2273`; PDF text e.g. pages ~350–360, 460–469)
- Description: Markdown source keeps correct REPL shape (`> (car x)` then `2` on the next line). The generated PDF frequently collapses or reorders interactions (`> (2 car x)`, `> ((listappend …) …)`, broken box borders `| [| | 手続き]`). Label swap `[procedure]`→`[手続き]` changes box width inside fixed-width ASCII tables, which already do not reflow; combined with dense monospaced blocks this makes the ~100+ page language reference section hard to use in the PDF product path.
- Suggestion: Prefer real Markdown tables / definition lists for API boxes instead of fixed-width ASCII frames; or keep English `[procedure]` labels inside boxes; validate a sample of PDF pages after each rebuild. EPUB may fare better—spot-check both formats, not only PDF.
- Status: open

### Issue 3 -- Severity: suggestion
- File: `/home/mevius/my-project/htdp-ja-translation/.gitignore:1-11`; tree under `appendix_original_html/`, `extracted/appendix/gui/`, root `htdp2e-ja.pdf` / `htdp2e-ja.epub`
- Description: Hygiene cost of this commit is high.
  - Diff un-ignores most of `extracted/` so `original_markdown_*.md` is tracked (intentional for SoT), but also lands ~100 GUI HTML pages + 100 extracted GUI markdown files that are **not** in the Japanese build (`15`–`21` only cover quick + htdp-langs).
  - Binary artifacts: PDF ~13 MB (was ~2.5 MB), EPUB ~364 KB—both committed in the same change set.
  - `appendix_original_html/` is fully committed (reproducible via `download_appendix_docs.py`); no ignore for HTML mirrors, build outputs, or `__pycache__` already present on disk.
  - Removing `download_book.py` from `.gitignore` is fine if that script should be tracked, but the net effect is a much larger clone for sources that are regenerate-able.
- Suggestion: Document a clear policy: (A) track only English extracts that translators need (quick + htdp-langs for now), download gui/cheat on demand; or (B) track extracts but gitignore `appendix_original_html/` and root EPUB/PDF (CI/release assets). Add `*.epub` / `*.pdf` or `htdp2e-ja.*` to `.gitignore` if binaries should not bloat history. Consider Git LFS only if you must keep large binaries in-repo.
- Status: open

### Issue 4 -- Severity: suggestion
- File: no CI / tests; related: `tools/translate_htdp_langs_appendix.py`, `build_translation.sh:39-61`
- Description: There is no automated check for fence parity, unbalanced fences, or “prose still mostly English.” The only assurance is a manual note in `trans-log.md` that beginner has 220 `` ```racket `` fences (spot-check agrees: JA 220 vs EN 220). A broken regenerate of the glossary tool or a future extract change could silently ship missing examples. Nested ``| ```racket |`` inside ASCII boxes (present in both EN extract and JA) is structurally awkward for naive fence scanners, though the current translator correctly treats those as table lines (leading `|`), not fence terminators.
- Suggestion: Add a small script (and optional CI job) that for each JOB pair in `translate_htdp_langs_appendix.py` and for Quick asserts: equal count of lines matching `^```(racket)?$`, equal count of `^```racket`, and optionally hash of fenced bodies. Fail the build if `*appendix*` count from `??-*.md` drops below expected (currently 7 files: `15`–`21`).
- Status: open

### Issue 5 -- Severity: suggestion
- File: `/home/mevius/my-project/htdp-ja-translation/tools/translate_htdp_langs_appendix.py` (overall design)
- Description: Maintainability of the MT tool is weak for a regenerable pipeline:
  - Large embedded `long_map` / glossary with fragile exact-string keys (whitespace/join sensitive).
  - No tests; re-run overwrites root JA files wholesale.
  - No report of untranslated residual English rate.
  - Phrase rule `^Checks (.*)\.$` → `…を検査します` applied to long English tails produces the half-translated fragments in Issue 1.
  - `len(t) < 220` glossary gate still mangles medium paragraphs.
- Suggestion: Split data (YAML/JSON phrase bank) from code; write dry-run mode that only prints residual-English stats; never overwrite without `--force`; add unit tests on a few golden paragraphs (cond, define, check-expect). For API docs, translating only headings + labels + one-line “Determines whether…” blurbs and leaving longer paragraphs in English may be higher-value than false-Japanese.
- Status: open

### Issue 6 -- Severity: suggestion
- File: `/home/mevius/my-project/htdp-ja-translation/README.md:26-33`, `:55-62`; `/home/mevius/my-project/htdp-ja-translation/extracted/appendix/README.md:17`
- Description: Workflow docs are slightly stale vs what this commit actually ships:
  - Stage-3 table still says “＋将来の付録日本語ドラフト” while `15`–`21` already exist and are built.
  - Progress section lists only main-book partial status; no mention of appendix A/B draft state or quality caveats.
  - `extracted/appendix/README.md` still says Japanese drafts will live under e.g. `appendix-ja/`, but the project correctly uses root `??-*.md` (aligned with `build_translation.sh`).
- Suggestion: Update README stages/progress to list appendix files, note htdp-langs is machine-draft, and fix appendix README path to root `1[5-9]-appendix-*.md` / `2[0-1]-appendix-*.md`.
- Status: open

### Issue 7 -- Severity: nit
- File: `/home/mevius/my-project/htdp-ja-translation/build_translation.sh:15-16`, `:39`; `/home/mevius/my-project/htdp-ja-translation/build_translation.ps1:153-157`
- Description: Build pipeline correctness for inclusion/order is **good**:
  - Both shells select root `??-*.md`, sort by name → `00`…`14` then `15-appendix-quick` … `21-appendix-htdp-langs-05-advanced`.
  - Bash counts `*appendix*` for logging; combined markdown is retained under `build/` (useful for debug). PS1 deletes the temp combined MD after success—minor cross-platform inconsistency.
  - Bash prefers a machine-local pandoc path (`/home/mevius/my-project/mypublish-books/tools/pandoc-3.6.4/bin/pandoc`) before `PATH`—works here but is non-portable for other contributors.
  - gui / racket-cheat extracts are intentionally **not** in the JA build (no root drafts); that is consistent with scope, not a silent drop of translated content.
- Suggestion: Prefer `command -v pandoc` first (or env `PANDOC=`); keep PS1 combined MD under `build/` like bash for parity; optionally assert `APPENDIX_COUNT -ge 7` and fail if zero.
- Status: open

### Issue 8 -- Severity: nit
- File: `/home/mevius/my-project/htdp-ja-translation/15-appendix-quick.md` vs `/home/mevius/my-project/htdp-ja-translation/extracted/appendix/quick/original_markdown_00_index.md`
- Description: Quick spot-check is favorable. Prose is natural Japanese; Racket bodies match intent; image placeholders retained; English comments inside `(define (square n) …)` stay in the code fence with a JA note outside—correct. Fence count is 30×`` ```racket `` in JA vs 28 in EN: the extra two are intentional improvements—`(provide rainbow square)` and the `use.rkt` program, which the English extract left mangled as inline prose (`line(provide rainbow square)then you can open…`). Not a regression.
- Suggestion: Optional follow-up: re-run extract for modules section so EN SoT also has proper fences, keeping parity scripts happy.
- Status: open

### Issue 9 -- Severity: nit
- File: `/home/mevius/my-project/htdp-ja-translation/extract_to_markdown.py` (Converter); examples in `extracted/appendix/htdp-langs/original_markdown_01_beginner.md:283-298`
- Description: Extraction embeds literal `` ```racket `` example blocks *inside* ASCII definition boxes. That is a pre-PDF readability wart in the English SoT itself. The translator preserves it (labels only). Not introduced by JA alone, but amplifies Issue 2 and confuses human editors.
- Suggestion: When extracting RBoxed content, put examples as sibling fenced blocks after the box, not as pseudo-cells containing fences.
- Status: open

### Issue 10 -- Severity: nit
- File: `/home/mevius/my-project/htdp-ja-translation/download_appendix_docs.py:100-114`; `/home/mevius/my-project/htdp-ja-translation/extract_appendix_to_markdown.py:27-63`
- Description: Download/extract scripts are coherent: polite crawl, same-manual path constraint, skip-if-exists, priority ordering for htdp-langs/gui TOC pages, reuse of `Converter`. Nested path handling (`if not rel_name or "/" in rel_name`) is a bit odd but current manuals are flat. No integrity hash of upstream docs—acceptable for a local mirror.
- Suggestion: Write a small manifest of URL→sha256 after download so drift is detectable; document that gui is optional for current book scope.
- Status: open

## What works (explicit positives)

1. **Appendices are in the build.** `build_translation.sh` / `.ps1` combine all root `??-*.md`; ordering places appendices after the epilogue; regenerated PDF contains Quick + full htdp-langs through Advanced Student hash tables.
2. **Code fences for htdp-langs beginner match** at 220 `` ```racket `` lines EN↔JA; sample blocks (`fahrenheit->celsius`, `list*`, `list-ref`) are byte-identical to the English extract aside from surrounding prose.
3. **Quick (`15-appendix-quick.md`) is high quality** relative to the extract—readable JA, preserved code, useful fence cleanup for the modules example.
4. **Pipeline separation is clear:** English SoT under `extracted/**/original_markdown_*.md`, JA under root `??-*.md`, scripts to regenerate both book and appendix extracts. `.gitignore` change to keep `original_markdown` while ignoring old `part3_*.txt` scratch is directionally right.
5. **trans-log.md** honestly flags htdp-langs as needing human polish—the code review agrees and elevates that from “note” to release-blocking quality for any “published translation” claim.

## Recommended priority

1. Do not advertise htdp-langs as finished Japanese; either re-translate or ship English prose for long sections.
2. Reduce committed bulk (gui HTML/MD and/or PDF) unless there is a deliberate archival policy.
3. Add fence-parity (+ residual-English) checks before the next regenerate/commit cycle.
4. Keep Quick-quality bar for any future appendix that students actually read front-to-back.
