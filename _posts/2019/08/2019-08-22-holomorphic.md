---
title: 『新訂解析学』学習ノート Part 5
mathjax: true
tags: math
---

熊原啓作著『新訂解析学』の学習ノート第五回。今回も居眠り。

## （続）正則関数の性質

### 正則関数列

実数の微分積分では、関数列 $\lbrace f_n(x) \rbrace$ の極限が微分可能であることと、この関数列が一様収束することが同値だ。
一方、正則関数列の極限が微分可能である条件は、それよりは緩い。

* **Th 7.6** 極限記号と積分記号の順序交換
  * $D$ を領域とする。
  * $\lbrace f_n(z) \rbrace$ を $D$ で定義された連続関数列であり、$f(z)$ に広義一様収束するものとする。

  このとき $D$ に含まれる任意の区分的に滑らかな閉曲線 $C$ について次が成り立つ：

  $$
  \lim_{n \to \infty}\int_C\!f_n(z)\,\mathrm dz = \int_C\!f(z)\,\mathrm dz.
  $$

  証明：
  仮定から関数 $f(z)$ は 領域 $D$ 上連続である。すなわち（有界閉集合である）曲線 $C$ 上積分が存在する。

  $L \coloneqq l(C)$ とおく。関数列の一様収束性により：

  $$
  \forall \varepsilon > 0
    \exists n_0 \in \N
        \forall n \ge n_0 \forall z \in \Complex (\lvert f_n(z) - f(z) \rvert < \varepsilon)).
  $$

  したがって $n \ge n_0$ のとき：

  $$
  \begin{aligned}
      \left\lvert \int_C\!f_n(z)\,\mathrm dz - \int_C\!f(z)\,\mathrm dz\right\rvert
      &\le \int_C\! \lvert f_n(z) - f(z)\rvert\,\lvert \mathrm dz \rvert\\
      &< \varepsilon L.
  \end{aligned}
  $$

  ここで $\varepsilon > 0$ は任意だから、所望の結論を得る。
  * コメント：曲線の有界性を仮定することが必要と思われる。
* **Th 7.7** 極限記号とシグマ記号の順序交換
  * $D$ を領域とする。
  * $\lbrace f_n(z) \rbrace$ を $D$ で定義された連続関数列であり、
  * $\sum f_n(z)$ は $D$ で広義一様収束するものとする。

  このとき区分的に滑らかな曲線 $C \subset D$ にたいして次が成り立つ：

  $$
  \sum_{n = 1}^\infty\int_C\!f_n(z)\,\mathrm dz
  = \int_C\! \sum_{n = 1}^\infty f_n(z)\,\mathrm dz.
  $$

  証明：
  $\displaystyle g_n(z) \coloneqq \sum_{j = 1}^n f_j(z)$ とおくと、関数列 $\lbrace g_n(z) \rbrace$ は
  **Th 7.6** の仮定を満たす。
* **Th 7.8** 極限と微分の順序交換
  * $D$ を領域とする。
  * $\lbrace f_n(z) \rbrace$ を領域 $D$ 内の正則関数列とする。
  * この関数列は $f(z)$ に $D$ 上広義一様収束するものとする。

  このとき：
  * $f(z)$ は正則である。
  * $f^\prime(z) = \lim f_n^\prime(z).$
  * 関数列 $\lbrace f_n^\prime(z) \rbrace$ は $D$ 上広義一様収束である。

  証明：
  * コメント：ここは特殊で、Cauchy の公式に加えて位相空間論の被覆定理を応用する。

  $z_0 \in D$ とする。$\exists \varepsilon > 0 (U_{\varepsilon}(z_0) \subset D).$

  閉曲線 $C \subset U_{\varepsilon}(z_0)$ をとる。
  $f_n(z)$ の仮定より Cauchy の積分定理が適用できる：

  $$
  \forall n\left(n \in \N \implies \int_C\!f_n(z)\,\mathrm dz = 0\right).
  $$

  **Th 7.6** より：

  $$
  \int_C\!f(z)\,\mathrm dz = \lim_{n\to\infty}\int_C\!f_n(z)\,\mathrm dz = 0.
  $$

  Morera の定理によれば $f(z)$ がこの円盤内部で正則であることが示される。
  $z_0$ は任意だから、結局 $D$ 全体で $f(z)$ は正則である。

  今度は $r \in {(0, \varepsilon)}$ をとり、曲線を $C = \lbrace z_0 + r\mathrm{e}^{i\theta}\,\mid\, \theta \in {[0, 2\pi]} \rbrace$ とする。
  Cauchy の積分公式を $f_n^\prime(z)$ に適用し、極限操作を施す：

  $$
  \begin{aligned}
  f_n^\prime(z) &= \frac{1}{2\pi i}\int_C\!\frac{f_n(\zeta)}{(\zeta - z)^2}\,\mathrm dz\\
  \therefore \lim_{n\to\infty}f_n^\prime(z) &= \frac{1}{2\pi i}\int_C\! \lim_{n\to\infty}\frac{f_n(\zeta)}{(\zeta - z)^2}\,\mathrm dz\\
  &= \frac{1}{2\pi i}\int_C\! \frac{f(\zeta)}{(\zeta - z)^2}\,\mathrm dz\\
  &= f^\prime(z).
  \end{aligned}
  $$

  仮定より $\forall r_1 \in {(0, r)}$ をとると閉円盤 $\overline{U_{r_1}(z_0)}$ で $f_n$ は一様収束する。
  $D$ はコンパクトであるから、閉円盤族から有限個を選んで $D$ 全体を被覆できる。これは $f_n$ が $D$ で広義一様収束することにほかならない。
