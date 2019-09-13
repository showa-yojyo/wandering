---
title: 『岩波基礎講座 基礎数学 集合と位相』学習ノート Part 1
tags: math
---

彌永昌吉・彌永健一著『岩波基礎講座 基礎数学 9 集合と位相 I』より。

本書で使われている記号と私がよく使う記号が衝突しているが、うまくごまかしてメモを取る。

----

* 集合論を記述するのに、その基礎となる論理的命題についての簡単な説明にとどめる。
  形式論理学的記号は用いない。
* §1.1 対象、族、命題、論理学
  * **排中律**を仮定する。$P \lor \lnot P$ はつねに成り立つとする。
    * この「または」は数学では珍しい（というか、直接的にはここにしか出てこない）論理的排他和の意味に取る。
  * **命題**とは、文章の一種であり、数学的対象について記号などを用いて記述されたものだ。
  * **定理**とは、命題の一種であり、論理的操作によりそれが成り立つことが示されたものだ。
  * **証明**とは、論理的操作の一種であり、ある定理が成り立つことを示すものだ。
  * **公理**とは、仮定の一種であり、証明のための出発点となるものだ。
  * (1.1) 「ならば」を否定と「または」で言い換える

    $$
    \forall P \forall Q (P \implies Q) \iff (\lnot P \lor Q).
    $$

    * 証明
      * 十分条件：$P$ が成り立つことから、
        * $\lnot P$ が成り立たない。排中律による。
        * $Q$ が成り立つ。仮定に書いてある。

      以上により $\lnot P \lor Q$ は成り立つ。
      * 必要条件：$(\lnot P \lor Q) \land P$ のとき、明らかに $Q$ が成り立つことが必要。
        すなわち $P \implies Q$ が成り立つ。
  * (1.2) これをみるといつも不思議に思う：

    $$
    \lnot P \lor P \implies Q
    $$

    * (1.1) を用いて真理表を書くとわかる。
    * $P \implies Q$ を考える。$\lnot P$ が真ならば $Q$ の如何を問わず $P \implies Q$ が成立する。
  * 命題に関する各種ルール（二重否定は肯定、べき等律、交換律、結合律）
  * (1.3) 対偶

    $$
    (P \implies Q) \iff (\lnot Q \implies \lnot P)
    $$

  * 命題に関する性質（推移律、de Morgan の法則）
  * 帰謬法（背理法と同義だろう）

    $$
    (P \implies Q \land \lnot Q) \implies \lnot P.
    $$

    * 証明：(1.3) を利用して、さらに排中律を適用する。
    * $P$ を仮定すると「$Q$ であると同時に $Q$ ではない」という矛盾に陥る。
      すなわち $P$ を仮定するべきではなかったのであり、$P$ は偽だということだ。
  * 命題に関する性質（分配法則）
  * 変数をとる命題を $P(x)$ などのように表す。
    * この $x$ を**変数**という。
    * $\forall x P(x)$ や $\exists x P(x)$ のような $x$ を**束縛変数**という。
      * プログラミング用語のそれはここから拝借したのだろう。
      * 記号 $\forall$ と $\exists$ を**限定記号**という。
    * そうでない変数を**自由変数**という。
  * (1.4) 限定記号のついた命題の否定

    $$
    \lnot(\forall x P(x)) \iff \exists x \lnot P(x).
    $$

  * 大昔に習った（英語の）否定文の作り方は論理の問題だった。
* §1.2 外延性公理、集合、§1.3 非順序対、合併、無限公理
  * **集合**には 10 個からなる公理がある。今まで全然承知していなかった。
    (S1) から (S10) までを記すが、最後の方の公理はもっと後になって出てくるようだ。
  * (S1) 外延性公理
    * 集合同士が一致する条件？

    $$
    \forall a \forall b (a = b \iff \forall x (x \in a \iff x \in b)).
    $$

  * (S2) 空集合の存在定理
    * **空集合**と呼ばれる集合が（ただ一つ）存在する。

    $$
    \exists a \forall x (\lnot (x \in a)).
    $$

    * 一意性は証明で得られる。
    * この述語部分はふだんは $x \notin a$ と記される。
  * (S3) 非順序対の存在公理

    $$
    \forall a \forall b \exists c \forall x (x \in c \iff x = a \lor x = b).
    $$

    * 非順序対とは、プログラミング用語でいうところの unordered pair そのものだ。
    * これを $c = \lbrace a, b\rbrace$ と記す。
    * $b = a$ のときは $c = \lbrace a\rbrace$ と記す。
    * $\varnothing \ne \lbrace\varnothing\rbrace$ とする。
  * (S4) 合併集合の公理

    $$
    \forall a \exists b \forall x (x \in b \iff \exists c (c \in a \land x \in c)).
    $$

    * この $b$ を $\displaystyle \bigcup_{c \in a}c$ とか $\displaystyle \bigcup a$ とかで表す。
    * この公理により $a \cup b$ の概念が定まった。
    * 先述の unordered pair の概念が unordered tuple の概念に拡張されている。
      プログラミングの考え方が論理の理解に役立つのは面白い（本当は逆だろうが）。
  * (S5) 無限公理

    $$
    \exists a (\varnothing \in a \land \forall x (x \in a \implies x^+ \in a)).
    $$

    * ただし $x^+ = x \cup \lbrace x\rbrace$ とする。**後継ぎ**と呼ぶ。
    * 後継ぎは集合 $x$ に対して得られる新しい集合と考えられる。
    * この公理をみたす集合を**無限系譜**とよぶ（これは一意的に定まるか考えてみる）。
