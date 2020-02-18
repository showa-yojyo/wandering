---
title: Galois cohomology 学習ノート
tags: math
---

Hilbert の定理 90 およびその応用の理解を目標とする学習ノート。

## Galois cohomology

以前多様体上の微分形式を習ったときに少しかじった群の cohomology についてまとめておく。

$G$ と $N$ をそれぞれ群、Abel 群とする。
$G$ が $N$ に左から作用しているとする。

**定義 (cochain)**: 次の集合 $C^n(G, N)$ を群 $G$ の Abel 群 $N$ に関する
**$n$-cochain** という：

$$
C^n(G, N) \coloneqq \{ f\colon G^n \longrightarrow N\}.
$$

ただし $C^0(G, N) = N$ とする（定数関数のようなもの全部と思っていい）。

----

準同型写像 $\delta^n\colon C^n(G, N) \longrightarrow C^{n + 1}(G, N)$ を次で定義する：

$$
\begin{aligned}
(\delta^nf)(\sigma_1, \dotsc, \sigma_{n + 1})
&\coloneqq \sigma_1f(\sigma_2, \dotsc, \sigma_{n + 1})\\
&\qquad+ \sum_{i = 1}^n(-1)^if(\sigma_1, \dotsc, \sigma_{i-1}\sigma_{i+1}, \dotsc, \sigma_n)\\
&\qquad+ (-1)^{n+1}f(\sigma_1, \dotsc, \sigma_n).
\end{aligned}
$$

* この準同型写像は $n$ 変数関数を $n + 1$ 変数関数へ写す。
* 右辺の初項の $f$ の引数には $\sigma_1$ がない。
* シグマ各項の $f$ の引数の $\sigma_{i-1}\sigma_{i+1}$ に注意。
* 右辺の末項の $f$ の引数には $\sigma_{n+1}$ がない。

**例（低次数）**：$x \in N,$ $\rho, \sigma, \tau \in G$ とする。

$$
\begin{aligned}
(\delta^0x)(\sigma) &= \sigma x - x.\\
(\delta^1f)(\sigma, \tau)
&= \sigma f(\tau) - f(\sigma\tau) + f(\sigma).\\
(\delta^2f)(\rho, \sigma, \tau)
&= \rho f(\sigma, \tau) + -f(\rho\sigma, \tau) + f(\rho, \sigma\tau) - f(\rho, \sigma)
\end{aligned}
$$

**補題（境界の境界はゼロ）**： $n \in \N$ に対して次が成り立つ：

$$
\delta^{n+1}\circ\delta^n = 0.
$$

**検討**：直接計算するとある。数学的帰納法でコード量を減らせないだろうか。

**証明**：後回し。

----

ここまでのことから次の複体を得る：

$$
\def\a#1{ \overset{\delta^{#1}}{\longrightarrow} }
\begin{aligned}
0 \a{-1} C^0 \a{0} \cdots \a{n-2} C^{n-1} \a{n-1} C^n \a{n} C^{n+1} \a{n+1} \cdots
\end{aligned}
$$

$\operatorname{im}{\delta^{n - 1}} \subset \ker\delta^{n}$ が成り立つ。

----

**定義 (cocycle, coboundary, cohomology)**: 上述の
$G, N, \delta$ に対して次のように集合を定義する：

$$
\begin{aligned}
Z^n(G, N) &\coloneqq \ker\delta^n & \subset C^n(G, N).\\
B^n(G, N) &\coloneqq \operatorname{im}\delta^{n-1} & \subset C^n(G, N).\\
H^n(G, N) &\coloneqq Z^n(G, N)/B^n(G, N).
\end{aligned}
$$

* $Z^n(G, N)$ の元を $n$-cocycle という。
* $B^n(G, N)$ の元を $n$-coboudnary という。
* $H^n(G, N)$ を第 $n$-cohomology 群という。

**補題 ($H^0 = Z^0$)**：

$$
\begin{aligned}
H^0(G, N) = Z^0(G, N) &= N^G\\
&\coloneqq \{x \in N\,|\,\forall \sigma \in G(\sigma x = x)\}.
\end{aligned}
$$

**検討**：$n = 0$ のときの考察は少し混乱する。写像というより値を扱う感じだ。

**証明**：

$$
\begin{aligned}
x \in Z^0(G, N)
&\iff x \in C^0(G, N) \land \delta\sigma = 0\\
&\iff x \in N \land \sigma x - x = 0\\
&\iff x \in N^G.
\quad\blacksquare
\end{aligned}
$$

**補題（$f \in Z^1$ の条件）**：

$$
f \in Z^1(G, N) \iff f(\sigma\tau) = f(\sigma) + \sigma f(\tau).
$$

とくに $\forall \sigma \in G \forall x \in N(\sigma(x) = x)$ であるとき

$$
f \in Z^1(G, N) \iff f \in \operatorname{Hom}(G, N).
$$

**証明**：前半は先述の例で示されている。$\Box$

後半は前半と作用の自明性から：

