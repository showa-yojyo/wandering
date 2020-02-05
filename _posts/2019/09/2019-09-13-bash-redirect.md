---
title: Bash Redirection ノート
tags: bash
---

暇なので `bash` のリダイレクトを復習する。本稿では file descritor を FD と呼ぶ。

## Redirection

* 入力元や出力先を「向き直す」という意味に捉える。
* 覚えにくい要素が複数あるのが困る。
  * 基本的な指示方法：数字、不等号、アンドマークの順番が基本。
  * 既定値の存在のうっかり：毎度 FD を明示すればいいが、それはダサい。
  * コマンドとリダイレクト宣言を同一ラインに書いたときの処理順序
* `/dev/null` の説明が本節にはない。どこだろう？
* まず FD を閉じる方法を押さえる。

  ```shell
  bash$ exec n>&-
  bash$ exec n<&-
  ```

* リダイレクトに用いられる特別なファイル名というのがある：
  * `/dev/fd/`*fd*
  * `/dev/stdin`: FD 0 に相当。
  * `/dev/stdout`: FD 1 に相当。
  * `/dev/stderr`: FD 2 に相当。
  * `/dev/tcp/`*host/port*: 後述の `<>` の例で扱う。
  * `/dev/udp/`*host/port*

### Redirecting Input

読み込み FD の開き方とでも言えばいいのか。

```shell
bash$ some_command n< some_source
```

* 不等号の**前に**数字を宣言する。
* 省略すると標準入力 1 が指定されたものとみなされる。
* 結果、指定した FD とファイル（と今の段階ではしておく）が結び付けられる。

こういう使い方もある：

```shell
bash$ exec 3< some_file
bash$ some_command <& 3 # 後述
```

### Redirecting Output

書き込み FD の開き方。

```shell
bash$ some_command n> some_destination
```

* 不等号の**前に**数字を宣言する。
* 省略すると標準出力 2 が指定されたものとみなされる。
* 結果、指定した FD とファイルが結び付けられる。

この機能で問題になりがちなのは、標準エラー出力の内容を（ファイルに）欲しいときだ。
次の書き方をする：

```shell
bash$ some_command 2> some_destination
bash$ some_command > stdout.txt 2> stderr.txt
```

* シェルオプション `noclobber` のセットの有無によって、ファイルに上書きできたりできなかったりすることは覚えておく。
* 明示的に既存ファイルの上書きを防ぐリダイレクトの記法は：

  ```shell
  bash$ some_command >| some_destination
  ```

### Appending Redirected Output

```shell
bash$ some_command n>> some_destination
```

基本。ここはいい。

### Redirecting Standard Output and Standard Error

```shell
bash$ some_command &> some_destination # preferred; equivalent to `some_command > some_destination 2>& 1`.
bash$ some_command >& some_destination
```

記号の順序を記憶できなくて困っていたが、実はどちらも同じ意味だったようだ。

### Appending Standard Output and Standard Error

```shell
bash$ some_command &>> some_destination # equivalent to `some_command >> some_destination 2>& 1`.
```

### Here Documents

```shell
bash$ some_commands <<word
    here-documents
delimiter
```

* この機能はリダイレクト機能の一種だ。`word` には `EOF` がよく採用される。
* `<<word` だけでなく `<<-word` という指示もある。行頭タブ文字を無視するようになる。

### Here Strings

```shell
bash$ some_command <<<word
```

* これもリダイレクトの一種。
* 文字列を標準入力化する機能がある。使用例を示したほうがわかりやすいか：

  ```shell
  bash$ sed '/s/:/\n/g' <<<$PATH # or `echo -n ${PATH//:/\\n}`
  /bin
  /usr/local/bin
  ...
  ```

### Duplicating File Descriptors

```shell
bash$ some_command n<&word # default: n=0 (stdin)
bash$ some_command n>&word # default: n=1 (stdout)
```

何が複製なのかよくわからない。例えば `some_cmd > some_dest 2>&1` とすると、
`some_cmd` の標準出力の内容と標準エラー出力の内容の両方が標準出力に流出する。

### Moving File Descriptors

```shell
bash$ exec n<&digit-
bash$ exec n>&digit-
```

どちらも右辺の FD を左辺のそれに名前を変える。
何に使うのがいいのかわからない（少し調べたら、descriptor の復元に使えるらしいが）。

### Opening File Descriptors for Reading and Writing

```shell
bash$ exec n<>word
```

ファイルを FD `n` として定義して、以降の処理で読み書き両方に取り扱えるようにする。

```shell
bash$ exec 9<>/dev/tcp/www.example.com/80
bash$ echo -e "GET / HTTP/1.1\n..." >&9
bash$ cat <&9
```

----

あまりまとまらなかった。
