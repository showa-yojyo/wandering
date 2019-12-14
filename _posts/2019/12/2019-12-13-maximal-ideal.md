---
title: 極大イデアル学習ノート
tags: math
---

単位的可換環、1 を持つ可換環（以下、単に環と書く）の極大イデアルについてまとめておく。

# 定義

$R$ を環とする。$R$ のイデアル $J$ が極大であるとは、次の条件をすべて満たすイデアルを言う：

* $J \subsetneq R.$
* $J \subsetneq K \subsetneq R$ を満たすイデアル $K$ が存在しない。

つまり、$R$ のすべての真イデアルを包含関係により一列に並べるとき、
$J$ がその極大元であることを意味する。

# 性質

## 極大イデアルによる剰余環は体と同値

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

## 極大イデアルは素イデアル

**定理**：
$R$ を環とし、$M$ を $R$ の極大イデアルとする。

このとき $M$ は $R$ の素イデアルである。

**証明**：先述の定理により剰余環 $R/M$ は体である。
定義より体が整域である。したがって $R/M$ は整域である。
[素イデアルの性質]({{ site.baseurl }}{% post_url 2019/12/2019-12-11-prime-ideal %})で示したように、
剰余環 $R/M$ が整域であることと $M$ が素イデアルであることは同値である。
$\blacksquare$

## 単項イデアル整域の非零素イデアルは極大イデアル

**定理**：
$D$ を単項イデアル整域とする。$J \subsetneq D$ を $(0)$ でない素イデアルとする。

このとき $J$ は極大イデアルである。

**検討**：
* 極大性の証明なので論証中に「最小最大パターン」が現れるだろう。
* 利用する事実は次だ：整域において、
  * 素元は既約元である
  * 既約元で生成された単項イデアルは極大イデアルであることと同値である

証明を記す。

----

**定理**：整域における素元は既約元である。

**証明**：
$p \in D$ を素元とする。$p = ab$ なる $a, b \in D$ があると仮定する。
以下、$a$ または $b$ が単元であることを示すことにより $p$ が既約元であることを示す。

値のとり方から $p$ は $ab$ を割り切る。$p$ は素元であるので、
$p$ が $a$ を割り切るか、または $p$ が $b$ を割り切る。
どちらでも同じことなので $p \mid a$ とする。
このときある $t \in D$ が存在して $pt = a.$

$$
\begin{aligned}
1a &= a = pt\\
&= (ab)t = a(bt).\\
\therefore a &= a(bt).
\end{aligned}
$$

$D$ は整域であるから簡約律が適用できて $1 = bt.$ すなわち $b$ は単元である。
したがって $p = ab$ のとき $a$ または $b$ が単元であることが示され、$p$ は既約元であることが示された。
$\blacksquare$

----

**定理**：整域において、既約元で生成される単項イデアルは極大イデアルである。
逆に、整域における極大イデアルは既約元から生成される単項イデアルである。

**検討**：
極大性をうまく使う。背理法と相性が良いようだ。

**証明**：
$\implies\colon$ 整域 $D$ における既約元 $p$ を一つとる。
このときイデアル $(p)$ が $D$ における極大イデアルでないと仮定して矛盾を導く。

まず、$p$ が既約元であるから単元ではない。ゆえにイデアル $(p)$ は $D$ よりも真に小さい：
$(p) \subsetneq D.$

包含関係による列 $(p) \subsetneq K \subsetneq D$ が成り立つようなイデアル $K$ が存在すると仮定する。

$D$ は整域であるので、イデアル $K$ は単項生成である。
すなわち、何か $x \in D$ が存在して $(x) = K$ を満たす。
先ほどの系列を書き直すと：

$$
(p) \subsetneq (x) \subsetneq D.
$$

$(p) \subsetneq (x)$ と再び整域の単項イデアルの性質から $x$ は $p$ を割り切る。
つまり何か $t \in R$ が存在して $p = xt$ を満たす。
ここで $p$ が既約元であることから、$x$ が $D$ の単元であるか、あるいは $t$ がそうである。
$x$ から見ると、
* $x$ が $D$ の単元であるか、
* $x$ が $p$ と互いに割り切る関係にある

