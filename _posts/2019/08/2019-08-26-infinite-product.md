---
title: 『新訂解析学』学習ノート Part 8
tags: math
---

熊原啓作著『新訂解析学』の学習ノート第八回。

# 無限乗積

微分積分で習ったから複素数にしても大丈夫かと思いきや、応用が難しい。

## 無限乗積

実数の微分積分で学んだ記述は飛ばす。

* **Th 10.1** 複素数列 $\lbrace\alpha_n\rbrace$ がゼロを含まないとする。このとき

  $\displaystyle \prod^\infty \alpha_n$ が収束する $\displaystyle \iff \lim_{m < n \atop m, n \to \infty} \alpha_{m+1}\dotsm\alpha_n = 1.$

* **C 10.1**

  $\displaystyle \prod^\infty \alpha_n$ が収束する $\displaystyle \implies \lim_{n\to\infty} \alpha_n = 1.$

以下、$\displaystyle \prod^\infty(1 + a_n),\;\lim_{n\to\infty}a_n = 0$ の形の無限乗積を取り扱う。

* **Th 10.2** $a_n \ge 0$ のとき

  $\displaystyle \prod^\infty(1 + a_n)$ が収束する。
  $\displaystyle \iff \sum^\infty a_n$ が収束する。

* **E 10.1**

  $$\prod^\infty_{n=1} \left(1 - \frac{1}{n^2}\right) < \infty.$$

* 無限乗積の**絶対収束**とは、$\prod(1 + \lvert a_n \rvert)$ が収束することをいう。
* **Th 10.3** 順序交換

  $\prod(1 + a_n)$ が絶対収束する $\implies$ 項の順序を任意に入れ替えても同じ値に収束する

  * コメント：証明は実数のときと同じで、添字が多くて目に疲れるものなので省略。
* **各点収束**、**一様収束**、**広義一様収束**を複素関数列 $\lbrace f_n(z) \rbrace$ の
  無限乗積 $\prod f_n(z)$ について、部分積 $\displaystyle p_n(z) := \prod^n(1 + f_k(z))$ を用いて定義する。
  * 部分和が集合 $E \subset \Complex$ で関数 $p(z)$ に～収束するとき、それぞれ $E$ で～収束するという。
