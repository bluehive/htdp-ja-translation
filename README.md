# 「How to Design Programs, Second Edition」日本語翻訳プロジェクト

本書は Matthias Felleisen、Robert Bruce Findler、Matthew Flatt、Shriram Krishnamurthi による名著『How to Design Programs, Second Edition』(HTDP 2e) を日本語に翻訳する有志プロジェクトです。

## 目的
*   書籍全体（目次、序文、プロローグ、全6部、エピローグ）を日本語に翻訳
*   サンプルコード（Racket / BSL / ISL など）は学習のために原文のまま厳密に保持
*   結合した成果物を PDF および EPUB 形式としてビルドし、電子書籍リーダー等で閲覧可能にする

## 翻訳手法
本プロジェクトの翻訳は、**Gemini 3.5** を含む AI アシスタントを用いて行われています。原文の論理的な構造やプログラムの仕様を完全に崩さず、日本語として読みやすく自然な表現に仕上げています。

## 現在の進捗状況
*   **前付け・目次 (00)**: 翻訳完了
*   **序文・プロローグ (01-02)**: 翻訳完了
*   **第I部 固定サイズのデータ (03)**: 
    *   第1章・第2章: コードブロックを保持した簡易訳を追加完了
    *   第3章 (How to Design Programs): 詳細な日本語翻訳が完了
    *   第4章 (Intervals, Enumerations, Itemizations): 詳細な日本語翻訳が完了
*   **第III部 抽象化 (07)**:
    *   第14章 (Similarities Everywhere): 詳細な日本語翻訳が完了
    *   第15章 (Designing Abstractions): 詳細な日本語翻訳が完了
    *   第17章 (Nameless Functions): 無名関数 (lambda) の翻訳下書きを配置完了

その他の部・章・Intermezzoについては、今後の翻訳作業用の見出しプレースホルダーファイルを作成済みです。

## ビルド方法

### 必要ツール
1.  **Pandoc**: Markdown の結合・EPUB/PDF 生成に使用します。
2.  **Typst**: Pandoc の PDF 生成エンジンとして使用する、非常に軽量かつ高速な組版ツールです。
    *   システムにない場合、ビルドスクリプトが Windows の `winget` 経由で自動検出・インストールを行います。
3.  **BIZ UDMincho フォント**: Windows 10/11 に標準搭載されているユニバーサルデザインフォントです。PDF の日本語表示にデフォルトで適用されます。

### ビルド実行手順
Windows の PowerShell を起動し、リポジトリのルートディレクトリで以下のスクリプトを実行します：

```powershell
.\build_translation.ps1
```

実行後、ルートディレクトリに以下の成果物が生成されます：
*   **EPUB形式**: `htdp2e-ja.epub` (目次およびメタデータ付)
*   **PDF形式**: `htdp2e-ja.pdf` (BIZ UDMinchoフォントによる高品位組版)

## ライセンス

*   **本翻訳プロジェクトコード・翻訳文書**: **MIT License**
*   **原著（英文）**: Matthias Felleisen, Robert Bruce Findler, Matthew Flatt, Shriram Krishnamurthi (CC BY-NC-ND)
    *   原典: https://htdp.org/
