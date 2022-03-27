---
title: 『常微分方程式』学習ノート Part 3
mathjax: true
tags: math
---

高崎金久著『常微分方程式』（日本評論社）ノートその三。先に第 5 章をやる。

## 第 5 章 線形常微分方程式

今日は §5.1 と §5.2 を読む。

### §5.1 線形常微分方程式の一般的性質

$$
y^{(n)} + a_1(x)y^{(n-1)} + \dotsc + a_n(x)y = b(x).
$$

* まず同次方程式の性質を調べてから、非同次方程式の性質を調べるという手順を採る。
* 前回の場合と同様に、上の ODE で $b(x)$ を**非同次項**といい、$b(x) \equiv 0$ と置き換えたものを元の非同次方程式の**同次形**と呼ぶ。
* 一般解に関する性質を三点挙げる：
  * $y = u_1(x), u_2(x)$ が同次形の解ならば、それらの定数係数の線形結合も解である
    （同次形の解はベクトル空間をなす）。
  * $y = u_1(x), u_2(x)$ がそれぞれ $b_1(x), b_2(x)$ を非同次項とする ODE の解であるならば、
    それらの定数係数の線形結合 $C_1u_1(x) + C_2u_2(x)$ は $C_1b_1(x) + C_2b_2(x)$ を非同次項とする ODE の解である。
  * 非同次方程式の一般解は、次の形である：

    非同次形の特殊解 + 同次形の一般解

* **微分作用素**：形式的に、次のように記号を定める：

  $$
  \begin{aligned}
  D &\coloneqq \frac{\mathrm{d}}{\mathrm{d}x},\\
  D^n &\coloneqq \frac{\mathrm{d}^n}{\mathrm{d}x^n},\\
  A(x, D) &\coloneqq D^n + a_1(x)D^{n-1} + \dotsb + a_n(x).
  \end{aligned}
  $$

  * 関数から関数への写像と思っていい：

  $$
  A(x, D) \colon u(x) \longmapsto u^{n}(x) + a_1(x)u^{n-1}(x) + \dotsb + a_n(x).
  $$

  * この記号を利用すると、線形 ODE の一般形を次のように表すことができて、線形代数の応用ができるように見える：

    $$
    A(x, D)y = b(x).
    $$

    * コメント：線形代数の教科書の方程式の章に出てくる数式 $A\bm x = \bm b$ と似ている。
    * 事実、$A(x, D)$ は線形写像であり、同次形の解全体のなす空間は $\ker A(x, D)$ に等しい。

* (Def 5.1) **基本解系**
  * 基本解系とは、同次形 $A(x, D)y = 0$ の解の組 $(u_1(x), \dotsc, u_n(x))$ であって、次の性質があるものをいう：
    * 任意の解 $y = u(x)$ がこれらの定数係数線形結合として表される。
    * そのときの係数は $u(x)$ に対して一意的に定まる。
  * コメント：基本解系は、同次形の解空間の一つの基底である。

* 例 5.1, 5.2
  * $y^{\prime\prime} + a^2y = 0\quad(a \ne 0)$ には基本解系として
    * $(\cos ax, \sin ax)$ や
    * $(\mathrm{e}^{aix}, \mathrm{e}^{-aix})$ が挙げられる。
  * $y^{\prime\prime} - a^2y = 0\quad(a \ne 0)$ には基本解系として
    * $(\cosh ax, \sinh ax)$ や
    * $(\mathrm{e}^{ax}, \mathrm{e}^{-ax})$ が挙げられる。

* 基本解系の決定手順
  1. 初期条件を設定する点を一つ定める e.g. $x = x_0.$
  2. 同次形に対して初期条件

     $$
     y(x_0) = c_0,\quad
     y^\prime (x_0) = c_1,\quad
     \dotsc,\quad
     y^{(n-1)}(x_0) = c_{n-1}
     $$

     の下での初期値問題の解が、任意の $c_0, c_1, \dotsc, c_{n-1}$ に対して一意的であると仮定する。
  3. 次の初期条件群をみたす解 $u_1, \dotsc, u_n$ を考える：

     $$
     \begin{alignedat}{}
         u_1(x_0) &= 1, & u_1^\prime(x_0) &= 0, & u_1^{\prime\prime}(x_0) &= 0, & \dotsc,& & u_1^{(n-1)}(x_0) &= 0,\\
         u_2(x_0) &= 0, & u_2^\prime(x_0) &= 1, & u_2^{\prime\prime}(x_0) &= 0, & \dotsc,& & u_2^{(n-1)}(x_0) &= 0,\\
         \dots\\
         u_n(x_0) &= 0, & u_n^\prime(x_0) &= 0, & u_n^{\prime\prime}(x_0) &= 0, & \dotsc,& & u_n^{(n-1)}(x_0) &= 1,\\
     \end{alignedat}
     $$

  * (Th 5.1) これらの解 $u_1, \dotsc, u_n$ は同次形の基本解系を与える。
* 非同次形の一般解は、同次形の解に定数変化法を適用して得る：定数係数を関数係数に置き換えて、不定積分を計算する。

