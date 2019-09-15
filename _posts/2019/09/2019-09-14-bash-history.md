---
title: Bash 履歴展開機能についてのノート
tags: bash
---

`bash` の履歴機能の研究。
というより履歴展開機能のことが完全に頭から抜けているので学ぼう。
今からでも遅くない。これを習得して上キーを連打する習慣とはおさらばしたい。

## 履歴拡張

履歴拡張の意味は後で記す。

* ふつうは履歴拡張機能は有効になっているが、`set +H` で無効にすることもできる。
* シェルオプション `histverify` を有効にすると、履歴置換を行った結果をすぐにシェルに渡させずに、代わりに展開結果を編集バッファに出力して編集状態にできる。
* シェルオプション `histreedit` を有効にすると、履歴展開失敗時に展開結果を編集バッファに出力して編集状態にできる。
* `history -p` で履歴展開のプレビューができる。
* `history -s` でコマンドを実行なしで履歴に追加できる。

## Event Descritors

履歴に残っているコマンドからこれから何をしたいのかを述べるためのパターンの仕様だ。

基本：履歴の番号は組み込みコマンド `history` または `fc -l` で確認できる。
プロンプト `PS1` に履歴番号を仕込んでもいい。

| Event&nbsp;Descriptor&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 挙動 | コメント |
| ------------- | ------------------- | -- |
| `!n` | コマンド履歴の n 番目のコマンドを実行する。| 忘れていたので使うようにしたい。 |
| `!-n` | n 個前のコマンドを実行する。| 編集不要時でも上キーを何度も押さずに済む。 |
| `!!` | A synonym for `!-1`. | 編集不要ならば上キーで間に合う。 |
| `!string` | `string` から**始まる**履歴最後にいちばん近いコマンドを再実行。 | `C-r string` の代わりに使うかもしれない。 |
| `!?string[?]` | `string` を**含む**履歴最後にいちばん近いコマンドを再実行。 | `C-r string` の代わりに使うかもしれない。 |
| `^ string1 ^ string2 ^` | 直前のコマンドの `string1` を `string2` に置換して実行。 | タイプミスしたコマンド実行の直後に修正して使うという用途だろう。 |
| `!#` | これまでに打ち込んだコマンドライン全体。 | 実行時に展開される。使えるか？ |

以上のものについては詳細な説明や例示は不要だろう。

## Word Designators

Event を述べたあと、オプショナルにそこから何かの部分を指示することができる。

* Event 直後に `:` を入力してから指示する。
  * ただし event を与えない場合も使える。そのときは直前実行コマンドが採用されることになっている。
  * ただし WD が `^`, `$`, `*`, `-`, `%` のいずれかで始まる場合には省略可。
* Word には行の先頭から番号が振られる（先頭が 0 番目）。
* Word は現在の行に空白文字で区切られて挿入される。

| WD&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 意味 | コメント |
| ---| --- | ------ |
| `0` | 0 番目の word | コマンド名になるのが普通だ。 |
| `n` | n 番目の word | NC |
| `^` | 1 番目の word | コマンドの最初の引数であるのが普通だ。 |
| `$` | 最後の word | 最後の引数はよく参照する機会があるだろう。 |
| `%` | 最近行った `!?string?` 検索にマッチする word | NC |
| `[x]-y` | word の範囲指定 | `y` 番目を含む。 |
| `x*` | `x-$` と同値 | NC |
| `*` | `1-$` と同値 | つまりコマンド名以外。 |
| `x-` | `x-$` に似ているが、最後の word を含まない | 最終引数だけ変えたいときなどに有用。 |

## Modifiers

オプションで、WD の後には modifier を `:` 区切りで指定することができる。

| Modifier | だいたいの意味 | コメント |
| ----- | --- | ----- |
| `h` | パスのディレクトリー部分以降を捨てる | 例参照 |
| `t` | パスのファイル名以前を捨てる | 例参照 |
| `r` | ファイル名の拡張子以降を捨てる | 例参照 |
| `e` | ファイル名の拡張子以前を捨てる | 例参照 |
| `p` | 展開プレビュー | ``echo`` の代わり |
| `q` | 指定 words を括るように引用符で囲む | パスが空白文字を含むときに有用か |
| `x` | 指定各 word を引用符で囲む（空白文字で単語分割する） | 例参照 |
| `s/old/new/` | `sed` の置換と似ている | 例参照 |
| `&` | 直前の置換を繰り返す | `s/old/new/` の `new` に込められる |
| `g` | 置換の際に置換を全体にまんべんなく適用する | 例参照 |
| `a` | A synonym for `g` | NC |
| `G` | 置換の際に置換を一つの word に対して一度だけ行う | 例参照 |

### Examples

ディレクトリー名とファイル名を扱う `h` と `t`:

```shell
[1]bash$ echo /usr/local/bin/perl
/usr/local/bin/perl
[2]bash$ echo !1:$:h and !1:$:t
echo /usr/local/bin and perl
/usr/local/bin and perl
```

拡張子を取り扱う `r` と `e`:

```shell
[3]bash$ touch README.rst
[4]bash$ echo !3:$:r and !3:$:e
echo README and .rst
README and .rst
```

引用符で囲む modifiers の挙動の違いを示す（例に深い意味はない）：

```shell
[5]bash$ git mv hikihune.md hikifune.md
...
[6]bash$ echo !5:*:q
echo 'mv 00-hikihune.md 00-hikifune.md'
mv 00-hikihune.md 00-hikifune.md
[7]bash$ echo !5:*:x
echo 'mv' '00-hikihune.md' '00-hikifune.md'
mv 00-hikihune.md 00-hikifune.md
```

置換の例。`g` と `G` の違いをドキュメントから理解しにくかった。想像で試したら正しかった：

```shell
[8]bash$ code A.cpp B.cpp C.cpp
...
[9]bash$ !!:gs/.cpp/.h/
code A.h B.h C.h
...

[10]bash$ echo cppcppcppcpp
cppcppcppcpp
[11]bash$ !10:Gs/cpp/cccp/
echo cccpcppcppcpp
cccpcppcppcpp
[12]bash$ !10:gs/cpp/cccp/
echo cccpcccpcccpcccp
cccpcccpcccpcccp
```
