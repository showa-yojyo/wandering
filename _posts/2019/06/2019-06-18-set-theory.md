---
title: 『岩波基礎講座 基礎数学 集合と位相』学習ノート Part 2
tags: math
---

彌永昌吉・彌永健一著『岩波基礎講座 基礎数学 9 集合と位相 I』より。

----

* §1.4 分出公理、共通部分、べき集合
  * $(S6)$ **分出公理**

    集合とその要素に対する述語（性質）をそれぞれ $a, P(\cdot)$ とする。
    このとき「$P(x)$ が真である $a$ の要素 $x$ の全体 $b$」は集合である：

    $$
    \tag*{$(S6)$}
    \forall a \exists b \forall x (x \in b \iff x \in a \land P(x)).
    $$

    * つまり $\lbrace x \in a\,\mid\, P(x)\rbrace$ は集合であるといっている。
      * しかも $a$ の部分集合である。
    * この公理のキモは $P(\cdot)$ がどんな言葉で表されているかにある。
      そして、その仕様にバリエーションが多い……。
    * Russel の逆理を回避するための公理だそうだが、どういうことかわかるか。

      $$\{x \,|\, x \notin x\}$$

  * **共通部分**、**べき等律**、**交換律**、**結合律**等々の定義および性質。
  * **分配法則**
  * **集合論的差** $a-b$
    * $a \setminus b$ のこと。
  * **補集合**
    * $a^{c}$ の記号を採用する。
  * $(S7)$ **べき集合の公理**

    集合 $a$ には、$x \subset a$ ならば $x \in b$ を満たす集合 $b$ が存在する：

    $$
    \tag*{$(S7)$}
    \forall a \exists b \forall x (x \in b \iff x \subset a).
    $$

    * 部分集合全体からなる集合が存在することをいっている。
    * テキストによっては $\impliedby$ しか言わないものもあるが、他の公理
      $(S1), (S6)$ から $\implies$ も成り立つ。
    * べき集合は本書では $\mathscr{P}(a)$ のような記号を採用しているが、このノートでは $2^a$ を採用する。
