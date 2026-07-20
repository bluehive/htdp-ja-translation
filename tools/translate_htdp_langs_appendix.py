#!/usr/bin/env python3
"""
Translate extracted/appendix/htdp-langs/original_markdown_*.md to Japanese
root appendix files. Preserves code fences and definition-box structure.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "extracted" / "appendix" / "htdp-langs"

JOBS = [
    (
        "original_markdown_00_index.md",
        "16-appendix-htdp-langs-00-index.md",
        "付録 B: How to Design Programs 言語リファレンス",
        "extracted/appendix/htdp-langs/original_markdown_00_index.md",
    ),
    (
        "original_markdown_01_beginner.md",
        "17-appendix-htdp-langs-01-beginner.md",
        "付録 B-1: Beginning Student Language（#lang htdp/bsl）",
        "extracted/appendix/htdp-langs/original_markdown_01_beginner.md",
    ),
    (
        "original_markdown_02_beginner-abbr.md",
        "18-appendix-htdp-langs-02-beginner-abbr.md",
        "付録 B-2: Beginning Student with List Abbreviations（#lang htdp/bsl+）",
        "extracted/appendix/htdp-langs/original_markdown_02_beginner-abbr.md",
    ),
    (
        "original_markdown_03_intermediate.md",
        "19-appendix-htdp-langs-03-intermediate.md",
        "付録 B-3: Intermediate Student（#lang htdp/isl）",
        "extracted/appendix/htdp-langs/original_markdown_03_intermediate.md",
    ),
    (
        "original_markdown_04_intermediate-lam.md",
        "20-appendix-htdp-langs-04-intermediate-lam.md",
        "付録 B-4: Intermediate Student with lambda（#lang htdp/isl+）",
        "extracted/appendix/htdp-langs/original_markdown_04_intermediate-lam.md",
    ),
    (
        "original_markdown_05_advanced.md",
        "21-appendix-htdp-langs-05-advanced.md",
        "付録 B-5: Advanced Student（#lang htdp/asl）",
        "extracted/appendix/htdp-langs/original_markdown_05_advanced.md",
    ),
]

LABELS = {
    "[procedure]": "[手続き]",
    "[value]": "[値]",
    "[syntax]": "[構文]",
    "[signature form]": "[シグネチャ形式]",
    "[signature]": "[シグネチャ]",
    "[structure]": "[構造体]",
    "[constant]": "[定数]",
    "[form]": "[形式]",
}

# Exact full-paragraph replacements (English source as key with \n preserved)
EXACT: dict[str, str] = {}

# Load exact map from companion data file if present; also embed core set below.
CORE_EXACT = {
    "Example:": "例:",
    "A placeholder for indicating that a function definition is a template.": "関数定義がテンプレートであることを示すためのプレースホルダ。",
    "The empty list.": "空リスト。",
    "The #true value.": "#true の値。",
    "The #false value.": "#false の値。",
    "Selects the first item of a non-empty list.": "空でないリストの先頭要素を取り出します。",
    "Selects the rest of a non-empty list.": "空でないリストの残り（rest）を取り出します。",
    "Determines whether some value is the empty list.": "値が空リストかどうかを判定します。",
    "Determines whether some value is on the list (comparing values with equal?).": "値がリスト上にあるかどうかを判定します（equal? で比較）。",
    "else cannot be used outside of cond.": "else は cond の外では使えません。",
    "number. See round.": "数値です。round を参照。",
    "variable.": "変数。",
    "How to Design Programs Languages": "How to Design Programs 言語",
}

# Heading fragments
HEADING_SUB = [
    (r"^# How to Design Programs Languages\s*$", "# How to Design Programs 言語"),
    (r"^## (\d+)\s+Beginning Student\s*$", r"## \1 Beginning Student（初級学生言語）"),
    (
        r"^## (\d+)\s+Beginning Student with List Abbreviations\s*$",
        r"## \1 Beginning Student with List Abbreviations（リスト略記つき初級）",
    ),
    (r"^## (\d+)\s+Intermediate Student\s*$", r"## \1 Intermediate Student（中級学生言語）"),
    (
        r"^## (\d+)\s+Intermediate Student with Lambda\s*$",
        r"## \1 Intermediate Student with Lambda（lambda つき中級）",
    ),
    (r"^## (\d+)\s+Advanced Student\s*$", r"## \1 Advanced Student（上級学生言語）"),
    (r"Pre-defined Variables", "あらかじめ定義された変数"),
    (r"Template Variables", "テンプレート変数"),
    (r"^### ([\d.]+)\s+Syntax\s*$", r"### \1 構文"),
    (r"Syntaxes for Beginning Student with List Abbreviations", "リスト略記つき初級の構文"),
    (r"Syntax for Intermediate with Lambda", "lambda つき中級の構文"),
    (r"Syntax for Intermediate", "中級の構文"),
    (r"Syntax for Advanced", "上級の構文"),
    (r"Common Syntaxes", "共通の構文"),
    (r"Signature Forms", "シグネチャ形式"),
    (r"Struct Signatures", "構造体シグネチャ"),
    (r"Pre-defined Functions", "あらかじめ定義された関数"),
    (r"Pre-Defined Functions", "あらかじめ定義された関数"),
    (r"Numbers: Integers, Rationals, Reals, Complex, Exacts, Inexacts", "数: 整数・有理数・実数・複素数・正確数・非正確数"),
    (r"Numbers \(relaxed conditions plus\)", "数（緩和条件・拡張）"),
    (r"Numbers \(relaxed conditions\)", "数（緩和条件）"),
    (r"^### ([\d.]+)\s+Booleans\s*$", r"### \1 真偽値"),
    (r"^### ([\d.]+)\s+Symbols\s*$", r"### \1 シンボル"),
    (r"^### ([\d.]+)\s+Lists\s*$", r"### \1 リスト"),
    (r"^### ([\d.]+)\s+Posns\s*$", r"### \1 Posn"),
    (r"^### ([\d.]+)\s+Characters\s*$", r"### \1 文字"),
    (r"^### ([\d.]+)\s+Strings\s*$", r"### \1 文字列"),
    (r"String \(relaxed conditions\)", "文字列（緩和条件）"),
    (r"^### ([\d.]+)\s+Images\s*$", r"### \1 画像"),
    (r"^### ([\d.]+)\s+Misc\s*$", r"### \1 その他"),
    (r"^### ([\d.]+)\s+Signatures\s*$", r"### \1 シグネチャ"),
    (r"Higher-Order Functions \(with Lambda\)", "高階関数（lambda つき）"),
    (r"Higher-Order Functions", "高階関数"),
    (r"Reading and Printing", "読み取りと表示"),
    (r"^### ([\d.]+)\s+Vectors\s*$", r"### \1 ベクタ"),
    (r"^### ([\d.]+)\s+Boxes\s*$", r"### \1 ボックス"),
    (r"Hash Tables", "ハッシュ表"),
    (r"^### Contents\s*$", "### 目次"),
]


def phrase_translate(text: str) -> str:
    """Heuristic Japanese for short API description lines."""
    t = text.strip()
    if not t:
        return text

    # Already mostly Japanese
    if re.search(r"[\u3040-\u30ff\u4e00-\u9fff]", t) and not re.search(
        r"\b(the|and|with|from|that|this|Determines|Constructs)\b", t
    ):
        return text

    rules = [
        (
            r"^Determines whether (.*)\.$",
            r"\1 かどうかを判定します。",
        ),
        (
            r"^Determines if (.*)\.$",
            r"\1 かどうかを判定します。",
        ),
        (
            r"^Constructs (.*)\.$",
            r"\1 を構築します。",
        ),
        (
            r"^Computes (.*)\.$",
            r"\1 を計算します。",
        ),
        (
            r"^Extracts (.*)\.$",
            r"\1 を取り出します。",
        ),
        (
            r"^Produces (.*)\.$",
            r"\1 を生成します。",
        ),
        (
            r"^Converts (.*)\.$",
            r"\1 を変換します。",
        ),
        (
            r"^Selects (.*)\.$",
            r"\1 を選択します。",
        ),
        (
            r"^Checks (.*)\.$",
            r"\1 を検査します。",
        ),
        (
            r"^Compares (.*)\.$",
            r"\1 を比較します。",
        ),
        (
            r"^Creates (.*)\.$",
            r"\1 を作成します。",
        ),
        (
            r"^Evaluates (.*)\.$",
            r"\1 を評価します。",
        ),
        (
            r"^Updates (.*)\.$",
            r"\1 を更新します。",
        ),
        (
            r"^Finds (.*)\.$",
            r"\1 を探します。",
        ),
        (
            r"^Returns (.*)\.$",
            r"\1 を返します。",
        ),
        (
            r"^Applies (.*)\.$",
            r"\1 を適用します。",
        ),
        (
            r"^Signature for (.*)\.$",
            r"\1 のシグネチャ。",
        ),
        (
            r"^Like (.*), but (.*)\.$",
            r"\1 と同様ですが、\2。",
        ),
        (
            r"^LISP-style (.*)\.$",
            r"LISP 風の \1。",
        ),
    ]
    for pat, rep in rules:
        m = re.match(pat, t)
        if m:
            out = re.sub(pat, rep, t)
            # light cleanup of remaining English articles inside
            return out

    # Multi-sentence or longer: apply token-level glossary
    glossary = [
        ("function definition", "関数定義"),
        ("function call", "関数呼び出し"),
        ("function", "関数"),
        ("expression", "式"),
        ("variable", "変数"),
        ("structure", "構造体"),
        ("empty list", "空リスト"),
        ("list", "リスト"),
        ("string", "文字列"),
        ("number", "数"),
        ("boolean", "真偽値"),
        ("symbol", "シンボル"),
        ("character", "文字"),
        ("image", "画像"),
        ("signature", "シグネチャ"),
        ("template", "テンプレート"),
        ("argument", "引数"),
        ("value", "値"),
        ("error", "エラー"),
        ("module", "モジュール"),
        ("random", "乱数"),
        ("exact", "正確"),
        ("inexact", "非正確"),
        ("integer", "整数"),
        ("rational", "有理数"),
        ("complex", "複素数"),
        ("real number", "実数"),
        ("real", "実数"),
        ("predicate", "述語"),
        ("identifier", "識別子"),
        ("keyword", "キーワード"),
        ("library", "ライブラリ"),
        ("teacher", "教師"),
        ("student", "学生"),
        ("program", "プログラム"),
        ("definition", "定義"),
        ("clause", "節"),
        ("condition", "条件"),
        ("otherwise", "そうでなければ"),
        ("must not", "〜してはならない"),
        ("must be", "でなければならない"),
        ("reports an error", "エラーを報告する"),
        ("evaluates to", "評価結果は"),
        ("evaluates", "評価する"),
        ("returns", "返す"),
        ("Determines whether", "〜かどうかを判定する: "),
        ("Determines", "判定する: "),
        ("Constructs", "構築する: "),
        ("Computes", "計算する: "),
        ("The ", ""),
        (" the ", " "),
        (" a ", " "),
        (" an ", " "),
        (" of ", " の "),
        (" to ", " へ "),
        (" for ", " のための "),
        (" with ", " とともに "),
        (" from ", " から "),
        (" that ", " という "),
        (" which ", " であり "),
        (" and ", " と "),
        (" or ", " または "),
        (" is ", " は "),
        (" are ", " は "),
        (" in ", " の中の "),
        (" on ", " 上の "),
        (" by ", " によって "),
        (" as ", " として "),
        (" if ", " もし "),
        (" when ", " のとき "),
        (" into ", " へ "),
        (" its ", " その "),
        (" their ", " それらの "),
        (" this ", " この "),
        (" these ", " これらの "),
        (" those ", " それらの "),
        (" any ", " 任意の "),
        (" all ", " すべての "),
        (" each ", " 各 "),
        (" some ", " ある "),
        (" not ", " ない "),
        (" cannot ", " できない "),
        (" can ", " できる "),
        (" may ", " してもよい "),
        (" should ", " すべき "),
        (" Also ", " また "),
        (" Also", " また"),
        ("For example,", "たとえば、"),
        ("for example,", "たとえば、"),
        ("Note that", "注意:"),
        ("See ", "参照: "),
        ("Using ", "使用: "),
        ("Like ", "同様: "),
        ("Unlike ", "異なり: "),
        ("After ", "のあと "),
        ("Before ", "の前に "),
        ("When ", "とき: "),
        ("If ", "もし "),
        ("It is ", ""),
        ("It ", "それ "),
        ("This ", "これ "),
        ("These ", "これら "),
        ("Here ", "ここで "),
        ("Under ", "のもとで "),
        ("Normally, ", "通常、"),
        ("In particular, ", "特に、"),
        ("In other words, ", "言い換えると、"),
        ("In contrast, ", "対照的に、"),
        ("Instead ", "代わりに "),
        ("However, ", "しかし、"),
        ("Thus, ", "したがって、"),
        ("Hence ", "ゆえに "),
        ("Additionally, ", "さらに、"),
        ("Furthermore, ", "さらに、"),
        ("Finally, ", "最後に、"),
        ("First, ", "まず、"),
        ("Second, ", "次に、"),
        ("Then ", "その後 "),
        ("Also,", "また、"),
    ]
    # Only apply glossary pass for short-ish lines to avoid garbage
    if len(t) < 220 and re.match(r"^[A-Za-z\"'#\\(\[]", t):
        out = t
        for a, b in glossary:
            out = out.replace(a, b)
        # if still mostly ASCII letters words, prefix note
        letters = sum(1 for ch in out if ch.isalpha() and ord(ch) < 128)
        jp = sum(1 for ch in out if "\u3040" <= ch <= "\u9fff")
        if letters > 40 and jp < 5:
            return "（説明）" + out
        return out
    return text


def translate_heading(line: str) -> str:
    s = line.strip()
    for pat, rep in HEADING_SUB:
        ns = re.sub(pat, rep, s)
        if ns != s:
            s = ns
    return s


def translate_prose_paragraph(para: str) -> str:
    key = para.strip("\n")
    if key in CORE_EXACT:
        return CORE_EXACT[key]
    if key in EXACT:
        return EXACT[key]

    # heading
    if key.startswith("#"):
        return translate_heading(key)

    # bullet lists of contents-like lines: "1.1 Pre-defined Variables"
    if re.match(r"^-?\s*[\d.]+\s+\S", key) or key.startswith("- "):
        # translate known section names inside
        out = key
        for eng, ja in [
            ("Pre-defined Variables", "あらかじめ定義された変数"),
            ("Template Variables", "テンプレート変数"),
            ("Signature Forms", "シグネチャ形式"),
            ("Struct Signatures", "構造体シグネチャ"),
            ("Pre-defined Functions", "あらかじめ定義された関数"),
            ("Pre-Defined Functions", "あらかじめ定義された関数"),
            ("Numbers: Integers, Rationals, Reals, Complex, Exacts, Inexacts", "数: 整数・有理数・実数・複素数・正確数・非正確数"),
            ("Numbers (relaxed conditions plus)", "数（緩和条件・拡張）"),
            ("Numbers (relaxed conditions)", "数（緩和条件）"),
            ("Booleans", "真偽値"),
            ("Symbols", "シンボル"),
            ("Lists", "リスト"),
            ("Posns", "Posn"),
            ("Characters", "文字"),
            ("Strings", "文字列"),
            ("String (relaxed conditions)", "文字列（緩和条件）"),
            ("Images", "画像"),
            ("Misc", "その他"),
            ("Signatures", "シグネチャ"),
            ("Higher-Order Functions (with Lambda)", "高階関数（lambda つき）"),
            ("Higher-Order Functions", "高階関数"),
            ("Reading and Printing", "読み取りと表示"),
            ("Vectors", "ベクタ"),
            ("Boxes", "ボックス"),
            ("Hash Tables", "ハッシュ表"),
            ("Common Syntaxes", "共通の構文"),
            ("Syntaxes for Beginning Student with List Abbreviations", "リスト略記つき初級の構文"),
            ("Syntax for Intermediate with Lambda", "lambda つき中級の構文"),
            ("Syntax for Intermediate", "中級の構文"),
            ("Syntax for Advanced", "上級の構文"),
            ("Syntax", "構文"),
            ("Beginning Student with List Abbreviations", "リスト略記つき初級学生言語"),
            ("Beginning Student", "初級学生言語"),
            ("Intermediate Student with lambda", "lambda つき中級学生言語"),
            ("Intermediate Student", "中級学生言語"),
            ("Advanced Student", "上級学生言語"),
            ("Posn", "Posn"),
        ]:
            out = out.replace(eng, ja)
        return out

    # multi-line paragraph: translate line by line with phrase rules, then join
    lines = key.split("\n")
    # try whole as phrase first
    joined = " ".join(x.strip() for x in lines)
    if joined in CORE_EXACT:
        return CORE_EXACT[joined]
    if joined in EXACT:
        return EXACT[joined]

    # known long paragraphs (space-normalized keys)
    long_map = {
        "The grammar notation uses the notation X... (bold dots) to indicate that X may occur an arbitrary number of times (zero, one, or more). Separately, the grammar also defines... as an identifier to be used in templates.": "文法の記法では、X...（太字の点）という書き方で、X が任意の回数（0回、1回、またはそれ以上）現れてよいことを示します。別に、文法はテンプレートで使う識別子として ... も定義します。",
        "See How to Design Programs/2e, Intermezzo 1 for an explanation of the Beginning Student Language.": "Beginning Student Language の説明は、How to Design Programs/2e の Intermezzo 1 を参照してください。",
        "A name or a variable is a sequence of characters not including a space or one of the following:": "名前 (name) または変数 (variable) は、空白や次の文字を含まない文字の並びです。",
        "A number is a number such as 123, 3/2, or 5.5.": "数 (number) とは、123、3/2、5.5 のような数です。",
        "A boolean is one of: #true or #false.": "真偽値 (boolean) は #true または #false のいずれかです。",
        "The languages documented in this manual are provided by DrRacket to be used with the How to Design Programs book.": "このマニュアルで説明されている言語は、How to Design Programs の本と一緒に使うために DrRacket が提供するものです。",
        "While these languages are normally selected using the Choose Language dialog in DrRacket, they can also be accessed using the #lang language directive as the first line of code in DrRacket or other editors.": "通常これらの言語は DrRacket の Choose Language ダイアログで選びますが、DrRacket や他のエディタでは、コードの先頭行に #lang 言語指定を書いてもアクセスできます。",
        "When programs in these languages are run in DrRacket, any part of the program that was not run is highlighted in orange and black. These colors are intended to give the programmer feedback about the parts of the program that have not been tested. To avoid seeing these colors, use check-expect to test your program. Of course, just because you see no colors, does not mean that your program has been fully tested; it simply means that each part of the program has been run (at least once).": "これらの言語のプログラムを DrRacket で実行すると、実行されなかった部分がオレンジと黒で強調表示されます。この色は、まだテストされていない部分についてプログラマにフィードバックするためのものです。この色を見たくなければ、check-expect でプログラムをテストしてください。もちろん、色が見えないからといって十分にテスト済みとは限りません。各部分が（少なくとも1回）実行された、という意味にすぎません。",
        "Beginning Student #lang htdp/bsl": "初級学生言語 #lang htdp/bsl",
        "Beginning Student with List Abbreviations #lang htdp/bsl+": "リスト略記つき初級 #lang htdp/bsl+",
        "Intermediate Student #lang htdp/isl": "中級学生言語 #lang htdp/isl",
        "Intermediate Student with lambda #lang htdp/isl+": "lambda つき中級 #lang htdp/isl+",
        "Advanced Student #lang htdp/asl": "上級学生言語 #lang htdp/asl",
        "Alternative spellings for the #true constant are #t, true, and #T. Similarly, #f, false, or #F are also recognized as #false.": "#true 定数の別表記は #t、true、#T です。同様に #f、false、#F も #false として認識されます。",
        "A symbol is a quote character followed by a name. A symbol is a value, just like 42, \'(), or #false.": "シンボル (symbol) は、クォート文字に続く名前です。シンボルは 42、\'()、#false などと同じく値です。",
        "A character begins with #\\ and has the name of the character. For example, #\\a, #\\b, and #\\space are characters.": "文字 (character) は #\\ で始まり、その文字の名前を持ちます。たとえば #\\a、#\\b、#\\space は文字です。",
        "In function calls, the function appearing immediately after the open parenthesis can be any functions defined with define or define-struct, or any one of the pre-defined functions.": "関数呼び出しでは、開き括弧の直後に現れる関数は、define や define-struct で定義した関数、またはあらかじめ定義された関数のいずれかです。",
        "Defines a function named name. The expression is the body of the function. When the function is called, the values of the arguments are inserted into the body in place of the variables. The function returns the value of that new expression.": "name という名前の関数を定義します。expression は関数本体です。関数が呼ばれると、引数の値が変数の代わりに本体へ挿入されます。関数は、その新しい式の値を返します。",
        "The function name’s cannot be the same as that of another function or variable.": "関数名は、他の関数や変数と同じであってはなりません。",
        "Defines a variable called name with the the value of expression. The variable name’s cannot be the same as that of another function or variable, and name itself must not appear in expression.": "expression の値で name という変数を定義します。変数名は他の関数や変数と同じであってはならず、name 自身が expression に現れてはなりません。",
        "else cannot be used outside of cond.": "else は cond の外では使えません。",
        "The empty list.": "空リスト。",
        "Multiplies all numbers.": "すべての数を掛け合わせます。",
        "Adds up all numbers.": "すべての数を足し合わせます。",
        "Subtracts the second (and following) number(s) from the first; negate the number if there is only one argument.": "第1引数から第2（およびそれ以降）の数を引きます。引数が1つだけのときは符号を反転します。",
        "Divides the first by the second (and all following) number(s).": "第1引数を第2（およびそれ以降）の数で割ります。",
        "Determines whether some value is a number.": "値が数かどうかを判定します。",
        "Determines whether some number is an integer (exact or inexact).": "数が整数（正確・非正確）かどうかを判定します。",
        "Determines whether some value is a boolean.": "値が真偽値かどうかを判定します。",
        "Determines whether some value is a string.": "値が文字列かどうかを判定します。",
        "Determines whether some value is a symbol.": "値がシンボルかどうかを判定します。",
        "Determines whether some value is a character.": "値が文字かどうかを判定します。",
        "Determines whether some value is an image.": "値が画像かどうかを判定します。",
        "Determines whether some value is a function.": "値が関数かどうかを判定します。",
        "Determines whether two values are structurally equal.": "2つの値が構造的に等しいかどうかを判定します。",
        "Determines whether two values are eq?.": "2つの値が eq? かどうかを判定します。",
        "Determines whether two values are eqv?.": "2つの値が eqv? かどうかを判定します。",
        "A string is a sequence of characters enclosed by a pair of \". Unlike symbols, strings may be split into characters and manipulated by a variety of functions. For example, \"abcdef\", \"This is a string\", and \"This is a string with \\\" inside\" are all strings.": "文字列 (string) は、一対の \" で囲まれた文字の並びです。シンボルと違い、文字列は文字に分割したり、さまざまな関数で操作したりできます。たとえば \"abcdef\"、\"This is a string\"、および \"This is a string with \\\" inside\" はすべて文字列です。",
        "If none of the question-expressions evaluates to #true, cond’s value is the answer-expression of the else clause. If there is no else, cond reports an error. If the result of a question-expression is neither #true nor #false, it is an error.": "どの question-expression も #true に評価されない場合、cond の値は else 節の answer-expression です。else がなければ cond はエラーを報告します。question-expression の結果が #true でも #false でもなければエラーです。",
        "A check-expect expression must be placed at the top-level of a student program. Also it may show up anywhere in the program, including ahead of the tested function definition. By placing check-expects there, students can easily navigate to the test cases of a function.": "check-expect 式は学生プログラムのトップレベルに置く必要があります。また、テスト対象の関数定義より前を含め、プログラムのどこに置いてもかまいません。そこに check-expect を置くことで、関数のテストケースへ簡単に移動できます。",

    }
    if joined in long_map:
        return long_map[joined]

    # Multi-line English paragraph: join then phrase-translate as one unit
    if len(lines) > 1:
        return phrase_translate(joined if joined.endswith(".") else joined + "")
    return phrase_translate(lines[0].strip())


def translate_box_line(line: str) -> str:
    out = line
    for a, b in LABELS.items():
        out = out.replace(a, b)
    return out


def translate_file(src: Path, dst: Path, title: str, source_note: str) -> None:
    text = src.read_text(encoding="utf-8")
    lines = text.splitlines()
    out: list[str] = []
    out.append(f"# {title}")
    out.append("")
    out.append(f"**原本:** `{source_note}`")
    out.append("")
    out.append("初学者向けに、説明文を日本語へ翻訳しています。コード・シグネチャ・実行例は原文のまま保持します。")
    out.append("")

    i = 0
    in_fence = False
    fence_is_box = False
    # skip original HTML comment headers
    while i < len(lines) and (
        lines[i].startswith("<!--") or lines[i].strip() == ""
    ):
        i += 1

    buf: list[str] = []

    def flush_buf():
        nonlocal buf
        if not buf:
            return
        para = "\n".join(buf)
        out.append(translate_prose_paragraph(para))
        out.append("")
        buf = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("```"):
            flush_buf()
            if not in_fence:
                in_fence = True
                # peek next non-empty to detect box
                fence_is_box = False
                for j in range(i + 1, min(i + 5, len(lines))):
                    if lines[j].strip().startswith("+") or lines[j].strip().startswith("|"):
                        fence_is_box = True
                        break
                    if lines[j].strip() and not lines[j].strip().startswith("|"):
                        break
                out.append(line)
            else:
                out.append(line)
                in_fence = False
                fence_is_box = False
            i += 1
            continue

        if in_fence:
            if fence_is_box:
                out.append(translate_box_line(line))
            else:
                out.append(line)  # code unchanged
            i += 1
            continue

        if stripped.startswith("<!--"):
            i += 1
            continue

        if stripped == "":
            flush_buf()
            if out and out[-1] != "":
                out.append("")
            i += 1
            continue

        # Markdown headings only (not Racket literals like #true / #F)
        if re.match(r"^#{1,6}\s", stripped):
            flush_buf()
            out.append(translate_heading(stripped))
            out.append("")
            i += 1
            continue

        buf.append(line.rstrip())
        i += 1

    flush_buf()
    # tidy blank lines
    text_out = "\n".join(out)
    text_out = re.sub(r"\n{3,}", "\n\n", text_out).strip() + "\n"
    dst.write_text(text_out, encoding="utf-8")


def main() -> None:
    # merge more exact phrases from frequency file if we expand later
    EXACT.update(CORE_EXACT)
    for src_name, dst_name, title, note in JOBS:
        src = SRC_DIR / src_name
        dst = ROOT / dst_name
        if not src.exists():
            print("MISSING", src)
            continue
        translate_file(src, dst, title, note)
        print(f"Wrote {dst.name} ({dst.stat().st_size:,} bytes) from {src.name}")


if __name__ == "__main__":
    main()
