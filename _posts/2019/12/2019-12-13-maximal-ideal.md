---
title: 極大イデアル学習ノート
tags: math
---

単位的可換環、1 を持つ可換環（以下、単に環と書く）の極大イデアルについてまとめておく。

## 定義

$R$ を環とする。$R$ のイデアル $J$ が極大であるとは、次の条件をすべて満たすイデアルを言う：

* $J \subsetneq R.$
* $J \subsetneq K \subsetneq R$ を満たすイデアル $K$ が存在しない。

つまり、$R$ のすべての真イデアルを包含関係により一列に並べるとき、
$J$ がその極大元であることを意味する。

## 性質

### 極大イデアルによる剰余環は体と同値

**定理**：
$R$ を環とし、$J$ を $R$ のイデアルとする。このとき次は同値である：

* $J$ が極大イデアルである
* 剰余環 $R/J$ は体である

**検討**：

* 同値命題の証明なので十分条件と必要条件を両方向とも示す。
* 体、極大イデアル、剰余環、同値類の定義を丁寧に参照する。

**証明**：
$\implies\colon$
$J$ が極大イデアルであると仮定する。$J$ は $R/J$ の零元であることに注意する。

今、任意に零でない $A \in R/J$ をとり、任意に $a \in A$ をとる。
$A$ のとり方から $a \notin J.$

ここで $K \coloneqq J + A$ を考える。これは $R$ のイデアルになる。
このイデアルは $\lbrace j + ra \,\mid\, j \in J, r \in R\rbrace$ を含む。

$J$ の極大性および $K$ はイデアルであることから $J \subsetneq K.$
すると $K = R$ が必要である。このとき $1 \in R$ であるのでイデアルの性質から
$u + ra = 1$ を満たす $u \in J$ が存在する。

したがって

$$
\begin{aligned}
\bar r\cdot \bar a
&= \overline{1 - u} && \because u + ra = 1\\
&= \bar 1 && \because u \in J.

\end{aligned}
$$

これは $\bar r$ が $\bar a$ の逆元であることを示している。
$A$, $a$ は任意だと仮定したので、$R/J$ は体である。
$\Box$

$\impliedby\colon$
$R/J$ を体と仮定し、$K$ を $J \subsetneq K \subset R$ を満たすイデアルと仮定する。
すると実は $K = R$ であることを以下に示す。

今 $x \in K\setminus J$ を任意にとる。すると $x \notin J$ であることから $\bar x \ne J.$

さらに $R/J$ が体であることから、$\bar x$ には逆元が存在する。それを $\bar s \in R/J$ とおく：

$$
\bar x \cdot \bar s = \overline{xs} = \bar1.
$$

群論の同値類に関する定理 $xH = yH \iff x^{-1}y \in H$ より

$$
\tag*{$\spadesuit$}
1 - sx \in J \subsetneq K.
$$

$K$ がイデアルであることから $x \in K, s \in R$ について $sx \in K.$
これと $\spadesuit$ により再び$K$ がイデアルであることから：

$$
(1 - sx) + sx = 1 \in K.
$$

イデアル $K$ が $1$ を含むことが示された。したがって $K = R.$
したがって $J \subsetneq K = R$ は極大イデアルであることがわかった。
$\blacksquare$

### 極大イデアルは素イデアル

**定理**：
$R$ を環とし、$M$ を $R$ の極大イデアルとする。

このとき $M$ は $R$ の素イデアルである。

**証明**：先述の定理により剰余環 $R/M$ は体である。
定義より体が整域である。したがって $R/M$ は整域である。
[素イデアルの性質]({{ site.baseurl }}{% post_url 2019/12/2019-12-11-prime-ideal %})で示したように、
剰余環 $R/M$ が整域であることと $M$ が素イデアルであることは同値である。
$\blacksquare$

## 参考資料

* ProofWiki
  * [Definition:Maximal Ideal of Ring](https://proofwiki.org/wiki/Definition:Maximal_Ideal_of_Ring)
  * [Maximal Ideal iff Quotient Ring is Field](https://proofwiki.org/wiki/Maximal_Ideal_iff_Quotient_Ring_is_Field)
  * [Maximal Ideal of Commutative and Unitary Ring is Prime Ideal](https://proofwiki.org/wiki/Maximal_Ideal_of_Commutative_and_Unitary_Ring_is_Prime_Ideal)
