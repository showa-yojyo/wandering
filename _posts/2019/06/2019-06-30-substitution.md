---
title: 『岩波基礎講座 基礎数学 集合と位相』学習ノート Part 10
tags: math
---

彌永昌吉・彌永健一著『岩波基礎講座 基礎数学 9 集合と位相 I』より。

----

* §6.1 続き
  * $(S9)$ **置換公理**

    $a$ を集合、$P(x, y)$ を命題とする：

    $$
    \tag*{$(S9)$}
    \forall x(x \in a \implies \forall y \forall z(P(x, y) \land P(x, z) \implies y = z))
    \\
    \implies
    \\
    \exists b \forall u(u \in b \iff \exists x(x \in a \land P(x, u))).
    $$

    砕けた書き方をすると：
    $\forall x \in a P(x, y) \implies y \text{ is unique}$ とする。
    そのとき $\exists b P(x, u) (x \in a),$ 「$b$ は $u$ の全部」という。

    * コメント：より「伝わる」言い換えが欲しい。
  * (Th 6.4) 整列集合に順序同型な順序数が一意的に存在する。
    * 仮定：$(a, \prec)$ を整列集合とする。
    * 結論：次のような順序数 $\alpha$ が一意的に存在する： $a \simeq \alpha.$
    * 証明

      1. 命題 $P(a, \xi)$ を「$x \in a$ かつ $\xi$ は順序数かつ $s(x) \simeq \xi$」とおく。
         (Th 6.1) により、これが存在すれば一意的である。
      2. 命題 $Q(x)$ を 「$x \in a$ かつ $s(x)$ を順序同型な順序数が存在する」とおく。
      3. 次の条件を満たす順序数 $\xi_y$ が 1. により一意的に存在する：

         $$
         \forall y \in s(x)Q(y) \implies s(y) \simeq \xi_y.
         $$

      4. $(S9)$ により、集合 $b = \lbrace\xi_y \,\mid\, y \in s(x)\rbrace$ が存在する。
      5. $\beta \coloneqq \bigcup b$ とおく。これはその定義により順序数である。
      6. したがって $\xi \in b \implies \xi^+ \in \beta.\quad\because\beta \subset \beta.$
      7. ゆえに写像 $f\colon s(x) \longrightarrow \beta^+$ を $y \longmapsto \xi_y$ により定められる。
         $f$ は順序を保つ単射である。
      8. $\alpha_x \coloneqq f(s(x))$ とおく。$\alpha_x \subset \beta^+.\quad\therefore\alpha_x \in \beta^+ \lor \alpha_x = \beta.$
         ゆえに $\alpha_x$ は $s(x)$ と順序同型な順序数である。すなわち $Q(x)$ が真である。
      9. 超限帰納法により $\forall x \in a Q(x).$ すなわち $s(x) \simeq \alpha_x$ となる順序数 $\alpha_x$ が存在し、しかも一意的であることが示された。
      10. $(S9)$ をもう一度用いる：集合 $c = \lbrace\alpha_x \,\mid\, x \in a\rbrace$ が存在する。
      11. $\gamma \coloneqq \bigcup c$ とおき、5. から 9. の推論を繰り返せば、次のような順序数 $\alpha$ が存在するといえる：

          $$
          \alpha \subset \gamma^+ \land \alpha \simeq a.
          $$

  * 記号 $\operatorname{ord}(a, \prec)$ で、整列集合 $(a, \prec)$ に順序同型なただ一つの順序数を表すことにする。
