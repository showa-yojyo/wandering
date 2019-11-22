---
title: ベクトルの積分公式ノート
tags: math
---

Green の定理、Stokes の定理、Gauss の発散定理のノート。

# Green の定理

$D$ を平面の領域、$F, G$ を $D$ 上で定義された $C^1$ 級関数とする：

$$
\int_{\partial D}\!(F(x, y)\,\mathrm dx + G(x, y)\,\mathrm dy)
= \iint_D\!\left(\frac{\partial G(x, y)}{\partial x} - \frac{\partial F(x, y)}{\partial y}\right)\,\mathrm dx \mathrm dy
$$

## 検討：矩形領域で確認する

$D = {[x_0, x_1]} \times {[y_, y_1]}$ とすると、
例えば右辺第一項を逐次積分に変換できる：

$$
\begin{aligned}
\iint_D\!\frac{\partial G(x, y)}{\partial x}\,\mathrm dx \mathrm dy
&= \int_{y_0}^{y_1}\!\left(\int_{x_0}^{x_1}\!\frac{\partial G(x, y)}{\partial x}\,\mathrm dx\right)\,\mathrm dy\\
&= \int_{y_0}^{y_1}\!(G(x_1, y) - G(x_0, y))\,\mathrm dy\\
&= \int_{y_0}^{y_1}\!G(x_1, y)\,\mathrm dy - \int_{y_0}^{y_1}\!G(x_0, y)\,\mathrm dya\\
\end{aligned}
$$

ここで $\partial D = C_1 + C_2 + C_3 + C_4$ とおく。ただし
$C_1 \coloneqq x_1 \times {[y_0, y_1]}, \dots$ のようにする。すると上の積分は次のように書ける：

$$
\begin{aligned}
    \int_{y_0}^{y_1}\!G(x_1, y)\,\mathrm dy - \int_{y_0}^{y_1}\!G(x_0, y)\,\mathrm dy
    &= \int_{C_1}\!G(x, y)\,\mathrm dy + \int_{C_3}\,G(x, y)\,\mathrm dy.
\end{aligned}
$$

ところで $C_2, C_4$ における $y$ に関する線積分はゼロであるから、右辺は $C$ 上の線積分と等しい。
したがって：

$$
\tag*{$\spadesuit1$}
\iint_D\!\frac{\partial G(x, y)}{\partial x}\,\mathrm dx \mathrm dy
= \int_C\!G(x, y)\,\mathrm dy.
$$

同様に $F$ について行うと：

$$
\tag*{$\spadesuit2$}
\iint_D\! \frac{\partial F(x, y)}{\partial y}\,\mathrm dx \mathrm dy
= -\int_C\!F(x, y)\,\mathrm dx.
$$

$\spadesuit1$ と $\spadesuit2$ の差をとれば主張の等式だ。
$\blacksquare$

## 検討：関数で挟まれた領域で確認する

領域 $D$ の境界 $\partial D$ が点 $A, B$ で二つの曲線
$C_1\colon y = h_1(x),\ C_2 \colon y = h_2(x)$ に分割されているとする。
ここで関数 $h_1, h_2$ はどちらも閉区間 ${[a, b]}$ 上で定義されていて、

$$
\begin{aligned}
    h_1(a) = h_2(a),\\
    h_1(b) = h_2(b).
\end{aligned}
$$

このときも重積分を逐次積分に変換できて：

$$
\tag*{$\clubsuit1$}
\begin{aligned}
\iint_D\!\frac{\partial F(x, y)}{\partial y}\,\mathrm dx \mathrm dy
&= \int_a^b\!\left(\int_{y = h_1(x)}^{y = h_2(x)}\!\frac{\partial F(x, y)}{\partial y}\,\mathrm dy\right)\mathrm dx\\
&= \int_a^b\!(F(x, h_2(x)) - F(x, h_1(x)))\,\mathrm dx\\
&= \int_{C_2 - C_1} \!F(x, y)\,\mathrm dx\\
&= -\int_{\partial D}\!F(x, y)\,\mathrm dx.
\end{aligned}
$$

次は $\partial D$ を $y$ の関数のグラフで分割することを考えて次を得る：

