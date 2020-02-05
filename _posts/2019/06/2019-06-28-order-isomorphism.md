---
title: 『岩波基礎講座 基礎数学 集合と位相』学習ノート Part 9
tags: math
---

彌永昌吉・彌永健一著『岩波基礎講座 基礎数学 9 集合と位相 I』より。

----

* §5.4 順序同型写像
  * (Th 5.6) 整列集合の自身への順序同型写像の特徴
    * 仮定
      1. $(a, \prec)$ を整列集合とする。
      2. $F\colon a \longrightarrow a$ を順序同型写像とする。
    * 結論 $\forall x(x \in a \implies x \prec F(x)).$
    * 証明
      * $s = \lbrace x \in a \,\mid\, F(x) \precneqq x \rbrace$ とおく。
        以下、$s \ne \varnothing$ を仮定して矛盾を導く。
      * $\alpha = \min s$ とおく。
        * コメント：整列集合の空でない部分集合は最小元を持つ。
      * $\alpha \in s$ なので $F(\alpha) \precneqq \alpha.$ ゆえに $F(\alpha) \notin s.$
        * コメント：$s$ の最小元よりも真に前にあるので $s$ の元ではない。
      * 一方 $F$ の性質より $F\circ F(\alpha) \precneqq F(\alpha).$ ゆえに $F(\alpha) \in s.$
        * コメント：一つ前の推論の「不等式」の両辺に $F$ を施している。
      * 矛盾が生じた。これは $s = \varnothing$ が必要であることを示している。
  * (Cor 5.6.1) 整列集合の順序同型群は位数が 1 である。
    * 仮定 $(a, \prec)$ を整列集合とする。
    * 結論 $\operatorname{Aut}(a, \prec) = \lbrace 1_a\rbrace.$
    * 証明
      * $F \in \operatorname{Aut}(a, \prec)$ をとる。前定理 (Th 5.6) より $\forall x \in a (x \prec F(x)).$
      * $F^{-1} \in \operatorname{Aut}(a, \prec)$ に対して：
        * $F^{-1}(x) \prec F^{-1} \circ F(x) = x.$
        * 再び前定理より $x \prec F^{-1}(x).$
        * したがって $\forall x \in a(x = F^{-1}(x)).$
      * 以上により $F = F^{-1} = 1_a.$
  * (Cor 5.6.2) 二つの整列集合間に全単射順序同型写像が存在すれば、それは一意的に定まる。
    * 仮定
      1. $(a, f)$, $(b, g)$ を整列集合とする。
      2. $F\colon a \longrightarrow b$, $G\colon a \longrightarrow b$ を全単射順序同型写像とする。
    * 結論 $F = G.$
    * 証明 $G \circ F^{-1} \in \operatorname{Aut}(a, f)$ に (Cor  5.6.1) を適用すると
      $G \circ F^{-1} = 1_a.\quad\therefore F = G.$
  * (Cor 5.6.3) 切片とは順序同型にできない。
    * 仮定
      1. $(a, \prec)$ を整列集合とする。
      2. $x \in a$
    * 結論 $(a, \prec)$ と $(s(x), \prec)$ とは順序同型ではない。
    * 証明
      全単射な順序同型写像 $F\colon a \longrightarrow s(x)$ の存在を仮定する。
      このとき $F(x) \in s(x).$ 切片の性質から $F(x) \precneqq x$ であるのだが、この順序関係は (Th 5.6) に矛盾する。
      ゆえにこのような $F$ は存在しない。
  * (Th 5.7) 比較可能定理
    * 仮定 $(a, f)$, $(b, g)$ を整列集合とする。
    * 結論：次のうち、一つの場合しか起こらない：
      1. $(a, f) \simeq (b, g).$
      2. $\exists y(y \in b \land (a, f) \simeq (s(y), g)).$
      3. $\exists x(x \in a \land (s(x), f) \simeq (b, g)).$
    * 証明
      1. $a_0 = \lbrace x \in a \,\mid\, \exists y(y \in b \land (s(x), f) \simeq (s(y), g))\rbrace$ とおく。
      2. $\min a \in a_0.$
         * コメント： $s(\min a) = \varnothing$ だから $s(\min b) = \varnothing$ と順序同型であるとみなせる。
      3. $x \in a_0 \implies s(x) \subset a_0.$
      4. ゆえに $a\setminus a_0 \ne \varnothing \implies a_0 = s(\min a\setminus a_0).$
      5. また、$x \in a_0$ のとき $s(x) \simeq s(y)$ なる $y \in b$ は (Cor 5.6.3) により一意的に定まる。
         これを $F\colon a_0 \ni x \longrightarrow y \in b$ と定めると、順序同型写像である。
      6. 同様の推論により $b\setminus F(a_0) \ne \varnothing \implies F(a_0) = s(\min b\setminus F(a_0)).$
      7. したがって次が成り立つ：
         * $a_0 \simeq F(a_0),$
         * $a_0 = a \lor a_0 = s(a),$
         * $F(a_0) = b \lor F(a_0) = s(\min b\setminus F(a_0)).$
      8. $a_0 \subsetneq a \implies F(a_0) = b$ を示す：

         $a_0 = s(\min a\setminus a_0) \land F(a_0) = s(\min b\setminus F(a_0)) \implies s(\min a\setminus a_0) \simeq s(\min b\setminus F(a_0)).$
         $\min a\setminus a_0 \in a_0$ で矛盾。
  * 帰納定理は $\omega$ の代わりに整列集合でも成り立つか？
    * $F(n)$ が $F(n - 1)$ から定まる

    ということに相当するのは

    * $F(x)$ が $F(s(x))$ または $F\vert_{s(x)}$ から定まる

    ということだ。
    * 要点は、$x$ の直前の元は存在せずとも切片 $s(x)$ ならば存在するということにある。

  * **$A$ に含まれる $x$ 型の点列**とは、写像 $f\colon s(x) \longrightarrow A$ であって、
    $x$ は整列集合 $(a, \prec)$ の元であり、集合 $A$ は空集合でないものとする。

    $$
    \varSigma(a, A) \coloneqq \{f \in 2^{a \times A}\,|\,
      \exists x(x \in a \land f \in \operatorname{Map}(s(x), A)\}.
    $$

    * コメント：グラフを念頭に置いている。
  * (Th 5.8) **超限帰納定理**
    * 仮定
      1. $(a, \prec)$ を整列集合とする。
      2. 集合 $A$ は空集合でないとする。
      3. 写像 $\varphi\colon\varSigma(a, A) \longrightarrow A$ があるとする。
    * 結論
      * $\exists F(F \in \operatorname{Map}(a, A) \land \forall x \in a(F(x) = \varphi(F\vert_{s(x)})).$
      * $F$ は一意的に定まる。
    * 証明
      * まず $F$ の存在を示す。
        1. 次のように $\mathscr{F}$ を定義する：

           $$
           \mathscr F = \{\tilde F \in 2^{a\times A}\,|\,
             \forall x \forall f(\\
               x \in a\\
               \land f \in F(x) \in \operatorname{Map}(s(x), A)\\
               \land f \subset \tilde F \implies (x, \varphi(f)) \in \tilde F)\}.
           $$

        2. $F = \bigcap \mathscr F$ が求めるものであることを示す。
           それにはまず $F$ が $a \longrightarrow A$ の写像であることを示す。
           その結果 $F\vert_{s(x)}$ は $A$ に含まれる $x$ 型の点列だから、$F$ が定理の条件を満たすことがわかる。
        3. $c = \lbrace x \in a\,\mid\,F(x) \ne \lbrace A \rbrace\rbrace$ とおく。$c = \varnothing$ を示す。
        4. $c \ne \varnothing$ だと仮定すると、$\exists y = \min c.$
        5. $F$ は $A$ に含まれる $x$ 型の点列だから $(y, \varphi(F\vert_{s(y)})) \in F.$
        6. 一方 $y \in c$ より $\exists X \in F(y)(X \ne \varphi(F\vert_{s(y)})).$
        7. $F' = F\setminus\lbrace(y, X)\rbrace$ とすると $F' \in \mathscr F.$
        8. ところが $F' \subsetneq F$ なので $F = \bigcap \mathscr F$ に矛盾する。
      * 次に $F$ は一意的に定まることを示す。
        1. $F$ の他に $G\colon a \longrightarrow A$ も存在して定理の条件を満たすと仮定する。
        2. $x \in a$ に関する命題 $P(x)$ を $F(x) = G(x)$ で定める。
        3. $\forall y \in s(x) P(y) \implies F\vert_{s(x)} = G\vert_{s(x)}$ なので、

           $$
           F(x) = \varphi(F\vert_{s(x)}) = \varphi(G\vert_{s(x)}) = G(x).
           $$

           すなわち $P(x)$ は真である。
        4. 超限帰納法により $F = G.$
* §6.1 順序数
  * コメント：自然数といったらこれを思い出すこと：

    $$
    \def\set#1{\{#1\}}
    \def\zero{\varnothing}
    \def\one{\set{\zero} }
    \def\two{\set{\zero, \one} }
    \begin{alignedat}{}
        0 &= \varnothing,\\
        1 &= \set{0} &=& \one,\\
        2 &= \set{0, 1} &=& \two,\\
        3 &= \set{0, 1, 2} &=& \set{\varnothing, \one, \two},\\
        &\dots &\dots
    \end{alignedat}
    $$

    $2 \in 3$ だの $2 \subset 3$ だのという表現があるのはこのため。
  * $\omega^+ \coloneqq \omega \cup \lbrace \omega \rbrace$ と定義する。
  * 自然数、自然数全体の集合 $\omega$, $\omega^+$ などは包含関係によって整列集合をなす。
    このうちの何かを $x$ とすると、$s(x) = x$ という性質がある。
    * コメント：e.g. $s(3) = \lbrace 0, 1, 2\rbrace = 3.$
  * **順序数 (ordinal number)** とは、整列集合であって、その任意の元 $x$ について
    $s(x) = x$ が成り立つものであるとする。
    * $\prec$ は $\subset$ にほかならない。
    * $x, y \in (a, \prec)$ とすると：

      $$
      \begin{aligned}
      x \precneqq y &\iff x \in s(y) \iff x \in y,\\
      x \precneqq y &\iff s(x) \subsetneq s(y).\\
      \therefore x \precneqq y &\iff s(x) \subsetneq s(y) \iff x \in y.
      \end{aligned}
      $$

    * 順序数の切片もまた順序数である。
  * **超限順序数**とは、無限の順序数をいう。
    * コメント：無限集合である整列集合が順序数の性質を満たしているもの。
  * **predecessor** とは、$\alpha, \beta$ を順序数とし、$\alpha = \beta^+$ であるとする。
    このとき $\beta$ は $\alpha$ の predecessor であるという。
    * コメント：TODO: 和名を確認する。
  * **孤立順序数**とは、一意的な predecessor をもつ順序数をいう？
  * **極限数**とは、predecessor をもたない順序数をいう。
    * コメント：順序数はそもそも整列集合に付随する概念だから、順序数は
      孤立順序数か極限数のどちらか一方に分類されるはずだ。

  * (Th 6.1) 順序同型の二つの順序数は同じ集合である。
    * 仮定
      1. $\alpha, \beta$ を順序数とする。
      2. $\alpha \simeq \beta.$
    * 結論 $\alpha = \beta.$
    * 証明：超限帰納法による。

      1. $f\colon a \longrightarrow b$ を順序同型写像とする。
      2. $x \in a$ についての命題 $P(x)$ を $f(x) = x$ で定める。
      3. 仮に $(y \in s(x)P(y)) \land f(x) = z$ ならば $s(z) = f(s(x)) = s(x).$
      4. 一方 $s(x) = x \land s(z) = z$ より $f(x) = x.$ $P(x)$ は真である。
      5. 超限帰納法により $f = 1_a.$

    TODO: この証明を手直ししたい。

  * (Cor 6.1) $\alpha, \beta$ を順序数とすると、次のうち一つの場合しか起こらない (cf. (Th 5.7))：
    1. $\alpha \subsetneq \beta,$
    2. $\alpha = \beta,$
    3. $\beta \subsetneq \alpha.$
  * (Th 6.2)
    * 仮定 $A$ を順序数の集合とする。
    * 結論 順序数 $\alpha$ が存在して次が成り立つ

      $$
      \forall \xi \in A (\xi \subsetneq \alpha).
      $$

    * 証明 $\alpha = \bigcup A \cup \lbrace\bigcup A\rbrace.$
  * (Cor 6.2) 順序数全体からなる集合は存在しない。
  * (Th 6.3) 順序数からなる集合 $A$ には包含関係による順序を入れることができる。
    * 証明
      1. $S \subset A \quad(S \ne \varnothing)$ をとる。
      2. $\alpha \in S$ をとる。
      3. $s = \lbrace \beta \in S \,\mid\, \beta \subsetneq \alpha\rbrace$ とする。これは $\alpha \cap S$ に等しい：

         $$
         s = \{\beta \in S\,|\,\beta \in \alpha\} = \alpha \cap S.
         $$

      4. ゆえに整列集合 $(\alpha, \subset)$ に $s$ の最小元が存在する： $\alpha \ni \gamma = \min s$
      5. $A$ と $S$ が全順序集合であるので $\gamma = \min S.$