* §6.2 順序数の和・積・べき
  * $1 + 2 = 3$ だが $\lbrace 0 \rbrace + \lbrace 0, 1 \rbrace$ をどう処理するか。
    次に示すように、各オペランドを変形することで順序関係を入れられる：

    $$
    \def\set#1{ \{#1\} }

    \begin{aligned}
    \set{0} + \set{0, 1} &\coloneqq \set{(0, 0), (0, 1), (1, 1)},\\
    (0, 0) &\le (0, 1),\\
    (0, 0) &\le (1, 1),\\
    (0, 1) &\le (1, 1).
    \end{aligned}
    $$

    この二項演算のオペランドを順序集合 (poset) に一般化する。
    $(a, f), (b, g)$ を順序集合とし、二項演算 $\oplus$ を次で定義する：

    $$
    \def\set#1{ \{#1\} }
    a \oplus b \coloneqq a \times \set{0} \cup b \times \set{1}.
    $$

    $(x, m), (y, n) \in a \times b$ に対して二項関係 $\le$ を次で定義する：

    $$
    (x, m) \le (y, n) \iff\\
    \begin{aligned}
    &m < n \\
    &\lor (m = n = 0 \land x \precneqq y)\\
    &\lor (m = n = 1 \land x \precneqq y).
    \end{aligned}
    $$

    このとき $\le$ は順序関係になり、特に $a, b$ が整列集合ならば $(a \oplus b, \le)$ も整列集合である。

    * コメント：例として $(1 \oplus 2, \le) \simeq 3.$

  * 和
    * 順序数 $\alpha, \beta$ の和 $\alpha \oplus \beta$ を次で定義する：

      $$
      \alpha \oplus \beta \coloneqq \operatorname{ord}(\alpha \oplus \beta, \le)
      $$

    * 諸注意
      * $\alpha \oplus 0 = 0 \oplus \alpha.$
      * $\alpha \oplus 1 = \alpha^+.$ しかし $1 \oplus \alpha = \alpha^+$ とは限らない：
        $\alpha = \omega$ のとき写像 $F\colon 1 + \omega \longrightarrow \omega$ を次で定義すると、
        $F$ は $1 + \omega \simeq \omega$ を与える：

        $$
        \begin{aligned}
        F((0, 0)) &= 0,\\
        F((n, 1)) &= n^+ \quad (n \in \omega).
        \end{aligned}
        $$

      * $\forall n, m \in \omega (n \oplus m = n + m).$

  * (Th 6.5) 順序数の「差」の存在？
    * 仮定：$\alpha, \beta, \gamma$ は順序数。
    * 結論：$\alpha \subsetneq \beta \iff \exists\gamma(\gamma \ne 0 \land \beta = \alpha \oplus \gamma).$
    * 証明：
      * ($\impliedby$): 明らかに成り立つ。
      * ($\implies$): 条件を満たす順序数を具体的に構成する。

        1. 集合 $c \coloneqq \beta\setminus\alpha$ とおく。これは $\beta$ の部分集合とみなせる。包含関係について整列集合である。
        2. $\beta = \alpha \cup c \land \alpha \cap c = \varnothing.$ 非交和分解になっている。
        3. $\alpha \in \beta$ が整列集合であるので $\alpha = s(\alpha).$
        4. したがって $\xi \in x \implies \forall \eta \in \alpha (\eta \subsetneq \xi).$
           * コメント：$c$ のほうが「上にある」ということか。
        5. $\gamma \coloneqq \operatorname{ord}(c, \subset)$ とおく。このとき $\beta \simeq \alpha \oplus \gamma$ であることは明らかだ。
           ゆえに $\beta = \alpha \oplus \gamma.$
  * (Cor) 順序数 $\alpha$ が無限集合 $\iff \exists\beta(\alpha = \omega \oplus \beta).$
    * ($\impliedby$): 明らかに成り立つ。
    * ($\implies$):
      1. (Th 6.1) により、$\alpha$ と $\omega$ に対して $\alpha = \omega, \alpha \subsetneq \omega, \omega \subsetneq \alpha$ のうち、いずれかのちょうど一つが成り立つ。
      2. $\alpha = \omega$ であるときは $\beta = 0$ として成り立つ。
      3. $\alpha \subsetneq \omega$ は成り立たない。$\omega$ の元をいくつか取り除いてそれを $\alpha$ とするならば、それは順序数ではなくなる。
      4. $\omega \subsetneq \alpha$ であるときは、(Th 6.5) である。

  * コメント：以上は和の二項演算版の定義だった。以下、対象を添数付けられた順序集合に拡張し、併せて順序数の積を定義する。

    1. 定義
       * 集合 $I$ を添数の集合に使う。
       * 集合族 $\lbrace w_i\rbrace_{i \in I}$ を $I$ を添数とする添字付けられた集合とする。
       * $a_i \coloneqq w_i \times \lbrace i \rbrace$ とおく。これも $I$ を添数とする添字付けられた集合である。
         * コメント：これを導入する理由は、非交和分解のためだ。$i, j \in I, i \ne j \implies a_i \cap a_j = \varnothing.$
       * **非交和 (disjoint sum)** を定義する：

         $$
         \bigoplus_{i \in I}w_i \coloneqq \bigsqcup_{i \in I}a_i.
         $$

    2. 特に $(I, \prec)$ と各 $(w_i, f_i)$ が整列集合ならば、$a_i$ に関係 $\tilde f_i$ を
       $(w_i, f_i) \simeq (a_i, \tilde f_i)$ となるように自然に与えられる。
       先程の要領で $\bigoplus w_i$ に順序関係 $\le$ を導入でき、
       $(\bigoplus w_i, \le)$ が整列集合になる。
    3. **和**。$\operatorname{ord}(\bigoplus \alpha_i, \le)$ を $\lbrace \alpha_i \rbrace_{i \in I}$ の和といい、次で表す：

       $$
       {\sum_{i \in I}}^{\oplus} \alpha_i \coloneqq \operatorname{ord}\left(\bigoplus_{i \in I} \alpha_i, \le\right).
       $$

    4. 性質
       * 順序数の和について結合法則が成り立つ。
       * $\alpha \oplus \beta = \alpha \oplus \gamma \iff \beta = \gamma.$
  * (Q 6.2) $\alpha$ を順序数、$n \in \omega\setminus 0$ とする。
    $\alpha$ が無限集合であることと $n \oplus \alpha = \alpha$ は同値である。
  * **逆辞書式順序関係**
    * $\bigoplus w_i$ において、すべての $(w_i, f_i)$ が共通の整列集合 $(w, f)$ に等しいとき、次のように順序関係を定められる：

      $$
      (x, i) \le (y, j) \iff i \prec j \lor (i = j \land x \prec_f y).
      $$

    * 特に $w$, $I$ を順序数にとると、$(w \times I, \le)$ は整列集合になる。
      これから定まる順序数 $\operatorname{ord}(w \times I, \le)$ を $w \otimes I$ と書く。
    * 性質
      * $\alpha \otimes 0 = 0 \otimes \alpha = 0.$
      * $\alpha \otimes 1 = 1 \otimes \alpha = \alpha.$
      * $\alpha \oplus \alpha = \alpha \otimes 2, \alpha \oplus \alpha \oplus \alpha = \alpha \otimes 3, \dotsc.$
      * $n, m \omega$ のとき $n \otimes m = nm.$
      * 結合法則、**左**分配法則が成り立つ： $\alpha \otimes(\beta \oplus \gamma) = \alpha\otimes\beta \oplus \alpha\oplus\gamma.$
      * 交換法則は成り立たない。
      * **右**分配法則は成り立たない。
    * 指数の記号も定められる。

      $$
      \begin{aligned}
      \alpha^{\otimes 2} &\coloneqq \alpha \otimes \alpha,\\
      \alpha^{\otimes 3} &\coloneqq \alpha^{\otimes 2} \otimes \alpha,\\
      &\dots,\\
      \end{aligned}
      $$

      * $\alpha^{\otimes 0} \coloneqq 1$ とする。
  * **上界**：(Th 6.2) のような（順序数からなる集合 $A$ があり、その任意の $\xi$ を真に含むような）順序数からなる集合を $A$ の上界という。

    $$
    \{\alpha \,|\,\forall \xi \in A (\xi \subsetneq \alpha)\}.
    $$

  * **上限**：次の集合を $A$ の上限と呼ぶ：

    $$
    \sup A \coloneqq \{\beta \in \alpha\,|\,\bigcup A \subset \beta\} \cup \{\alpha\}.
    $$

    この集合は $\alpha$ によらずに $A$ だけから定まる。

  * (Q 6.3)

    $$
    \begin{aligned}
    \alpha \oplus A  &\coloneqq \{\alpha \oplus \xi\,|\,\xi \in A\} \subset \alpha \oplus (\bigcup A)^+,\\
    \alpha \otimes A &\coloneqq \{\alpha \otimes \xi\,|\,\xi \in A\}.
    \end{aligned}
    $$

    とすると、次が成り立つ：

    $$
    \begin{aligned}
    \alpha \oplus \sup A &= \sup(\alpha \oplus A),\\
    \alpha \otimes \sup A &= \sup(\alpha \otimes A).\\
    \end{aligned}
    $$

  * $\alpha^{\otimes \omega} \coloneqq \sup \lbrace\alpha^{\otimes n}\rbrace_{n \in \omega}$ と定義する。$(S9)$ による。
  * 以下 $\omega^{\otimes\omega}$ の議論と**制限直積**の定義。
    * 定義から $\forall n (\omega^{\otimes n} \subset \omega^{\otimes\omega}).$

    1. 添数付き集合 $\lbrace \alpha_n \rbrace _{n \in \omega}$ で、$\alpha_n = \omega$ となるものを考える。
       平たく言えば $\omega$ 個の $\omega$ だ。
    2. $\displaystyle a = \prod_{n \in \omega}\alpha_n$ とおく。集合の直積。
    3. 写像 $\lambda_n\colon\omega^n\longrightarrow a$ を

       $$
       \lambda_n(x_0, \dotsc, x_{n-1}) = (x_0, \dotsc, x_{n-1}, 0, 0, \dotsc)
       $$

       で定める。この単射で $\omega^n$ と $\lambda_n(\omega^n) \subset a$ を同一視する。

    * こうしてしまうと $a$ に順序関係を入れても整列集合にはならない。元があり過ぎる。
    * そこで $\lambda_n(\omega^n) \subset s \subset a$ なる $s$ をさがすことにする：

      $$
      s \coloneqq \{(x_i) \in a\,|\,\exists n \in \omega \forall m \in \omega\!\setminus\!n^+ (x_m = 0)\}.
      $$

      * コメント：ほとんどの座標成分がゼロである元をかき集めたものが上記の集合だ。

    * 制限直積 $s$ の性質
      * $\forall n \in \omega \lambda_n(\omega^n) \in s.$
      * $(s, \le)$ は整列集合である。ただし $\le$ を逆辞書式とする。
        * 確認： $b \subset s, b \ne \varnothing$ をとると、$\min b$ が存在することを示す。
        * コメント：文字列長が $\omega$ の単語しかない辞書の見出しの順序。
      * $(s, \le)$ は順序数でもあり、これが $\omega^{\otimes\omega}$ に等しい。
  * 制限直積を一般化する。$\omega$ を一般の添数集合 $I$ に置き換える。
    * 制限直積とは、整列集合 $(I, \prec) \ne \varnothing$ を添数集合とする、
      添数付けられた順序数 $\alpha_i \ne \varnothing$ の直積 $\displaystyle \prod_{i \in I} \alpha_i$ の部分集合であって、
      有限個の添数を除いて座標成分 $x_i$ が最小元 $\min\alpha_i$ と等しい元全部からなるものをいう。
    * これを記号 $\displaystyle {\prod_{i \in I}}'\alpha_i$ で表す。
      * コメント：$I$ が有限なときにも成り立つような、下位互換的定義になっている。
    * 逆辞書式順序関係 $\le$ を入れると、$({\prod}'\alpha_i, \le)$ は整列集合になる。
  * 積
    * $\prod^\otimes \alpha_i \coloneqq \operatorname{ord}({\prod}'\alpha_i, \le)$ を $\alpha_i$ の積という。
    * 性質
      * $\exists i (\alpha_i = 0) \implies \prod^\otimes \alpha_i = 0.$
      * $I = 0 \implies \prod^\otimes \alpha_i = 1.$
      * $I = 2 \implies \prod^\otimes \alpha_i = \alpha_0 \otimes \alpha_1.$
      * $\alpha$ を順序数、$\beta = \alpha^+$ とし、$\lbrace \gamma_\xi\rbrace_{\xi \in \beta}$ を添数付けられた順序数集合とする。このとき：

        $$
        \prod_{\xi \in \beta}{}^\otimes \gamma_\xi
        = \prod_{\xi \in \alpha}{}^\otimes \gamma_\xi \otimes \gamma_\alpha.
        $$

      * $\alpha$ を極限数とすると：

        $$
        \prod_{\xi \in \alpha}{}^\otimes \gamma_\xi
        = \sup\{\prod_{\xi \in \beta}{}^\otimes \gamma_\xi\,|\,\beta\in\alpha\}.
        $$

  * べき
    * 上述の積において $\gamma_\xi$ がすべて共通の順序数 $\beta$ に等しいとき、
      この積を $\beta$ の $\alpha$ 乗、あるいは $\alpha$ べきだと呼んで、記号 $\beta^{\otimes\alpha}$ で表す。
    * 性質
      * $\beta^{\otimes 0} = 1.$
      * $\alpha \ne 0 \implies 0^{\otimes\alpha} = 0.$
      * $\beta^{\otimes 1} = \beta.$
      * $\alpha$ が孤立順序数で $\alpha = \gamma^+ \implies \beta^{\otimes\gamma} = \beta^{\otimes\gamma}\otimes\beta.$
      * $\alpha$ が極限数 $\implies \beta^{\otimes\alpha} = \sup \lbrace \beta^{\otimes\gamma}\rbrace_{\gamma \in \alpha}.$
      * $\forall n \forall m \in \omega (n^{\otimes m} = n^m).$
  * (Q 6.4) 指数法則
  * 一般に $(\alpha \otimes \beta)^{\otimes\gamma} \ne \alpha^{\otimes\gamma}\otimes \beta^{\otimes\gamma}.$
  * 次のように順序数を名付けておく：

    $$
    \begin{aligned}
    \omega_2 & \coloneqq \omega^{\otimes\omega},\\
    \omega_3 & \coloneqq \omega^{\otimes\omega_2},\\
    \dots\\
    \omega_{n+1} &= \omega^{\otimes\omega_n},\\
    \varepsilon_0 & \coloneqq \sup \{\omega_n\}_{n \in \omega}.
    \end{aligned}
    $$
