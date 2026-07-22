# SE Review: commit e42aea2 — Advanced Student (htdp-langs §5) re-translation

**Reviewer:** Senior SE (worktree isolation / deliverable audit)  
**Commit:** `e42aea264cd48cf04aa56386cc604029d1e74a80`  
**Branch:** `experimental/20260721-feat`  
**Worktree:** `/home/mevius/my-worktree`  
**Main repo:** `/home/mevius/my-project/htdp-ja-translation`  
**Message:** `Re-translate Advanced Student (htdp-langs §5) into natural Japanese.`  
**Date of review:** 2026-07-21  

---

## Summary

| Area | Result |
|------|--------|
| Process checklist (isolation, parity, residual MT, headings, Drive, commit) | **PASS** |
| Product quality vs prior glossary MT draft (`8b1d8b0` Issue 1) | **PASS** (fixed for this file) |
| Shinchosha / 新潮社-level prose (spot-checked) | **PASS** with minor tone notes |
| Merge readiness for “finished JA appendix §5” | **Yes** (this file alone) |
| Acceptable as experimental branch snapshot | **Yes** |

**Overall:** Commit `e42aea2` successfully replaces the unreadable glossary-style machine draft of `21-appendix-htdp-langs-05-advanced.md` with natural Japanese prose while preserving fence/label parity with the English extract. Master remains at `4b79811`; the commit lives only on `experimental/20260721-feat`. EPUB/PDF exist in the worktree and under `/home/mevius/GoogleDrive/`. No residual MT salad patterns of the prior review were found. Minor remaining issues are register inconsistency (ですます vs 常体 in late API blurbs) and carried-forward PDF/ASCII-box hygiene concerns—not blockers for this process gate.

---

## Process checklist

| # | Requirement | Status | Evidence |
|---|-------------|--------|----------|
| 1 | Isolation: master still `4b79811`; commit on experimental only | **PASS** | See §Verification 1 |
| 2 | Fence parity: EN vs JA `` ``` `` and `` ```racket `` | **PASS** | 1290=1290; 305=305 |
| 3 | Label counts: `[procedure]`→`[手続き]`, `[syntax]`→`[構文]`, `[value]`→`[値]` | **PASS** | 267 / 51 / 20 both sides |
| 4 | No residual MT salad (`できる be`, `へ mutate`, `Chooses 節`, …) | **PASS** | See §Verification 4 |
| 5 | Section headings 5.1–5.26 present in JA | **PASS** | 26 `### 5.N` headings |
| 6 | Drive copies of epub/pdf exist | **PASS** | `/home/mevius/GoogleDrive/htdp2e-ja.{epub,pdf}` |
| 7 | Spot-check prose (define-struct, check-expect, map/filter) | **PASS** | Natural JA; code preserved |
| 8 | Note remaining issues | **PASS** | See §Issues |

**Process checklist verdict: PASS**

---

## Verification detail

### 1. Isolation

| Ref | SHA |
|-----|-----|
| Worktree HEAD | `ref: refs/heads/experimental/20260721-feat` → `e42aea264cd48cf04aa56386cc604029d1e74a80` |
| `master` | `4b798117f21704ad7d6314923eacb89ed90e7be0` (unchanged) |
| Worktree gitdir | `/home/mevius/my-project/htdp-ja-translation/.git/worktrees/my-worktree` |

**Branch log (experimental only):**

```
4b79811  branch: Created from master
8d93ba1  Translate racket-cheat and gui appendices; rebuild EPUB/PDF.
f83fa32  Polish GUI class drafts after SE review; re-ship EPUB/PDF.
e42aea2  Re-translate Advanced Student (htdp-langs §5) into natural Japanese.
```

**Master log tip:** ends at `4b79811` (`Polish htdp-langs beginner and bsl+ Japanese prose.`) — no `e42aea2`.

**Commit message body (COMMIT_EDITMSG):** documents full prose re-translation from English extract, fence parity, EPUB/PDF rebuild, Drive ship — matches task scope.

### 2. Fence parity

