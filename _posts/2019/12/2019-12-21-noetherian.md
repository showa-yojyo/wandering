---
title: Noether 環学習ノート
mathjax: true
tags: math
---

Noether 環に関する学習ノート。以下、単に環と書くときは 1 を持つ可換環を意味する。

## 定義

### 有限生成イデアル

**定義**：環 $A$ のイデアル $I$ が有限生成であるとは、有限集合 $X \subset A$ が存在して、
$I$ が次の形に表されることを意味する：

$$
I = \left\{\left. \sum_{i = 1}^n r_i \cdot x_i \cdot s_i \,\right|\, n \in \N, r_i \in A, x_i \in X, s_i \in A\right\}.
$$

**検討**：単項イデアルは有限生成イデアルである。$\lvert X \rvert = 1$ という特殊な場合だ。

### 昇鎖律

昇鎖律については[単項イデアル整域のノート][pid]を参照。

**検討**：そこで証明した性質により、単項イデアル整域は Noether 環の一種だ。

### Noether 環

**定義**：次の同値な条件を満たす環 $A$ のことを **Noether 環**と呼ぶ：

* $A$ のどのイデアルも有限生成である。
* $A$ においてイデアルの昇鎖律が成り立つ。
* $A$ においてイデアルの極大律が成り立つ：
  $A$ のイデアルを要素とする空でない任意の集合には包含関係を順序関係とする順序に関する極大元が存在する。

## 定理

### Noether 環の定義で述べた 3 条件は同値である

**証明**：

#### 有限生成性 $\implies$ 昇鎖律

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

#### 昇鎖律 $\implies$ 有限生成性

イデアル $I \subset A$ が存在して有限生成でないと仮定して矛盾を導く。
すると、任意の有限部分集合 $\coloneqq \lbrace x_1, \dots, x_n \rbrace \subset A$ が生成する有限生成イデアルは
$I$ ではあり得ない。

次のイデアルの昇鎖を考える：

$$
(x_1) \subset (x_1, x_2) \subset \dotsb \subset (x_1, \dotsc, x_n).
$$

$n \in \N$ が任意であるから、昇鎖律を満たさないものがイデアルの増加列が存在することになり矛盾。
$\blacksquare$

#### 昇鎖律 $\implies$ 極大律

イデアルを要素とする集合族 $\varnothing \ne \mathscr I \coloneqq \lbrace I_\lambda \rbrace_{\lambda \in \Lambda}$
が存在し、これが極大律を満たさないと仮定して矛盾を導く。

イデアルの昇鎖 $I_1 \subsetneq \dotsb \subsetneq I_n$ が $\mathscr I$
に含まれていて極大律を満たさないと仮定する。すなわちさらに「大きい」イデアル $I_{n + 1} \in \mathscr I$ が存在する。
そしてそれをこの昇鎖に接続して、より長い昇鎖を構成することができる。
この手続きは任意の長さに続き、結局昇鎖律が成り立たないことになるので矛盾する。

したがって $\mathscr I$ は極大律を満たすか、あるいは空集合でなければならない。
$\blacksquare$

#### 極大律 $\implies$ 昇鎖律

$A$ のイデアルを要素とする空でない任意の集合 $\mathscr I$ には包含関係を順序関係における極大元が存在すると仮定する。
$\mathscr I$ のどのイデアル昇鎖にもある極大元が存在し、したがって昇鎖律が成り立つ。
$\mathscr I$ は任意であるから、$A$ の任意のイデアル昇鎖において昇鎖律が成り立つ。
$\blacksquare$

## Noether 環の剰余環は Noether 環

**定理**：Noether 環の剰余環は Noether 環である。

**検討**：Noether 環についてはこの種の命題が多いので、系統的に証明する方法も存在する。

**証明**：$A$ を Noether 環とし、その任意のイデアル $I$ による剰余環 $A/I$ を考える。
イデアル $[J] \in A/I$ が与えられたとき、これが有限生成であることを示す。

$\pi\colon A \longrightarrow A/I$ を $A$ から剰余環への自然な射影とする。

Noether 環の定義から $J \subset A$ が有限生成である。
よって、ある $a_1, \dotsc, a_n \in A$ が存在して

$$
\begin{aligned}
J &= \pi^{-1}([J]) = (a_1, \dotsc, a_n).\\
\therefore [J] &= (\pi(a_1), \dotsc, \pi(a_n)).
\end{aligned}
$$

イデアル $[J] \in A/I$ もまた有限生成である。
$I$ は任意であったから、Noether 環の剰余環は Noether 環であることが示された。
$\blacksquare$

## Hilbert の基底定理

**定理**：Noether 環 $A$ 上の一変数多項式環 $A[X]$ もまた Noetherian である。

**検討**：$A[X]$ の任意のイデアルが有限生成であることを示せば十分だ。
イデアルを $I$ として、有限個の生成元 $f_1, \dotsc, f_n \in A[X]$ を決定する方針で行く。

