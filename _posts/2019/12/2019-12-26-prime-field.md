---
title: 体論学習ノート 4 素体編
mathjax: true
tags: math
---

Galois 論に入る前に体の基本的な性質を理解してゆくノート。今回は素体と prime subfield を学ぶ。

## 定義

### 素体 (prime field)

**定義**：**素体**とは、体であり**真の部分体**をもたないものである。

**検討**：真の部分体 (proper subfield) の定義は「部分体であって自身と一致しないもの」でよい。

### （和名不明）Prime Subfield

**定義**：体 $K$ の部分体すべての交差をとって得られる部分体 $P$ のことを $K$ の **prime subfield** という。

**検討**：

* [部分体の交差は部分体である][subfield]から、
  * $P$ が $K$ の部分体であることは正しい。
  * $P$ は極小性を有する：prime subfield には真の部分体は存在しない。
  * $P$ は $K$ のすべての部分体に含まれる。
* その他の性質を証明とともに後述する。

## 性質

### 素数を法とする剰余類環は素体である

**定理**：$p$ を素数とする。$\Z_p \coloneqq \Z/p\Z = \Z/(p)$ とする。

このとき $\Z_p$ は素体である。

**検討**：

* 部分集合 $K \subset \Z_p$ が体であれば、それが自明な部分体であることを示す。
* 素数位数の群の性質を利用する。

**証明**：部分体 $K \subset \Z_p$ を任意にとる。
その加法群 $(K, +)$ は加法群 $(\Z_p, +)$ の部分群でなければならない。
ここで $(\Z_p, +)$ の位数は素数 $p$ である。素数位数の群には自明な部分群しか存在しないので、
$(K, +)$ は自明な部分群である。

部分体と仮定したので $(K, +) \ne \lbrace 0 \rbrace.$
したがって $(K, +) = (\Z_p, +).$
位数の考察から $K = \Z_p.$

$\Z_p$ の部分体が自分自身しかないことが示された。したがって $\Z_p$ は素体であることが示された。
$\blacksquare$

### 有理数体は素体である

**定理**：$\mathbb{Q}$ は素体である。

**検討**：任意の部分体を一つとり、それがどんな要素を含むのかを示す。すると結局 $\mathbb Q$ 全体に等しいとわかる。

**証明**：部分体 $K \subset \mathbb Q$ を一つとる。$K$ は体であるので
$K \ne \lbrace  0 \rbrace$ かつ $K \ne \varnothing$ である。

したがって任意に $a \in K$ を一つとることができる。$K$ は体であるので
加法と乗法それぞれの逆元 $-a,\;a^{-1} \in K$ がとれる。

$a a^{-1} = 1 \in K.$ ここで $n \in \N \implies n \in K$ を仮定すると
加法に関して閉じているから $n + 1 \in K.$ 数学的帰納法により $\N \subset K.$
一方 $n \in K \implies -n \in K$ であるから、もっと強く $\Z \subset K.$

したがって任意の $p \in \Z \subset K,\;0 \ne q \in \Z \subset K$ に対して
$p/q \in K.$

[体の部分集合が部分体である条件][subfield]により、$K = \mathbb Q$ が示された。
$\blacksquare$

### 標数 $p$ の体の prime subfield

**定理**：標数が $p \ne 0$ の体 $K$ には次の条件を満たす部分体 $P$ が一意的に存在する：

$$
P \cong \Z_p.
$$

**証明**：有理整数環 $\Z$ から $K$ への環の準同型 $\varphi\colon\Z \longrightarrow K$ を
$\varphi(n) = n \cdot 1_K$ で定義する。$p$ は $K$ の標数であるから
$p \cdot 1_K = 0.$ つまり $\ker \varphi = (p)$ である。

準同型定理により次の同型が成り立つ：

$$
\Z_p \coloneqq \Z/(p) = \Z/\ker\varphi \cong \operatorname{im}(\varphi).
$$

剰余類環 $\Z_p$ は体であるから、$\operatorname{im}\varphi \subset K$ もまた体である。
$P \coloneqq \operatorname{im}\varphi$ とおけば主張の一意的な部分体であることを満たす。
$\blacksquare$

### 標数 $0$ の体の prime subfield

**定理**：標数が $0$ の体 $K$ には次の条件を満たす部分体 $P$ が一意的に存在する：

$$
P \cong \mathbb Q.
$$

**証明**：標数が $0$ であることは、$K$ の任意の部分体 $L$ が任意の整数を含むことを意味する。
それはすなわち $\mathbb Q \subset L$ を意味する（ここまでの推論は前述「有理数体は素体」を参照）。

したがって $P$ を $K$ の部分体すべての交差として定義すれば $P \cong \mathbb Q$
であり、定義から一意的に定まる。
$\blacksquare$

### 体は素体を部分体としてもつ

**定理**：体は素体を部分体としてもつ。

**証明**：体を $K$ とする。$K$ は可換な斜体であるので、$K$ の部分斜体はすべて実際は $K$ の部分体である。
**部分斜体すべての交差は prime subfield であるから（要証明）**、$K$ の部分体すべての交差は
$K$ の部分体であるような素体である。
$\blacksquare$

## 参考資料

* [Category:Prime Fields](https://proofwiki.org/wiki/Category:Prime_Fields) - ProofWiki
* [Prime subfield is either isomorphic to $\mathbb{Q}$ or $\mathbb F_p$](https://math.stackexchange.com/questions/1942821/prime-subfield-is-either-isomorphic-to-mathbbq-or-f-p) - Mathematics Stack Exchange

[subfield]: {% post_url 2019/12/2019-12-25-subfield %}
