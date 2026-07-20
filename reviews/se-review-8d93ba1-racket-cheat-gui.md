# SE Review: commit 8d93ba1 — racket-cheat + gui appendices

**Reviewer:** Senior SE (worktree isolation / deliverable audit)  
**Commit:** `8d93ba1a1e758e979ae2a480c4289b60f04c548b`  
**Branch:** `experimental/20260721-feat`  
**Worktree:** `/home/mevius/my-worktree`  
**Main repo:** `/home/mevius/my-project/htdp-ja-translation`  
**Message:** `Translate racket-cheat and gui appendices; rebuild EPUB/PDF.`  
**Date of review:** 2026-07-21  

---

## Summary

| Area | Result |
|------|--------|
| Process checklist (isolation, mapping, build, Drive copy, commit) | **PASS** |
| Translation quality (overview / cheat sheet) | **PASS** (high) |
| Translation quality (deep class API docs) | **FAIL / needs polish** |
| Merge readiness for “published JA appendix” | **Not merge-ready as finished product** |
| Acceptable as experimental branch snapshot | **Yes** |

**Overall:** The process work is solid. Commit `8d93ba1` lives only on the experimental worktree branch; master remains at `4b79811`. All requested sources map to Japanese root files (`22` + `23`–`46`), EPUB/PDF exist and were copied to Google Drive, and fence/section coverage for key overview pages is good. The product risk is volume + quality of machine-assisted **class reference** prose (`text%`, `window<%>`, etc.): large portions are readable-but-scrambled Japanese that would not meet a 新潮社-level bar, and the rebuilt PDF is ~927 pages.

---

## Process checklist

| # | Requirement | Status | Evidence |
|---|-------------|--------|----------|
| 1 | Worktree isolation; experimental has commit; master not moved | **PASS** | See §Verification |
| 2 | Source → JA mapping (racket-cheat 1; gui 00–99) | **PASS** | 100 EN pages → 25 JA files |
| 3 | Code unchanged; ASCII for images; no omissions; 3-level recursion OK | **PASS*** | Overview solid; deep class docs present but quality uneven |
| 4 | Generate epub/pdf | **PASS** | Root + Drive copies; PDF 927 pp ends at `window<%>` |
| 5 | Copy to `/home/mevius/GoogleDrive/` | **PASS** | `htdp2e-ja.{epub,pdf}` present |
| 6 | Commit + SE verify | **PASS** (this review) | Commit on experimental only |

\* “No omissions” as *file coverage*: yes. “New-cho-sha quality” for all class methods: no.

---

## Issues

### Issue 1 — Severity: **bug** (product quality)

