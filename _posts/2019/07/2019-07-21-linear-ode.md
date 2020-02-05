---
title: 『常微分方程式』学習ノート Part 5
tags: math
---

高崎金久著『常微分方程式』（日本評論社）ノートその五。第 6 章。

# 第 6 章 線形連立一階系

次の記号を用いる：

$$
\begin{aligned}
\bm y^\prime &= A(x)\bm y + \bm b(x),\\

\def\arraystretch{1.5}
A(x) &= \begin{pmatrix}
a_{11}(x) & \dots & a_{1n}(x)\\
\vdots & \ddots & \vdots\\
a_{n1}(x) & \dots & a_{nn}(x)
\end{pmatrix}\!,\\

\bm y &= \begin{pmatrix}
y_1\\
\vdots\\
y_n
\end{pmatrix}\!,
\\
\bm b(x) &= \begin{pmatrix}
    b_1(x)\\
    \vdots\\
    b_n(x)
\end{pmatrix}\!.
\end{aligned}
$$

これまでと同様に、最初の方程式を非同次系、$\bm b(x) \equiv 0$ と置き変えたものをその同次形とそれぞれ呼ぶ。

## §6.1 線形連立一階系の一般的性質

* 同次形の解空間はベクトル空間である。その基底を基本解系と呼ぶ。
* 同次形の任意の解は次の形をしている：

  $$
  \bm y = c_1 \bm u_1(x) + \dotsb + c_n \bm u_n(x),
  $$

  * ここで解 $\bm u_i(x)$ は初期条件 $\bm u_i(x_0) = \bm e_i$ を満たす。
    * $x = x_0$ は関数の定義域内の点であるとする。
    * $e_i$ は正規直交基底の $i$ 番目のベクトルであるとする。
  * 各 $c_j\;(j = 1, \dotsc, n)$ は定数である。

* **基本解行列**とは、基本解系を並べた行列である：

  $$
  U(x) \coloneqq \begin{pmatrix}
      \bm u_1(x) & \dots & \bm u_n(x)
  \end{pmatrix}
  $$

  * $U(x)$ は正則である。ベクトル空間の基底を全部並べたのだから当然そうなる。
  * $\displaystyle \frac{\mathrm{d}U(x)}{\mathrm{d}x} = A(x)U(x).$ $u_i(x)$ が基本解であることによる。
  * $U(x_0) = I_n.$ $u_i(x)$ の初期値条件による。
  * そして以下の性質がある：
    * $\displaystyle \frac{\mathrm{d}U(x)^{-1}}{\mathrm{d}x} = -U(x)^{-1}A(x).$
    * $\displaystyle \frac{\mathrm{d}}{\mathrm{d}x}\det U(x) = \operatorname{tr}A(x)\det{U(x)}.$
    * 同次形の一般解は $\bm y = U(x)\bm c,$ ここで $\bm c$ は定ベクトルである。
    * 解空間の基底変換は、$U(x)$ に対して右から正則行列を乗じることに相当する。
      そうして得られる基底もまた基本解行列である。

次に定数変化法による非同次形の一般解について考える。

* $\bm y = U(x)\bm c$ に代えて、$\bm y = U(x)\bm z(x)$ の形が一般解であると仮定する。
* それを微分する：

  $$
  \begin{aligned}
  \bm y^\prime &= U^\prime(x)\bm z(x) + U(x)\bm z^\prime(z)\\
  &= A(x)U(x)\bm z(x) + U(x)\bm z^\prime(z)\\
  &= A(x)\bm y + U(x)\bm z^\prime(z)\\
  \end{aligned}
  $$

  $\bm b(x) = U(x)\bm z^\prime(z)$ が必要であることがわかった：

  $$
  \therefore \bm z^\prime(z) = U(x)^{-1}\bm b(x).\\
  $$

  $\bm y = U(x)\bm z(x)$ の不定積分をとる：

  $$
  \begin{aligned}
  \bm y &= U(x)\left(\int_{x_0}^x\! U(\tau)^{-1} \bm b(\tau)\,\mathrm d\tau + \bm c\right)\\
  &= \int_{x_0}^x\! U(x)U(\tau)^{-1}\bm b(\tau)\,\mathrm d\tau + U(x)\bm c.
  \end{aligned}
  $$

  * 第一項が非同次形の特殊解である。
    * 被積分関数の行列の積の部分が Green 関数と呼ばれるものになる。
  * 第二項が同次形の一般解である。
  * コメント：線形 ODE の一般解がこの構成であることを覚えておくこと。

次に高階線形 ODE $A(x, D)y = b(x)$ を連立一階系に書き直すことを考える：

