---
title: 『岩波基礎講座 基礎数学 集合と位相』学習ノート Part 3
mathjax: true
tags: math
---

彌永昌吉・彌永健一著『岩波基礎講座 基礎数学 9 集合と位相 I』より。

自然数の話題が続くようだ。

----

* **特性関数**：関数であって、引数が $a$ の元ならば 1 を、そうでなければ 0 をとるものをいう。
  教科書の表現とは異なるが、次の式で覚えることにする：

  $$
  \chi_a(a) = \begin{cases}
  0, & x \notin a,\\
  1, & x \in a.
  \end{cases}
  $$

  * 写像 $\alpha \in 2^a \longmapsto \chi_\alpha \in \operatorname{Map}(a, \lbrace 0, 1\rbrace)$ は全単射。
* **変換**とは、$\operatorname{Map}(a, a)$ の元のことをいう。
  * コメント：定義域と値域が同じ写像を言い換えた。
* §2.3 自然数の和、積
  * (Th 2.5) 帰納定理
    * コメント：ある写像の一意的存在定理だ。
    * 仮定：
      * $A \ne \varnothing$
      * $a \in A$
      * $f\colon A \longrightarrow A$ を変換とする。
    * 結論：次を満たす写像 $F\colon\omega \longrightarrow A$ が存在する：

      $$
      \begin{aligned}
      \text{(i)} & \quad F(0) = a,\\
      \text{(ii)} & \quad \forall n \in \omega F(n^+) = f(F(n)).
      \end{aligned}
      $$

    * 証明：概要だけ言う。
      1. 結論の条件を満たす対応 $F$ が存在することをまず示す。
      2. その $F$ が実は写像であることを示す。

      まず 1. だが、次の集合 $S$ を考える：

      $$
      S = \{x \in \omega \times A\,\mid\,
        (x \ni (0, a) \land x \ni (n, \alpha))
        \implies x \ni (n^+, f(\alpha))\}.
      $$

      $\omega \times A \in S \ne \varnothing$ より集合族 $F \coloneqq \bigcap S$ が確定する。
      $F \in 2^{\omega \times A}$ ゆえに $F$ はグラフ $((\omega, A), F)$ である。
      このことから、 $F \ni (0, a) \land F \ni (n, \alpha) \implies F \ni (n^+, f(\alpha)).$

      次に 2. だが、次に注目する： $x_0 \in 2^{\omega \times A}$ で、

      $$
      x_0 \ni (n, \alpha) \iff (n, \alpha) = (0, \alpha) \lor (n, \alpha) \in (\omega\!\setminus\!\{0\}) \times A
      $$

      を満たすものは $x_0 \subset S$ となる。
      これで $F \subset x_0$ がいえて、さらに $F(0) = a$ となる。残りは：

      $$
      n \in \omega, F(n) = \alpha \implies F(n^+) = f(\alpha)
      $$

      を示すことだ。これを言えれば Th 1.8 より $F$ は写像であることが示せる。

      証明は背理法による（TODO: 消化していないので後回し）。
  * この (Th 2.5) より和、積、べきが写像として確定する。常識的な演算規則が成り立つことが証明できるようになる。
    いったん省略。
    * 和：$f\colon n \longmapsto n^+$ を用いて、写像 $\alpha_a$ を次のようにとる：

      $$
      \alpha_a(x) = \begin{cases}
          a, & x = 0,\\
          \alpha_a(n)^+, & x = n^+.
      \end{cases}
      $$

      そして $\alpha_a(n)$ を $a + n$ と表す。
      * コメント：例えば $\alpha_a(1) = \alpha_a(0)^+ = a^+$ すなわち $a + 1.$

    * 積：和を用いて次のように写像 $\mu_a\colon\omega \longrightarrow \omega$ を定義する：

      $$
      \mu_a(x) = \begin{cases}
          0, & x = 0,\\
          \alpha_a(\mu_a(n)), & x = n^+.
      \end{cases}
      $$

      記法として $\mu_a(n)$ を $an$ だとか $a \cdot n$ などと表す。

    * べき：積を用いる：

      $$
      \pi_a(x) = \begin{cases}
          1, & x = 0,\\
          \mu_a(\pi_a(n)),& x = n^+.
      \end{cases}
      $$
  * (Th 2.6) $a, b \in \omega$ について $a \ge b \iff \exists c (c \in \omega, a = b + c).$
    * コメント：小学生でも知っている事実ではある。
  * 約数、倍数、素数
    * 省略。
  * 加法、乗法
    * 例えば $(a, b) \in \omega^2$ に和を対応させる写像が定まることが示されたが、このときこの写像を $\omega$ の加法と言って、$+$ の記号で表す：$a + b.$
* §2.4 代数系、半群、群
  * **代数系** $(A, O)$ とは、平たくいえば集合と演算の組をパッケージにしてとらえたものだ。
    * この集合 $A$ を代数系の**台集合**と呼ぶ。空集合ではないものとする。
    * **算法（族）** $O$ は $\operatorname{Map}(A \times A, A)$ の部分集合である。
  * 代数系の算法が一種しかない ($O = \lbrace \alpha \rbrace$) とき、これを $(A, \alpha)$ と略記するものとし、$\alpha$ 系と呼ぶ。
  * 交換法則、可換、可換系、結合法則、結合的、半群などの諸概念を一気に定義する。
  * 積の順序に関する議論（略）
  * 準同型写像、同型写像、同型の諸概念の定義。
    * コメント：二つの群にではなく、**同類**である二つの代数系に関する概念らしい。
      同類というのは $(A, O)$ に対する $(A, O')$ のような関係だ。これを $O \approx O'$ と表す。
  * ～について閉じている、包含写像、**部分代数系**の定義（略）。
  * 単位元、単位的、正則（元）、逆元の諸概念の定義（略）。
  * 群、対称群、部分群、置換群、変換半群、$n$ 次対称群 $\mathfrak{S}_n$ の諸概念の定義。
    * コメント：群は単位的半群として定義。
  * 作用、～からの作用の定義（略）。
    * コメント：作用は写像に対する概念であり、左作用・右作用は半群に対する概念。
  * **$A$-空間**：順序対 $(A, B)$ であって、$A$ が $e$ を単位元とする群であり、
    $B$ に左から作用して、つねに次が成り立つものいう：

    $$
    \forall x (x \in B \implies e(x) = x).
    $$

  * コメント：この章でやったことは、数学的帰納法の原理をベースにして、自然数全体の集合、自然数同士の大小関係、算術を定義する作業だ。
    たまに $1 + 1 = 2$ がわからないで悩む子供がいるという話を聞くが、それは当然だった。
