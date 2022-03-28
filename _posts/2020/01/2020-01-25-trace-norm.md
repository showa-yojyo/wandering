---
title: 拡大体の元に対するトレースとノルム 学習ノート
mathjax: true
tags: math
---

体の同型写像で定義される拡大体の元のトレースおよびノルムについて学習する。

参照：桂利行著『代数学 III 体とガロア理論』

## トレースとノルム

**定義**：$L/K$ を有限次分離拡大とし、$L^{\prime}/K$ を Galois 拡大とする。
$L^{\prime} \supset L$ とする。
$L \longrightarrow L^{\prime}$ であるような中への $K$ 同型写像の集合を
$\lbrace \sigma_1, \dotsc, \sigma_n\rbrace$
とする。

$\alpha \in L$ の**トレース**および**ノルム**を次で定義する：

$$
\begin{aligned}
\operatorname{Tr}_{L/K}\alpha &\coloneqq \sum_{i=1}^n\sigma_i(\alpha).\\
\operatorname{N}_{L/K}\alpha &\coloneqq \prod_{i=1}^n\sigma_i(\alpha).\\
\end{aligned}
$$

コメント：今さらだが上記の言い回しに注意したい。「中への」と明記しないと $L \cong L^{\prime}$ なのかと誤解するおそれがある。

----

**補題**：
$\operatorname{Tr} _ {L/K}\alpha \in K,$
$\operatorname{N} _ {L/K}\alpha \in K.$

**証明**：
任意の $\tau \in \operatorname{Gal}(L^{\prime}/K)$ と $\sigma_i$ に対し、ある $M_i \subset L^{\prime}$ が存在して

* $\sigma_i\colon L \longrightarrow M_i$ が同型写像、
* $\tau\mid_M\colon M \longrightarrow M_i$ が自己同型写像

であるから、写像 $\tau\sigma_i\colon L \longrightarrow M_i$ もまた
$L \longrightarrow L^{\prime}$ であるような中への $K$ 同型写像である。
したがって

$$
\{ \tau\sigma_1, \dotsc, \tau\sigma_n \} = \{ \sigma_1, \dotsc, \sigma_n\}.
$$

したがって、

$$
f_\alpha(X) \coloneqq \prod_{i=1}^n (X - \sigma_i(\alpha))
$$

とおくと、$\tau(f_\alpha(X)) = f_\alpha(X).$
$\tau$ により像が不変であることから $f_\alpha(X) \in K[X]$ であることが示された。

$X^{n - 1}$ の係数および定数項がそれぞれトレースとノルム（の高々符号違い）であるので、
$$\operatorname{Tr}_{L/K}\alpha \in K$$ および
$$\operatorname{N}_{L/K}\alpha$$ であることが示された。
$\blacksquare$

----

**命題（トレースとノルムの性質）**：
体の有限次分離拡大 $L/K$ のトレースおよびノルムには次の性質がある：
$\alpha, \beta \in L$ に対して

$(1)$ $\operatorname{Tr}(\alpha + \beta) = \operatorname{Tr}\alpha + \operatorname{Tr}\beta.$

$(2)$ $\operatorname{N}(\alpha\beta) = (\operatorname{N}\alpha)(\operatorname{N}\beta).$

$(3)$ 拡大体 $L/K$ の中間体 $M$ に対し

$$
\begin{aligned}
\operatorname{Tr}_{L/K}\alpha &= \operatorname{Tr}_{M/K}(\operatorname{Tr}_{L/M}\alpha),\\
\operatorname{N}_{L/K}\alpha &= \operatorname{N}_{M/K}(\operatorname{N}_{L/M}\alpha).
\end{aligned}
$$

**証明**：教科書に証明がまったくないので、以下ゼロから書く。

$(1), (2)$ は体の同型写像の性質から成り立つ。
$\Box$

$(3)$ は等式に整合性があることから示す。
$L/K$ が分離拡大なので、中間体 $M$ に対して $L/M$ は分離拡大である。
Galois 拡大 $L^{\prime}/L$ のとり方 $L^{\prime} \supset L \supset M$ から
$$\operatorname{Gal}(L^{\prime}/M), \operatorname{Tr}_{L/M}, \operatorname{N}_{L/M}$$ は有効。

