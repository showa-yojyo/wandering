---
title: Lebesgue の被覆定理学習ノート
tags: math
---

位相空間論入門で出てくる Lebesgue の被覆定理を習うためのエントリー。

## 主張

二通りの主張が手許にあるので比較したい。以下、

* $(X, d_X)$ を距離空間、
* $\lbrace U_\lambda \,\mid\, \lambda \in \Lambda\rbrace$ を $X$ の開被覆

と仮定する。

### 主張 1

$(X, d_X)$ をコンパクトとする。

このとき、$\delta \gt 0$ が存在して、任意の $A \subset X$
について次が成り立つ：直径

$$
d(A) \coloneqq \sup \{d_X(x, x^\prime)\,|\,x, x^{\prime} \in A\}
$$

が $\delta$ より小ならば、ある $\lambda \in \Lambda$ があって、$A \subset U_\lambda$
となる。

### 主張 2

$(X, d_X)$ を点列コンパクトとする。

このとき、$\delta \gt 0$ が存在して、任意の点 $x \in X$ に対して次が成り立つ：
ある $\lambda \in \Lambda$ があって、$B(x, \delta) \subset U_\lambda$ となる。

## 証明

距離空間では点列コンパクト集合とコンパクト集合は同じだ。
最初の証明ではその事実を利用するが、二番目の主張では点列コンパクトの性質を活用した証明をする。

### 主張 1 の証明

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
$\blacksquare$

### 主張 2 の証明

背理法により証明する。結論を否定して矛盾を導く。

主張の仮定をきちんと表現するとこうなる：

$$
\exists\delta(\delta \gt 0(\forall x
    (x \in X \exists\lambda(\lambda \in \Lambda(
        B(x, \delta) \subset U_\lambda))))).
$$

そして結論を否定するということは：

$$
\forall\delta(\delta \gt 0(\exists x
    (x \in X \forall\lambda(\lambda \in \Lambda(
        B(x, \delta) \nsubseteq U_\lambda))))).
$$

「各 $n \in \N$ に対して次のような点 $x_n \in X$ が存在する：
どの $\lambda \in \Lambda$ に対しても開近傍 $B\left(x_n, \dfrac{1}{n + 1}\right)$ が $U_\lambda$ に含まれない」
として、以下矛盾を導く。

* コメント：$\delta = 1/(n + 1).$

これらの点 $x_n (n \in \N)$ は点列 $\lbrace x_n \rbrace$ を構成する。
$X$ の点列コンパクト性により、この点列は何らかの点 $x_\infty \in X$ に収束する部分列 $\lbrace x_{n_k}\rbrace$ を含む。
したがって、$\lambda_\infty \in \Lambda$ が存在して $x_\infty \in U_{\lambda_\infty}.$
さらに $U_{\lambda_\infty}$ に対して、開集合の性質により、ある $\varepsilon \gt 0$ が存在して $B(x_\infty, \varepsilon) \subset U_{\lambda_\infty}.$

部分列 $\lbrace x_{n_k}\rbrace$ が収束することから、ある添字 $k \in \N$ を適当に取れば次のようにできる：

$$
\def\eps{ \frac{\varepsilon}{2} }
\frac{1}{n_k + 1} \lt \eps \ \land\ d_X(x_{n_k}, x_\infty) \lt \eps.
$$

これは次を意味する：

$$
B\left(x_{n_k}, \frac{1}{n_k}\right) \subset B(x_\infty, \varepsilon) \subset U_{\lambda_\infty}.
$$

しかしこのことは「どの $\lambda \in \Lambda$ も $B\left(x_{n_k}, \dfrac{1}{n_k}\right) \nsubseteq U_\lambda$」という仮定に矛盾する。
背理法により、主張の結論は真である。
$\blacksquare$

### 主張 1 の証明別バージョン

背理法で証明することを試みる。点列コンパクト性で示したい。

$$
\exists \delta(\delta > 0 \forall A(
    A \subset X (d(A) \lt \delta \implies \exists \lambda(
        \lambda \in \Lambda(A \subset U_\lambda))))).
$$

この結論の否定は：

$$
\forall \delta(\delta > 0 \exists A(
    A \subset X (d(A) \lt \delta \implies \forall \lambda(
        \lambda \in \Lambda(A \nsubseteq U_\lambda))))).
$$

真似っこして $\delta$ としてすべての自然数 $n \in \N$ を考える。
各 $n$ に対して次のような集合 $A_n$ が存在する。

$$
A_n \subset X,\ d(A_n) \lt n \implies \forall \lambda(
        \lambda \in \Lambda(A_n \nsubseteq U_\lambda)).
$$

各集合から一点ずつとってくる：$x_n \in A_n.$

* コメント：自信はないが、これは要選択公理ではないのか。

$X$ の点列コンパクト性から点列 $\lbrace x_n \rbrace$ は収束する部分列 $\lbrace x_{n_k}\rbrace$ を含む。
その極限を $x_\infty \in X$ とおく。それを含む開被覆のメンバーを $U_{\lambda_\infty} \ni x_\infty$ とする。

* コメント：半径・直径の細かい調整が必要だろうが、証明はできる見通しがたったので中断する。

## コメント

* この証明 1 は教科書の丸写しだが、証明 2 のように背理法でも証明することができるだろう。
* $\varepsilon/2$ がよく現れるが、この値は開近傍の半径を意識している。
* 主張 2 の証明では $\delta$ を具体的に構成することなしに済んでいる。
* 主張 2 はもともと「点列コンパクト空間はコンパクト空間である」の証明に用いるためのものだ。

## 参考資料

* 石川剛郎著『位相のあたま』(p. 99)
* [Lebesgue number lemma](https://ncatlab.org/nlab/show/Lebesgue+number+lemma): in nLab
