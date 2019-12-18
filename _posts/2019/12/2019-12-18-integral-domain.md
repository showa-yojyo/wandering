---
title: 整域学習ノート
tags: math
---

代数の整域に関するノート。以下の記述では、

* 単に環というときでも 1 を持つ可換環を指すとする。
* 零因子は $0$ を除外してあるとする。

# 定義

## 整域 (integral domain)

**定義**：1 を持つ可換環 $D$ が整域であるとは、次の条件をすべて満たすものをいう：

* $D \ne \lbrace 0_D \rbrace.$
* $D$ は零因子を含まない。

## 最大公約元 (GCD, $\gcd$)

**定義**：$D$ を整域とし、$a, b \in D$ を $a \ne 0_D$ または $b \ne 0$ を満たす要素とする。

ある $d \in D$ が次の条件を満たすとき、これを $a$ と $b$ の最大公約元であるといい、
記号 $d = \gcd(a, b)$ で表す：

* $d \mid a \land d \mid b.$
* $\forall c \in D(c \mid a \land c \mid b \implies c \mid d).$

言葉で言い換えると、$d$ は $a$ と $b$ の公約元であり、かつ任意の他の $a, b$ の公約元は $d$ を割り切る。

**検討**：
* 「最大」の付かない公約元、共通因数の概念は環で定義される。
* このような性質の要素が（整域の段階では）常に存在するとは保証されないし、また存在しても一意的であるとは限らない。
* 記号はほんとうは $\gcd\lbrace a, b\rbrace$ のように集合を引数に取る。タイプが面倒なので丸括弧で代用する。

## 同伴 (associates)

**定義**：$D$ を整域とする。$x, y \in D$ とする。
$D$ において $x$ と $y$ が同伴であるとは、次の条件をすべて満たすものをいう：

* $x$ が $y$ を割り切る。
* $y$ が $x$ を割り切る。

**検討**：

* 同値な言い換えがある：
  * 単項イデアルが等しい：$(x) = (y).$
  * 一方が他方の単元倍で表される。
* 同伴は同値関係である。

# 性質

無印の整域くらいではまだ良い性質がないようだ。
整域の次の「サブクラス」は[素元分解整域][UFD]なので、そこから定理を調べていく。

## 標数は $0$ または素数

**証明**：$D$ を整域とし、その標数を $\operatorname{char}(D)$ で表すことにする。

$\operatorname{char}(D)$ の値は $0$ または素数である。

**証明**：
$D$ が無限集合の場合には、$0_D$ 以外の $x \in D$ で
$x + x + \dotsb + x = 0$ となる要素は明らかに存在しない。ゆえに
$\operatorname{char}(D) = 0.$

$D$ が有限の場合に $\operatorname{char}(D) = n = rs,$
ただし $r, s$ はどちらも $2$ 以上の自然数であると表されると仮定して矛盾を導く。

環の性質から（整域の乗法の演算子と整数のそれとを同じ $\cdot$ で記すが）：

$$
\begin{aligned}
(r \cdot 1_D)(s \cdot 1_D)
&= (rs)(1_D \cdot 1_D)\\
&= (rs)1_D\\
&= n \cdot 1_D\\
&= 0_R.\\
\end{aligned}
$$

整域の定義により $D$ に真の零因子は含まれない。したがって
$r \cdot 1_D = 0_D$ または $s \cdot 1_D = 0_D$ が成り立つ。
しかしこれはどちらの場合でも $r$ または $s$ の定義に矛盾する。
ゆえに $\operatorname{char}(D) = rs$ の形には書けないことが示された。
すなわち、$\operatorname{char}(D)$ は素数である。

以上により、整域の標数は $0$ または素数であることが示された。
$\blacksquare$

## 単数の因数は単数に限る

**定理**：整域において、単数は単数以外では割り切れない。

**証明**：整域を $D$ とし、$U_D \subset D$ をその単元すべてからなる集合とする。
$(U_D, \cdot)$ は群をなす。

このとき $x \in D$ が $u \in U_D$ を割り切るならば $x \in U_D$ が成り立つことを示す。

「割り切る」の定義により、$u = tx$ をみたす $t \in D$ が存在する。
ここで $u$ は単元だから、その逆元 $u^{-1} \in U$ を両辺に乗じる。
$1_D = u^{-1}u = u^{-1}tx.$

$D$ は乗法に関して可換であるから

$$
u^{-1}tx = 1_D = xu^{-1}t.
$$

この等式は $x$ が逆元 $u^{-1}t$ をもつことを表している。ゆえに $x \in U_D.$
$\blacksquare$

## 逆元が自身と等しい単元は $\pm1_D$

**定理**：$D$ を整域とし、$x \in D$ は $x^2 = 1_D$ を満たす要素とする。

このとき $x = \pm1_D.$

**証明**：下記の式変形において整域であること、零因子が存在しないことが本質的である：

$$
\begin{aligned}
    &\phantom{\iff}x^2 = 1_D\\
    &\iff (x + 1_D)(x - 1_D) = 0_D\\
    &\iff x + 1_D = 0 \lor x - 1_D = 0_D.\\
    &\iff x = -1_D \lor x = 1_D.
\end{aligned}
$$

$\blacksquare$

## 単数すべての積は $-1_D$

**定理**：$D$ を有限個の単数を含む整域であるとし、単数全ての集合を $U_D \subset D$ とする。
このとき次が成り立つ：

$$
\prod_{u \in D_U}u = -1_D.
$$

**証明**：$S \coloneqq U_D\setminus\lbrace \pm1_D\rbrace$ とおく。
$\operatorname{card}S$ により場合分けを行う：

$\operatorname{card}S$ が偶数の場合。このとき $S$ を次の対の分割として表されることに注目する：

$$
S = \bigsqcup \{u, u^{-1}\}.
$$

各対において $uu^{-1} = 1_D$ だから、求める乗積はこれに $1_D$ と $-1_D$ を乗じて $-1_D$ である。

$\operatorname{card}S$ が奇数の場合。さきほどと同様の分割を考えると、

$$
S = \{x\} \cup \bigcup \{u, u^{-1}\}
$$

の形になる。ここで $x$ は $x = x^{-1}$ を満たす要素である。
しかし自分自身がその逆元であるような要素は $\pm 1_D$ のいずれかであるが、
これは $\pm 1_D \notin S$ に矛盾する。背理法により
$\operatorname{card}S$ が奇数の場合はあり得ないことが示された。

以上により、整域の単元すべての積は $-1_D$ に等しいことが示された。
$\blacksquare$

## 整域の条件は零イデアルが素であること

[素イデアル学習ノート][primeideal]参照。

## ～は整域である

例に関しては各サブクラスのもっとも性質の良い整域のノートで挙げていきたい。

# 参考資料

* ProofWiki
  * [Category:Definitions/Integral Domains](https://proofwiki.org/wiki/Category:Definitions/Integral_Domains)
  * [Category:Integral Domains](https://proofwiki.org/wiki/Category:Integral_Domains)

[UFD]: {{ site.baseurl }}{% post_url 2019/12/2019-12-17-ufd %}
[primeideal]: {{ site.baseurl }}{% post_url 2019/12/2019-12-11-prime-ideal %}
