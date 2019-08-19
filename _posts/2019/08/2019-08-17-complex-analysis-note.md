---
title: 『新訂解析学』学習ノート第二回
---

熊野啓作著『新訂解析学』の学習ノート第二回。

# 一次分数変換

コメント：先に群論の入門部分を学習しておくとよい。

## 一次分数変換

$$
w = f(z) = \frac{\alpha z + \beta}{\gamma z + \delta},\quad \alpha\delta - \beta\gamma \ne 0.
$$

* このような関数 $f$ 全体の集合 $G$ は、関数の合成を演算とする群をなす。
  恒等写像もこの条件を満たし、$f^{-1}$ もこの形になり $G$ に含まれる。
  これを**一次分数変換群**などと呼ぶ。

* 複素平面上の平行移動、回転移動、相似変換、反転、対称移動は一次分数変換として表せる。
  * 平行移動は $z \longmapsto z + \mu$ の形をしている。
  * 平行移動を表す変換の集合は $G$ の部分群になり $(\Complex, +)$ と同型。
  * 回転・相似変換は $z \longmapsto \lambda z \quad (\lambda \ne 0)$ の形。
  * 回転移動と相似変換（とそれらの合成）からなる変換の集合も部分群であり $(\Complex^\times, \cdot)$ と同型。
  * 反転・対称変換は $z \longmapsto \dfrac{1}{z}$ である。
  * そして、$\forall f \in G$ はこれらの合成で表現される：

    $$
    \frac{\alpha z + \beta}{\gamma z + \delta} =
    \begin{dcases}
        \frac{\alpha}{\gamma} - (\alpha\delta - \beta\gamma)\frac{1}{\gamma z + \delta}, & \gamma \ne 0,\\
        \frac{\alpha}{\delta} + \frac{\beta}{\delta},& \gamma = 0.
    \end{dcases}
    $$

* $GL(2, \Complex)$ は $G$ と準同型である。ただし単射ではない。

  $$
  \varphi\colon
  \begin{pmatrix}
      \alpha & \beta\\
      \gamma & \delta
  \end{pmatrix}
  \longmapsto
  \left(z \longmapsto \frac{\alpha z + \beta}{\gamma z + \delta}\right)
  $$

* そこで $GL(2, \Complex)$ の部分群 $SL(2, \Complex)$ を考える。
  行列式が 1 のものに制限したため、定数倍の問題がかなり緩和される。
* ここで準同型定理より同型が得られる：

  $$
  PSL(2, \Complex) := SL(2, \Complex)/\ker\varphi|_{SL} \cong \operatorname{im}\varphi|_{SL} = G.
  $$

## 円円対応

* 円を一次分数変換すると、やはり円になる。
  * コメント：$\alpha\delta - \beta\gamma \ne 0$ が効いている。
* **非調和比**
  * 相異なる四つの複素数から得られる複素数である：

    $$
    [z_1, z_2; z_3, z_4] := \frac{z_1 - z_3}{z_1 - z_4}/\frac{z_2 - z_3}{z_2 - z_4}.
    $$

  * 四つのうちちょうど一つは $\infty$ であってもよい。
  * 非調和比は一次分数変換で不変である。
  * (Th 4.4) 非調和比が実数であることと、四点を通過する円が存在することは同値である。
    * 証明概略：偏角を考える。円周角の定理の逆などから円の存在が示される。
* **鏡像**の位置
  * $z_1, z_2 \in \Complex$ がある円または直線に関して互いに鏡像の位置にあるとは、次の状態を意味するものとする：
    * 二点を通過する円が存在して、この円または直線に直交する。
  * (Th 4.5) 一次分数変換 $g,$ 点 $z,$ 円 $C$ について、$z$ の $C$ に関する鏡像を $z^\prime$ とする。
    このとき $g(z)$ と $g(z^\prime)$ は鏡像の位置にある。

### 一次分数変換群

以下 Riemann 球面を $P^1(\Complex)$ で表す。