- **Files:** esp. `/home/mevius/my-worktree/46-appendix-gui-classes-86-99.md` (`text%`, `window<%>`, …); also other `39`–`46` class bundles; PDF pp. ~900–927
- **Description:** Deep GUI class documentation is largely **machine-translated and often unusable**. Identifiers/`[メソッド]` boxes are preserved, but surrounding prose is broken line-order Japanese, false-friend tokens, and mangled changelogs. Examples:

  | Location (approx.) | Problem sample |
  |--------------------|----------------|
  | `46-…:2948` | `再帰内部を追加しましたか?口論` (intended: *Added the recursive-internals? argument*) |
  | `46-…:2610` | `を削除するために「戻る」を変更しました` + next line `文字の代わりに書記素。` |
  | `46-…:3087` | residual `口論。` after a cross-ref |
  | PDF p.920+ `window<%>` | Scrambled method specs (“いいね get-label”, “ショーならされます。？が #f の場合…”) |

  By contrast, overview pages (`24` windowing, `28` editor, `25` widget gallery, `22` cheat sheet, `button%` intro prose) are natural Japanese. Quality is **bimodal**: human/careful on layer 1–2, MT dump on layer 3 bulk.

- **Suggestion:**
  1. Mark `39`–`46` (and optionally long method sections) as **draft / EN preferred** in front matter and README.
  2. Prefer: JA headings + keep long method bodies in English until true translation; or re-run with a quality gate that rejects residual patterns (`口論`, `しましたか?`, line-start `Changed in version`).
  3. Do **not** advertise full GUI toolkit as finished Japanese reference.
- **Status:** open

### Issue 2 — Severity: **bug** (incomplete translation residual)

- **Files:** `42`–`44-appendix-gui-classes-*.md` (18× `Changed in version …` still English); mixed JA changelogs elsewhere (`パッケージ … で変更`)
- **Description:** Changelog lines are inconsistently handled: some files leave pure English, others produce broken JA (Issue 1). Progress log claimed “英文残存（The/This/When… 行頭）: 0” — true for that narrow pattern, but **false as residual-English claim**.
- **Suggestion:** One pass: either leave all `Changed in version` lines in English (consistent, searchable) or translate with a fixed template `パッケージ X のバージョン V で変更: …`.
- **Status:** open

### Issue 3 — Severity: **suggestion** (PDF size / product scope)

- **Files:** `htdp2e-ja.pdf` (worktree + Drive); build via `build_translation.sh`
- **Description:** PDF is **927 pages** (document end confirmed: page 927 = last `window<%>` methods). Prior appendix commit grew PDF from ~2.5 MB → ~13 MB; this commit adds full GUI class corpus and will dominate clone size and reader UX. Pandoc + monospaced ASCII definition boxes already reflow poorly (prior review Issue 2); more of the same at scale.
- **Suggestion:**
  - Option A: Ship book + quick + htdp-langs + **GUI overviews only** (`23`–`38`) in the main PDF; class refs as separate optional EPUB/PDF.
  - Option B: Keep full build but gitignore binaries; release artifacts only via Drive/CI.
  - Always spot-check PDF end pages after rebuild (current end is readable enough to confirm inclusion, not quality).
- **Status:** open

### Issue 4 — Severity: **suggestion** (repo hygiene / binary commit)

- **Files:** root `htdp2e-ja.pdf`, `htdp2e-ja.epub`; commit includes rebuild binaries on experimental branch
- **Description:** Same hygiene concern as prior SE review: large binary artifacts in git history. Experimental branch is the right place to land them temporarily; merging to master without policy will bloat the main line.
- **Suggestion:** Policy in README: track JA markdown only; binaries → Drive (already done) or GitHub Releases. Consider LFS only if history must keep PDFs.
- **Status:** open (carried forward)

### Issue 5 — Severity: **suggestion** (untracked / local tooling)

- **File:** `/home/mevius/my-worktree/mise.toml` (and main-repo copy)
- **Description:** Worktree setup intentionally copies `mise.toml` even when uncommitted (`wt:setup` comment). Present on disk in both trees; risk of accidental commit of local paths (`/home/mevius/...`) if someone `git add`s it, or of confusion that experimental tasks depend on untracked config.
- **Suggestion:** Either commit a sanitized `mise.toml` to master, or ensure `.gitignore` lists it and document that setup always copies from a known location.
- **Status:** open (noted risk)

### Issue 6 — Severity: **nit** (heading consistency)

- **Files:** class bundle titles
  - `39`/`40`/`41`: `# 付録 D（続き）: GUI クラス参照（…）`
  - `42`–`46`: `# 付録：GUI クラス参照（…）` (drops “D”)
- **Description:** Minor TOC inconsistency in EPUB/PDF outline.
- **Suggestion:** Normalize to `付録 D（続き）: GUI クラス参照（NN–MM）`.
- **Status:** open

### Issue 7 — Severity: **nit** (racket-cheat section split improvement)

- **Files:** `22-appendix-racket-cheat.md` vs EN extract
- **Description:** EN extract collapses Syntax/Macros under an unheaded table after Classes (`##` count EN=27, JA=28). JA correctly adds `## 構文（Syntax / Macros）`. Fence count remains 58↔58. **Improvement**, not a regression.
- **Suggestion:** Optionally fix EN extract similarly for parity scripts.
- **Status:** note only

### Issue 8 — Severity: **nit** (widget gallery fence inflation)

- **Files:** `25-appendix-gui-02-widget-gallery.md` (60 fence lines) vs EN (30)
- **Description:** Extra fences are intentional ASCII sketches replacing images (rule 2). Not a fidelity bug.
- **Status:** expected

### Issue 9 — Severity: **nit** (TOC front matter)

- **File:** `00-toc-and-front.md`
- **Description:** Front TOC still focuses on main book; no explicit 付録 C/D entries. Build still includes appendices via filename sort of `??-*.md`.
- **Suggestion:** Add appendix list (Quick, HTDP langs, Cheat, GUI) for navigability.
- **Status:** open

---

## What works (explicit positives)

1. **Worktree isolation is correct.** Experimental branch tip = `8d93ba1`; master HEAD = `4b79811` (last master commit: htdp-langs polish). Main checkout tree has no `22`–`46` JA files.
2. **Complete source mapping:**
   - racket-cheat `00` → `22-appendix-racket-cheat.md`
   - gui `00`–`15` → `23`–`38-appendix-gui-*.md` (1:1)
   - gui `16`–`99` (84 pages) → `39`–`46` class bundles (10+10+10+10+10+10+10+14 = 84 `##` class headings)
3. **Overview quality is good:** windowing 1.1–1.8 and editor 5.1–5.10 headings match EN; sample Racket blocks in §1.1 are byte-identical to EN (comments preserved).
4. **Code/API fidelity on spot-checks:** constructor/method boxes keep Racket contracts; `[image: …]` retained; ASCII widget sketches added.
5. **Fence parity on key pages:**

   | Pair | Fence lines (`^````) |
   |------|----------------------|
   | racket-cheat EN ↔ JA | 58 = 58 |
   | windowing-overview EN ↔ JA | 26 = 26 |
   | windowing-functions EN ↔ JA | 176 = 176 |
   | editor-overview EN ↔ JA | 20 = 20 |
   | Windowing Functions `[procedure]`/`[parameter]` boxes | 81 = 81 |

6. **Build pipeline includes new files:** `build/htdp2e-ja-combined.md` contains 付録 C / ウィンドウ機構; PDF last pages are GUI class material.
7. **Google Drive distribution:** both `htdp2e-ja.epub` and `htdp2e-ja.pdf` present under `/home/mevius/GoogleDrive/`; Drive PDF page count matches worktree (927).
8. **Progress / trans-log documentation** exists (`appendix-translation-progress.md`, `trans-log.md` 2026-07-21 section).

---

## Verification commands and results

Commands requested (results via git refs / filesystem inspection; no live shell in this review environment—equivalent checks applied):

```text
# Worktree tip
git -C /home/mevius/my-worktree log -1 --oneline
# → 8d93ba1 Translate racket-cheat and gui appendices; rebuild EPUB/PDF.
# (refs/heads/experimental/20260721-feat = 8d93ba1a1e758e979ae2a480c4289b60f04c548b)

# Main checkout HEAD (must stay on master, not advanced by this work)
git -C /home/mevius/my-project/htdp-ja-translation rev-parse --short HEAD
# → 4b79811
# HEAD file: ref: refs/heads/master
# master log tip: Polish htdp-langs beginner and bsl+ Japanese prose.

# Drive artifacts
ls -lh /home/mevius/GoogleDrive/htdp2e-ja.{epub,pdf}
# → both present (exact byte sizes not reported by this environment;
#    PDF text extract: 927 pages, content matches worktree PDF end)

# Isolation cross-check
# worktree: gitdir → .../worktrees/my-worktree; branch experimental/20260721-feat
# main tree listing: JA files only through 21-appendix-htdp-langs-05-advanced.md
# worktree listing: 22–46 present
```

### Mapping table (abbreviated)

| EN source | JA output |
|-----------|-----------|
| `extracted/appendix/racket-cheat/original_markdown_00_index.md` | `22-appendix-racket-cheat.md` |
| `gui/original_markdown_00_index.md` … `_15_doc-index.md` | `23` … `38` |
| `gui/original_markdown_16_*` … `_99_window___.md` | `39`–`46` (bundled) |

### Sample fence / section checks

```text
# Sections 1.1–1.8
rg '^### 1\.' 24-appendix-gui-01-windowing-overview.md
# → 1.1 … 1.8 (8)  matches EN

# Editor 5.1–5.10
rg '^### 5\.' 28-appendix-gui-05-editor-overview.md
# → 10 headings  matches EN

# Class ## count across 39–46
rg -c '^## ' 3[9]-appendix-gui-classes-*.md 4[0-6]-appendix-gui-classes-*.md
# → total 84  (= EN pages 16–99)

# Residual English (narrow progress-log pattern)
rg '^(The |This |When )' 2[2-9]-appendix-*.md 3?-appendix-*.md 4?-appendix-*.md
# → no matches on this task's files

# Residual English (changelog)
rg 'Changed in version' *-appendix-gui*.md
# → 18 hits in 42–44  (Issue 2)

# MT failure tokens
rg 'しましたか\?|口論' 46-appendix-gui-classes-86-99.md
# → multiple hits  (Issue 1)
```

### Code fidelity sample (`24` vs EN `01`)

First ```racket block (frame show example) is identical including English comments—correct under “code unchanged.”

---

## Risks (explicit)

| Risk | Severity | Notes |
|------|----------|-------|
| PDF size / page count (~927 pp) | High | Full GUI class dump in student book product |
| Machine-assisted class docs quality | High | Unreadable method prose in large sections |
| Binary commit on experimental branch | Medium | OK for experiment; gate before master merge |
| Untracked `mise.toml` | Low–Med | Local absolute paths; accidental commit risk |
| Progress log overclaims residual EN = 0 | Low | Pattern was too narrow |
| Prior htdp-langs quality debt | Medium | Still in book from earlier commits; out of this commit’s primary scope |

---

## Recommendation

| Question | Answer |
|----------|--------|
| Process complete for the assigned task? | **Yes** — map, translate, build, Drive, commit, SE review. |
| Merge to master as finished appendix translation? | **No** — polish required for class-reference quality (Issues 1–2) and product scope (Issue 3). |
| Keep on experimental / use as intermediate artifact? | **Yes** — isolation is clean; overviews + cheat sheet are merge-candidate quality after light nits. |
| Suggested next steps | (1) Label class refs draft or split PDF; (2) fix/normalize changelogs; (3) human pass on high-traffic classes (`frame%`, `canvas%`, `text%`, `window<%>`) or leave those method bodies English; (4) decide binary policy before master merge; (5) optional TOC + title nits. |

**Verdict:** **Process PASS / Product quality CONDITIONAL FAIL.**  
Ship-ready for experimental archival and overview appendices; **not** ready to claim full Japanese GUI reference quality.
