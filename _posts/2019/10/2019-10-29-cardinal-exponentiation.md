---
title: 基数のべき乗 復習ノート
tags: math
---

基数のべき乗の定義や性質を復習する。本稿では集合 $X$ の基数を $\lvert X \rvert$ で表す。

# 定義

$A, B$ を集合とし、$\mathfrak{a} = \lvert A \rvert$,
$\mathfrak{b} = \lvert B \rvert$ とする。
このとき $\mathfrak{a}$ と $\mathfrak{b}$ の**べき乗**を次により定義する：

$$
\mathfrak{a^b} \coloneqq \lvert A^B\rvert.
$$

ここで集合 $A^B$ は $B$ から $A$ への写像すべてを要素とする。

# 性質

基数のべきのもつ性質をいくつか見ていく。

## ゼロ乗は常に 1 に等しい

**命題**：任意の基数 $\mathfrak a$ に対して

$$
\mathfrak a^0 = 0.
$$

**証明**：$\mathfrak a = \lvert A \rvert$ を満たす集合 $A$ を一つとる。
また $0 = \lvert \varnothing\rvert.$
「空集合から任意の集合への写像は一意的に存在する」ルールにより、

$$
\lvert A^\varnothing\rvert = 1.
\quad\blacksquare
$$

## べき乗の恒等元は 1 である

**命題**：任意の基数 $\mathfrak a$ に対して

$$
\mathfrak{a}^1 = \mathfrak{a}.
$$

**証明**：$\mathfrak a = \lvert A \rvert$ を満たす集合 $A$ を一つとる。
また $1 = \lvert \lbrace \varnothing \rbrace\rvert.$
写像 $f\colon \lvert \lbrace \varnothing \rbrace\rvert \longrightarrow A$
すべてからなる集合は、定義域の要素が一意的であるため $A$ と対等である：
写像 $f_a: \lbrace\varnothing\rbrace \longrightarrow A$ を $f_a\colon \varnothing \longmapsto a$ で定義する。
このとき集合 $A$ とこのような写像すべての集合 $F \coloneqq \lbrace f_a \,\mid\, a \in A\rbrace$
との間に全単射写像 $a \longmapsto f_a$ が存在するので、

$$
\mathfrak{a}^1 = \lvert A^{\lbrace \varnothing \rbrace} \rvert
= \lvert F \rvert = \lvert A \rvert = \mathfrak{a}.
\quad\blacksquare
$$

## 指数の和に対する分配律

**命題**：任意の基数 $\mathfrak{a, b, c}$ に対して：

$$
\mathfrak{a^{b+c} = a^b a^c}.
$$

**証明**：集合 $A, B, C$ を次のすべてが成り立つようにとる：

$$
\begin{aligned}
    \mathfrak{a} = \lvert A \rvert,\\
    \mathfrak{b} = \lvert B \rvert,\\
    \mathfrak{c} = \lvert C \rvert,\\
    B \cap C &= \varnothing.
\end{aligned}
$$

このとき和集合 $B \cup C$ が非交和 $B \sqcup C$ に等しいことに注意する。
示すべきは

* $B \cup C = B \sqcup C$ から $A$ への写像すべての集合の基数と
* $B$ から $A$ への写像すべての集合の基数と
  $C$ から $A$ への写像すべての集合の基数との積

との和が等しいことだ。TBW

## 指数の積に対する分配律

**命題**：任意の基数 $\mathfrak{a, b, c}$ に対して：

$$
\mathfrak{(ab)^c = a^c b^c}.
$$

**証明**：集合 $A, B, C$ を次のすべてが成り立つようにとる：

$$
\begin{aligned}
    \mathfrak{a} = \lvert A \rvert,\\
    \mathfrak{b} = \lvert B \rvert,\\
    \mathfrak{c} = \lvert C \rvert.\\
\end{aligned}
$$

集合の対等性 $(A \times B)^C \approx A^C \times B^C$ を示せばよい。TBW

## 指数の積は逐次べき乗に等しい

**命題**：任意の基数 $\mathfrak{a, b, c}$ に対して：

$$
\mathfrak{a^{bc} = (a^b)^c}
$$

**証明**：集合 $A, B, C$ を次のすべてが成り立つようにとる：

$$
\begin{aligned}
    \mathfrak{a} = \lvert A \rvert,\\
    \mathfrak{b} = \lvert B \rvert,\\
    \mathfrak{c} = \lvert C \rvert.\\
\end{aligned}
$$

すると結論は $A^{B \times C} \approx (A^B)^C$ と同値になる。こちらを証明する。

写像の集合 $(A^B)^C$ から写像の集合 $A^{B \times C}$ への写像 $F$ を次で定義する：

$$
F(f)(b, c) = (f(b))(c), \quad b \in B, c \in C.
$$

すると $F$ は全単射となり、その結果主張が真であることを証明する。

* コメント：ここがわかりにくい。

$F(f_1) = F(f_2)$ を仮定する。すると $F$ の定義により

$$
\begin{aligned}
\forall b \forall c(b \in B, c \in C &\implies (f_1(b))(c) = (f_2(b))(c)).\\
&\therefore f_1(b) = f_2(b).\\
&\therefore f_1 = f_2.
\end{aligned}
$$

ゆえに $F$ は単射であることが示された。

次に $F$ が全射であることを示す。任意の写像 $g \in A^{B \times C}$ をとる。
そして写像 $f$ を $(f(b))(c) = g(b, c)$ により定義する。

写像 $F$ および $f$ の性質から

$$
F(f)(b, c) = (f(b))(c) = g(b, c).
$$

したがって $F$ は全射である。

以上より $F$ が全単射であることが示されたので、
$A^{B \times C} \approx (A^B)^C.$ ゆえに主張は真である。
$\blacksquare$

# 参考資料

* [Category:Cardinals](https://proofwiki.org/wiki/Category:Cardinals) - ProofWiki