* **C 7.2** シグマ版（省略）

### 等角写像

目標は意外なことに正則関数版逆写像定理だ。

* 複素平面上にある 2 曲線のなす角を、交点における接線ベクトル同士のなす角で定義する。
  すなわち $\arg z_2^\prime(s_0) - \arg z_1^\prime(t_0)$ のように求められる量だ。
* **等角写像** 関数 $f\colon\Complex \longrightarrow \Complex$ によって、二曲線 $C_1,\;C_2$ が
  $\varGamma_1\colon f \circ z_1,\;\varGamma_2\colon f \circ z_2$ に写されるとする。
  もし点 $z_0 \in C_1 \cap C_2$ において、曲線のなす角が $f(z) \in \varGamma_1 \cap \varGamma_2$ において
  **向きを込めて**一致するとき、$f$ は点 $z_0$ において等角写像であるという。
* **Th 7.9** 正則関数は等角写像である。
  * $f(z)$ を点 $z = z_0$ で正則であり、
  * $f^\prime(z_0) = 0$ であるとする。

  このとき $w = f(z)$ は $z = z_0$ で等角写像である。

  証明：曲線とパラメーターを適当に定義して、偏角の差が不変であることを計算で示す（省略）。
* **E7.1** 一次分数変換は等角写像である。
* **E7.2** 上半平面を原点を中心とする単位円内部に写す一次分数変換

  $$
  w = \mathrm{e}^{i\theta}\frac{z - \lambda}{z - \overline\lambda}.
  $$

* **E7.3** 一点を除いて等角写像である例

  $$
  w = f(z) = z^2.
  $$

  TODO: 不審な点があるので、もう一度教科書で確認する。
* **E7.4** 等角写像の決定例

  問：次の領域間の写像 $f\colon E \longrightarrow D$ で等角写像となるものを決定しろ。

  $$
  \begin{aligned}
      E &= \!\left\{\left. z \right| \left. z \in {\left(0, \frac{\pi}{4}\right)} \right.\right\}\!,\\
      D &= \{ z \,|\, \lvert z \rvert < 1\}.
  \end{aligned}
  $$

  解：おそらく $E$ を上半平面に写す等角写像 $z \longmapsto z^4$ を見つけて、それと **E 7.2** の一次分数変換と合成するのだと思われる：

  $$
  w = -\frac{z^4 - i}{z^4 + i}.
  $$

* 正則関数 $f(z) = u(x, y) + iv(x, y)$ に対して Cauchy-Riemann の方程式より次が成り立つ：

  $$
  f^\prime(z) \ne 0 \iff \frac{\partial(u, v)}{\partial(x, y)} \ne 0.
  \quad \because \frac{\partial(u, v)}{\partial(x, y)} = \lvert f^\prime(z)\rvert^2.
  $$

* **Th 7.10** 正則関数版逆写像定理
  * $w = f(z)$ は点 $z_0$ で正則であり $f^\prime(z_0) \ne 0$ とする。
  * $w_0 = f(z_0)$ とする。

  このとき写像 $f$ は $z_0$ を含むある領域 $D$ から $w_0$ を含むある領域 $\varDelta$ への単葉関数を与え、
  逆関数 $z = f^{-1}(w)$ は $\varDelta$ 上正則かつ

  $$
  \frac{\mathrm{d}z}{\mathrm{d}w} = \frac{1}{f^\prime(z)}.
  $$

  証明：
  $f(z) = u(x, y) + iv(x, y)$ とおく。$z_0 = x_0 + i y_0$ とおいて
  $\R^2$ における写像 $F\colon(x, y) \longmapsto (u, v)$ に対して、微分に関する仮定と陰関数定理により次を満たす各点の近傍 $D_1, \varDelta_1$ が存在する：

  * $(x_0, y_0) \in D_1 \subset \R^2$
  * $(u(x_0, y_0), v(x_0, y_0)) \in \varDelta_1 \subset \R^2$

  かつ写像 $F\mid_{D_1}\colon D_1 \longrightarrow \varDelta_1$ はこの近傍間の全単射である。逆写像も含めて $C^\infty$ 級であるが、
  これを複素平面上 $w, z$ に置き換えて考えると結論は理解できる。

----

第 7 章は以上。次回は第 8 章以降。