以前言い忘れたがこの拡大で $M/K$ も分離拡大である。これは分離拡大の定義からそうなる。
$L^{\prime} \supset L \supset M \supset K$ ゆえ
$$\operatorname{Tr}_{M/K}, \operatorname{N}_{M/K}$$ は有効。

$\lbrace \tau_j \rbrace$ を $L \longrightarrow L^{\prime}$ の中への $M$ 同型写像とすると
$\alpha \in L$ に対して

$$
\operatorname{Tr}_{L/M}\alpha = \sum_{j = 1}^n \tau_j(\alpha)\in M.
$$

$\lbrace \sigma_i \rbrace$ を $M \longrightarrow L^{\prime}$ の中への $K$ 同型写像とすると

$$
\begin{aligned}
\operatorname{Tr}_{M/K}(\operatorname{Tr}_{L/M}\alpha)
&= \sum_{i = 1}^m \sigma_i\left(\sum_{j = 1}^n \tau_j(\alpha)\right)\\
&= \sum_{i = 1}^m\sum_{j = 1}^n \sigma_i(\tau_j(\alpha)) \in K.\\
\end{aligned}
$$

Galois の基本定理から $L \longrightarrow L^{\prime}$ の中への $K$ 同型写像の集合は
$\lbrace \sigma_i\tau_j \rbrace$ に等しいので、この等式の右辺は
$$\operatorname{Tr}_{L/K}\alpha$$ に等しいことが示された。

$\operatorname{N}$ についても同様に示される。
$\blacksquare$

----

この補題群がこのあと学ぶ巡回 Kummer 拡大の基本だ。

**補題（半群の準同型写像の線形独立性 - Artin）**：
$K$ と $S$ をそれぞれ体と半群とする。
準同型写像 $\chi_i\colon S \longrightarrow K^\times\;(i = 1, \dotsc, m)$ が存在してこれらは相異なるものとする。

このときある $\alpha_i \in K\;(i = 1, \dotsc, m)$ が存在して任意の $s \in S$ に対して

$$
\tag*{$\spadesuit1$}
\sum_{i=1}^m \alpha_i\chi_i(s) = 0
$$

であるならば $\alpha_1 = \dotsb = \alpha_m = 0.$

**証明**：背理法によって示す。ある $(\alpha_1, \dotsc, \alpha_m) \ne (0, \dotsc, 0)$
が存在して $\spadesuit1$ が成り立つと仮定する。そのようなもののうち $m$ が最小のものを考える。
このとき $\alpha_1 \ne 0, \dotsc, \alpha_m \ne 0$ と仮定できる。

まず $m \ne 1$ である。なぜなら $\alpha_1\chi_1(s) = 0$ ならば
$\alpha_1 = 0$ が必要であり今の仮定に矛盾する。
したがって $m \ge 2$ が必要である。

任意の $t \in S$ に対して $\spadesuit1$ の $s$ の代わりに $st$ を置いた等式を考える。

$$
\tag*{$\spadesuit2$}
\sum_{i=1}^m \alpha_i\chi_i(st) = 0.
$$

$\spadesuit2 - \spadesuit1 \times \chi_m(t)$ を計算すると：

$$
\sum_{i = 1}^{m - 1}\alpha_i\chi_1(s)(\chi_i(t) - \chi_m(t)) = 0.
$$

$i \ne m$ のとき $\chi_i \ne \chi_m$ であるから、ある $t \in S$ が存在して
$\chi_i(t) \ne \chi_m(t)$ をみたす。この $t$ に対して
$\beta_i \coloneqq \alpha_i\chi_1(s)(\chi_i(t) - \chi_m(t))$ とおけば任意の $s \in S$ に対して

$$
\sum_{i = 1}^{m - 1}\beta_i\chi_i(s) = 0.
$$

かつ $\beta \ne 0$ となる。ところがこれは $m$ の最小性に矛盾する。
したがってある $(\alpha_1, \dotsc, \alpha_m) \ne (0, \dotsc, 0)$
が存在して $\spadesuit1$ が成り立つと仮定することはできないことが示された。

