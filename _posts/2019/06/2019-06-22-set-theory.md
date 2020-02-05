---
title: 『岩波基礎講座 基礎数学 集合と位相』学習ノート Part 5
tags: math
---

彌永昌吉・彌永健一著『岩波基礎講座 基礎数学 9 集合と位相 I』より。実数論。

----

* §4.1 実数
  * テーマ：実数を定義する。
  * 説明のためにいくつか集合を定義する。
  * $S = \lbrace f\,\mid\, f \in \mathbb Q^\omega\rbrace$: 有理数列全部の集合
    * $(S, +, \cdot)$ は可換環となる。有理数列版の零元と単位元を含む。
    * $\mathbb Q$ を $S$ の部分環とみなせる。$a \in \mathbb Q$ と $(a, a, \dotsc, a, \dotsc) \in S$ を同一視すればよい。
    * $S$ は整域ではない。零元が何であるかと、$S$ における乗算の定義を少し考えれば解る。
  * $B = \lbrace f \in S\,\mid\, \exists a \in \mathbb Q (a \ge 0 \land \forall n \in \omega(\lvert f(n)\rvert \le a))\rbrace \subset S$: 有界な有理数列全部の集合。
    * 数列 $f \in B$ の**絶対上界**とは、集合 $\lbrace a (\in \mathbb Q) \,\mid\, \lvert f(n)\rvert \le a\rbrace$ の元である。
    * $B \subset S$ は部分環である。
      * コメント：加法と乗法について閉じている。
  * (Th 4.1) 任意の有理数に対して、それを押さえる 1 の逆数と整数の存在

    $$
    \forall a \in \mathbb Q(a > 0 \implies
      \exists n \in \N \exists m \in \N (\\
          n \ne 0 \land m \ne 0 \land
              0 < \frac{1}{n} \le a \le m)).
    $$

    証明：仮定より $a = \dfrac{m}{n}\quad (m \ge 1, n \ge 1)$ とおける。
    簡単な式変形で結論の不等式が得られる。

  * (Th 4.2) (Th 4.1) のべき乗版

    $$
    \forall k \in \N \forall a \in \mathbb Q \left(
        k > 1 \implies \left(\exists m \in \N
            \forall n \in \N\left(
                n \ge m \implies
                \left(\frac{1}{k^n} \le a \le k^n\right)\right)\right)\right).
    $$

    コメント：直観的には正しい。まず $k^n > n$ を証明する。それから (Th 4.1) を用いる。

  ここで少し話が飛ぶ。$\displaystyle f(n) \coloneqq \sum_{i = 0}^n\dfrac{1}{k^n} \in S$ を考える。
  実は $f \in B$ であり、さらに実は後にいう Cauchy 列である。

  * **有理 Cauchy 列**とは（略）である。
  * $C \coloneqq \lbrace f \in S\,\mid\, f\text{ is Cauchy}\rbrace$ とおく。
  * $C \subset B$ i.e. Cauchy 列は有界である。
    * 実は部分環となっている。
    * コメント：$g \in S$ がある $f \in B$ によって押さえられるとき、$g \in C.$

  * 集合 $N \subset S$ を「0 に収束する有理数列全部の集合」と定義する。
    * (Q 4.2) だが、$N \subset C$ はイデアルである。
    * 実は $N \subset C$ は極大イデアルである（証明するのに準備がいる）。そうなると剰余環 $C/N$ は体であるということになる。
      これを $\R = C/N$ と表して**実数体**と呼ぼうということだ。
    * $\mathbb Q \subset C/N$ が部分体とみなせることにも注意。
    * 極大イデアルであることを示す手順を記す：

      1. $f \in C/N$ を一つとる。このとき $0 < \exists a \in \mathbb Q \exists m \in \N \forall n \ge m \lvert f(n)\rvert \ge a.$
      2. $g \in S$ を次のように定義すると $g \in C:$

         $$
         g(n) = \begin{cases}
             0, & n < m,\\
             \dfrac{1}{f(n)}, & n \ge m.
         \end{cases}
         $$

         解析入門の証明問題であるかのように示す。
      3. $h = fg$ とおく。$h - 1 \in N.$
      4. $A$ が $C$ のイデアルであり、$N$ を真に含むならば $A \ni 1,$ すなわち $A = C.$

      以上 1.-4. より、$N$ は $C$ の極大イデアルである。
  * **極限**とは、$f \in C$ に対して $f$ を代表元とする $\R$ の元であるとする。
    * コメント：Cauchy 列で実数を定義したので、例えば $(\lim f)(\lim g) = \lim(fg)$ などの性質を証明するのが容易い。
  * (Th 4.3) 実数を押さえる有理数の存在性

    $$
    \forall \alpha \in \R (\alpha > 0 \implies \exists a \in \mathbb{Q} \exists b \in \mathbb{Q} (
       0 < a \le \alpha \le b
    )).
    $$

    証明：Cauchy 列を基にして淡々と示す。
  * 以上、実数体が構成でき、その基本的な性質が明らかになった。