### §5.2 定数係数線形常微分方程式の基本解系

* **指数関数解**とは、$y = C \mathrm{e}^{\lambda x}$ の形の解をいう。ODE $y^\prime = \lambda y$ の一般解である。
* 本節のポイントは $\def\elx{ \mathrm{e}^{\lambda x} } D^k\elx  = \lambda^k \elx$ が成り立つことにある。
* 先程の記号 $A(x, D)$ を流用して $A(\lambda) \coloneqq \lambda^n + a_1 \lambda^{n-1} + \dotsb + a_n$ で定義する。
* (Th 5.2) $A(\lambda) = 0$ ならば $y = C\mathrm{e}^{\lambda x}$ は定数係数同次形 $A(D)y = 0$ の解である。
* (Def 5.2) 定数係数同次形 $A(D)y = 0$ に対応して、
  * **特性多項式**とは、多項式 $A(\lambda)$ のことである。
  * **特性方程式**とは、方程式 $A(\lambda) = 0$ のことである。
  * **特性根**とは、特性方程式の根のことである。
* コメント：線形代数でいう正方行列 $A$ の特性方程式 $\det(A - \lambda I) = 0$ との関係は？
* 例 5.4 をよく見ておくこと。
* (Th 5.3) 特性方程式 $A(\lambda) = 0$ の根 $\alpha_1, \dotsc, \alpha_n$ がすべて相異なるならば、指数関数解の組

  $$
  \def\a#1{ \mathrm{e}^{\alpha_{#1}x} }
  \a 1, \dotsc, \a n
  $$

  は対応する同次形 $A(D)y = 0$ の基本解系をなす。

* それでは特性根が重根であるようなものを含む特性多項式についてはどうなるか。
  実はそれでも基本解系は得られる。

* (Th 5.4) $\alpha$ が特性方程式 $A(\lambda) = 0$ の $m$ 重根であるならば、

  $$
  x^k \mathrm{e}^{\alpha x}\quad(k = 0, 1, \dotsc, m - 1)
  $$

  はすべて同次形 $A(D)y = 0$ の解である。

* 特性方程式 $A(\lambda) = 0$ を次のように因数分解されるとする：

  $$
  A(\lambda) = \prod_{r = 1}^s (\lambda - \beta_r)^{m_r},\quad (r \ne q \implies \beta_r \ne \beta_q)
  $$

  各 $\beta_r$ に対して $m_r$ 個の $x^j \mathrm{e}^{\beta_r x}$ の形の解があるので、同次形に対して全部で
  $m_1 + \dotsb + m_s = n$ 個の解が得られる。

* (Th 5.5) これらの $x^j \mathrm{e}^{\beta_r x}$ は線形独立であり、同次形 $A(D)y = 0$ の基本解系を与える。

* §5.2.5 は速度に比例する抵抗を加えたバネ運動の運動方程式に関する考察だ。
  簡単に言うと特性方程式が二次方程式になるので、根のあり方が三通り考えられる。
  それに応じて減衰運動になったり臨界減衰になったりすると説明している。

  $$
  m \frac{\mathrm{d}^2x}{\mathrm{d}t^2} = -kx - c \frac{\mathrm{d}x}{\mathrm{d}t},\quad (k > 0, c > 0).\\
  \begin{aligned}
  \frac{\mathrm{d}^2x}{\mathrm{d}t^2} + \frac{c}{m}\frac{\mathrm{d}x}{\mathrm{d}t} + \frac{k}{m}x &= 0.\\
  \frac{\mathrm{d}^2x}{\mathrm{d}t^2} + \omega^2\frac{\mathrm{d}x}{\mathrm{d}t} + \gamma x &= 0.
  \end{aligned}
  $$

  よって特性方程式は：

  $$
  A(\lambda) = \lambda^2 + \gamma\lambda + \omega^2 = 0.
  $$

  判別式 $\Delta = \gamma^2 - 4\omega^2$ の符号で場合分けする。
  1. $\Delta > 0:$ 相異なる実数解：運動が単調に収束する。

     $$
     \alpha_{\pm} = \frac{-\gamma \pm \sqrt{\Delta}}{2},\quad x = C_+ \mathrm{e}^{\alpha_+t} + C_-\mathrm{e}^{\alpha_-t}.
     $$

  2. $\Delta < 0:$ 相異なる複素数解：減衰運動（グラフを描くといい）。

     $$
     \alpha_{\pm} = \frac{-\gamma \pm \sqrt{-\Delta}i}{2},\quad x = \mathrm{e}^\mu(C_1\cos\nu t + C_2\sin \nu t).
     $$

  3. $\Delta = 0:$ 重根（実数解）：臨界減衰（グラフ描画推奨）。

     $$
     \alpha = -\frac{\gamma}{2}, \quad x = C_1\mathrm{e}^{\alpha t} + C_2 t\mathrm{e}^{\alpha t}.
     $$

* さらに LRC 電気回路のなす ODE の同次形が上述のバネ運動方程式と同じ構造であることを指摘している。

§5.3 以降は後日やる。