* 一次分数変換 は $P^1(\Complex)$ 上の変換とみなせる。
* $G$ は $P^1(\Complex)$ に**推移的に作用する**：

  $$
  \forall z_1 \forall z_2(
      z_1 \in P^1(\Complex) \land z_2 \in P^1(\Complex) \implies
      \exists g(g \in G \land g(z_1) = z_2)).
  $$

  * 証明：次のように $g_w \in G$ をとる：

    $$
    g_w(z) =
    \begin{dcases}
        \frac{z + w}{z + 1}, & w \notin \{1, \infty\},\\
        \frac{2z + 1}{z + 1}, & w = 1,\\
        \frac{z - 1}{z}, & w = \infty.
    \end{dcases}
    $$

    $g_w(0) = w,\; g_1(0) = 1,\; g_\infty(0) = \infty$ に注意すると
    $g$ を決定できる：

    $$
    g = g_{z_2} \circ g_{z_1}^{-1}.
    $$

* **等質空間**（商空間）
  * $SL(2, \Complex)$ における $0 \in P^1(\Complex)$ の固定部分群を $B$ とする：

    $$
    B = \left\{
        \begin{pmatrix}
            \alpha & 0\\
            \gamma & \delta
        \end{pmatrix}
        \in SL(2, \Complex)
        \left.  \right\vert \left. \alpha\delta = 1 \right.\right\}.
    $$

  * $P^1(\Complex) = G/B.$
  * $SL(2, \Complex)$ は $\Complex^2$ に自然に作用する。
    * $\Complex^2$ のベクトルの成分同士の商 $z$ を考えて $P^1(\Complex)$ に写す（射影）と、$G$ が自然に現れる。

      $$
      SL(2, \Complex) \ni
      \begin{pmatrix}
          1 & z\\
          0 & 1
      \end{pmatrix}
      B
      \longmapsto
      g
      \begin{pmatrix}
          1 & z\\
          0 & 1
      \end{pmatrix}
      B
      =
      \begin{pmatrix}
          1 & g(z)\\
          0 & 1
      \end{pmatrix}
      \in SL(2, \Complex).
      $$

    * 話が見えない？

      $$
      \begin{pmatrix}
      \alpha & \beta\\
      \gamma & \delta
      \end{pmatrix}
      =
      \def\arraystretch{2.0}
      \begin{pmatrix}
      1 & \dfrac{\beta}{\delta}\\
      0 & 1
      \end{pmatrix}
      \begin{pmatrix}
      \dfrac{1}{\delta} & 0\\
      \gamma & \delta
      \end{pmatrix}
      \in SL(2, \Complex)/B.
      $$

      ベクトル $(\beta, \gamma)$ が本来の $P^1(\Complex)$ の元と考えられ、
      商 $\beta/\gamma$ は Riemman 球面上にあるか、$\infty$ である。

    * コメント：次の対応関係に注意：

      $$
      z \longleftrightarrow
      \begin{pmatrix}
          1 & z\\
          0 & 1
      \end{pmatrix}B,
      \quad
      g(z) \longleftrightarrow
      g
      \begin{pmatrix}
          1 & z\\
          0 & 1
      \end{pmatrix}B.
      $$

# 複素積分

## 線積分

積分の定義：

$$
\int_C\!f(z)\mathrm dz = \int_a^b\!f(z(t))z^\prime(t)\,\mathrm dt.
$$

曲線 $C$ のパラメーター $t$ までの長さ：

$$
s(t) = \int_a^t\!\lvert z^\prime(t)\rvert\,\mathrm dt.
$$

* 全長は $s(b)$ であるが、これを $\displaystyle \int_C\!\lvert \mathrm dz\rvert$ と書くことがある。
* (E 5.1) 単位半円弧上で $f(z) = \dfrac{1}{z}$ を積分する。すると、上半分と下半分とで値が異なる。
* (E 5.3) 円 $\lvert z - z_0 \rvert = r$ 上で $f(z) = (z - z_0)^n$ を積分する。

  $$
  \begin{aligned}
  \int_C\! \frac{\mathrm dz}{z}
  &= \int_0^{2\pi}\!(r \mathrm{e}^{it})^n ir \mathrm{e}^{it}\,\mathrm dt\\
  &= ir^{n + 1} \int_0^{2\pi}\! \mathrm{e}^{i(n+1)t}\, \mathrm dt\\
  &=
  \begin{dcases}
      i\int_0^{2\pi}\!\mathrm dt = 2\pi i, & n = -1,\\
      ir^{n+1}\left[\frac{\mathrm e^{i(n+1)t}}{i(n+1)}\right]_0^{2\pi} = 0, & n \ne -1.
  \end{dcases}
  \end{aligned}
  $$

