---
title: Eisenstein の既約判定法証明 学習ノート
tags: math
---

Eisenstein の既約判定法の証明ノート。書き終わったあとに思ったが、[Gauss の補題][Gauss]も併せてノートにとらないと弱い。

## Eisenstein

**定理**：多項式 $f(X) = a_nX^n + \dotsb + a_0 \in \Z[X]$
と素数 $p$ が次を満たす：

* $(1)\;$ $p$ は $a_0, a_1, \dotsc, a_{n - 1}$ を割り切る。$p$ は $a_n$ を割り切らない。
* $(2)\;$ $p^2$ は $a_0$ を割り切らない。

このとき、$f$ は $\mathbb{Q}[X]$ 上既約である。

**検討**：

* [Gauss の補題][Gauss]は使えるとすると、$\Z[X]$ 上既約であることを示せば十分だ。
* 背理法で示す。

**証明**：$f(X) = g(X)h(X),\ g(X), h(X)\in\Z[X],$ かつ
$f$ も $g$ も定数でない多項式と書けると仮定して矛盾を導く。
$g, h$ を次のように表せるとする：

$$
\begin{aligned}
    g(X) &= b_sX^s + \dotsb + b_0, & b_i \in \Z,\\
    h(X) &= c_tX^t + \dotsb + c_0, & c_i \in \Z,.
\end{aligned}$$

条件を詳細に記すことは省略するが、係数 $b_i, c_i$ は多項式が定数とならない値であると仮定する。
すると $i = 0, 1, \dotsc, n$ に対して次が成り立つ：

$$
a_i = \sum_{j + k = i}b_j c_k.
$$

特に $a_0 = b_0c_0$ であるので、仮定 $(2)$ により、必要ならば $g$ と $h$ を入れ替えることで、
$p \nmid c_0$ が成り立つとしてよい。また仮定 $(1)$ により $p \mid b_0$ が成り立つ。

一方、$a_n = b_s c_t$ と仮定 $(2)$ より $p \nmid a_n.$
したがって $p \nmid b_s.$

「すべての $b_i$ が $p$ で割り切れる」ことがないことが示された。
つまり $p \nmid b_i$ を満たす最小の $0 \lt i \le s$ が存在する。
その $i$ について：

$$
a_i = b_0c_i + b_1c_{i-1} + \dotsb + b_ic_0
$$

（ただし $j > a$ ならば $h_j = 0$ とみなす）を考える。
$i$ の決め方から $k = 0, \dotsc, i - 1$ に対して $p \mid b_k\colon$

$$
\begin{aligned}
    a_i &= b_0c_i + b_1c_{i-1} + \dotsb + b_ic_0\\
    &= p(b_0^{\prime}c_i + b_1^{\prime}c_{i-1} + \dotsc + b_{i-1}^{\prime}c_1) + b_ic_0.
\end{aligned}
$$

また $c_0$ も $b_i$ も $p$ で割り切れないのだから最終項
$b_ic_0$ は $p$ で割り切れない。したがって $p \nmid a_i.$
ところがこれは仮定 $(1)$ と矛盾する。

したがって背理法により、$f(X) = g(X)h(X)$ の形には表せない。すなわち
$f$ は $\Z[X]$ 上既約である。

[Gauss の補題][Gauss]により $f$ は $\mathbb{Q}[X]$ 上でも既約である。
$\blacksquare$

## 参考資料

* ProofWiki
  * [Schönemann-Eisenstein Theorem](https://proofwiki.org/wiki/Sch%C3%B6nemann-Eisenstein_Theorem)

[Gauss]: {% post_url 2019/12/2019-12-10-gauss %}
