---
title: Galois 拡大の正規底 学習ノート
tags: math
---

Galois 論の教科書で後回しマークが付きがちな正規底についての学習ノート。

* $I_n$ で $n$ 次単位行列を表す。

## 正規底

$L/K$ を $n$ 次分離拡大、$\langle u_1, \dotsc, u_n \rangle$ を基底とする。

$L^{\prime}/K$ を $L$ を含む Galois 拡大とし、$L$ から $L^{\prime}$
の中への同型写像全体を $\lbrace \sigma_1, \dotsc, \sigma_n\rbrace$ とする。

$n$ 次正方行列 $A$ を $(i, j)$ 成分が $\operatorname{Tr}(u_iu_j)$ であるものとする：

$$
A \coloneqq (\operatorname{Tr}(u_iu_j)).
$$

トレースについては[以前のノート][trace]参照。とくに $A$ は正則かつ対称行列である。

**定義（分離拡大の基底に関する判別式）**：
$t_1, \dotsc, t_n \in L$ に対して次のようにおく：

$$
\begin{aligned}
D(t_1, \dotsc, t_n) &\coloneqq \det(\operatorname{Tr}(t_it_j)),\\
\Delta(t_1, \dotsc, t_n) &\coloneqq \det(\sigma_j(t_i)).
\end{aligned}
$$

この $D$ を拡大 $L/K$ の基底 $\langle u_1, \dotsc, u_n \rangle$ に関する**判別式**という。

----

**補題（判別式と $\Delta$ の関係）**：

$$
\tag*{$\spadesuit1$}
D(t_1, \dotsc, t_n) = \Delta(t_1, \dotsc, t_n)^2.
$$

**検討**：行列式の対象となる行列を直接計算する。
同型写像、対称行列の性質が効いている。

**証明**：

$$
\begin{aligned}
\operatorname{Tr}(t_it_j)
&=\left(\sum_{k = 1}^n \sigma_k(t_it_j)\right)\\
&= \begin{pmatrix}
\sigma_1(t_1) & \cdots & \sigma_n(t_1)\\
\sigma_1(t_2) & \cdots & \sigma_n(t_2)\\
\vdots & \ddots & \vdots\\
\sigma_1(t_n) & \cdots & \sigma_n(t_n)\\
\end{pmatrix}\!\!\!
\begin{pmatrix}
\sigma_1(t_1) & \cdots & \sigma_1(t_n)\\
\sigma_2(t_1) & \cdots & \sigma_2(t_n)\\
\vdots & \ddots & \vdots\\
\sigma_n(t_1) & \cdots & \sigma_n(t_n)\\
\end{pmatrix}.
\end{aligned}
$$

したがって $\spadesuit1$ が示された。
$\blacksquare$

----

**命題（分離拡大の基底の条件）**：$\langle t_1, \dotsc, t_n \rangle$ が $L/K$ の基底である条件は
$\Delta(t_1, \dotsc, t_n) \ne 0.$

**証明**：$\implies:$
$\langle t_1, \dotsc, t_n \rangle$ が $L/K$ の基底であると仮定する。
$\operatorname{Tr}(u_iu_j)$ が [非退化対称双線形形式][trace]であるから判別式

$$0 \ne D(t_1, \dotsc, t_n) = \Delta(t_1, \dotsc, t_n)^2.$$

したがって $\Delta(t_1, \dotsc, t_n) \ne 0$ が示された。
$\Box$

$\impliedby:$ $\Delta(t_1, \dotsc, t_n) \ne 0$ を仮定する。ある
$a_1, \dotsc, a_n \in K$ に対して

$$
\sum_{i = 1}^n a_it_i = 0
$$

であるとする。これがすべて $0$ に等しいことを示す。

この線形結合の各 $\sigma_i$ による像を考えれば
各 $j = 1, \dotsc, n$ に対して次が成り立つ：

$$
\sum_{j = 1}^na_j\sigma_i(t_j) = 0.
$$

したがって

