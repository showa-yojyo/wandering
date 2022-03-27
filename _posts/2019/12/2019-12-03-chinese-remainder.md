---
title: 中国剰余定理学習ノート
mathjax: true
tags: math
---

群と環の中国剰余定理の証明を検討するためのノート。

## 中国剰余定理 1: 剰余群の直積の場合

**定理**：$m, n$ を互いに素な正の整数とする。このとき次が成り立つ：

$$
\tag*{$\spadesuit1$}
\def\S#1{ \Z/{#1}\Z }
\S{mn} \cong \S{m} \times \S{n}.
$$

ここで各剰余群は加法群とする。

**検討**：

* 群の準同型定理を用いて証明する。核と像の性質を利用する。
* 実は逆も成り立つ。

**証明**：

準同型写像 $\def\S#1{ \Z/{#1}\Z } f\colon \Z \longrightarrow \S{m} \times \S{n}$ を次で定める：

$$
f(x) = (x + m\Z, x + n\Z).
$$

この核が $mn\Z$ であるので（ここに $m, n$ が互いに素という条件を用いた）、準同型定理により $\Z/mn\Z \cong \operatorname{im}f.$
以下、元の個数を確認することにより $\operatorname{im}f = m\Z \times n\Z$ を示す。

* 準同型定理の同型関係より $\lvert \operatorname{im}f \rvert = mn.$
* 準同型の像としての性質より $\operatorname{im}f \subset \Z/m\Z \times \Z/n\Z.$
* $\lvert \Z/m\Z \times \Z/n\Z \rvert = mn.$

以上より $\operatorname{im}f = m\Z \times n\Z.$
これと準同型定理による同型関係により $\spadesuit1$ は成り立つ。
$\blacksquare$

## 中国剰余定理 2: 剰余群の直積複数の場合

**定理**：$r \ge 2$ とし、$m_1, m_2, \dotsc, m_r$ を互いに素な正の整数とする。
積を $m \coloneqq m_1 m_2 \dotsm m_r$ とおく。このとき次の関係が成り立つ：

$$
\tag*{$\spadesuit2$}
\def\S#1{ \Z/{#1}\Z }
\S{m} \cong \S{m_1} \times \S{m_2} \times \dotsb \times \S{m_r}.
$$

ここで各剰余群は加法群とする。

**検討**：二個の直積で成り立つことと、互いに素な条件と数学的帰納法を組み合わせて証明する。

**証明**：数学的帰納法により証明する。

$r = 2$ のときは前節の定理である。

一般の場合については、素数 $m_1$ と別の相異なる素数同士の積 $m_2 \dotsm m_r$ とが互いに素であるので、

$$
\def\S#1{ \Z/{#1}\Z }
\S{m} \cong \S{m_1} \times \S{(m_2\dotsm m_r)}.
$$

数学的帰納法を右辺第二項に適用して：

$$
\def\S#1{ \Z/{#1}\Z }
\S{(m_2\dotsm m_r)} \cong \S{m_2} \times \dotsb \times \S{m_r}.
$$

群の直積の同型は結合律が成り立つので、これらから $\spadesuit2$ が成り立つ。
$\blacksquare$

## 中国剰余定理 3: イデアルの直積の場合

**定理**：$A$ を 1 を持つ可換環とし、$I, J$ は $A$ のイデアルであって
$I + J = A$ を満たす。写像 $\varphi\colon A \longrightarrow A/I \times A/J$
を

$$
\varphi(x) = (x + I, x + J)
$$

で定める。このとき写像 $\varphi$ は全射な環の準同型写像であり、次の同型を与える：

$$
\tag*{$\spadesuit3$}
A \cong A/I \times A/J
$$

**検討**：
教科書にあるように $I + J = A \implies I \cap J = IJ.$

証明のプロット：まず写像が環の準同型写像であることを示す。
次に準同型定理を適用して、$\spadesuit3$ の式を導く。
準同型の核と像がどうなるかというのが本定理の急所だ。

**証明**：
まず写像 $\varphi$ が環の準同型写像であることを示す。
任意の $x, y \in A$ に対して次が成り立つ：

$$
\begin{aligned}
\varphi(x + y) &= (x + y + I, x + y + J)\\
&= (x + I, x + J) + (y + I, y + J)\\
&= \varphi(x) + \varphi(y).\\
\varphi(xy) &= (xyI, xyJ)\\
&= (xI, xJ)(yI, yJ)\\
&= \varphi(x)\varphi(y).\\
\varphi(1) &= (1 + I, 1 + J) = 1_{A/I \times A/J}.\\
\end{aligned}
$$

したがって写像 $\varphi$ は環の準同型写像である。

写像 $\varphi$ の核は $\ker\varphi = I \cap J = IJ.$

写像 $\varphi$ の像は $\varphi$ が全射ならば $A/I \times A/J$ であると言えるので、それを示す。

$(p + I, q + J) \in A/I \times A/J$ を任意にとる。ここで
$p \in A, q \in A, p + I \in A/I, q + J \in A/J$ を意味するものとする。
以下、$A$ の元 $z$ で $\varphi(z) = (p + I, q + J)$ を満たすものが存在することを示す。

$I + J = A$ と仮定したので $a + b = 1$ を満たす $a \in I, b \in J$ が存在する。
ここで $z \coloneqq bp + aq$ とおく。このとき：

$$
\begin{aligned}
    z - p &= (bp + aq) - p\\
    &= (b - 1)p + aq\\
    &= -ap + aq\\
    &= a(q - p) = (q - p)a \in I.
\end{aligned}
$$

よって $z$ の剰余類と $p$ の剰余類はイデアル $I$ に関して等しい：$z + I = p + I.$
同様に $z + J = q + J.$ したがって、

$$
\varphi(z) = (z + I, z + J) = (p + I, q + J).
$$

すなわち $\varphi$ は全射であることが示された。したがって $\operatorname{im}\varphi = A/I \times A/J.$

以上を環の準同型定理に適用して：

$$
A/\ker\varphi = A/(IJ) \cong \operatorname{im}f = A/I \times A/J.
$$

したがって $\spadesuit3$ が成り立つ。
$\blacksquare$

## 中国剰余定理 4: 標準的な中国剰余定理

**定理**：$n \ge 2$ とする。$A$ を 1 を持つ可換環、
$I_1, I_2, \dotsc, I_n$ は $A$ のイデアルであって、
任意の相異なる $i$ と $j$ に対して $I_i + I_j = A$ が成り立つ。

このとき次の環の同型が存在する：

$$
\tag*{$\spadesuit4$}
A/(I_1I_2\dotsm I_n) \cong A/I_1 \times A/I_2 \times \dotsb \times A/I_n.
$$

**検討**：

* $n = 2$ のときの証明で本質的だった関係式の一般版 $\bigcap_i I_i = I_1I_2 \dotsm I_n$ を示す。
* 写像 $\varphi\colon A \longrightarrow A/I_1 \times A/I_2 \times \dotsb \times A/I_n$ を、
  核と像を吟味すれば準同型定理が $\spadesuit4$ の形に適用できるように定義する。

**証明**：
気が向いたらやる。

## 参考資料

* 川口周著『代数学入門』
