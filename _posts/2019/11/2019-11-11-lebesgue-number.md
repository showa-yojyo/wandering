---
title: Lebesgue の被覆定理学習ノート
tags: math
---

位相空間論入門で出てくる Lebesgue の被覆定理を習うためのエントリー。

# 主張

二通りの主張が手許にあるので比較したい。以下、

* $(X, d_X)$ を距離空間、
* $\lbrace U_\lambda \,\mid\, \lambda \in \Lambda\rbrace$ を $X$ の開被覆

と仮定する。

## 主張 1

$(X, d_X)$ をコンパクトとする。

このとき、$\delta \gt 0$ が存在して、任意の $A \subset X$
について次が成り立つ：直径

$$
d(A) \coloneqq \sup \{d_X(x, x^\prime)\,|\,x, x^{\prime} \in A\}
$$

が $\delta$ より小ならば、ある $\lambda \in \Lambda$ があって、$A \subset U_\lambda$
となる。

## 主張 2

$(X, d_X)$ を点列コンパクトとする。

このとき、$\delta \gt 0$ が存在して、任意の点 $x \in X$ に対して次が成り立つ：
ある $\lambda \in \Lambda$ があって、$B(x, \delta) \subset U_\lambda$ となる。

# 証明

距離空間では点列コンパクト集合とコンパクト集合は同じだ。
最初の証明ではその事実を利用するが、二番目の主張では点列コンパクトの性質を活用した証明をする。

## 主張 1 の証明

$\delta$ の決定問題として証明する。

$x \in X$ に対してそれを含む開被覆のメンバーが存在するので、それを $U_{\lambda(x)}$ と記す。

$U_\lambda$ は開集合であるから、ある $\delta(x) \gt 0$ が存在して $B(x, \delta(x)) \subset U_{\lambda(x)}$ を満たす。

ここで $x$ を空間全体にまんべんなく動かして得られる開被覆 $\lbrace B(x, \delta(x)/2) \,\mid\, x \in X \rbrace$ を考える。

コンパクト空間であるという仮定から、この中の有限個、$r$ 個とする、のメンバーにより空間全体が被覆されている。
開近傍に対応する点を $x_i$ のように書くと：

$$
X = \bigcup_{i = 1}^rB(x_i, \delta(x_i)/2).
$$

ここで $\delta \gt 0$ を次で定義する：

$$
\delta \coloneqq \min \!\left\{\left. \frac{\delta(x_i)}{2} \right| \left. i \in 1..r \right.\right\}\!.
$$

以下、$A \subset X$ が主張の仮定を満たすときに、主張の結論が成り立つことを示す。

直径と $\delta$ の大小関係により $\forall a(a \in A \implies A \subset B(a, \delta)).$

このとき
* ある $i \in 1..r$ が存在して $a \in B(x_i, \delta(x_i)/2).$
* $d_X(a, x_i) \lt \delta(x_i)/2.$

したがって任意の $x \in A$ に対して

$$
\begin{aligned}
d_X(x, x_i) &\le d_X(x, a) + d_X(a, x_i) \\
&\lt \delta + \delta(x_i)/2\\
&\le \delta(x_i).\\
\therefore x &\in B(x_i, \delta(x_i)) \subset U_{\lambda(x_i)}.\\
\therefore A &\subset U_{\lambda(x_i)}.
\end{aligned}
$$

最後の包含関係の右辺は仮定の開被覆のメンバーであり、$x$ に依存しない。

## 主張 2 の証明

背理法により証明する。結論を否定して矛盾を導く。

TBW

# 参考資料

* 石川剛郎著『位相のあたま』(p. 99)
* [Lebesgue number lemma](https://ncatlab.org/nlab/show/Lebesgue+number+lemma): in nLab