| Pattern | EN (`original_markdown_05_advanced.md`) | JA (`21-appendix-htdp-langs-05-advanced.md`) |
|---------|------------------------------------------|-----------------------------------------------|
| lines matching `^``` ` | **1290** | **1290** |
| lines matching `^```racket` | **305** | **305** |
| table-embedded `\| ```racket` | **2** | **2** |

Nested fences inside ASCII definition boxes (cond/if) are preserved on both sides — same structural wart as prior SE notes; not a regression.

### 3. Label counts

| EN label | Count | JA label | Count |
|----------|------:|----------|------:|
| `[procedure]` | 267 | `[手続き]` | 267 |
| `[syntax]` | 51 | `[構文]` | 51 |
| `[value]` | 20 | `[値]` | 20 |

Residual English labels in JA: **0** (`[procedure]`/`[syntax]`/`[value]` grep empty).

Matches `trans-log.md` (2026-07-21 Advanced Student 再翻訳).

### 4. Residual MT salad

Searched JA for patterns called out in prior review (`8b1d8b0` Issue 1) and related fragments:

| Pattern | Hits in JA prose |
|---------|------------------|
| `できる be` | 0 |
| `へ mutate` / `Chooses 節` / `An alternate way へ` | 0 |
| `できない be` / `named name must` / `関数s.` | 0 |
| `Defines a new` / `Constructs a list` / `Chooses a clause` (leftover EN heads) | 0 |
| English sentence openers (`Defines|Returns|…`) outside REPL | only **`The test passed!`** (REPL success output — correct to keep) |
| `cannot` | only inside **error-message example strings** (`tag-with-a:this name was defined previously and cannot be re-defined`) — correct |

**Verdict:** Prior unreadable EN/JA token salad is gone from this file.

### 5. Section headings 5.1–5.26

All 26 present in JA with Japanese titles; EN counterparts present:

| § | JA heading |
|---|------------|
| 5.1 | あらかじめ定義された変数 |
| 5.2 | テンプレート変数 |
| 5.3 | 上級の構文 |
| 5.4 | 共通の構文 |
| 5.5 | あらかじめ定義された関数 |
| 5.6 | シグネチャ |
| 5.7 | 数: 整数・有理数・実数・複素数・正確数・非正確数 |
| 5.8 | 真偽値 |
| 5.9 | シンボル |
| 5.10 | リスト |
| 5.11 | Posn（位置） |
| 5.12 | 文字 |
| 5.13 | 文字列 |
| 5.14 | 画像 |
| 5.15 | その他 |
| 5.16 | シグネチャ |
| 5.17 | 数（緩和条件） |
| 5.18 | 文字列（緩和条件） |
| 5.19 | Posn（位置） |
| 5.20 | 高階関数 |
| 5.21 | 数（緩和条件・追加） |
| 5.22 | 高階関数（ラムダつき） |
| 5.23 | 読み取りと表示 |
| 5.24 | ベクタ |
| 5.25 | ボックス |
| 5.26 | ハッシュ表 |

### 6. Drive / build artifacts

| Path | Present |
|------|---------|
| `/home/mevius/my-worktree/htdp2e-ja.epub` | yes |
| `/home/mevius/my-worktree/htdp2e-ja.pdf` | yes |
| `/home/mevius/GoogleDrive/htdp2e-ja.epub` | yes |
| `/home/mevius/GoogleDrive/htdp2e-ja.pdf` | yes |

### 7. Prose spot-check (Shinchosha bar)

#### define-struct (`21-…:516–527`)

> structure-name という新しい構造体を定義します。構造体のフィールドは field-name たちで名付けられます。…  
> 上級学生言語（Advanced）では、define-struct は次の追加関数も導入します。  
> set-structure-name-field-name! : …フィールドを与えられた値へ破壊的更新します。

- Faithful to EN “Defines a new structure… mutates the instance’s field…”
- Natural です/ます; technical terms (`make-structure-name`, `#true`) kept as identifiers
- **No** glossary wreckage of the old `へ mutate` style

#### check-expect (`21-…:605–617`)

> 最初の expression が、expected-expression と同じ値に評価されることを検査します。  
> check-expect 式は、学生プログラムのトップレベルに置かなければなりません。…構文エラーは…意図的に実行時まで遅延されます。  
> …非正確数については、素朴な等値比較を行うのは原理的に誤りです。…関数同士を比較することは証明可能に不可能です。

