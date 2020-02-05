---
title: 『新訂解析学』学習ノート Part 4
tags: math
---

熊原啓作著『新訂解析学』の学習ノート第四回。居眠りしてあまり消化できなかった。

## 正則関数の性質

* 正則関数は $C^\omega$ 級関数である。
* 一致の定理が成り立つ
* 等角写像（次回以降）

### Taylor 級数展開

しばらくの間次を仮定する：

* 集合 $D \subset \Complex$ を領域とする。
* 関数 $f(z)$ を $D$ で定義された正則関数とする。
* **Th 7.1** Taylor 級数展開
  * $z_0$ を $D$ 内の任意の点とする。
  * $R_0 = d(z_0, \partial D)$ とする（最短距離）。

  このとき $f(z)$ は開円盤 $U_{R_0}(z_0)$ において次のようにべき級数に展開可能である：

  $$
  f(z) = \sum_{n = 0}^\infty c_0(z - z_0)^n,\quad
  c_n = \frac{f^{(n)}(z_0)}{n!} = \frac{1}{2\pi i}\int_{\lvert \zeta - z_0 \rvert = R}\!\frac{f(\zeta)}{(\zeta - z)^{n+1}}\,\mathrm d\zeta.
  $$

  証明：

  $\lvert z - z_0 \rvert < R < R_0$ を満たす $R$ をとる。
  $f(z)$ と円 $\lvert z - z_0 \rvert = R$ に対して Cauchy の積分公式を適用すると次の等式が成り立つ：

  $$
  f(z) = \frac{1}{2\pi i}\int_{\lvert \zeta - z_0 \rvert = R}\!\frac{f(\zeta)}{\zeta - z}\,\mathrm d\zeta.
  $$

  右辺を変形していく：

  $$
  \def\C{ {\lvert \zeta - z_0 \rvert = R} }
  \begin{aligned}
      f(z) &= \sum_{k = 1}^{n - 1}\frac{(z - z_0)^k}{2\pi i}\int_\C\!\frac{f(\zeta)}{(\zeta - z)^{k+1}}\,\mathrm d\zeta + \rho_n,\\
      \rho_n &= \frac{(z - z_0)^n}{2\pi i}\int_\C\!\frac{f(\zeta)}{(\zeta - z)(\zeta - z_0)^n}\,\mathrm d\zeta.
  \end{aligned}
  $$

  この式変形には次の関係（等比級数の和の公式を逆に見る）を利用した：

  $$
  \frac{1}{\zeta - z} = \frac{1}{\zeta - z_0}\sum_{k = 0}^{n - 1}\left(\frac{z - z_0}{\zeta - z_0}\right)^k
  + \frac{(z - z_0)^n}{(\zeta - z)(\zeta - z_0)^n}.
  $$

  あとは $\lvert \rho_n \rvert$ を評価して適当に極限を検討する。
  * 積分路上 $\lvert f(z) \rvert \le M$ および
  * $r = \lvert z - z_0 \rvert$

  とおくと：

  $$
  \def\C{ {\lvert \zeta - z_0 \rvert = R} }
  \begin{aligned}
      &\phantom{\le} \left\lvert \frac{(z - z_0)^n}{2\pi i}\int_\C\!\frac{f(\zeta)}{(\zeta - z)(\zeta - z_0)^n}\,\mathrm d\zeta \right\rvert\\
      &\le \frac{r^n}{2\pi} \int_\C\! \left\lvert \frac{f(\zeta)}{(\zeta - z)(\zeta - z_0)^n}\right\rvert\lvert \mathrm d\zeta\rvert\\
      &\le \frac{r^n}{2\pi} \frac{M}{(R - r)R^n}\cdot 2\pi R\\
      &= \frac{MR}{R - r}\left(\frac{r}{R}\right)^n.
  \end{aligned}
  $$

  ここで $n \to \infty$ とすると右辺、すなわち級数の剰余項はゼロに収束する。
* **L 7.1**

  **Th 7.1** と同じ仮定をする。このとき：

  $$
  \forall n(n \in \N \implies f^{(n)}(z_0) = 0)
  \implies
  \forall z(z \in U_R(z_0) \implies f(z) = 0).
  $$