* (E 5.4) $z^n$ の積分。省略。
* (C 5.1) $f(z)$ が定義領域内で原始関数をもつならば、その領域内にある任意の閉曲線 $C$ に対して線積分はゼロである。
* 不定積分を線積分で定義したいが、実数のときと異なり経路が一意的に定まらない。経路に依存して値が決まる可能性がある。

  もし連続関数 $f(z)$ に対して固定した点 $\alpha \in D$ と任意の点 $z \in D$ を結ぶ曲線 $C$ に沿った線積分の値が
  $C$ に依らず終点 $z$ だけで定まるとき、不定積分 $F(z)$ を定められる：

  $$
  F(z) = \int_C\!f(z)\,\mathrm dz = \int_a^z\!f(z)\,\mathrm dz.
  $$

* (L 5.2) 関数 $f(z)$ に不定積分 $F(z)$ が存在するならば、$F(z)$ は正則であり、$F^\prime(z) = f(z)$ が成り立つ。
* (Th 5.2) 連続関数 $f(z)$ が定義領域 $D$ 内の任意の閉曲線 $C$ に対して

  $$
  \int_C\!f(z)\,\mathrm dz = 0
  $$

  であれば、$f(z)$ は不定積分をもつ。

## Green の公式

* (Th 5.3) $P(x, y), Q(x, y)$ は閉領域 $D \cup \partial D$ において $C^1$ 級であるとする。
  このとき次の等式が成り立つ：

  $$
  \int_{\partial D}\!P(x, y)\,\mathrm dx + Q(x, y)\,\mathrm dy
  = \iint_{D}\!\left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\!\mathrm dx \mathrm dy.
  $$

  * コメント：微分形式の Stokes の定理によると：

    $$
    \begin{aligned}
    \int_{\partial D}\!P(x, y)\,\mathrm dx + Q(x, y)\,\mathrm dy
    &= \iint_D\!\mathrm d \left(P(x, y)\,\mathrm dx + Q(x, y)\,\mathrm dy\right)\\
    &= \iint_D\!\mathrm dP \wedge \mathrm dx + \mathrm dQ \wedge \mathrm dy\\
    &= \iint_D\!(P_x \,\mathrm dx + P_y \,\mathrm dy) \wedge \mathrm dx
        + (Q_x \,\mathrm dx + Q_y \,\mathrm dy)\wedge \mathrm dy\\
    &= \iint_D\!P_y \,\mathrm dy \wedge \mathrm dx
        + Q_x \,\mathrm dx \wedge \mathrm dy\\
    &= \iint_D\!(Q_x - P_y)\,\mathrm dx \wedge \mathrm dy.
    \end{aligned}
    $$

* (C 5.2) 閉領域の面積は次である：

  $$
  S = \frac{1}{2}\int_{\partial D}\!-y\,\mathrm dx + x\,\mathrm dy.
  $$

  * コメント：微分形式の Stokes の定理によると：

    $$
    \begin{aligned}
    \frac{1}{2}\int_{\partial D}-y \mathrm dx + x \mathrm dy
    &= \frac{1}{2} \iint_D\! \mathrm d(-y \mathrm dx + x \mathrm dy)\\
    &= \frac{1}{2} \iint_D\! - \mathrm dy \wedge \mathrm dx + \mathrm dx \wedge \mathrm dy\\
    &= \iint_D\!\mathrm dx \wedge \mathrm dy\\
    &= S.
    \end{aligned}
    $$

----

第三回へ続く。