* §4.2 有理数と実数
  * テーマ：$\R$ が $\mathbb{Q}$ を真に含むことを見ていく。
    * コメント：補集合の元を無理数と呼んでいる。
    * コメント：$\sqrt{2} \notin \mathbb{Q}$ と $\sqrt{2} \in \R$ を両方とも示すようだ。
  * (Th 4.5) 上限の存在
    * 結論：$\R$ の空でない部分集合 $S$ が上に有界であるとき、上限 $\sup S$ が存在する（意訳）。
    * 証明：$f \in S \cap C$ をとる。その極限が $S$ の上界であることを示す。
      その値は $S$ の任意の上界よりも大きくない必要があることを示す：

      1. $\alpha \in S$ を何かとり、$\beta \in \R$ を $S$ の上界とする。
         このとき $\exists a \in \mathbb Q \exists b \in \mathbb Q (a \le \alpha \land \beta \le b).$
      2. 次の有理数列 $f$ を考える。帰納定理によれば、このような数列は一意的に定まる。

         $$
         f(n) = \begin{cases}
             a, & n = 0,\\
             f(n - 1) - \dfrac{b - a}{2^{n-1}}, & f(n - 1) \text{ is an upper bound of S,}\\
             f(n - 1) + \dfrac{b - a}{2^{n-1}}, & f(n - 1) \text{ is not an upper bound of S,}\\
         \end{cases}
         $$

      3. $f$ が Cauchy であることを示す（解析入門の要領で）。
      4. $s \coloneqq \lim f(n)$ は $S$ の上界であることを示す。背理法による。
      5. $s$ の決め方から、これは上界の最小限である。

  * 実数値**連続関数**を定義する（略：解析入門参照）。
    * 連続関数同士の和や積もまた連続である。
    * コメント：だから多項式の形の関数は連続である。

  * (Th 4.6) 中間値の定理（略：解析入門参照）
    * コメント：どの教科書も同じ証明になると思う。
* §4.3 収束列と Cauchy 列
  * テーマ：さきほど $\mathbb{Q}$ から $\R$ を構成した。同様の手口を $\R$ に適用すると、何か新しい集合が得られるか？
  * 答えは否。実 Cauchy 列全部の集合をゼロ数列全部の集合からなる剰余環は $\R$ 自身になる。
  * (Th 4.7) 実数列 $f$ が収束することと $f$ が実 Cauchy であることは同値である。
    * 証明：解析入門で習ったとおり、$\impliedby$ の証明が本質的系だ。
      * 以下、$S$, $C$, $B$, $N$ の「実数版」をチルダをつけて表すことにする。
      * $f \in \tilde{C}$, $n \in \omega$ に対して $f(\omega\setminus n)$ が上下に有界である。
      * $\sup{f(\omega\setminus n)}, \inf{f(\omega\setminus n)}$ を考える。両者が一致することを示したい。
      * 一方 $f - g \in \tilde N$ を示す。これにより $f - \alpha = (f - g) + (g - \alpha) \in \tilde N.$
        ゆえに $\lim f = \alpha.$

  * 関数が C 型であるとは、関数による Cauchy 列の像がまた Cauchy であるものをいうことにする。
    * コメント：$C^0$ 級関数は C 型である。
  * ここでその反対の状況を考える。C 型関数は連続であるか？
    言葉を替えると関数 $F\colon\R \longrightarrow \R$ は一点 $a \in R$ で不連続であるというだけで
    C 型たり得ないか？

    例として $F$ を原点で不連続な関数とする。$\forall \varepsilon > 0$ に対して、
    次の集合 $S_n$ はいずれも空集合でない：

    $$
    S_n = \{ x \in \R \,|\, \lvert x\rvert < \frac{1}{2^n} \land \lvert F(x) - F(0)\rvert > \varepsilon \}
    $$

    実数列 $f$ を $\exists s_n \in S_n (f(n) = s_n)$ のように定義できるか？
    この例では不可能なのだ：

    $\lvert s_n \rvert < \dfrac{1}{2^n}$ より $f$ は収束し、$F(0) = \lim(F \circ f)$ ではある。
    一方、$S_n$ の定義から $\forall n \in \N \lvert F\circ f(n) - F(0)\rvert > \varepsilon.$

    一般的な状況では $s_n$ がとれるかどうかが明らかではない。
    そこで次の節に続く。
