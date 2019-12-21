---
title: Noether 環学習ノート
tags: math
---

Noether 環に関する学習ノート。以下、単に環と書くときは 1 を持つ可換環を意味する。

# 定義

## 有限生成イデアル

**定義**：環 $A$ のイデアル $I$ が有限生成であるとは、有限集合 $X \subset A$ が存在して、
$I$ が次の形に表されることを意味する：

$$
I = \left\{\left. \sum_{i = 1}^n r_i \cdot x_i \cdot s_i \,\right|\, n \in \N, r_i \in A, x_i \in X, s_i \in A\right\}.
$$

**検討**：単項イデアルは有限生成イデアルである。$\lvert X \rvert = 1$ という特殊な場合だ。

## 昇鎖律

昇鎖律については[単項イデアル整域のノート][pid]を参照。

**検討**：そこで証明した性質により、単項イデアル整域は Noether 環の一種だ。

## Noether 環

**定義**：次の同値な条件を満たす環 $A$ のことを **Noether 環**と呼ぶ：

* $A$ のどのイデアルも有限生成である。
* $A$ においてイデアルの昇鎖律が成り立つ。
* $A$ においてイデアルの極大律が成り立つ：
  $A$ のイデアルを要素とする空でない任意の集合には包含関係を順序関係とする順序に関する極大元が存在する。

# 定理

## Noether 環の定義で述べた 3 条件は同値である。

**証明**：

### 有限生成性 $\implies$ 昇鎖律：

イデアルの昇鎖 $I_1 \subset I_2 \subset \dotsb$ が存在すると仮定する。
和集合 $J \coloneqq \bigcup_{i} I_i$ もまた $A$ のイデアルである。
$I_i \subset J$ に注意する。

イデアル $J$ は有限生成であるので、ある $b_1, \dotsc, b_m \in A$ が存在してそれらが $J$ を生成している。

昇鎖の性質からある番号 $k$ のイデアル $I_k$ がこれらの生成元すべてを含む。
言い換えると：

$$
I_k = (b_1, \dotsc, b_m) = J.
$$

一方 $I_k \subset I_{k + 1} \subset \dotsb \subset J$ より
$I_k = I_{k + 1} = \dotsb = J.$
したがって $A$ のどのイデアルも有限生成ならば、$A$ においてイデアルの昇鎖律が成り立つことが示された。
$\blacksquare$

### 昇鎖律 $\implies$ 有限生成性

イデアル $I \subset A$ が存在して有限生成でないと仮定して矛盾を導く。
すると、任意の有限部分集合 $\coloneqq \lbrace x_1, \dots, x_n \rbrace \subset A$ が生成する有限生成イデアルは
$I$ ではあり得ない。

次のイデアルの昇鎖を考える：

$$
(x_1) \subset (x_1, x_2) \subset \dotsb \subset (x_1, \dotsc, x_n).
$$

$n \in \N$ が任意であるから、昇鎖律を満たさないものがイデアルの増加列が存在することになり矛盾。
$\blacksquare$

### 昇鎖律 $\implies$ 極大律

イデアルを要素とする集合族 $\varnothing \ne \mathscr I \coloneqq \lbrace I_\lambda \rbrace_{\lambda \in \Lambda}$
が存在し、これが極大律を満たさないと仮定して矛盾を導く。

イデアルの昇鎖 $I_1 \subsetneq \dotsb \subsetneq I_n$ が $\mathscr I$
に含まれていて極大律を満たさないと仮定する。すなわちさらに「大きい」イデアル $I_{n + 1} \in \mathscr I$ が存在する。
そしてそれをこの昇鎖に接続して、より長い昇鎖を構成することができる。
この手続きは任意の長さに続き、結局昇鎖律が成り立たないことになるので矛盾する。

したがって $\mathscr I$ は極大律を満たすか、あるいは空集合でなければならない。
$\blacksquare$

### 極大律 $\implies$ 昇鎖律

$A$ のイデアルを要素とする空でない任意の集合 $\mathscr I$ には包含関係を順序関係における極大元が存在すると仮定する。
$\mathscr I$ のどのイデアル昇鎖にもある極大元が存在し、したがって昇鎖律が成り立つ。
$\mathscr I$ は任意であるから、$A$ の任意のイデアル昇鎖において昇鎖律が成り立つ。
$\blacksquare$

# 参考資料

同値な定義およびその証明と、極大条件の細かいところを主に参考にした。

* [Equivalence of Definitions of Noetherian Ring](https://proofwiki.org/wiki/Equivalence_of_Definitions_of_Noetherian_Ring) - ProofWiki
* [Noetherian ring](https://en.wikipedia.org/wiki/Noetherian_ring) - Wikipedia
* [abstract algebra - Why noetherian ring satisfies the maximal condition?](https://math.stackexchange.com/questions/2631016/why-noetherian-ring-satisfies-the-maximal-condition) - Mathematics Stack Exchange

[pid]: {{ site.baseurl }}{% post_url 2019/12/2019-12-19-pid %}
