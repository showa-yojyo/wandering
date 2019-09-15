---
title: Git の単語補完およびプロンプト変更導入ノート
tags: bash git
---

Cygwin の `bash` ターミナルにおいて、Git が提供する文字列補完機能とメインプロンプトを変更する機能を取り込む。
いずれの実現もファイル `.bashrc` の編集を前提とする。

# 補完編

取り込む手順の概要を記す。個人だけで保管機能を有効にする状況を想定している。

1. ファイル `.git-completion.sh` をインストール済み Git のどこかディレクトリーから自分の `HOME` に複製する。
2. ファイル `$HOME/.bashrc` を適宜編集する。

   元ネタがどこに記述されていたのか忘れたが、こういうコードを `.bashrc` に追加すればいい。

   ```bash
   if [ -f "${HOME}/.git-completion.sh" ] ; then
       source "${HOME}/.git-completion.sh"
   fi
   ```

複製したファイル `.git-completion.sh` はとりあえずは編集しなくてよい。当然、最新版の内容を上書きすることはあるだろう。

この結果、この設定が有効であるセッションではコマンド `git` のパラメーター入力時にタブキーを二発打ち込むと、
文脈に応じて有効な文字列が画面に表示される。一例を以下に示す。

```shell
bash$ git log --s<TAB><TAB>
--shortstat                --simplify-merges          --sparse                   --stat
--simplify-by-decoration   --since=                   --src-prefix=              --summary
```

なお、Git には別名機能も実装されているが、こちらに肩代わりさせるのがいいと思われる。

# プロンプト編

取り込む手順の概要を記す。

1. ファイル `.git-prompt.sh` をインストール済み Git のどこかディレクトリーから自分の `HOME` に複製する。
2. ファイル `$HOME/.bashrc` を適宜編集する。

   編集内容は次のようになる：

   ```bash
   GIT_PS1_SHOWUPSTREAM="verbose"
   GIT_PS1_SHOWCOLORHINTS="yes"

   if [ -f "${HOME}/.git-prompt.sh" ] ; then
     source "${HOME}/.git-prompt.sh"
   fi

   #export PS1='[$OSTYPE \s \W \!]\\$ '
   export PROMPT_COMMAND='__git_ps1 "[$OSTYPE \\s \\W" " \\!]\\\$ "'

   # PS2, PS3, PS4...
   ```

   最初の塊はメインプロンプトの Git によるカスタマイズのオプション指定を意味する。
   これらの変数の役割は、後述する関数 `__git_ps1` の挙動を調整することだ。
   有効な変数と値の定義はコメントが丁寧に付いている `.git-prompt.sh` を読めばわかる。

   二番目の塊でスクリプトファイル `.git-prompt.sh` をセッションに取り込んでいる。

   最後の `export` 文は、メインプロンプト `PS1` を直接変更する代わりに、
   環境変数 `PROMPT_COMMAND` にコマンドを指示することで間接的に変更する。
   関数 `__git_ps1` の挙動を制御するのが、さきほどの変数だ。

私の実際の例を次に示す。変数 `PS1` の定義は上の通りだ。

```shell
[cygwin bash dotfiles (master u+2) 118]$ git push
Enumerating objects: 8, done.
...
   a6efe1d..0470d90  master -> master
[cygwin bash dotfiles (master u=) 119]$
```

ここではわからないが、実際にはブランチ名には色が着く。
ブランチ名に続く `u+2` や `u=` などが作業コピーの状態を示唆しているのは明らかだ。
しょっちゅう `git status` を実行する人は、プロンプトをこのように改造するのがいいだろう。

