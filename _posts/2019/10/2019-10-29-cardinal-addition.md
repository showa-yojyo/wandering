---
title: 基数の和 復習ノート
tags: math
---

基数の和の定義や性質を復習する。本稿では集合 $X$ の基数を $\lvert X \rvert$ で表す。

# 定義

$A, B$ を集合とし、$\mathfrak{a} = \lvert A \rvert$,
$\mathfrak{b} = \lvert B \rvert$ とする。
このとき $\mathfrak{a}$ と $\mathfrak{b}$ の**和**を次により定義する：

$$
\mathfrak{a} + \mathfrak{b} \coloneqq \lvert A \sqcup B \rvert.
$$

* コメント：$A$ と $B$ は交わりがないことを前提としている。
  あるいは交わりが合っても、例えばムリヤリ $A \times \lbrace 0 \rbrace$ と
  $B \times \lbrace 1 \rbrace$ の非交和の基数として扱うことをこの定義は要請している。

# 性質

基数の和のもつ性質をいくつか見ていく。

## 基数の加法に関する恒等元

$0$ とは空集合の基数を意味する：

$$
0 \coloneqq \lvert \varnothing \rvert.
$$

**命題**：$0$ は基数の加法に関する恒等元として振る舞う。すなわち任意の基数 $\mathfrak{a}$ に対して：

$$
\def\a{ \mathfrak{a} }
\a + 0 = 0 + \a = \a.
$$

**証明**：集合 $A$ を $\mathfrak{a} = \lvert A \rvert$ であるようにとる。このとき空集合の定義から
* $A \cup \varnothing = A$
* $A \cap \varnothing = \varnothing$
であるので、二つの集合 $A, \varnothing$ は disjoint である。したがって

$$
\def\a{ \mathfrak{a} }
\begin{aligned}
    \a + 0 &= \lvert A \sqcup \varnothing \rvert\\
    &= \lvert A \rvert + \lvert \varnothing \rvert\\
    &= \lvert A \rvert + 0\\
    &= \a.
\end{aligned}
$$

$0 + \mathfrak{a}$ についても同様（先に可換律を証明するのがいいかもしれない）。
$\blacksquare$

## 結合律

**命題**：$\mathfrak{a}, \mathfrak{b}, \mathfrak{c}$ を基数とする。このとき：

$$
(\mathfrak{a} + \mathfrak{b}) + \mathfrak{c}
= \mathfrak{a} + (\mathfrak{b} + \mathfrak{c})
$$

**証明**：集合 $A, B, C$ を次のすべてを満たすようにとる：

$$
\begin{aligned}
    \mathfrak{a} &= \lvert A \rvert,\\
    \mathfrak{b} &= \lvert B \rvert,\\
    \mathfrak{c} &= \lvert C \rvert,\\
    A \cap B &= B \cap C = C \cap A = \varnothing.
\end{aligned}
$$

するとこれらの集合のうち相異なる二つをとったときの和は非交和になる。
例えば $A \cup B = A \sqcup B$ が成り立つ。ゆえに

$$
\begin{aligned}
    \mathfrak{a} + \mathfrak{b} &= \lvert A \sqcup B\rvert = \lvert A \cup B\rvert.\\
    \mathfrak{b} + \mathfrak{c} &= \lvert B \sqcup C \rvert = \lvert B \cup C\rvert.
\end{aligned}
$$

そして二つの和集合と残りの集合との交わりは空集合になる。例えば：

$$
\begin{aligned}
(A \cup B) \cap C &= (A \cap B) \cup (B \cap C) = \varnothing \cup \varnothing = \varnothing.\\
\therefore \lvert (A \cup B) \cup C \rvert
&= \lvert (A \cup B) \sqcup C \rvert\\
&= \lvert A \cup B \rvert + \lvert C \rvert\\
&= (\mathfrak{a} + \mathfrak{b}) + \mathfrak{c}.
\end{aligned}
$$

同様にして

$$
\lvert A \cup (B \cup C)\rvert = \mathfrak{a} + (\mathfrak{b} + \mathfrak{c}).
$$

集合同士の和をとる演算が結合律を満たす
$(A \cup B) \cup C = A \cup (B \cup C)$
ことから、両者は等しい。
$\blacksquare$

## 可換律

**命題**：$\mathfrak{a}, \mathfrak{b}$ を基数とする。次が成り立つ：

$$
\mathfrak{a} + \mathfrak{b} = \mathfrak{b} + \mathfrak{a}.
$$

**証明**：集合 $A, B$ を次のすべてを満たすようにとる：

$$
\begin{aligned}
    \mathfrak{a} &= \lvert A \rvert,\\
    \mathfrak{b} &= \lvert B \rvert,\\
    A \cap B & = \varnothing.
\end{aligned}
$$

このとき集合の和をとる演算が可換律を満たすので：

$$
\mathfrak{a} + \mathfrak{b}
= \lvert A \cup B \rvert
= \lvert B \cup A \rvert = \mathfrak{b} + \mathfrak{a}.
$$

$\blacksquare$

## 非減少性

**命題**：$\mathfrak{a}, \mathfrak{b}, \mathfrak{c}$ を基数とする。
このとき：

$$
\mathfrak a \le \mathfrak b
\implies
\mathfrak a + \mathfrak c \le \mathfrak b + \mathfrak c.
$$

**証明**：集合 $A, B, C$ を次のすべてを満たすようにとる：

$$
\begin{aligned}
    \mathfrak{a} &= \lvert A \rvert,\\
    \mathfrak{b} &= \lvert B \rvert,\\
    \mathfrak{c} &= \lvert C \rvert,\\
    B \cap C &= C \cap A = \varnothing.
\end{aligned}
$$

基数の定義から単射 $f\colon A\longrightarrow B$ が存在する。
そこで写像 $h\colon A \cup C \longrightarrow B \cup C$ を次のように定義する：

$$
h(x) \coloneqq \begin{cases}
f(x), & x \in A,\\
x, & x \in C.
\end{cases}
$$

この写像 $h$ が単射であれば基数の和の定義により $\mathfrak a + \mathfrak c \le \mathfrak b + \mathfrak c$
が成り立つことになる。以下、写像 $h$ が単射であることを示す。

$x_1, x_2 \in A \cup C$ が $h(x_1) = h(x_2)$ を満たすとする。このとき
$x_1 \in C$ または $x_1 \notin C$ のいずれか一方しか成り立たない。

前者ならば $h$ の定義から $x_1 = h(x_1).$ 今の仮定から $x_1 = h(x_1) = h(x_2).$
$h(x_2) \in C$ も必要になり $x_1 = x_2 \in C.$

後者ならば $h$ の定義から $h(x_1) = f(x_1).$ 一方 $x_1, x_2$ の仮定から
$h(x_2) = h(x_1) = f(x_1).$ $h(x_2) \notin C$ も必要になり $h(x_2) = f(x_2).$
結局 $f(x_1) = f(x_2)$ となり、$f$ の単射性から $x_1 = x_2.$

いずれの場合においても

$$
h(x_1) = h(x_2) \implies x_1 = x_2
$$

が成り立つ。ゆえに $h$ は単射である。
$\blacksquare$

# 参考資料

* [Category:Cardinals](https://proofwiki.org/wiki/Category:Cardinals) - ProofWiki
