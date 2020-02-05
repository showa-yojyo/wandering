---
title: 素イデアル学習ノート
tags: math
---

単位的可換環、1 を持つ可換環（以下、単に環と書く）の素イデアルについてまとめておく。

# 定義

## 素イデアル

$R$ を環とする。$P$ が $R$ の**素イデアル**であるとは、$R$ の任意のイデアル $I, J$ に対して
次が成り立つものを指す：

$$
IJ \subset P \implies I \subset P \lor J \subset P.
$$

言葉を替えると、$R$ の任意の要素 $a, b$ について

$$
ab \in P \implies a \in P \lor b \in P.
$$

* コメント：この条件を対偶の形で使うこともある。
* コメント：他にも等価な定義が存在する。しかしこれだけでいい。
* コメント：素イデアルは $R$ 自身と一致しないものとすると定義する流儀が多い。
  本稿もそれに従う。

$R$ の素イデアル全体の集合を $\operatorname{Spec}(R)$ とする。この記号は定着している。

## cf. 素元

* 素元 $p$ は $R$ の単元ではないという制約をつける。
* Def. 1: $\forall a\in R \forall b \in R(p \mid ab \implies p \mid a \lor p \mid b).$
* Def. 2: 単項イデアル $(p) \subsetneq R$ が素イデアルであるような元 $p \in R$。
  * この定義を採用する場合は素イデアルの定義を素元により定義しないこと。

# 性質

## 素イデアルの鎖の交差もまた素イデアル

**定理**：
$R$ を環とし、$\operatorname{Spec}(R)$ を $R$ の素イデアルすべてからなる集合とする。
$\lbrace P_{\lambda}\rbrace_{\lambda \in \Lambda} \subset \operatorname{Spec}(R)$ を空でない鎖とする。
$P \coloneqq \bigcap_{\lambda \in \Lambda}P_\lambda$ とおく。
このとき $P \in \operatorname{Spec}(R).$

**検討**：

* 鎖という概念に久しぶりに会うが、整列集合の性質を利用できることを感じる。

**証明**：
$P$ がイデアルであることは証明抜きで利用する。

$P$ が素イデアルであることを示す。
そのため、任意の $a \notin P \land b \notin P$ に対して
$ab \notin P$ が成り立つことを示す。

$a \notin P$ よりある $\alpha \in \Lambda$ が存在して $a \notin P_\alpha.$
$b \notin P$ よりある $\beta \in \Lambda$ が存在して $b \notin P_\beta.$
鎖 $\lbrace P_{\lambda}\rbrace_{\lambda \in \Lambda}$ は包含関係による全順序集合であるので、
$P_\alpha \subset P_\beta$ か $P_\beta \subset P_\alpha$ かのどちらか一方が成り立つ。

どちらでも同じことなので $P_\alpha \subset P_\beta$ が成り立っていると仮定する。
すると $b \notin P_\alpha$ も成り立つ。$P_\alpha$ は素イデアルなので
$ab \notin P_\alpha.$ すなわち $ab \notin P.$

以上により 任意の $a \notin P \land b \notin P$ に対して
$ab \notin P$ が成り立つことが示され、したがって $P$ が素イデアルであることが示された。
$\blacksquare$

## 素イデアルによる剰余環は整域である

**定理**：$R$ を環とし、$J \subset R$ をそのイデアルとする。
このとき $J$ が素イデアルであることと剰余環 $R/J$ が整域であることは同値である。

**検討**：

* 同値命題の証明なので十分条件と必要条件を両方向とも示す。
* 基本的には用語の定義に従って推論していけばいい。
* 素イデアルが選言で定義されていることから場合分けが生じるようだ。

**証明**：剰余環 $R/J$ が環である事実を証明なしに利用する。

$\implies\colon$
$J \subset R$ が素イデアルであることから $R/J$ が整域であることを示す。
以下 $a \in R$ に対して $\bar{a} \coloneqq a + J \in R/J$ と書く。

$\bar{x}, \bar{y} \in R/J$ が $\bar{x}\cdot\bar{y} = 0_{R/J}$ を満たすとする。
このとき $\bar{x} = 0_{R/J}$ または $\bar{y} = 0_{R/J}$ であることを示す。

$R/J$ の零元 $0_{R/J}$ は $J$ であるので
$\bar{x}\cdot\bar{y} = 0_{R/J}$ ならば $x \cdot y \in J.$

$J$ が素イデアルであることから $x \in J$ または $y \in J$ のどちらかが成り立つ。

* $x \in J$ の場合には $\bar{x} = J = 0_{R/J}.$
* $y \in J$ の場合には $\bar{y} = J = 0_{R/J}.$

