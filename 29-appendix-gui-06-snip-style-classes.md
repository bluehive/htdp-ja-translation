# 6 スニップとスタイルのクラス

**原本:** `extracted/appendix/gui/original_markdown_06_Snip_and_Style_Classes.md`  
**Source URL path:** `/gui/Snip_and_Style_Classes.html`

```
+------------------------+---------------------+
|  (require racket/snip) | package: `snip-lib` |
+------------------------+---------------------+
+------------------------+---------------------+
```

`racket/snip` コレクションは、`racket/gui/base` に依存せずに、スニップおよびスタイルの中核クラスを提供します。この分離により、エディタと連携できる一方で、GUI が無い文脈でも動作するライブラリを書けるようになります。

スニップとアドミニストレータ：

```
+--------------------------------------------------+
| snip% readable-snip<%>                           |
+--------------------------------------------------+
| `|`- string-snip%                                |
| `|` `|`- tab-snip%                               |
| `|`- image-snip%                                 |
| `|`- editor-snip% `(`not provided by racket`/`s… |
| snip-admin%                                      |
+--------------------------------------------------+
```

スニップリスト：

```
+--------------------+
| snip-class%        |
+--------------------+
| snip-class-list<%> |
+--------------------+
```

スタイル：

```
+------------------------------------+
| style<%> style-delta% add-color<%> |
+------------------------------------+
| style-list% mult-color<%>          |
+------------------------------------+
```

アルファベット順：

### 目次

- 6.1 add-color<%>
- 6.2 image-snip%
- 6.3 mult-color<%>
- 6.4 readable-snip<%>
- 6.5 snip%
- 6.6 snip-admin%
- 6.7 snip-class%
- 6.8 snip-class-list<%>
- 6.9 string-snip%
- 6.10 style<%>
- 6.11 style-delta%
- 6.12 style-list%
- 6.13 tab-snip%
