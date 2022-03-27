---
title: ベクトルの積分公式ノート
mathjax: true
tags: math
---

Green の定理、Stokes の定理、Gauss の発散定理のノート。

## Green の定理

$D$ を平面の領域、$F, G$ を $D$ 上で定義された $C^1$ 級関数とする：

$$
\int_{\partial D}\!(F(x, y)\,\mathrm dx + G(x, y)\,\mathrm dy)
= \iint_D\!\left(\frac{\partial G(x, y)}{\partial x} - \frac{\partial F(x, y)}{\partial y}\right)\,\mathrm dx \mathrm dy
$$

### 検討：矩形領域で確認する

$D = {[x_0, x_1]} \times {[y_, y_1]}$ とすると、
例えば右辺第一項を逐次積分に変換できる：

$$
\begin{aligned}
\iint_D\!\frac{\partial G(x, y)}{\partial x}\,\mathrm dx \mathrm dy
&= \int_{y_0}^{y_1}\!\left(\int_{x_0}^{x_1}\!\frac{\partial G(x, y)}{\partial x}\,\mathrm dx\right)\,\mathrm dy\\
&= \int_{y_0}^{y_1}\!(G(x_1, y) - G(x_0, y))\,\mathrm dy\\
&= \int_{y_0}^{y_1}\!G(x_1, y)\,\mathrm dy - \int_{y_0}^{y_1}\!G(x_0, y)\,\mathrm dy\\
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

$\spadesuit2$ と $\spadesuit1$ の差をとれば主張の等式だ。
$\blacksquare$

### 検討：関数で挟まれた領域で確認する

領域 $D$ の境界 $\partial D$ が点 $A, B$ で二つの曲線
$C_1\colon y = h_1(x),\ C_2 \colon y = h_2(x)$ に分割されているとする。
ここで関数 $h_1, h_2$ はどちらも閉区間 ${[a, b]}$ 上で定義されていて、

$$
\begin{aligned}
    h_1(a) = h_2(a),\\
    h_1(b) = h_2(b).
\end{aligned}
$$

それぞれが領域の「床」と「天井」になる。このときも重積分を逐次積分に変換できて：

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

等式変形の途中で線積分に変換した。
同様に $\partial D$ を $y$ の関数のグラフで床と天井に分割することを考えて次を得る：

$$
\tag*{$\clubsuit2$}
\iint_D\!\frac{\partial G(x, y)}{\partial x}\,\mathrm dx \mathrm dy
= \int_{\partial D}\!G(x, y)\,\mathrm dy.
$$

$\clubsuit1$ と $\clubsuit2$ の和を取れば主張の等式を得る。
$\blacksquare$

### 一般の場合

領域の境界が区分的に $C^1$ 級な Jordan 曲線であることが Green の定理の必要条件だ。
あとは、複数の領域を連結成分とするような定義域に対しても成り立つようだ。

## Stokes の定理

Green の定理で妙なのは

* 二変数関数が二つ現れること
* ベクトル解析の教科書が扱う定理にもかかわらず、ベクトルが表に出てこない

だろう。これは次のように定理を立体的に進化させることで、基本としての意味があると納得できる。

* $F, G$ を括って二次元ベクトル化する
* そのベクトル関数から Green の定理の被積分部分をひねりだす
* 三次元に持ってくる

### 二次元ベクトル化

$$
\bm F \coloneqq F(x, y)\bm e_x + G(x, y)\bm e_y.
$$

### 被積分関数をベクトル関数で表す

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

スカラー積が 1-form になることは覚えておこう。

### 三次元に高める

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
\tag*{$\heartsuit0$}
\begin{aligned}
\int_{\partial S}\!\bm F \cdot \mathrm d \bm r
&= \iint_{S}(\nabla \times \bm F) \cdot \bm n\,\mathrm dS\\
&= \iint_{S}(\nabla \times \bm F) \cdot \mathrm d \bm S\\
\end{aligned}
$$

**証明の検討**：
右辺を成分に分解して、一つの成分に対して左辺にどれだけ似てくるのかを見る。

