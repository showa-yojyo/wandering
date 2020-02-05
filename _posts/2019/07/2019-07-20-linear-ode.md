---
title: 『常微分方程式』学習ノート Part 4
tags: math
---

高崎金久著『常微分方程式』（日本評論社）ノートその四。第 5 章後半。

## 第 5 章 線形常微分方程式（続き）

$$
A(x, D)y = b(x).
$$

### §5.3 非同次方程式と定数変化法

* **Wroński 行列式**とは、次で定義された行列式である：

  $$
  W(u_1(x), \dotsc, u_n(x)) \coloneqq
  \def\arraystretch{1.5}
  \begin{vmatrix}
      u_1(x) & u_2(x) & \dots & u_n(x)\\
      u_1^\prime(x) & u_2^\prime(x) & \dots & u_n^\prime(x)\\
      \vdots & \vdots & \ddots & \vdots\\
      u_1^{(n-1)}(x) & u_2^{(n-1)}(x) & \dots & u_n^{(n-1)}(x)
  \end{vmatrix}.
  $$

* 同次方程式の基本解系を得てから、これを基に対応する非同次方程式の解を得る。
  1. 同次方程式 $A(x, D)y = 0$ の基本解系 $(u_1(x), \dotsc, u_n(x))$ を一組とる。
  2. Wroński 行列式 $W(u_1, \dotsc, u_n) \ne 0$ を仮定する。
  3. 定数変化法。次の $y$ が非同次形の一般解であると仮定する：

     $$
     y = \sum_{j = 1}^n z_j(x)u_j(x).
     $$

  4. $y^\prime, y^{\prime\prime}, \dotsc, y^{(n-1)}$ を計算する。この過程で以下の条件を勝手に加える：

     $$
     \def\s#1{ \sum_{j=1}^n z_j^\prime(x)u_j^{#1}(x)}
     \begin{aligned}
     \s{} &= 0,\\
     \s{\prime} &= 0,\\
     \s{\prime\prime} &= 0,\\
     \dotsc,\\
     \s{(n-2)} &= 0,\\
     \s{(n-1)} &= b(x).
     \end{aligned}
     $$

     これらの条件により、各導関数は簡略化される：

     $$
     y^{(k)} = \sum_{j=1}^n z_j(x) u_j^{(k)}(x),\quad k = 1, \dotsc, n - 1.
     $$

     追加した条件は $z_1^\prime(x), \dotsc, z_n^\prime(x)$ に関する連立一次方程式になり、
     その係数行列式は $W(u_1, \dotsc, u_n)$ であることが本質的だ。仮定 2. が効いて線形代数で $z_j^\prime(x)$ が求まる：

     $$
     z_j^\prime(x) = (-1)^{n - j}\frac{W(u_1, \dotsc, \cancel{u_j}, \dotsc, u_n)}{W(u_1, \dotsc, u_n)}b(x).
     $$

  5. $z_j^\prime(x)$ の不定積分を計算すれば $z_j(x)$ が得られる：

     $$
     z_j(x) = \int\!z_j^\prime(x)\,\mathrm dz + C_j.
     $$

  6. 非同次方程式 $A(x, D)y = b(x)$ の一般解は次になる：

     $$
     \begin{aligned}

     y &= \sum_{j=1}^n\left(
       (-1)^{n - j}\int\!\frac{W(u_1, \dotsc, \cancel{u_j}, \dotsc, u_n)}{W(u_1, \dotsc, u_n)}b(x)\,\mathrm dx + C_j
       \right)u_j(x).\\

       &= \sum_{j=1}^n\left(
       (-1)^{n - j}\int\!\frac{W(u_1, \dotsc, \cancel{u_j}, \dotsc, u_n)}{W(u_1, \dotsc, u_n)}b(x)\,\mathrm dx
       \right)u_j(x) + f^{(n)}g(x).
     \end{aligned}
     $$

     * シグマの項が非同次方程式の特殊解であり、第二項は同次方程式の一般解であることに注意。
  * Wroński 行列式に関する仮定 2. は、実際には任意の基本解系について成り立っている。
    * まず、$A(x, D)y = 0$ の $n$ 個の解 $u_1, \dotsc, u_n$ の Wroński 行列式に関して次が成り立つ：

      $$
      \exists x_0(W(x_0) \ne 0) \iff \forall x(W(x) \ne 0).
      $$

    * 次に、任意の基本解系と「ある特殊な初期条件によって決まる基本解系」とは基底変換で写り合う（線形代数）。
      「特殊な条件」とは、$v_j^{(k)}(x_0) = \delta_{jk}$ を満たす基本解系 $(v_1, \dotsc, v_n)$ とする。
      この特殊な基本解系の Wroński 行列式の値が 1 になることに注意。