$$
\begin{aligned}
y_1 &\coloneqq y,\\
y_2 &\coloneqq y^\prime,\\
&\vdots\\
y_n &\coloneqq y^{(n-1)}.
\end{aligned}
$$

非同次形における各構成要素の中身はこうなる：

$$
\begin{aligned}
\def\arraystretch{1.5}
A(x) &= \begin{pmatrix}
0 & 1 & 0 & \dots & 0\\
0 & 0 & 1 & \dots & 0\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
0 & 0 & 0 & \dots & 1\\
-a_n(x) & -a_{n-1}(x) & -a_{n-2}(x) & \dots & a_1(x)
\end{pmatrix}\!,\\

\bm b(x) &= \begin{pmatrix}
    0\\
    0\\
    \vdots\\
    b(x)
\end{pmatrix}\!,
\\
\bm u_i(x) &= \begin{pmatrix}
    u_i(x)\\u_i^\prime(x)\\\vdots\\u_i^{(n-1)}(x)
\end{pmatrix}\!,\quad (i = 1, \dotsc, n - 1).
\end{aligned}
$$

* $U(x)$ の中身が Wroński 行列式の中身と一致していることに注意。

## §6.2 定数係数線形連立一階系の基本解行列

$$
\begin{aligned}
\bm y^\prime &= A\bm y + \bm b(x),\\

\def\arraystretch{1.5}
A(x) &= \begin{pmatrix}
a_{11} & \dots & a_{1n}\\
\vdots & \ddots & \vdots\\
a_{n1} & \dots & a_{nn}
\end{pmatrix}\!.\\
\end{aligned}
$$

* 当然同次形の解をまず考える。そして
  $\bm y^\prime = A\bm y$ の基本解行列は $\mathrm{e}^{Ax}$ である。ただし：

  $$
  \mathrm{e}^{Ax} \coloneqq \sum_{k = 0}^\infty \frac{x^k}{k!}A^k.
  $$

  * この行列は成分ごとに絶対収束する。証明方法：行列に対する最大値ノルム $\Vert \cdot \rVert$ を導入して、級数の項の $(i, j)$ 成分が
    $\mathrm{e}^{n \lVert A \rVert x}$ で押さえられることを示す。
* 初期条件 $U(x_0) = I$ を満たす同次形の基本解行列 $U(x)$ は次で与えられる：

  $$
  U(x) = \mathrm{e}^{A(x - x_0)}.
  $$
* 行列 $e^A$ の性質
  * 正方行列 $A$ と $B$ が可換ならば次が成り立つ：

    $$
    \mathrm{e}^A \mathrm{e}^B = \mathrm{e}^B \mathrm{e}^A = \mathrm{e}^{A + B}.
    $$

  * $e^A$ は正則である： $(\mathrm{e}^A)^{-1} = \mathrm{e}^{-A}.$
  * 正方行列 $A$ と正則行列 $P$ について次が成り立つ：

    $$
    P \mathrm{e}^A P ^{-1} = \mathrm{e}^{PAP^{-1}}.
    $$

以下、$e^A$ の計算方法について考える。ここからは線形代数。

* 正方行列 $A$ を対角化できるものなら、次のようになる：
  * $\exists B \exists P (A = PBP ^{-1});$ $B$ は対角行列、$P$ は基本行列。
  * 次のように簡単に求められる：

    $$
    \begin{aligned}
    \mathrm{e}^A &= P \mathrm{e}^B P ^{-1}\\
    &= P \operatorname{diag}(
        \mathrm{e}^{b_1} & \dots & \mathrm{e}^{b_n}
    )P^{-1}.
    \end{aligned}
    $$

* $A$ を対角化できない場合は Jordan 標準形を利用するしかない：
  * $\exists B \exists J (A = PJP ^{-1});$
    * $P$は基本行列。
    * $J$ は Jordan 標準形の行列で $J = \operatorname{diag}(J_1, \dotsc, J_s)$ とする。
      ここで各 $J_k$ は Jordan ブロックである。
  * 次のように $e^A$ を求められる：

    $$
    \begin{aligned}
    \mathrm{e}^A &= P \mathrm{e}^J P ^{-1}\\
    &= P \operatorname{diag}(\mathrm{e}^{J_1}, \dotsc, \mathrm{e}^{J_s})P ^{-1}.
    \end{aligned}
    $$

  * コメント：解が求まるとはいえ、Jordan 標準形の計算そのもののほうがむしろ難度が高い。
    本文では一般固有空間や Jordan 分解の話題まで出てきているくらいだ。

以上で第 6 章のノートを終わる。次回は ODE の解の存在性と一意性の証明に取り組みたい。