$$
\iint_{S}(\nabla \times \bm F) \cdot \bm n\,\mathrm dS
= \iint_{S}\nabla \times (F_x\bm e_x + F_y\bm e_y + F_z\bm e_z) \cdot \bm n\,\mathrm dS.
$$

例えば $x$ 成分の面積分を見ていく。すると $\mathrm dS$ は $xy$ 平面への射影として評価する。
$x$ 成分の面積分は：

$$
\iint_{S}(\nabla \times F_x\bm e_x)\cdot \bm n\,\mathrm dS.
$$

被積分部分を少しずつ見ていく。ベクトル積部分は：

$$
\def\pd#1{ \partial / \partial {#1} }

\nabla \times F_x \bm e_x
= \begin{vmatrix}
    \bm e_x & \bm e_y & \bm e_z \\
    \pd x & \pd y & \pd z\\
    F_x & 0 & 0
  \end{vmatrix}
= \frac{\partial F_x}{\partial z}\bm e_y

- \frac{\partial F_x}{\partial y}\bm e_z.
$$

法線ベクトルとのスカラー積は：

$$
\tag*{$\heartsuit1$}
(\nabla \times F_x\bm e_x)\cdot \bm n
= \frac{\partial F_x}{\partial z}\bm e_y \cdot \bm n

- \frac{\partial F_x}{\partial y}\bm e_z \cdot \bm n
$$

一方、曲面 $S\colon z = f(x, y)$ 上の位置ベクトル $\bm r = x \bm e_1 + y \bm e_2 + f(x, y)\bm e_3$
について、$\partial\bm r/\partial x, \partial\bm r/\partial y$ は曲面の接ベクトルだ。
接ベクトル

$$
\frac{\partial \bm r}{\partial y} = \bm e_y + \frac{\partial f(x, y)}{\partial y}\bm e_z
$$

が法線ベクトル $\bm n$ と直交することから：

$$
\begin{aligned}
\bm n \cdot \frac{\partial \bm r}{\partial y}
&= \bm n \cdot \bm e_y + \frac{\partial f(x, y)}{\partial y}\bm n \cdot \bm e_z
= 0.\\
\therefore \bm n \cdot \bm e_y &= -\frac{\partial f(x, y)}{\partial y}\bm n \cdot \bm e_z.
\end{aligned}
$$

この等式を $\heartsuit1$ に代入して次を得る：

$$
\begin{aligned}
(\nabla \times F_x\bm e_x)\cdot \bm n
&= -\frac{\partial F_x}{\partial z}\frac{\partial f(x, y)}{\partial y}\bm n \cdot \bm e_z

- \frac{\partial F_x}{\partial y}\bm e_z \cdot \bm n\\
&= -\left(\frac{\partial F_x}{\partial z}\frac{\partial f(x, y)}{\partial y} + \frac{\partial F_x}{\partial y}\right)\bm e_z \cdot \bm n\\
&= -\left(\frac{\partial F_x}{\partial z}\frac{\partial z}{\partial y} + \frac{\partial F_x}{\partial y}\right)\bm e_z \cdot \bm n.
\end{aligned}
$$

括弧内第一項の $z$ による偏微分は $F_x$ が曲面上で $x, y$ だけで表せる

$$
F_x = F_x(x, y, z) = F_x(x, y, f(x, y))
$$

ためゼロである。$\varphi(x, y)\coloneqq F_x(x, y, f(x, y))$ とすると：

$$
\tag*{$\heartsuit2$}
\begin{aligned}
(\nabla \times F_x\bm e_x)\cdot \bm n
&= -\frac{\partial \varphi(x, y)}{\partial y}\bm e_z \cdot \bm n.
\end{aligned}
$$

一方、先に注意したように $\bm e_z \cdot \bm n\,\mathrm dS = \mathrm dx \mathrm dy$ である。
これと $\heartsuit2$ を利用して、$S$ の $xy$ 平面への射影領域を $S_{xy}$ と書くとこうなる：