- Multi-sentence pedagogical prose is fully Japanese and readable
- Code sample `(check-expect (fahrenheit->celsius 212) 100)` preserved under `` ```racket ``

#### cond / “Chooses a clause” (`21-…:547–549`)

> ある条件に基づいて節を選びます。cond は #true に評価される最初の question-expression を見つけ、対応する answer-expression を評価します。

- Exactly the pattern previously broken as `Chooses 節` — now proper Japanese

#### filter / map (`21-…:5048`, `5131`)

> リスト上の要素のうち、述語が成り立つものすべてからリストを構築する。  
> 1 つ以上の既存のリストの各要素に関数を適用して、新しいリストを構築する:

- Meaning correct; code bodies and REPL examples intact
- **Tone note:** these use 常体 (する), while §5.3–5.4 use です/ます — see Issue 1

#### set! / mutation intro (`21-…:237`)

> set! を使って変数を破壊的更新（ミューテーション）できます。

- Clear gloss; no `へ mutate` salad

---

## Issues

### Issue 1 — Severity: **nit** (register / 文体)

- **Files:** `21-appendix-htdp-langs-05-advanced.md` late sections (~§5.22–5.26), e.g. filter/map/hash one-liners ending in `構築する。` / `生成する。` / `返す。` (≈18 lines)
- **Description:** Front half and syntax essays use polite です/ます; many short procedure blurbs in HOF/vector/box/hash use plain 常体. Both are correct Japanese; mixing within one reference chapter is slightly uneven for a 新潮社-tight pass.
- **Suggestion:** Optional polish pass to unify on です/ます (preferred for book body) or document that short API glosses may stay 常体.
- **Status:** open (non-blocking)

### Issue 2 — Severity: **suggestion** (carried forward: PDF ASCII boxes)

- **From:** prior reviews `8b1d8b0` Issue 2, `8d93ba1` Issue 3
- **Description:** Label width change to `[手続き]`/`[構文]` still stresses fixed-width ASCII frames; nested `` ```racket `` inside boxes remains. Source fidelity is fine; PDF reflow may still look rough.
- **Suggestion:** Definition lists / real tables in a later extract pass; spot-check PDF pages for §5 after major rebuilds.
- **Status:** open (process for this commit still PASS — source + ship done)

### Issue 3 — Severity: **suggestion** (scope of sibling files)

- **Files:** `17`–`20-appendix-htdp-langs-*.md` (not in this commit’s primary rewrite claim)
- **Description:** This commit targets Advanced (§5 / `21-…`). Prior MT salad risk may still apply to Beginner / Intermediate siblings unless already hand-polished (beginner was polished on master as `4b79811`).
- **Suggestion:** Same re-translation quality gate for any remaining glossary-style htdp-langs files before advertising full 付録 B as finished.
- **Status:** note (out of e42aea2 scope)

### Issue 4 — Severity: **suggestion** (binary hygiene)

- **Files:** root + Drive `htdp2e-ja.{epub,pdf}`
- **Description:** Experimental branch continues to carry large rebuild binaries (prior reviews). Drive copy fulfills distribution requirement.
- **Suggestion:** Prefer markdown in git + Drive/CI for binaries when merging to master.
- **Status:** open (policy; not a fail for experimental process)

---

## Product quality verdict

| Criterion | Verdict |
|-----------|---------|
| Replaces unreadable MT salad for Advanced §5 | **PASS** |
| Code / signature / example fidelity | **PASS** |
| Label localization complete | **PASS** |
| Readable technical Japanese (syntax + checks + HOF) | **PASS** |
| Strict single-register 新潮社 polish throughout | **PASS with nits** (Issue 1) |

**Product quality verdict: PASS** (experimental ship + §5 re-translation goal met)

---

## Final gate

```
Process checklist:  PASS
Product quality:    PASS (minor 文体 nit; no MT salad)
Isolation:          PASS (master @ 4b79811; e42aea2 on experimental only)
Ready for parent push of experimental/20260721-feat:  YES
```