したがって $\spadesuit1$ が成り立てば $\forall i(\alpha_i = 0)$ である。
$\blacksquare$

**系 (Dedekind)**：
$L, L^{\prime}$ を体とし、$L$ から $L^{\prime}$ への中への相異なる同型写像
$\sigma_1, \dotsc, \sigma_m$ が存在する。

このとき、任意の $\alpha \in L$ に対して

$$
\sum_{i=1}^m \sigma_i(\alpha)\beta_i = 0
$$

が成り立つならば任意の $i = 1, \dotsc, m$ に対して $\beta_i = 0.$

**証明**：
写像 $\chi_i \coloneqq \sigma_i\mid_{L^\times}$
を定義すれば当然ながら半群 $L^\times$ から体の乗法群 $L^{\prime}{}^\times$ への相異なる準同型写像
$\chi_i\colon L^\times \longrightarrow L^{\prime}{}^\times$ が得られる。

前述の Artin の補題に $\chi_i \coloneqq \sigma_i$ を当てはめればよい。
$\blacksquare$

----

**命題（非退化対称双線形形式）**：
有限次分離拡大 $L/K$ に対して写像 $T\colon L \times L \longrightarrow K$
を次で定義すると、これは非退化かつ対称双線形形式である：

$$
T(\alpha, \beta) \coloneqq \operatorname{Tr}_{L/K}(\alpha\beta).
$$

**証明**：$T(\alpha, \beta) = T(\beta, \alpha)$ が成り立つから $T$ は対称である。

$\lambda, \beta \in L$, $\alpha_1, \alpha_2, \beta_1, \beta_2 \in L$ とするとトレースが線形写像であることから

$$
\begin{aligned}
    T(\lambda\alpha, \mu\beta) &= \lambda\mu T(\alpha, \beta),\\
    T(\alpha_1 + \alpha_2, \beta) &= T(\alpha_1, \beta) + T(\alpha_2, \beta),\\
    T(\alpha, \beta_1, \beta_2) &= T(\alpha, \beta_1) + T(\alpha, \beta_2)\\
\end{aligned}
$$

がすべて成り立つ。したがって $T$ が双線形形式であることが示された。

非退化であることは Dedekind の補題から示される。
$[L : K] = n$ とし、$\beta \in L^\times$ をとる。
$\sigma_1, \dotsc, \sigma_n$ を $L \longrightarrow \overline L$ なる中への $K$ 同型写像とする。

$\alpha \in L$ と $\beta_i \coloneqq \sigma_i(\beta)$ に対して

$$
\begin{aligned}
\operatorname{Tr}_{L/K}(\alpha\beta)
&= \sum_{i = 1}^n\sigma_i(\alpha\beta)\\
&= \sum_{i = 1}^n\sigma_i(\alpha)\sigma_i(\beta)\\
&= \sum_{i = 1}^n\sigma_i(\alpha)\beta_i.
\end{aligned}
$$

Dedekind より $\beta \ne 0$ に対してある $\alpha \in L$ が存在して
$\operatorname{Tr}_{L/K}(\alpha\beta) \ne 0.$
したがって $T$ は退化線形形式ではない。
$\blacksquare$

**系（分離拡大とトレースが零でないことは同値）**：$L/K$ を有限次分離拡大とする。
このとき $\operatorname{Tr}_{L/K}\alpha \ne 0$ をみたす $\alpha \in L$ が存在する。

とくに $\operatorname{Tr}_{L/K}\colon L \longrightarrow K$ は $K$ 全射準同型写像である。

**証明**：前半：非退化対称双線形形式に関する命題により
$$\operatorname{Tr}_{L/K}\alpha = T(\alpha, 1)$$ には
非退化であるから、ある $\alpha \in L$ が存在して $T(\alpha, 1) = \operatorname{Tr}_{L/K}\alpha\ne 0.$

後半：`$\operatorname{Tr}_{L/K}$` が零写像ではないことと $\dim_LL = 1$
より（線形代数の次元公式だったか？）$$\operatorname{im}{\operatorname{Tr}_{L/K}} = K.$$
$\blacksquare$