* **Th 10.4** 級数と無限乗積の関係？
  * $D$ を領域とする。
  * 関数列 $\lbrace f_n(z) \rbrace$ を $D$ 上の正則関数列とする。
  * 級数 $\sum \lvert f_n(z)\rvert$ は $D$ 上有界な和に一様収束するとする。

  このとき次が成り立つ：
  * 無限乗積 $\prod(1 + f_n(z))$ は $D$ 上の正則関数に一様絶対収束する。
  * その関数の零点は $1 + f_n(z)$ のある零点である。

  証明：
  絶対収束性は **Th 10.2** より成り立つ。

  仮定より

  $$
  \forall z(z \in D \implies \exists M
  \left(M > 0 \land \sum^\infty \lvert f_n(z) \rvert \le M\right).
  $$

  仮定の級数の極限を $p(z)$ とおくと：

  $$
  \begin{aligned}
      \lvert p(z)\rvert
      &= \left\lvert \prod^n_k(1 + f_k(z))\right\rvert\\
      &\le \prod^n_k(1 + \lvert f_k(z)\rvert)\\
      &\le \mathrm{e}^{\sum^n \lvert f_k(z)\rvert}\\
      &\le e^M.
  \end{aligned}
  $$

  * コメント：$\forall x(x \ge 0 \implies 1 + x \le \mathrm{e}^x)$ による。

  $p_n(z)$ をうまく変形して三角不等式を駆使する：

  $$
  \begin{aligned}
      p_n(z) &= p_1(z) + \sum_{k = 2}^n (p_k(z) - p_{k-1}(z))\\
      &= p_1(z) + \sum_{k = 2}^np_{k - 1}(z)f_k(z).
      \\
      \therefore m < n \implies\\
      \lvert p_n(z) - p_m(z) \rvert
      &\le \sum_{m + 1}^n \lvert p_{k-1}(z)\rvert \lvert f_k(z) \rvert\\
      &\le \mathrm{e}^M \sum_{m+1}^n \lvert f_k(z)\rvert.
  \end{aligned}
  $$

  ここで $m, n \to \infty$ とすると右辺はゼロに一様収束する。
  ゆえに $\lbrace p_n(z)\rbrace$ は $D$ 上一様収束する。

  必然的に $p(z) = \prod(1 + f_k(z))$ の零点は、ある $1 + f_k(z)$ の零点である。
* **Th 10.5** **対数微分**
  * $D$ を有界領域、
  * 関数列 $\lbrace f_n(z) \rbrace$ は $D$ で正則で、
  * 級数 $\sum \lvert f_n(z) \rvert$ は $D$ で一様収束し、その和は有界であるとする。

  このとき $p(z) := \prod(1 + f_n(z))$ が $D$ に零点をもたない $\implies$

  $$
  \frac{p^\prime(z)}{p(z)} = \sum^\infty\frac{f_n^\prime(z)}{1 + f_n(z)}.
  $$

  かつ $D$ 上広義一様収束である。

  証明：

  仮定より $f_n(z) \to 0$ （一様収束）である。ゆえに

  $$
  \exists N(N \in \N \land \forall n \forall z(n \ge N \land z \in D \implies 1 + f_n(z) \ne 0)).
  $$

  $n > N$ に対して関数列 $q_n(z)$ を次のようにおく：

  $$
  q_n(z) = \prod_{k = N}^n{1 + f_k(z)}.
  $$

  すると次を満たす $q(z)$ が存在する：

  * $D$ 上 $q_n(z) \to q(z)$（一様収束）
  * $q(z)$ は $D$ 上正則

  **Th 10.4** より $q(z) \ne 0$ がいえる。$q_n^\prime(z) \to q^\prime(z).$

  以上より有界閉集合 $K \subset D$ に対して：

  $$
  \forall z\left(z \in K \implies\\
  \begin{aligned}
  \frac{q^\prime(z)}{q(z)}
  &= \lim_{n\to\infty}\frac{q_n^\prime(z)}{q_n(z)}\\
  &= \lim_{n \to \infty}\sum_{k = N}^n \frac{f^\prime_k(z)}{1 + f_k(z)}\\
  &= \sum_{k = N}^\infty\frac{f^\prime_k(z)}{1 + f_k(z)}.
  \end{aligned}
  \right)
  $$

  これは一様収束である。

  $p(z) = (1 + f_1(z))\dotsm(1 + f_{N-1}(z))q(z)$ より結論のことがすべていえる。
* **E 10.2** $\sin$ の積公式

  $$
  \sin\pi z = \pi z \prod_{n = 1}^\infty \left(1 - \frac{z^2}{n^2}\right).
  $$

  $\sum\dfrac{1}{n^2}$ が収束するので右辺は $\Complex$ 上広義一様収束し、
  極限は正則関数であり、$n \in \Z$ を 1 位の零点にもつ。

  右辺を $F(z)$ とおく。**Th 10.5** より $\Complex\setminus\Z$ において次の等式が成り立つ：

  $$
  \frac{F^\prime(z)}{F(z)} = \frac{1}{z} + \sum_{n = 1}^\infty \frac{2z}{z^2 - n^2}.
  $$

  * コメント：$f_n(z) = -z^2/n^2$ とおくと $f_n^\prime(z) = -2z/n^2$ で

    $$
    \frac{f_n^\prime}{1 + f_n} = \frac{-2z/n^2}{1 - z^2/n^2}.
    $$

    $$
    \begin{aligned}
    \frac{(F(z)/\pi z)^\prime}{F(z)/\pi z}
    &= \frac{\pi z (F(z)/\pi z)^\prime}{F(z)}\\
    &= \frac{F^\prime - F/Z}{F}\\
    &= \frac{F^\prime}{F} - \frac{1}{z}.
    \end{aligned}
    $$

  **E 8.4** によると級数 $\displaystyle \sum_{n = 1}^\infty \frac{2z}{z^2 - n^2}$ は
  $\pi \cot \pi z$ に等しい。

  $$
  \pi \cot \pi z = \frac{\pi\cos\pi z}{\sin \pi z} = \frac{(\sin \pi z)^\prime}{\sin \pi z}
  $$

  なので、$G(z) = \sin \pi z$ とおくと $\Complex\setminus\Z$ 上

  $$
  \begin{aligned}
  \left(\frac{F}{G}\right)^\prime = \frac{F}{G}\left(\frac{F^\prime}{F} - \frac{G^\prime}{G}\right) = 0.\\
  \therefore \exists C(C \in \Complex \land F(z) = C\sin \pi z).
  \end{aligned}
  $$

  $C = 1$ だと思うが？

## $\varGamma$ 関数

実数を変数とするガンマ関数：

$$
\varGamma(x) = \int_0^\infty\!\mathrm{e}^{-t}t^{x - 1}\,\mathrm dt,\quad x > 0
$$

を拡張して複素数を変数とする関数を考える。

$$
\varGamma(z) = \int_0^\infty\!\mathrm{e}^{-t}t^{z - 1}\,\mathrm dt,\quad z \in \Complex.
$$

* $\varGamma(z)$ は $\Re z > 0$ で広義一様収束かつ正則関数。
* 実数では次が成り立つのだが、これが複素数でも通じるか $p_n(z) := 1/\varGamma(z)$ について考えていく。

  $$
  \varGamma(x) = \lim_{n\to\infty}\frac{n^x n!}{x(x + 1)\dotsm(x + n)}.
  $$

$$
\begin{aligned}
p_n(z) &= z(1 + z)\left(1 + \frac{z}{2}\right)\dotsm\left(1 + \frac{z}{n}\right)\frac{1}{n^z}\\
&= z \mathrm{e}^{z\left(1 + 1/2 + \dotsb + 1/n - \log n\right)}\prod_{k=1}^n\left(1 + \frac{z}{k}\right)\mathrm{e}^{-z/k}.
\end{aligned}
$$

* 最初の $\mathrm{e}$ の指数は $z\gamma$ に収束する。$\gamma$ はEuler の定数である。
* 無限乗積の部分は収束する。
  * この乗積の一般項を $1 + f_n(z)$ とおくと：

    $$
    \lvert f_n(z) \rvert = \left\lvert \left(1 + \frac{z}{n}\right)\mathrm{e}^{-z/n} - 1\right\rvert
    \le R^2 \mathrm{e}^R \frac{1}{n^2} \to 0 \quad(n \to \infty).
    $$

  * **Th 10.4** より広義一様収束。$p(z) := \lim p_n(z)$ とするとこれは $\Complex$ 上正則であり、
    $z = 0, 1, 2, \dotsc$ は 1 位の零点。

    ゆえに $1/p(z)$ は $z = 0, 1, 2, \dotsc$ を 1 位の極にもつ有理型関数であり、
    $z = x > 0$ 上 $\varGamma(x)$ と等しい。ということは、一致の定理より
    $\Re z > 0$ 上 $\varGamma(z) = \varGamma(x)$ (Gauss).

  $$
  \therefore \varGamma(z) = \lim_{n\to\infty}\frac{n^z n!}{z(z + 1)\dotsm(z + n)},\quad z \in
  \{z\,|\, z \in \Complex \land \Re z > 0\}.
  $$

* **Weierstrass の公式**

  $$
  \frac{1}{\varGamma(z)} = z \mathrm{e}^{\gamma z} \prod_{n = 1}^\infty \left(1 + \frac{z}{n}\right)\mathrm{e}^{-\frac{z}{n}}.
  $$

* $\operatorname{Res}(\varGamma, -n) = \dfrac{(-1)^n}{n!}.$
* **Euler の反転公式**：$\varGamma(z)\varGamma(1 - z) = \dfrac{\pi}{\sin \pi z}.$
* $\varGamma$ 関数に対数微分を適用するといろいろなことがわかる。

  $$
  \def\dp{ {\prime\prime} }
  \def\gg{ \varGamma(z)\varGamma\left(z + \frac{1}{2}\right) }
  \begin{aligned}
  \gamma &= -\lim_{z \to 0} \left(\frac{\varGamma^{\;\prime}(z)}{\varGamma(z)} + \frac{1}{z}\right).\\
  (\log\varGamma(z))^\dp &= \sum_{n = 1}^\infty\frac{1}{(z + n)^2}.\\
  \gg &= \sqrt{\pi}2^{1 - 2z}\varGamma(2z),\quad\text{(Legendre)}\\
      \because \left(\gg\right)^\dp &= (\log\varGamma(2z))^\dp.\\

  \sqrt{\pi} &= \lim_{n \to \infty}\frac{2^{2n}(n!)^2}{(2n)!},\quad\text{(Wallis)}
  \end{aligned}
  $$

  最後の公式は Legendre の公式で $z$ を $z/2$ に置き換えて Gauss を適用して $z = 1$ とすることで得られる。

TODO: Review once.

## Riemann の $\zeta$ 関数

$$
\zeta\left(s\right) := 1 + \frac{1}{2^s} + \frac{1}{3^s} + \dotsb + \frac{1}{n^s} + \dotsb = \sum_{n = 1}^\infty\frac{1}{n^s}.
$$

以下 $s := \sigma + i\tau$ とおく。

* $\Re s = \sigma > 1$ において広義一様収束する。
* この級数から分母が素数の $s$ 乗になっている項だけピックアップしたものを考える。これも広義一様収束する。
  **Th 10.4** より $F\left(s\right) := \prod 1/(1 - p_n^{-s})$ は $\Re s = \sigma > 1$ 上広義一様収束かつ正則。
* このとき一致の定理と素因数分解の一意性定理から $\Re s > 1$ 上 $F\left(s\right) = \zeta\left(s\right).$
  * $\Re s > 1$ の場合

    $$
    \zeta\left(s\right) = \frac{1}{\varGamma\left(s\right)}\int_0^\infty\! \frac{u^{s-1}}{\mathrm{e}^u - 1}\,\mathrm du.
    $$

    $\zeta\left(s\right)$ は $\Complex$ 上に有理型関数に解析接続する。
    * $s = 1$ に 1 位の極を持つ：$\operatorname{Res}(\zeta, 1) = 1.$
    * $s = -2, -4, -6, \dotsc$ に 1 位の零点を持つ。
  * $\Re s = \sigma = 0$ の場合

    $$
    n^{-s}\varGamma\left(\frac{s}{2}\right)\pi^{-s/2} = \int_0^\infty\! \mathrm{e}^{-n^2\pi x}x^{s/2 - 1}\,\mathrm dx.
    $$

    和をとって

    $$
    \begin{aligned}
        \zeta\left(s\right)\varGamma\left(\frac{s}{2}\right)\pi^{-s/2}
        &= \int_0^\infty\! \left(\sum_{n=1}^\infty \mathrm{e}^{-n^2\pi x}\right)x^{s/2 - 1}\,\mathrm dx.\\

        &= \zeta(1 - s)\varGamma\left(\frac{1 - s}{2}\right)\pi^{-(1 - s)/2}.
    \end{aligned}
    $$

    Gauss の相補公式より次のように変形できる。
    これにより $\Re s < 0$ の零点は $\varGamma\left(s\right)\cos\dfrac{\pi s}{2}$ のそれだけである（自明な零点）。

    $$
    \zeta(1 - s) = 2^{1 - s}\pi^{-s}\varGamma\left(s\right) \cos\frac{\pi s}{2} \cdot \zeta\left(s\right).
    $$

    Riemann によると自明でない零点は直線 $\Re s = 1/2$ 上にあるらしい。

----

* 第 11 章 一階常微分方程式
* 第 12 章 線形常微分方程式

は別で習ったからスキップして、次回は第 13 章から再開する。