### §5.4 定数係数の場合の非同次方程式

* 定数係数の非同次形 $A(D)y = b(x)$ の解を求めることもできる。
* 非同次項 $b(x)$ が特殊なものに対しては、定数係数であることを生かして解を直接的に求めることもできる。

#### 指数関数の場合

$$
A(D)y = B \mathrm{e}^{\beta x}, \quad \beta \ne 0.
$$

* $A(\beta) \ne 0$ の場合
  * 一般解を指数関数解と同次形の解 $h(x)$ の和の形をするものと仮定する：

    $$
    y = C \mathrm{e}^{\beta x} + h(x).
    $$

    §5.2 の指数関数解で議論から：

    $$
    \begin{aligned}
    A(D)y &= CA(\beta)\mathrm{e}^{\beta x}\\
    \therefore CA(\beta) &= B.\\
    \therefore y &= \frac{B}{A(\beta)}\mathrm{e}^{\beta x} + h(x).
    \end{aligned}
    $$

* $A(\beta) = 0$ の場合
  * 結論から言うと一般解は次のようになる：

    $$
    y = \frac{B}{A^{(m)}(\beta)}x^m\mathrm{e}^{\beta x} + h(x).
    $$

  * TODO: 後で確かめる。なぜ理解しにくいかというと、重根が生じるときにその多重度ぶんだけ微分を考えなければならなくなることが関係するようだ。

#### 三角関数の場合

$$
A(D)y = B_1\cos \beta x + B_2 \sin \beta x.
$$

* Euler の公式のおかげで指数関数の場合に帰着できる。
  すなわち $A(D)y = \mathrm{e}^{\pm\beta i x}$ の解 $y = u_{\pm}(x)$ の線形結合で与えられる。
* $A(\pm\beta i) \ne 0$ の場合
  * 同次形の解を $h(x)$ で表すことにすると：

    $$
    \begin{aligned}
    u_{\pm}(x) &= \pm\frac{\mathrm{e}^{\pm\beta i x}}{A(\pm\beta i)} + h(x).\\
    \therefore y &= \frac{B_1}{2}(v_+(x) + v_-(x)) + \frac{B_2}{2i}(v_+(x) - v_-(x)) + h(x).
    \end{aligned}
    $$
* $A(\pm\beta i) = 0$ の場合
  * $A(\lambda) = 0$ における特性根 $\lambda = \pm\beta i$ の重複度を $m_\pm$ とする：

    $$
    v_\pm = \frac{x^{m_\pm}\mathrm{e}^{\pm\beta i x}}{A^{(m_\pm)}(\pm\beta i)} + h(x).
    $$

  * $m = m_+ = m_-$ ならば次のように書き直せる：

    $$
    y = x^m \cos \beta x + x^m \sin \beta x + h(x).
    $$

#### 多項式の場合

$$
A(D)y = B_0 x^m + B_1 x^{m-1} + \dotsb + B_m.
$$

* 結論から言うと一般解は次のようになる：

  $$
  y = C_0 x^m + C_1 x^{m-1} + \dotsb + C_m + h(x).
  $$

* 事実 $A(D)z = x^m \mathrm{e}^{\lambda x}$ の解は

  $$
  z = u_m(x, \lambda) \coloneqq \frac{\partial ^m}{\partial \lambda^m}\frac{\mathrm{e}^{\lambda x}}{A(\lambda)}
  = \frac{x^m \mathrm{e}^{\lambda x}}{A(\lambda)}.
  $$

  である。この式において $\lambda = 0$ を考えると $A(D)z = x^m$ の（特殊）解になる。

* Leibniz rule からも説明がつく：

  $$
  u_m(x, 0) = \left.\frac{\partial ^m}{\partial \lambda^m}\frac{\mathrm{e}^{\lambda x}}{A(\lambda)}\right|_{\lambda = 0}
  = \left.\sum_{k = 0}^m \binom{m}{k}x^{m-k}\frac{\partial ^k}{\partial \lambda^k}\frac{1}{A(\lambda)}\right|_{\lambda = 0}.
  $$

以上で第 5 章のノートを終わる。