$$
\iint_S\!(\nabla \times F_x\bm e_x)\cdot \bm n\,\mathrm dS
= -\iint_{S_{xy}}\!\frac{\partial \varphi(x, y)}{\partial y}\,\mathrm dx \mathrm dy.
$$

Green の定理の証明中で得た $\spadesuit2$ を右辺に適用する：

$$
-\iint_{S_{xy}}\!\frac{\partial \varphi(x, y)}{\partial y}\,\mathrm dx \mathrm dy
= \int_{\partial S_{xy}}\!\varphi(x, y)\,\mathrm dx.
$$

$\varphi(x, y) = F_x(x, y, z)$ が $\partial S$ 上でも成り立つから：

$$
\int_{\partial S_{xy}}\!\varphi(x, y)\,\mathrm dx
= \int_{\partial S}\!F_x(x, y, z)\,\mathrm dx.
$$

これで $x$ 成分に関する検討は終わった：

$$
\tag*{$\heartsuit3$}
\iint_{S}(\nabla \times F_x\bm e_x)\cdot \bm n\,\mathrm dS
= \int_{\partial S}\!F_x(x, y, z)\,\mathrm dx.
$$

同じ推論により $y, z$ 成分については次を得る：

$$
\tag*{$\heartsuit4$}
\def\equ#1{
  \iint_{S}(\nabla \times F_{#1}\bm e_{#1})\cdot \bm n\,\mathrm dS
  = \int_{\partial S}\!F_{#1}(x, y, z)\,\mathrm d{#1} }
\begin{aligned}
    \equ y\\
    \equ z
\end{aligned}
$$

$\heartsuit3, \heartsuit4$ を加えて $\heartsuit0$ の（左辺と右辺が入れ替わった）等式を得る。
$\blacksquare$

## Gauss の発散定理

**定理**：
$V$ を区分的に $C^1$ 級の閉曲面で囲まれた有界な連結開集合とし、
$\bm F(x, y, z)$ を $V \cup \partial V$ で定義されている $C^1$ 級関数（ベクトル場）とする。
次の等式が成り立つ：

$$
\tag*{$\clubsuit0$}
\iint_{\partial V}\! \bm F \cdot \bm n\,\mathrm dS
= \iiint_V\! \nabla \cdot \bm F\,\mathrm dV.
$$

ここで、ベクトル $\bm n$ は曲面 $\partial V$ の単位法線ベクトルであるとする。
$\mathrm dS$ は $\partial V$ の面素？

**証明の検討**：ベクトル解析の教科書でこの定理の証明をまともに扱うものは多くないと思われる。
さきほどの Green の定理もそうだ。したがって、ここでもその方針でやってみる。

Green のときのように、曲面を「天井」「床」に分割して関数で表せる場合を証明する。

まず三重積分のほうを成分ごとに表しておく：

$$
\def\iv#1{ \iiint_V\!\frac{\partial F_{#1}}{\partial {#1}}\,\mathrm dV }
\iiint_V\!\nabla \cdot \bm F\,\mathrm dV
= \iv{x} + \iv{y} + \iv{z}.
$$

二重積分のほうも成分ごとに表しておく：

$$
\def\is#1{ \iint_{\partial V}\! F_{#1} \bm e_{#1} \cdot \bm n\,\mathrm dS }
\iint_{\partial V}\! \bm F \cdot \bm n\,\mathrm dS
= \is x + \is y + \is z.
$$

主張の等式が正しいことを示すには次のものを示せば十分だ：

$$
\tag*{$\clubsuit1$}
\def\eq#1{
    \iint_{\partial V}\! F_{#1} \bm e_{#1} \cdot \bm n\,\mathrm dS
    = \iiint_V\!\frac{\partial F_{#1}}{\partial {#1}}\,\mathrm dV
}
\begin{aligned}
    \eq{x},\\
    \eq{y},\\
    \eq{z}.
\end{aligned}
$$

まず $x$ に関する等式を証明する。
曲面 $\partial V$ の「床」と「天井」を関数 $x = f_1(y, z), x = f_2(y, z)$ によって表せると仮定する
（これが特別な仮定だ）。三重積分は逐次積分に変換され、まず $x$ についてから積分するように書き換える：

$$
\begin{aligned}
\iiint_V\!\frac{\partial F_{x}}{\partial {x}}\,\mathrm dV
&= \iint_B\int_{f_1(y, z)}^{f_2(y, z)}\! F_x(x, y, z)\,\mathrm dx \,\mathrm dA.
\end{aligned}
$$

ここで $B$ は $V$ あるいは $\partial V$ を $yz$ 平面に射影して得られる領域だ。
$\mathrm dA$ はその面素とする（つまり $\mathrm dy \mathrm dz$ のはず）。

さて、曲面 $\partial V$ の「壁」の積分はゼロだ。なぜなら $\bm n$ と $\bm e_x$ が直交するので
$\bm n \cdot \bm e_x = 0$ であるからだ。というわけで「天井」と「床」だけ考えればいい。

「天井」を見る。「天井」の一点を指す位置ベクトル $\bm r$ を

$$\bm r = f_2(y, z)\bm e_x + y\bm e_y + z\bm e_z$$

と書ける。曲面の接ベクトルのベクトル積を計算すると：

$$
\begin{aligned}
    \frac{\partial \bm r}{\partial y} \times \frac{\partial \bm r}{\partial z}
    &= \left(\frac{\partial f_2}{\partial y}\bm e_x + \bm e_y\right) \times
       \left(\frac{\partial f_2}{\partial z}\bm e_x + \bm e_z\right)\\
    &= \left(\bm e_x - \frac{\partial f_2}{\partial y}\bm e_y - \frac{\partial f_2}{\partial z}\bm e_z\right).
\end{aligned}
$$

このベクトルは法線ベクトル $\bm n$ に平行である（長さは 1 とは限らない）。
さて、これと $\bm e_x$ との内積が 1 であることから：

$$
\begin{aligned}
\iint_{\partial V(t)}\! F_{x} \bm e_{x} \cdot \bm n\,\mathrm dS
&= \iint_{\partial V(t)}\! F_{x} \bm e_{x} \cdot \left(\frac{\partial \bm r}{\partial y} \times \frac{\partial \bm r}{\partial z}\right)\mathrm dS\\
&= \iint_B\! F_x(f_2(y, z), y, z)\,\mathrm dA.\\

\end{aligned}
$$

コメント：ここはもう少し言葉を補いたい。$\bm e_x \cdot \bm n \mathrm dS = \mathrm dA$ が示せればいい。

「床」についても同様に次を得る。ただし $\bm n$ は射影すると $x$ が負の向きであることを考慮して符号を決める：

$$
\iint_{\partial V(b)}\! F_{x} \bm e_{x} \cdot \bm n\,\mathrm dS
= -\iint_B\! F_x(f_1(y, z), y, z)\,\mathrm dA.
$$

「天井」と「床」をまとめて次を得る：

$$
\begin{aligned}
\iint_{\partial V}\!F_{x} \bm e_{x} \cdot \bm n\,\mathrm dS
&= \iint_{\partial V(t)}\!F_{x} \bm e_{x} \cdot \bm n\,\mathrm dS

+ \iint_{\partial V(b)}\!F_{x} \bm e_{x} \cdot \bm n\,\mathrm dS\\
&= \iint_B\! F_x(f_2(y, z), y, z)\,\mathrm dA

- \iint_B\! F_x(f_1(y, z), y, z)\,\mathrm dA\\
&= \iiint_V\! \frac{\partial F_x}{\partial x}\,\mathrm dV.
\end{aligned}
$$

残りの $y, z$ についても同様の推論で証明される。よって $\clubsuit1$ が成り立つ。

$\clubsuit1 \implies \clubsuit0$ より、定理の主張は成り立つ。
$\blacksquare$

## 参考資料

* 村上雅人著『なるほどベクトル解析』
* [16.9 The Divergence Theorem](https://www.whitman.edu/mathematics/calculus_online/section16.09.html)
