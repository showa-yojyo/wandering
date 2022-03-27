---
title: 基数の積 復習ノート
mathjax: true
tags: math
---

基数の積の定義や性質を復習する。本稿では集合 $X$ の基数を $\lvert X \rvert$ で表す。

## 定義

$A, B$ を集合とし、$\mathfrak{a} = \lvert A \rvert$,
$\mathfrak{b} = \lvert B \rvert$ とする。
このとき $\mathfrak{a}$ と $\mathfrak{b}$ の**積**を次により定義する：

$$
\mathfrak{ab} \coloneqq \lvert A \times B\rvert.
$$

ここで $\times$ は集合の直積を意味するものとする。

* コメント：和の定義では直和を用いた。一方、積のそれでは直積を用いる。
  いずれにせよ、派生集合の基数で定義される。

## 性質

基数の積のもつ性質をいくつか見ていく。

### 基数の乗法に関する恒等元

$1$ を集合 $\lbrace \varnothing \rbrace$ の基数とする： $1 \coloneqq \lvert \lbrace \varnothing \rbrace \rvert.$

**命題**：任意の基底 $\mathfrak a$ に対して次が成り立つ：

$$
1 \mathfrak a = \mathfrak a 1 = \mathfrak a.
$$

**証明**：集合 $A$ を $\mathfrak{a} = \lvert A \rvert$ であるようにとる。
基数の積の定義から：

$$
1 \mathfrak a = \lvert \lbrace \varnothing \rbrace \times A\rvert.
$$

全単射写像 $f\colon\lbrace \varnothing \rbrace \times A \longrightarrow A$
が存在すれば $1\mathfrak{a} = \mathfrak{a}$ が正しいことが示される。以下、そのような $f$ を一つ構成する。

写像 $f$ を $A$ への自然な射影：$(\varnothing, a) \longmapsto a$ で定めると、
これが全単射であることを示す。

単射性を示す。$(\varnothing, a_1), (\varnothing, a_2) \in \lbrace \varnothing \rbrace \times A$
が $f(\varnothing, a_1) = f(\varnothing, a_2)$ をみたすとする。
$f$ の定義から直接 $a_1 = a_2$ であることが明らか。したがって

$$
f(\varnothing, a_1) = f(\varnothing, a_2) \implies a_1 = a_2.
$$

よって $f$ は単射である。

全射性は $f$ が射影であることから成り立つ：
$\forall a \exists b(a \in A \implies b = (\varnothing, a) \in \lbrace \varnothing \rbrace \times A).$

以上により $f$ は全単射であり、基数の積の定義より $1\mathfrak{a} = \mathfrak{a}.$

$\mathfrak{a}1 = \mathfrak{a}$ の証明も同様である。
$\blacksquare$

### 結合律

**命題**：$\mathfrak{a, b, c}$ を基数とする。このとき：

$$
\mathfrak{(ab)c = a(bc)}.
$$

**証明**：集合 $A, B, C$ を次のすべてを満たすようにとる：

$$
\begin{aligned}
    \mathfrak{a} &= \lvert A \rvert,\\
    \mathfrak{b} &= \lvert B \rvert,\\
    \mathfrak{c} &= \lvert C \rvert.\\
\end{aligned}
$$

基数の積の定義により、$\mathfrak{(ab)c}$ および $\mathfrak{a(bc)}$
はそれぞれ集合 $(A \times B) \times C$ および $A \times (B \times C)$ の基数を意味する。
これまた定義によりこれらの集合の間に全単射写像が存在することが示されれば、結論は真である。
以下、そのような写像 $f\colon (A \times B) \times C \longrightarrow A \times (B \times C)$ を構成する。

写像 $f$ を次で定義する：

$$
f((a, b), c) = (a, (b, c)).
$$

これは明らかに全単射である。

ゆえに $(A \times B) \times C \approx A \times (B \times C)$ であり、
したがって $\lvert (A \times B) \times C\rvert = \lvert A \times (B \times C)\rvert.$
結論は真である。
$\blacksquare$

### 可換律

**命題**：$\mathfrak{a, b}$ を基数とする。このとき：

$$
\mathfrak{ab = ba}.
$$

**証明**：集合 $A, B$ を $\lvert A \rvert = \mathfrak a$, $\lvert B \rvert = \mathfrak b$
であるようにとる。

直積 $A \times B$ と $B \times A$ は写像 $(a, b) \longmapsto (b, a)$
が全単射であることにより対等である。ゆえに：

$$
\mathfrak{ab} = \lvert A \times B \rvert
= \lvert B \times A\rvert = \mathfrak{ba}.
\quad\blacksquare
$$

### 非減少性

**命題**：$\mathfrak{a, b, c}$ を基数とする。このとき：

$$
\mathfrak a \le \mathfrak b
\implies
\mathfrak{ac} \le \mathfrak{bc}.
$$

**証明**：集合 $A, B, C$ を次のすべてを満たすようにとる：

$$
\begin{aligned}
    \mathfrak{a} &= \lvert A \rvert,\\
    \mathfrak{b} &= \lvert B \rvert,\\
    \mathfrak{c} &= \lvert C \rvert.\\
\end{aligned}
$$

仮定および基数の定義から単射 $f\colon A\longrightarrow B$ が存在する。
そこで写像 $g\colon A \times C \longrightarrow B \times C$ を次のように定義する：

$$
g(a, c) \coloneqq (f(a), c).
$$

この写像 $g$ が単射であれば、再び基数の積の定義から、結論の不等式が真であることになる。以下それを示す。

$(a_1, c_1), (a_2, c_2) \in A \times C$ を $g$ による像が等しいようにとる。
つまり $(f(a_1), c_1) = (f(a_2), c_2)$ であり、$f(a_1) = f(a_2) \land c_1 = c_2$ が必要。
$f$ が単射であることから結局 $a_1 = a_2.$ すなわち：

$$
g(a_1, c_1) = g(a_2, c_2) \implies (a_1, c_1) = (a_2, c_2).
$$

ゆえに写像 $g$ は単射である。
$\blacksquare$

### 分配律

**命題**：$\mathfrak{a, b, c}$ を基数とする。このとき：

$$
\mathfrak{a(b + c) = ab + ac}.
$$

**証明**：集合 $A, B, C$ を次のすべてを満たすようにとる：

$$
\begin{aligned}
    \mathfrak{a} &= \lvert A \rvert,\\
    \mathfrak{b} &= \lvert B \rvert,\\
    \mathfrak{c} &= \lvert C \rvert,\\
    B \cap C &= \varnothing.
\end{aligned}
$$

この仮定で $B \cup C = B \sqcup C$ であることに注意：

$$
\mathfrak{b + c} = \lvert B \sqcup C \rvert = \lvert B \cup C\rvert.
$$

次に $(A \times B) \cap (A \times C) = \varnothing$ に注意：

$$
(A \times B) \cap (A \times C) = A \times (B \cap C) = A \times \varnothing = \varnothing.
$$

最後に $\lvert (A \times B) \cup (A \times C)\rvert$ が結論の等式の左辺と右辺のどちらにも書けることを示す：

$$
\begin{aligned}
    \lvert (A \times B) \cup (A \times C)\rvert
    &= \lvert A \times B \rvert + \lvert A \times C\rvert\\
    &= \mathfrak{ab + ac}.\\
    \lvert (A \times B) \cup (A \times C)\rvert
    &= \lvert A \times (B \cup C)\rvert\\
    &= \mathfrak{a(b + c)}.
\end{aligned}
$$

## 参考資料

* [Category:Cardinals](https://proofwiki.org/wiki/Category:Cardinals) - ProofWiki