* §1.5 自然数
  * 当分の間、$(S5)$ で取り扱った**無限系譜**に関して「$x$ は無限系譜である」という言明を $M(x)$ で表すことにする。
  * **無限樹**とは、空でない集合 $a$ であって、$\forall x (x \in a \implies M(x))$ が成り立つものとする。
    * 例：$M(x)$ なる $x$ について $\lbrace x \rbrace.$
  * 以下、自然数全体の集合を構成する。

    1. $M(a)$ なる $a$ に対して $\tilde{a} = \lbrace x \in 2^a\,\mid\,M(x)\rbrace$ とおく。
    2. このとき $\tilde a$ は無限樹である。
    3. $\omega_a = \bigcap \tilde{a}$ とおくと、$M(\omega_a)$ が真であり、$\omega_a \in \tilde \omega$ が成り立つ。

    実は、任意の $M(b)$ なる $b$ に対して $\omega_a = \omega_{a\cap b} = \omega_b$ が成り立つ。
    もう添字は要らないので、この集合を単に $\omega$ と書く。これが自然数全体の集合である。

    * コメント：パッと見た感じでは何のことだかわからない。
  * **Peano の公理**：後述の性質 (P1)-(P4) をそう呼ぶ。
    * ある集合 $a$ が Peano の公理を満たせば、それは**算術的性質をもつ**という。
    * 上記 $\omega$ は算術的性質をもつ。
      * コメント：(P4) を示すのが難しい。
    * $\omega$ について (P3) が成り立つことから、数学的帰納法の定理が得られる：

      $n \in \omega$ に関する命題 $P(n)$ について、次が成り立てば $\forall n \in \omega P(n)$ である：

      $$
      \begin{aligned}
      \text{(i)} & \quad P(0),\\
      \text{(ii)} & \quad \forall n (n \in \omega \land P(n) \implies P(n^+)).
      \end{aligned}
      $$

    * Peano の公理をここに記す：
      * (P1) 後継ぎの存在： $x \in a \implies \exists x' \in a.$
      * (P2) 最小限の存在： $\exists \nu \in a (\forall x \in a x' \ne \nu).$
      * (P3) 数学的帰納法の原理： $(b \subset a, \nu \in b, \forall x(x \in b \implies x' \in b)) \implies b = a.$
      * (P4) 一致： $x \in a, y \in b, x' = y' \implies x = y.$

      コメント： (P1) について、$a = \omega$ のときは $x'$ を $x^+$ と書く。
      直感的にはプラス 1 だから。(P2) の $\nu$ はゼロを意味する。(P3) の一番内側の括弧の言明は、
      $b$ は $M(b)$ であるといっている。

    * 補題：$x, y \in \omega$ について $x \in y \iff x \ne y \land x \subset y.$
      * コメント：慣れないうちは、$1 \in 2$ は $\lbrace \varnothing, \lbrace \varnothing \rbrace \rbrace \in \lbrace \varnothing, \lbrace \varnothing, \lbrace \varnothing \rbrace \rbrace \rbrace$ であるとか、
        いろいろ手で書いて試してみるといい。
* §2.1 自然数の大小
  * ここで記号 $\le, \ge, <, >$ を導入する。意味は例えば $\le$ ならば、$m, n \in \omega$ について $m \le n \iff m \subset n$ のこととする。
  * $\min\omega = 0.$ 一方 $\max\omega$ は存在しない。$\because \forall n \in \omega \exists n^+ \in \omega.$
  * コメント：以下、写像を定義するために芋づる式に必要な概念を定義する。
  * **順序対** (ordered pair)
    * コメント：面白いことに非順序対で定義できる：

      $$(x, y) \coloneqq \{\{x\}, \{x, y\}\}.$$

      こうすることで $x \ne y \iff (x, y) \ne (y, x)$ が成り立つようにできる。
  * **直積**：略。
  * **対応（関係）**：集合 $a, b$ に関する順序対 $(a \times b, f)$ のことである。
    ただし、ここで $f$ とは $a \times b$ の部分集合である。
    * このとき $f$ をこの対応の**グラフ**と呼ぶ。
    * $a, b$ を明示する必要のないときは、単に $f$ と書いて、ある対応として扱う。
  * **像**：元に関するものと、集合に関するものがある。
  * **定義域**：集合であり、対応 $f\colon a \longrightarrow b$ に対して確定する集合 $\lbrace x \in a\,\mid\,f(x) \ne \varnothing\rbrace$ である。
    * 記号 $\operatorname{Dom}f$ で表すことがある。
  * **写像**：対応 $f\colon a \longrightarrow b$ であって、$\operatorname{Dom}{f} = a$ かつ
    $\forall x \in a, f(x) \in b$ が $b$ の元の singleton であるものをいう。
    * コメント：複数の元が対応しているものはダメだと言っている。
  * その他、雑多な定義と記号：
    * **対角線集合** $\varDelta_a \coloneqq \lbrace (x, y) \in a \times a\,\mid\, x = y\rbrace.$
    * **恒等写像** $1_a$
    * **標準的射影** $\operatorname{proj}_a$
    * おなじみの全射、単射、全単射、逆対応、制限・拡張、合成などの所概念（省略）。
    * **対等**の概念だけ注意したい。一対一対応がつく集合同士の関係をそう呼ぶ。記号は $\approx$ を使う。
  * **有限集合**とは、ある集合 $a$ であり、ある自然数 $n \in \omega$ と対等なものをいう：
    $a \approx n.$
    * この $n$ を集合 $a$ の個数、位数、基数、濃度などといい、絶対値の記号で表す。
    * 空集合の濃度はゼロとする。
  * **無限集合**も定義できる（集合であって有限集合でないものとする）。
  * 記号 $\operatorname{Map}(a, b)$ でグラフ $f\colon a \longrightarrow b$ 全体の集合を表す。
  * 次のような対等が存在する：

    $$
    a \times b \approx \{f \in \operatorname{Map}(\{0, 1\}, a \cup b)\,\mid\,f(0) \in a \land f(1) \in b\}.
    $$

    * コメント：何を言っているのかわからない。
  * **添数集合**、**添数**、**添数付けられた集合**：略。
  * 添数集合の**直積**：略。
    * コメント：あとで選出公理を議論するときの主役だ。