よって、いずれの場合にも $\bar{x}, \bar{y} \in R/J$ が $\bar{x}\cdot\bar{y} = 0_{R/J}$
ならば $\bar{x} = 0_{R/J}$ または $\bar{y} = 0_{R/J}$ であることが示された。
以上により、$J \subset R$ が素イデアルならば $R/J$ が整域であることが示された。
$\Box$

$\impliedby\colon$
$R/J$ は整域であると仮定する。
$x \cdot y \in J$ を満たす $x, y \in R$ を任意にとると
$x \in J$ または $y \in J$ が成り立つことを示す。

すると $\overline{x\cdot y} = 0_{R/J}.$
一方 $\overline{x\cdot y} = \bar x \cdot \bar y.$
したがって $\bar x \cdot \bar y = 0_{R/J}.$
$R/J$ が整域であることから、$\bar x = 0$ または $\bar y = 0$ が成り立つ。

* $\bar x = 0$ が成り立つならば $x \in J$ が、
* $\bar y = 0$ が成り立つならば $y \in J$ が

それぞれ成り立つ。これで $x \cdot y \in J$ を満たす $x, y \in R$ を任意にとると
$x \in J$ または $y \in J$ が成り立つことが示された。
すなわち $J$ は素イデアルである。
$\blacksquare$

## 環 $R$ が整域 $\iff$ $(0) \subset R$ が素イデアル

**定理**：環 $R$ が整域であることと、零イデアル $(0) \subset R$ が素イデアルであることは同値である。

**検討**：前定理により、$R/(0)$ が整域であることを示せば $(0)$ が $R$ の素イデアルであることが示される。
残りは $R/(0)$ と $R$ が「同じ」ことを言えばいい。
つまり

「環は零イデアルによる剰余環と同型である」

ことを示せばいい。

**証明**：まず $R$ が環であるならば $R \cong R/(0)$ を示す。

写像 $\operatorname{id}_R\colon R \longrightarrow R$ を恒等写像とすると、当然環準同型である。
この核と像はそれぞれ $0 = 0R = (0)$ および $R$ だから準同型定理により $R/(0) = R/\ker{f} \cong \operatorname{im}f = R.$
よって $R$ が環であるならば $R \cong R/(0)$ であることが示された。
$\Box$

$R$ が整域であるとすると、同型な $R/(0)$ も整域である。
このとき、前定理によりイデアル $(0)$ は素イデアルである。
$\blacksquare$

## 素イデアルの環の準同型写像に関する逆像もまた素イデアルである

**定理**：$R_1, R_2$ を環、写像 $f\colon R_1 \longrightarrow R_2$
を環準同型とし、$P$ を $R_2$ の素イデアルであるとする。このとき $f$ の逆像
$f^{-1}(P)$ は $R_1$ の素イデアルである。

**検討**：準同型写像の定義と素イデアルの定義は相性が良い。
最初の対象要素の選び方がやや直観的でない。

**証明**：イデアルの準同型写像による逆像がイデアルである事実を証明なしに利用する。

$f^{-1}(P)$ は $R_1$ の素イデアルであることを示す。

$a, b \in R_1$ を $ab \in f^{-1}(P)$ を満たす任意の要素とする。
これらの像を考えると $f$ が準同型写像であるから $f(ab) = f(a)f(b) \in P.$
$P$ が素イデアルであることから $f(a) \in P \lor f(b) \in P.$

* $f(a) \in P$ ならば $a \in f^{-1}(P).$
* $f(b) \in P$ ならば $b \in f^{-1}(P).$

つまり $ab \in f^{-1}(P)$ ならば $a \in f^{-1}(P)$ または $b \in f^{-1}(P)$
が成り立つことが示された。したがって、$f^{-1}(P)$ は $R_1$ の素イデアルである。
$\blacksquare$

# 参考資料

* ProofWiki
  * [Definition:Prime Ideal of Ring](https://proofwiki.org/wiki/Definition:Prime_Ideal_of_Ring)
  * [Intersection of Chain of Prime Ideals of Commutative Ring is Prime Ideal](https://proofwiki.org/wiki/Intersection_of_Chain_of_Prime_Ideals_of_Commutative_Ring_is_Prime_Ideal)
  * [Prime Ideal iff Quotient Ring is Integral Domain](https://proofwiki.org/wiki/Prime_Ideal_iff_Quotient_Ring_is_Integral_Domain)
  * [Integral Domain iff Zero Ideal is Prime](https://proofwiki.org/wiki/Integral_Domain_iff_Zero_Ideal_is_Prime)
    * [Quotient Ring by Null Ideal](https://proofwiki.org/wiki/Quotient_Ring_by_Null_Ideal)
  * [Preimage of Prime Ideal under Ring Homomorphism is Prime Ideal](https://proofwiki.org/wiki/Preimage_of_Prime_Ideal_under_Ring_Homomorphism_is_Prime_Ideal)