$I$ から次数の低い順に多項式 $f_1, f_2, \dotsc$ をとっていき、その主係数が生成するイデアルを考える。
$A$ のネーター性からこれは有限生成であるので、ある $a_1, \dotsc, a_n \in A$ により
イデアル $(a_1, \dotsc, a_n)$ が飽和状態になる。
これが $I$ と等しいことを多項式の次数に関する性質を利用して示す。

**証明**：$I \subset A[X]$ を任意のイデアルとする。これが有限生成であることを示す。

$f_1 \in I$ を $I$ で次数が最小の多項式とする。もし $(f_1) = I$ ならば言うことはない。

そこで $(f_1) \ne I$ と仮定する。$f_2 \in I\setminus(f_1)$ を $I\setminus(f_1)$ で次数が最小の多項式とする。
もしイデアル $(f_1, f_2) = I$ ならば言うことはない。

$k \ge 1$ について $(f_1, \dotsc, f_k) \ne I$ ならば
最小次数の多項式 $f_{k + 1}\in I\setminus(f_1, \dotsc, f_k)$ を選んでイデアルを大きくしていく手続きを考える。

多項式 $f_k$ の主係数、最高次数の係数を $a_k$ で表すことにする。
このとき、イデアル $(a_1, \dotsc, a_k, \dotsc) \subset A$ を考えると、$A$ が Noether 環であることから
これは有限生成イデアルである。ある $m \in \N$ が存在して次が成り立つ：

$$
(a_1, \dotsc) = (a_1, \dotsc, a_m).
$$

この主係数から生成したイデアルが $I$ と等しいことを背理法により示す。
もし等しくないならば、次の条件を満たす $f_{m + 1}\in A[X]$ と $a_{m + 1}$ が存在する：

* 任意の $i = 1, \dotsc, m$ に対して $\deg f_{m + 1} \ge f_i.$
* $f_{m + 1}(X)$ の主係数は $a_{m + 1}$ に等しい。
* $a_{m + 1} = \sum_{k = 1}^m u_ka_k$ を満たす $u_1, \dotsc, u_m \in A$ が存在する。

次の多項式 $g(X)$ を考える：

$$
\begin{aligned}
g(X) &\coloneqq \sum_{k = 1}^m u_k f_k(X) X^N \in (f_1, \dotsc, f_m),\\
\text{where } N &\coloneqq \deg f_{m+1} - \deg f_m.
\end{aligned}
$$

$g(X)$ の主係数と次数は $f_{m + 1}(X)$ のそれぞれと等しい。
その差 $g(X) - f_{m + 1}(X)$ はイデアル $(f_1, \dotsc, f_m)$ に**含まれない**。
また、$\deg(g(X) - f_{m + 1}(X)) \lt \deg f_{m + 1}(X)$ が成り立つ。
これは $f_{m + 1}(X)$ のとり方に矛盾する。

背理法により、$(a_1, \dotsc, a_m) = I.$
イデアル $I \subset A[X]$ は任意であるから $A[X]$ は Noether 環であることが示された。
$\blacksquare$

## 複数不定元版

**定理**：Noether 環 $A$ 上の多項式環 $A[X_1, \dotsc, X_n]\;(n \ge 1)$ もまた Noetherian である。

**証明**：数学的帰納法により示す。

$n = 1$ のときは Hilbert の基底定理ににより $A[X_1]$ は Noetherian である。

$A[X_1, \dotsc, X_{n - 1}]$ が Noether 環であると仮定する。
このとき $A[X_1, \dotsc, X_{n}]$ が Noetherian であることを示す。

多項式環の性質から次が成り立つ：

$$
A[X_1, \dotsc, X_n] = A[X_1, \dotsc, X_{n-1}][X_n].
$$

右辺は環 $A[X_1, \dotsc, X_{n-1}]$ を係数とする $X_n$ 上の多項式環の形式になっている。
ゆえに右辺は多項式環であり、再び Hilbert の定理を適用して Noether 環である。
よって $[A_1, \dotsc, X_n]$ もまた Noether 環である。

数学的帰納法により、$n \ge 1$ に対して $A[X_1, \dotsc, X_{n}]$ は Noether 環であることが示された。
$\blacksquare$

## 参考資料

同値な定義およびその証明と、極大条件の細かいところを主に参考にした。

* [Equivalence of Definitions of Noetherian Ring](https://proofwiki.org/wiki/Equivalence_of_Definitions_of_Noetherian_Ring) - ProofWiki
* [Noetherian ring](https://en.wikipedia.org/wiki/Noetherian_ring) - Wikipedia
* [abstract algebra - Why noetherian ring satisfies the maximal condition?](https://math.stackexchange.com/questions/2631016/why-noetherian-ring-satisfies-the-maximal-condition) - Mathematics Stack Exchange

[pid]: {% post_url 2019/12/2019-12-19-pid %}