$$
\tag*{$\clubsuit2$}
\iint_D\!\frac{\partial G(x, y)}{\partial x}\,\mathrm dx \mathrm dy
= \int_{\partial D}\!G(x, y)\,\mathrm dy.
$$

$\clubsuit1$ と $\clubsuit2$ の和を取れば主張の等式を得る。
$\blacksquare$

## 一般の場合

領域の境界が区分的に $C^1$ 級な Jordan 曲線であることが Green の定理の必要条件だ。
あとは、複数の領域を連結成分とするような定義域に対しても成り立つようだ。

# Stokes の定理

Green の定理で妙なのは
* 二変数関数が二つ現れること
* ベクトル解析の教科書が扱う定理にもかかわらず、ベクトルが表に出てこない

だろう。これは次のように定理を立体的に進化させることで、基本としての意味があると納得できる。

* $F, G$ を括って二次元ベクトル化する
* そのベクトル関数から Green の定理の被積分部分をひねりだす
* 三次元に持ってくる

## 二次元ベクトル化

$$
\bm F \coloneqq F(x, y)\bm e_x + G(x, y)\bm e_y.
$$

## 被積分関数をベクトル関数で表す

領域の位置ベクトルを $\bm r \coloneqq x\bm e_x + y\bm e_y$ と置いて微分する：

$$
\mathrm d \bm r = \mathrm dx \bm e_x + \mathrm dy \bm e_y.
$$

スカラー積をとると出てくるだろう：

$$
\begin{aligned}
    \bm F \cdot \mathrm d \bm r
    &= (F(x, y)\bm e_x + G(x, y)\bm e_y) \cdot (\mathrm dx \bm e_x + \mathrm dy \bm e_y)\\
    &= F(x, y)\,\mathrm dx + G(x, y)\,\mathrm dy.
\end{aligned}
$$

## 三次元に高める

ベクトル関数 $\bm F$ に戻り、これをいったん $z = 0$ に埋め込んで（？）演算 $\nabla\times$ を施す。

$$
\begin{aligned}
    \nabla \times \bm F
    &= \begin{vmatrix}
        \bm e_x & \bm e_y & \bm e_z\\
        \partial/\partial x & \partial/\partial y & \partial/\partial z\\
        F(x, y) & G(x, y) & 0
    \end{vmatrix}\\
    &= \begin{vmatrix}
        \partial/\partial y & \partial/\partial z\\
        G(x, y) & 0
    \end{vmatrix}\bm e_x
    - \begin{vmatrix}
        \partial/\partial x & \partial/\partial z\\
        F(x, y) & 0
    \end{vmatrix}\bm e_y
    + \begin{vmatrix}
        \partial/\partial x & \partial/\partial y\\
        F(x, y) & G(x, y)
    \end{vmatrix}\bm e_z\\
    &= -\frac{\partial G(x, y)}{\partial z}\bm e_x
    + \frac{\partial F(x, y)}{\partial z}\bm e_y
    + \left(\frac{\partial G(x, y)}{\partial x} - \frac{\partial F(x, y)}{\partial y}\right).
\end{aligned}
$$

$\nabla \times \bm F$ の $z$ 成分に Green の定理の一部が現れた。つまり：

$$
(\nabla \times \bm F) \cdot \bm e_z = \frac{\partial G(x, y)}{\partial x} - \frac{\partial F(x, y)}{\partial y}.
$$

これを利用して Green の定理の公式を書き換えると：

$$
\int_{\partial D}\!\bm F \cdot \mathrm d \bm r
= \iint_{D}(\nabla \times \bm F) \cdot \bm e_z\,\mathrm dx \mathrm dy.
$$

そして話を $xy$ 平面の領域から三次元空間の曲面に一般化したい。
次のような形になるはずだ：

$$
\begin{aligned}
\int_{\partial S}\!\bm F \cdot \mathrm d \bm r
&= \iint_{S}(\nabla \times \bm F) \cdot \bm n\,\mathrm dS\\
&= \iint_{S}(\nabla \times \bm F) \cdot \mathrm d \bm S\\
\end{aligned}
$$

TBW

# Gauss の発散定理

TBW