$$
\begin{aligned}
f \in Z^1(G, N)
&\iff \forall \sigma \in G \forall \tau \in G(f(\sigma\tau) = f(\sigma) + \sigma f(\tau))\\
&\iff \forall \sigma \in G \forall \tau \in G(f(\sigma\tau) = f(\sigma) + f(\tau))\\
&\iff f \in \operatorname{Hom}(G, N).
\quad\blacksquare
\end{aligned}
$$

----

ここからが本節の主題となる。

**定義 (Galois cohomology)**: $L/K$ を Galois 拡大とする。
このとき $G \coloneqq \operatorname{Gal}(L/K)$ 上の加群に関する cohomology 群を
**Galois cohomology** という。

乗法群 $L^\times$ への $G$ の作用を考える。

**命題（$H^0$ は基礎体の乗法群に等しい）**：

$$
H^0(G, L^\times) = K^\times.
$$

**証明**：Galois の基本定理から $K^G = L.$ 両辺から $0$ を取り去れば $(K^\times)^G = L^\times.$
ここに $H^0 = Z^0$ 補題を適用して

$$
H^0(G, L^\times) = (L^\times)^G
= ((K^\times)^G)^G = (K^\times)^G.
\quad\blacksquare
$$

----

**定理 (Hilbert's Theorem 90)**: $H^1(G, L^\times) = 0.$

**検討**：低次数の例と先ほどの補題を使うが、乗法群なので群演算の記号としては $+$ を使わない。

あと本書では $\alpha^\sigma$ 記法を採用しているが、その合理性が今わかった。

**証明**：$C^1(G, L^\times) \subset B^1(G, L^\times)$ を示せば十分であるのでそうする。

ある $\alpha \in L$ をとる。$f \in C^1(G, L^\times)$ に対し次が成り立つ：

$$
f \in Z^1(G, L^\times) \iff
\forall \sigma \in G \forall \tau \in G(f(\sigma)\sigma(f(\tau)) = f(\sigma\tau)).
$$

したがって

$$
f(\sigma)\sigma\!\!\left(\sum_\tau f(\tau)\tau(\alpha)\right)
= \sum_\tau (f(\sigma\tau) \cdot \sigma\tau(\alpha))
= \sum_\sigma f(\sigma)\sigma(\alpha).
$$

[Dedekind の補題][Dedekind]よりある $\alpha \in L^\times$ が存在して次を満たす：

$$
\sum_\sigma f(\sigma)\sigma(\alpha) \ne 0.
$$

この左辺を $\beta$ とおく。このとき例（低次数）で示したように次が成り立つ：

$$
\def\p{ (G, L^\times) }
\begin{aligned}
&f(\sigma) = \frac{\beta}{\sigma(\beta)} = (\delta^0\beta^{-1})(\sigma).\\
\therefore\quad& \delta^0\colon\beta^{-1} \longmapsto f.\\
\therefore\quad& f \in B^1(G, L^\times).\\
\end{aligned}
$$

$f$ は任意であったから $\def\p{ (G, L^\times) }C^1\p \subset B^1\p$
であり、したがって

$$
\def\p{ (G, L^\times) }
H^1\p = Z^1\p/B^1\p = 0
$$

が示された。
$\blacksquare$

----

Hilbert の定理 90 から系が大量に得られる。

**系**：$G \coloneqq \operatorname{Gal}(L/K)$ の指標を $\chi\colon G \longrightarrow K^\times$ とする。

このとき任意の $\sigma \in G$ に対してある $\beta \in L^\times$ が存在して
$\chi(\sigma) = \beta/\sigma(\beta)$ を満たす。

**証明**：仮定を言い換えると $\chi \in \operatorname{Hom}(G, L^\times).$

$$
\begin{aligned}
(\delta^1\chi)(\sigma, \tau) &= \sigma\chi(\tau)\chi(\sigma\tau)^{-1}\chi(\sigma)\\
&= \sigma\chi(\tau)\chi(\tau)^{-1}\chi(\sigma)^{-1}\chi(\sigma)\\
&= \sigma\chi(\tau)\chi(\tau^{-1})\\
&= \sigma(1_K) = 1_L.\\
\therefore \operatorname{Hom}(G, L^\times) &\subset Z^1(G, L^\times).
\end{aligned}
$$

あとは Hilbert の定理 90 の証明の途中に合流するから、

$$
\def\p{ (G, L^\times) }
\begin{aligned}
\chi(\sigma) = \frac{\beta}{\sigma(\beta)} = (\delta^0\beta^{-1})(\sigma).\\
\end{aligned}
$$

を満たす $\beta \in L^\times$ が存在することが示された。
$\blacksquare$

**系**： $L/K$ を巡回拡大とし、その Galois 群の生成元を $\sigma$ とする。

このとき $\alpha \in L$ が $\operatorname{N}_{L/K}\alpha = 1$ を満たすならば、ある
$\beta \in L$ が存在して $\alpha = \beta/\sigma(\beta)$ を満たす。

**検討**：$Z^1$ の元を一つ構成する。$n \coloneqq \lvert G\rvert$ とすると

$$
\operatorname{N}_{L/K}\alpha = 1
\iff \alpha\sigma(\alpha)\dotsm\sigma^{n-1}(\alpha) = 1.
$$

**証明**：$f \in C^1(G, L^\times)$ を次で定義する：

$$
f(\sigma) =
\begin{cases}
1, & \sigma = 1_G,\\
\alpha\sigma(\alpha)\dotsm\sigma^{i-1}(\alpha), & \sigma \ne 1_G.
\end{cases}
$$

これが $f \in Z^1(G, L^\times)$ を満たすことをまず示す。

$$
\def\expand#1{ \alpha\sigma(\alpha)\dotsm\sigma^{#1 - 1}(\alpha)}
\begin{aligned}
f(\sigma^i)\sigma^i(f(\sigma^j))
&= \expand{i}\sigma^i(\expand{j})\\
&= \expand{i}\sigma^i(\alpha)\sigma^{i+1}(\alpha)\dotsm\sigma^{i + j - 1}(\alpha)\\
&= \expand{i + j}.
\end{aligned}
$$

$i + j \le n - 1$ のときは $f(\sigma^{i + j})$ に等しい。

$i + j \ge n$ のときは $k \coloneqq i + j - n$ として

$$
\def\expand#1{ \alpha\sigma(\alpha)\dotsm\sigma^{#1 - 1}(\alpha)}
\expand{n} = \operatorname{N}\alpha = 1
$$

を利用して

$$
\def\expand#1{ \alpha\sigma(\alpha)\dotsm\sigma^{#1 - 1}(\alpha)}
\begin{aligned}
f(\sigma^i)\sigma^i(f(\sigma^j))
&= \expand{n}\expand{k}\\
&= f(\sigma^k).
\end{aligned}
$$

したがって、いずれの場合においても $f(\sigma^i)\sigma^if(\sigma^j) = f(\sigma^i)f(\sigma^j).$
$f \in Z^1$ の条件から $f \in Z^1(G, L^\times).$

Hilbert の定理 90 から $f \in Z^1(G, L^\times)$ に対して
$\beta \in L^\times \subset L$ が存在して次を満たす：

$$
f(\sigma^i) = \frac{\beta}{\sigma^i(\beta)}.
$$

とくに $i = 1$ とすれば $\alpha = \beta/\sigma(\beta).$
$\blacksquare$

**系**：有限体の拡大 $\mathbb F_{q^n}/\mathbb F_q$ のノルム

$$
\operatorname{N}_{\mathbb F_{q^n}/\mathbb F_q}\colon
\mathbb F_{q^n}^\times \longrightarrow \mathbb F_q^\times
$$

は乗法群の全射準同型写像である。

**証明**：$\langle \sigma \rangle \coloneqq\operatorname{Gal}(\mathbb F_{q^n}/\mathbb F_q)$
とする。

$$
0 \longrightarrow (1 - \sigma)\left(\mathbb F_{q^n}^\times\right)
\longrightarrow \mathbb F_{q^n}^\times
\longrightarrow \operatorname{N}\left(\mathbb F_{q^n}^\times\right)
\longrightarrow 0
$$

は完全系列である（確かめる）。したがって

$$
\tag*{$\spadesuit1$}
\lvert \mathbb F_{q^n}^\times \rvert
= \lvert (1 - \sigma)\mathbb F_{q^n}^\times \rvert
\lvert \operatorname{N}\left(\mathbb F_{q^n}^\times\right) \rvert.
$$

一方、$G(\mathbb F_{q^n}^\times) = \mathbb F_{q}^\times$ だから（確かめる）

$$
0
\longrightarrow \mathbb F_{q}^\times
\longrightarrow \mathbb F_{q^n}^\times
\longrightarrow (1 - \sigma)\mathbb F_{q^n}^\times
\longrightarrow 0
$$

もまた完全系列である。したがって

$$
\tag*{$\spadesuit2$}
\lvert \mathbb F_{q^n}^\times \rvert
= \lvert \mathbb F_{q}^\times \rvert
\lvert (1 - \sigma)\mathbb F_{q^n}^\times\rvert.
$$

$\spadesuit1, \spadesuit2$ から

$$
\begin{aligned}
\lvert \operatorname{N}\left(\mathbb F_{q^n}^\times\right) \rvert
&= \lvert \mathbb F_{q}^\times \rvert.\\
\therefore \operatorname{N}\left(\mathbb F_{q^n}^\times\right)
&= \mathbb F_{q}^\times.
\end{aligned}
$$

したがって拡大体のノルムが全射準同型写像であることが示された。
$\blacksquare$

----


## 参考

* 桂利行著『代数学 III 体とガロア理論』
* 雪江明彦著『環と体とガロア理論』

[Dedekind]: {{ site.baseurl }}{% post_url 2020/01/2020-01-25-trace-norm %}