$$
\begin{pmatrix}
\sigma_1(t_1) & \cdots & \sigma_1(t_n)\\
\sigma_2(t_1) & \cdots & \sigma_2(t_n)\\
\vdots & \ddots & \vdots\\
\sigma_n(t_1) & \cdots & \sigma_n(t_n)\\
\end{pmatrix}\!\!\!
\begin{pmatrix}
a_1 \\ a_2 \\ \vdots \\ a_n
\end{pmatrix}
= \bm 0.
$$

仮定より上の係数行列は正則である。ゆえにベクトルは零である。
したがって $\langle t_1, \dotsc, t_n \rangle$ は $K$ 上線形独立であることが示された。
$\blacksquare$

----

**定義（正規底）**：
$L/K$ を Galois 拡大、$G \coloneqq \operatorname{Gal}(L/K) = \lbrace \sigma_1, \dotsc, \sigma_n\rbrace$
とする。

$u \in L$ に対して
$\langle \sigma_1(u), \dotsc, \sigma_n(u) \rangle$ が $L$ の
$K$ ベクトル空間としての基底になるとき、これを Galois 拡大 $L/K$ の**正規底**という。

**例**：$\mathbb C/\R$ を $X^2 + 1$ の分解体と見る。
このとき $\operatorname{Gal}(\mathbb C/\R) = \lbrace 1, \operatorname{conj}\rbrace.$
$\mathbb C$ の $\R$ ベクトル空間としての基底 $\langle 1, \sqrt{-1} \rangle$ は正規底ではない。

$\langle 1 + \sqrt{-1}, 1 - \sqrt{-1} \rangle$ は正規底である。
なぜならこれはベクトル空間の基底である上に $u = 1 + \sqrt{-1}$ として

$$
1(u) = 1 + \sqrt{-1},\quad
\operatorname{conj}(u) = 1 - \sqrt{-1}
$$

あることによる。

----

次の定理が本節の目標だろう。

**定理（正規底の存在定理）**：Galois 拡大には正規底が存在する。

とくに $G \coloneqq \operatorname{Gal}(L/K)$ とおき
$K$ 上の群環を $K[G]$ で表すと $K[G]$-加群として

$$
K[G] \cong L.
$$

**検討**：

* 群環だの加群だの不慣れな概念が含まれている。
  * 群環は $\sum rg, r \in R, g \in G$ の形をする元からなる自由加群だ。
  * 自由加群とは基底を持つ加群だ。
  * $R$-加群はベクトル空間のようなものだと思って読む。係数を体ではなく環 $R$ にとる。
    本定理の条件では係数は体なのでほんとうにベクトル空間だ。
* 有限体と無限体とで分けて証明する。

**証明**：$K$ が有限体か無限体で場合分けをする。

**$K$ が有限体のとき**：有限次 Galois 拡大なので $G$ は巡回群である。
$n \coloneqq \lvert G \rvert = [L : K],$ $G = \langle \sigma \rangle$ とおく。

[Dedekind の補題][trace]から $1, \sigma, \sigma^2, \dotsc, \sigma^{n - 1}$
は $K$ 上線形独立である。$\sigma^n = 1$ であるから線形写像 $\sigma$ の最小多項式は
$X^n - 1$ であり、固有多項式と等しい。したがって線形代数の理論からベクトル空間
$L$ の $K$ 上のある基底 $\langle \alpha_1, \dotsc, \alpha_n \rangle$ が存在して、線形写像 $\sigma$
のこの基底に関する表現行列が次のように書ける：

$$
A \coloneqq \begin{pmatrix}
    \bm 0 & 1\\
    I_{n - 1} & \bm 0\\
\end{pmatrix}.
$$

巡回群の性質から

$$
\begin{aligned}
\alpha_2 &= \sigma(\alpha_1),\\
\alpha_3 &= \sigma(\alpha_2) = \sigma^2(\alpha_1),\\
\dots\\
\alpha_n &= \sigma(\alpha_{n-1}) = \sigma^{n-1}(\alpha_1)\\
\alpha_1 &= \sigma(\alpha_n)
\end{aligned}
$$

であるから、$\alpha \coloneqq \alpha_1$ に対して

$$
\langle \alpha, \sigma(\alpha), \sigma^2(\alpha), \dotsc, \sigma^{n-1}(\alpha) \rangle
$$

は有限次 Galois 拡大 $L/K$ の正規底である。
したがって有限次 Galois 拡大には正規底が存在することが示された。
$\Box$