* **Th 7.2 因数定理**
  * これまでと同じ仮定に加え、
  * $f(z_0) = 0 \land f(z) \not\equiv 0$

  とする。このとき次を満たす関数 $\varphi(z)$ が存在する：
  * $\varphi(z)$ は $U_R(z_0)$ で正則である。
  * $\exists m(m \in \Z \land f(z) = (z - z_0)^m\varphi(z) \land \varphi(z_0) \ne 0).$

  証明：

  * $f(z) \not\equiv 0$ であることから $\exists n(n \in \N \land n \ge 1 \land f^{(n)}(z_0) \ne 0).$
  * そのような $n$ の最小のものを $m$ とする。$f(z)$ の Taylor 展開は次数が $m$ の項から始まる。

  $$
  \begin{aligned}
  f(z) &= \sum_{n = m}^\infty \frac{f^{(n)}(z_0)}{n!}(z - z_0)^n\\
  &= (z - z_0)^m \sum_{n = m}^\infty \frac{f^{(n)}(z_0)}{n!}(z - z_0)^{n - m}.
  \end{aligned}
  $$

  * ここでシグマ部分を $\varphi(z)$ とおく。このべき級数も $U_R(z_0)$ で収束する。
    したがって正則であり、

    $$
    \varphi(z_0) = \frac{f^{(m)}(z_0)}{m!} \ne 0.
    $$

* **Th 7.2** のような点 $z_0$ を、$f(z)$ の**位数**が $m$ の**零点**という。
* **Th 7.3 一致の定理**
  * $f, g$ を $D$ で正則な関数であるとする。
  * 点列 $\lbrace z_n \rbrace \subset D$ があり、点 $z_0 \in D$ に収束するとする。

  このとき：

  $$
  \forall n(n \in \N \implies f(z_n) = g(z_n)) \implies
  \forall z(z \in D \implies f(z) = g(z)).
  $$

  証明：

  $h(z) \coloneqq f(z) - g(z)$ とおき、これが恒等的にゼロであることを示す。

  仮定から

  $$
  \exists R \in \R(R > 0 \land U_R(z_0) \subset D).
  $$

  点列の条件 $z_n \to z_0\;(n \to \infty)$ から：

  $$
  \exists N(n \in N \land \forall n(
      n \in N \land n \ge N \implies
      z_n \in U_R(z_0))).
  $$

  以下、背理法を用いて証明する。仮に次が成り立つと仮定して矛盾を導く：

  $$
  \exists z(z \in U_R(z_0) \land h(z) \ne 0).
  $$

  **Th 7.2** より次を満たす $D$ 上の正則関数 $\varphi(z)$ が存在する：

  $$
  \exists m(m \in \N \land h(z) = (z - z_0)^m\varphi(z) \land \varphi(z_0) \ne 0).
  $$

  このとき

  $$
  \forall n(n \ge N \implies 0 = h(z_n) = (z - z_0)^m\varphi(z_n))\\
  \therefore \forall n(n \ge N \implies\varphi(z_n) = 0).
  $$

  $n \to \infty$ として $\varphi(z_0)= 0.$ これは仮定 $\varphi(z_0) \ne 0$ に反する。
  ゆえに

  $$
  \forall z(z \in U_R(z_0) \implies h(z) \equiv 0).
  $$

  次に円盤から $D$ 全域に拡張しても一致が成り立つことを示す。

  まず点 $c \in D$ を一つとって固定する。それから点 $z_0$ と $c$ とを $D$ 内で結ぶ区分的に滑らかな曲線
  $C = z(t),\;t \in {(0, 1)}$ を一つとる。

  * 実数 $t_0$ を次のいずれもが成り立つようにとる：
    * $0 \le t < t_0 \implies h(z(t)) = 0.$
    * $t_0 \le t  \le 1 \implies h(z(t)) \ne 0.$
  * $t_0 > 0.$
  * 単調増加数列 $\lbrace t_n \rbrace$ を次が成り立つようにとる：
    * $t_1 = 0.$
    * $t_n \to t_0\;(n \to \infty)$
  * $z_n \coloneqq z(t_n)$ とおくと $z_n \to z(t_0) \land h(z_0) = 0.$
  * 前半の議論により $z_0$ を中心とするある円盤では $h(z) \equiv 0.$
  * $t_0 < 1$ と仮定すると $t_0$ のとり方（上限性がある）に矛盾するので
    $z(t_0) = c \land h(c) = 0.$ ゆえに $\forall z \in D(h(z) = 0).$