かのどちらかが成り立つ。

* しかし前者は成り立たない。なぜなら $(x) \subsetneq D$ から $(x) \ne D.$
  整域における単項イデアルの性質上、$x$ は単元ではありえない。
* そして後者も成り立たない。同様に $(p) \subsetneq (x)$ から $(p) \ne (x).$
  整域における単項イデアルの性質上、$x$ と $p$ とが互いに割り切るような関係はない。

この矛盾は $(p)$ が極大イデアルでないと仮定したことから生じた。
したがって $(p)$ は $D$ における極大イデアルであることが示された。
$\Box$

$\impliedby\colon$
$(p)$ を $D$ の極大イデアルと仮定すると、$p$ が既約元であることを示す。

$p$ の任意の既約分解 $p = fg$ において、$f$ も $g$ も単元ではないと仮定して矛盾を導く。

まず $(p) \subsetneq (f)$ を示す。

任意に $x \in (p)$ をとると、ある $q \in D$ が存在して $x = pq.$
このとき $x = pq = fgq \in (f).$
$x$ は任意であるから $(p) \subset (f).$

次に $f \in (p)$ を仮定する。するとある $r \in D$ が存在して $f = rp.$
このとき $f = pr = fgr.$ $D$ が整域であるから簡約律を適用できて $gr = 1.$
したがって $g$ は単元となる。これは矛盾なので、$f \notin (p)$ が成り立つ。

$f \notin (p)$ かつ $f \in (f)$ だから $(p) \subsetneq (f)$ が成り立つ。

次に $(f) = D$ と $(f) \ne D$ の成り立つ矛盾があることを示す。

したがって、$(p)$ が極大イデアルであることから $(f) = D$ が必要。
$f$ が単元でないという仮定から、$fh = 1$ を満たすような $h \in D$ は存在しない。
したがって、

$$
1 \notin (f) = \{fh\,|\,h \in D\}.
$$

そして $1 \in D$ なので：

$$
(f) \subsetneq D.
$$

これは $(f) = D$ に矛盾する。したがって $f$ も $g$ も単元ではないという仮定は成り立たない。
すなわち $p = fg$ において $f$ または $g$ の少なくとも一方は単元である。
よって、$p$ が既約元であることが示された。
$\blacksquare$

----

本題の証明に入る。

**証明**：$D$ が単項イデアル整域であることから、どのイデアルにも何か $r \in D$ が対応して単項イデアルの形 $(r)$ で表される。

今、$p \ne 0$ により生成される素イデアル $(p)$ をとる。
このとき $(p)$ は素元であるので既約元でもある。

整域における既約元で生成された単項イデアルは極大イデアルであるので、主張は正しい。
$\blacksquare$

# 参考資料

* ProofWiki
  * [Definition:Maximal Ideal of Ring](https://proofwiki.org/wiki/Definition:Maximal_Ideal_of_Ring)
  * [Maximal Ideal iff Quotient Ring is Field](https://proofwiki.org/wiki/Maximal_Ideal_iff_Quotient_Ring_is_Field)
  * [Maximal Ideal of Commutative and Unitary Ring is Prime Ideal](https://proofwiki.org/wiki/Maximal_Ideal_of_Commutative_and_Unitary_Ring_is_Prime_Ideal)
  * [Prime Ideal of Principal Ideal Domain is Maximal](https://proofwiki.org/wiki/Prime_Ideal_of_Principal_Ideal_Domain_is_Maximal)
    * [Principal Ideal of Principal Ideal Domain is of Irreducible Element iff Maximal](https://proofwiki.org/wiki/Principal_Ideal_of_Principal_Ideal_Domain_is_of_Irreducible_Element_iff_Maximal)
* [prime element is irreducible in integral domain](https://planetmath.org/primeelementisirreducibleinintegraldomain)