**$K$ が無限体のとき**：$G \coloneqq \lbrace 1 = \sigma_1, \dotsc, \sigma_n\rbrace$ とおく。
$\lbrace \sigma_1(\theta), \dotsc, \sigma_n(\theta)\rbrace$ が $K$ 上線形独立となる $\theta \in L$ を見つける。

写像 $\sigma_i$ に対して変数 $X_{\sigma_i}$ を対応させる。
その上で多項式 $f(X_{\sigma_1}, \dotsc, X_{\sigma_n})$ を次で定める：

$$
f(X_{\sigma_1}, \dotsc, X_{\sigma_n}) \coloneqq \det \begin{pmatrix}X_{\sigma_i^{-1}\sigma_j}\end{pmatrix}.
$$

$f(1, 0, \dotsc, 0) = \det I_n = 1$ ゆえ $f$ は恒等的にゼロではない。

$L/K$ の基底の一つを $\langle \alpha_1, \dotsc, \alpha_n \rangle$ とし、
$x_1, \dotsc, x_n$ を変数とする。さらに：

$$
\tag*{$\spadesuit2$}
\def\eq#1{ \sigma_{#1}(\xi)&= \sum_{i = 1}^n x_i\sigma_{#1}(\alpha_i) }
\begin{aligned}
\eq{1},\\
\eq{2},\\
\dots\\
\eq{n}.
\end{aligned}
$$

とおく。$\langle \alpha_1, \dotsc, \alpha_n \rangle$
が基底であることから命題（分離拡大の基底の条件）により：

$$
\det\begin{pmatrix}\sigma_i(\alpha_j)\end{pmatrix} \ne 0.
$$

つまり $\spadesuit2$ は変数変換として成立している。
$X_{\sigma_i} \coloneqq \sigma_i(\xi)$ とおけば
$f$ は $x_i$ の関数 $g$ として次の形に書け、恒等的にゼロとはならない：

$$
f(X_{\sigma_1}, \dotsc, X_{\sigma_n}) = g(x_1, \dotsc, x_n).
$$

$K$ には元が無数にあるので、ある $a_1, \dotsc, a_n \in K$ が存在して
$g(a_1, \dotsc, a_n) \ne 0.$
この $a_i$ を使って $\theta \coloneqq \sum a_i\alpha_i$ とおくと
$\langle \sigma_1(\theta), \dotsc, \sigma_n(\theta) \rangle$
が求める正規底であることを示す。

ある $c_i \in K$ が存在して $\sum c_i\sigma_i(\theta) = 0$ が成り立つとする。
任意の $j = 1, \dotsc, n$ に対して $\sigma_j^{-1}$ を考えると
$\sum c_i\sigma_j^{-1}\sigma_i(\theta) = 0.$
すなわち

$$
\def\row#1{ \sigma_{#1}^{-1}\sigma_1(\theta) & \cdots & \sigma_{#1}^{-1}\sigma_n(\theta) }
\begin{pmatrix}
\row{1}\\
\vdots & \ddots & \vdots\\
\row{n}
\end{pmatrix}\!\!\!
\begin{pmatrix}
    c_1 \\ \vdots \\ c_n
\end{pmatrix}
= \bm 0.
$$

左辺の正方行列を $B$ とおく。$\det B = g(a_1, \dotsc, a_n) \ne 0$
だから $B$ は正則。したがって $c_i = 0.$
つまり $\sigma_i(\theta)$ は線形独立。

したがって $\langle \sigma_1(\theta), \dotsc, \sigma_n(\theta) \rangle$
は正規底であることが示された。
$\Box$

$K$ 上の線形写像

$$
\begin{array}{c}
K[G] & \longrightarrow & L\\
\\
\sum a_\sigma \sigma & \longmapsto & \sum a_\sigma\sigma(\theta)
\end{array}
$$

が $K[G]$-加群としての同型 $K[G] \cong L$ を与える。
$\blacksquare$

## 参考

* 桂利行著『代数学 III 体とガロア理論』
* 雪江明彦著『環と体とガロア理論』

[trace]: {% post_url 2020/01/2020-01-25-trace-norm %}