* **Th 7.4 最大値の原理**：
  $\lvert f(z)\rvert$ が点 $z_0 \in D$ で最大値をとるならば、$f(z)$ は定数である。

  証明：

  $D$ が領域であることから $\exists R(R > 0 \land U_R(z_0) \subset D.$

  ここで次を仮定して背理法で証明する：

  $$
  \exists z_1(z_1 \in U_R(z_0) \land \lvert f(z_1) \rvert < \lvert f(z_0) \rvert).
  $$

  ここで $r, \theta_1$ を $z_1 - z_0 = r \mathrm{e}^{i\theta_1}$ をみたすものとする（コメント：$\theta_1$ は一意的に決まらないが気にしない）。

  $\theta_1$ の十分近くの $\theta$ について次が成り立つ：

  $$
  \lvert f(z_0 + r\mathrm{e}^{i\theta}) \rvert < \lvert f(z_0) \rvert
  $$

  ここで Cauchy の積分公式を応用すると：

  $$
  \begin{aligned}
      \lvert f(z_0 + r \mathrm{e}^{i\theta})\rvert
      &< \lvert f(z_0) \rvert\\
      &= \left\lvert \frac{1}{2\pi i}\int_{\partial U_r(z_0)}\!\frac{f(z)}{z - z_0}\,\mathrm dz \right\rvert\\
      &\le \frac{1}{2\pi}\int_0^{2\pi}\! \lvert f(z_0 + r \mathrm{e}^{i\theta})\rvert\,\mathrm d\theta\\
      &< \frac{1}{2\pi}\int_0^{2\pi}\! \lvert f(z_0)\rvert\,\mathrm d\theta\\
      &< \lvert f(z_0) \rvert.
  \end{aligned}
  $$

  つまり $\lvert f(z_0) \rvert < \lvert f(z_0) \rvert.$ 明らか非合理である。
  ゆえに背理法により：

  $$
  \forall z_1(z_1 \in U_R(z_0) \implies \lvert f(z_1) \rvert \ge \lvert f(z_0) \rvert).
  $$

  右辺は最大値であるので、結局 $\lvert f(z) \rvert$ は $D$ で定数である。
  絶対値が定数である正則関数は定数関数であるので、

  $$
  \forall z(z \in U_R(z_0) \implies f(z) = f(z_0)).
  $$

  一致の定理より

  $$
  \forall z(z \in D \implies f(z) = f(z_0)).
  $$

* **C 7.1** $f(z)$ が有界な領域 $D$ で正則かつ $D \cup \partial D$ 上で連続であるならば、
  $\lvert f(z) \rvert$ は境界 $\partial D$ 上のどこかで最大値を取る。
* **Th 7.5** (Schwarz)
  * $f(z)$ は $U_R(0)$ 上正則かつ有界であるとする。
  * $\lvert f(z) \rvert < M.$
  * $f(0) = 0.$
    * コメント：この仮定だけ証明のどこで使われたのかわからない。

  このとき：

  $$
  \forall z\left(z \in U_R(0) \implies
    \lvert f(z) \rvert \le \frac{M}{R}\lvert z \rvert
    \land \lvert f^\prime(0) \rvert \le \frac{M}{R}\right).
  $$

  $\lvert f(z) \rvert$ の不等式について、等号成立は次が成り立つときと同値である：

  $$
  \exists\theta\left(\theta \in \R \land f(z) = \mathrm{e}^{i\theta}\frac{M}{R}\right).
  $$

  証明：

  因数定理より $f(z) = z\varphi(z)$ を満たす $D$ 上の正則関数 $\varphi(z)$ が存在する。
  $0 < r < R$ なる $r$ をとる。$U_r(0)$ と $\varphi$ に最大値の原理（の補題？）を適用すれば次がわかる：

  $$
  \forall z\left(z \in U_r(0) \implies
    \lvert \varphi(z)\rvert \le \max_{\zeta \in \partial U_r(0)}\frac{\lvert f(\zeta)\rvert}{\lvert \zeta\rvert}
    = \frac{M}{R} \le \frac{M}{r}\right).
  $$

  不等式に $\lvert z \rvert$ を乗じて極限 $r \to R$ を考えれば、

  $$
  \forall z\left(z \in U_r(0) \implies
    \lvert f(z) \rvert \le \frac{M}{R}\lvert z \rvert\right).
  $$

  $f^\prime(0) = 1 \varphi(0) + 0 \varphi^\prime(0) = \varphi(0)$ および先程の不等式により：

  $$
  \lvert f^\prime(0) \rvert = \lvert \varphi(0) \rvert \le \frac{M}{R}.
  $$

  もし $z = z_0 \in U_R(0)$ で $\lvert f(z_0)\rvert = \dfrac{M}{R}\lvert z_0\rvert$ ならば
  $\lvert \varphi(z_0) \rvert = \dfrac{M}{R}.$

  再び最大値の原理により $\varphi(z)$ は定数である。このとき

  $$
  \exists \theta\left(\theta \in \R \land \varphi(z) = \mathrm{e}^{i\theta}\frac{M}{R}\right).
  $$

----

次回は§7.2 から。
