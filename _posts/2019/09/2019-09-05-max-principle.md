---
title: 正則関数の最大値の原理に関係する演習問題
mathjax: true
tags: math
---

簡単そうな問題なのにずっと考えている。

**Q.** 関数 $f(z)$ を単純曲線 $C$ に囲まれた領域 $D$ およびその境界 $C$ 上で正則であり、
$D$ において $f^\prime(z) \ne 0$ とする。このとき、$C$ 上の点で $\lvert f(z)\rvert$ は最小値をとる。

**A.** 以下のような答案を考えたのだが、何か穴がありそうな気がする。

----

条件より $f(z)$ は閉集合 $D \cup C$ 上の連続関数である。

今、任意に点 $z_0 \in C$ をとり、この点を始点かつ終点とする、任意の滑らかな閉曲線 $\gamma$ を $D$ に速度がゼロにならぬように描く：

$$
\varphi: {[a, b]} \longrightarrow \gamma,\quad
\varphi(a) = \varphi(b) = z_0 \in C,
\varphi^\prime(t) \ne 0.
$$

すると関数 $g(t) \coloneqq \lvert f(\varphi(t))\rvert$ は閉区間 $I \coloneqq {[a, b]}$ 上で定義された連続関数である。
従って最小値を必ずどこかでとる。ここで条件 $z \in D \implies f^\prime(z) \ne 0$ から、
および $\varphi^\prime(t) \ne 0$ から少なくとも曲線の端点を除いては
$g^\prime(t) \ne 0$ が成り立つ：
つまり、$g$ は単調関数である：最小値は開区間 ${(a, b)}$ ではとらないことが示された。
これは $D$ 内部で最小値をとらないことを意味する。

$z_0 \in D$ および $\gamma \subset D$ は任意であるから、結局 $D$ で $g$ は最小値をとらない：
$C$ 上の点で最小値をとる必要がある。（終）

----

上の言い分なら「最小」を「最大」に置き換えても成り立つが、そうなると Cauchy の積分公式による教科書の「最大値の原理」の証明は何なのだという話になる。
