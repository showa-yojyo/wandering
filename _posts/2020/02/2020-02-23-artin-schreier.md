---
title: Artin-Schreier 拡大学習ノート
mathjax: true
tags: math
---

Galois 論の教科書の最後の方にある理論に関する学習ノートだ。
教科書によって定義からアプローチが異なっていて困惑するところが多い。

* $p$ を素数とする。
* $Z_n$ を $n$ 次巡回群とする： $Z_n \cong \Z/n\Z.$

## Artin-Schreier 拡大

**定義**：標数 $p \ne 0$ の体 $K$ の Galois 拡大 $L/K$ が

* **Artin-Schreier 拡大**であるとは、$\operatorname{Gal}(L/K)$
  が $Z_p$ のいくつかの直積と同型であるようなものをいう。
* **巡回 Artin-Schreier 拡大**であるとは、$\operatorname{Gal}(L/K)$
  が $Z_p$ と同型であるようなものをいう。

----

かんたんなほうから構造を調べる。

**補題（巡回 Artin-Schreier 拡大の構造）**：$K$ を標数 $p$ の体とする。
$a \in K$ に対し、多項式 $X^p - X - a = 0$ は既約であるか、一次式因子の積に分解するかのいずれかである。

**検討**：次の写像 $\wp$ は加法群の準同型写像であり、その核は $\mathbb F_p$ になる：

$$
\def\arraystretch{1.4}
\begin{array}{rrccc}
\wp\colon & K & \longrightarrow & K\\
& a & \longmapsto & a^p - a\\
& \dfrac{1}{\wp}a & \longmapsto & a
\end{array}
$$

この準同型写像を $\overline K \longrightarrow \overline K$ に延長する。
このとき $\wp(\alpha) = a$ となる $\alpha \in \overline K$ の一つを
$\dfrac{1}{\wp}a$ と書けば、残りの逆像は次で与えられる：

$$
\def\a{ \frac{1}{\wp}a }
\a, \a + 1, \a + 2, \dotsc, \a + p - 1.
$$

**証明**：$\alpha \in \overline K$ を与えられた多項式の根の一つとする。
検討から

$$
\alpha \longmapsto \alpha + 1
$$

は根の置換を引き起こすことが言える：与えられた多項式の $K$ 上の既約因子
$g(X)$ に対してある $i \in \N$ があってどの既約因子も $g(X + i)$ と書ける。
つまり既約因子同士の次数は等しい。

与えられた多項式の次数が素数であることから、既約因子の次数は $p$ または $1$ である。

したがって与えられた多項式は既約であるか、一次式因子の積に分解するかのいずれかであることが示された。
$\blacksquare$

----

**定理（巡回 Artin-Schreier 拡大の条件）**：
拡大 $L/K$ が巡回 Artin-Schreier 拡大である条件は、ある
$a \in K$ が存在して $L$ が $K$ 上の既約多項式 $X^p - X - a$ の最小分解体である。

**証明**：$\implies:$
$\operatorname{Gal}(L/K) \cong Z_p$ を $\langle \sigma \rangle$ とおく。
$\operatorname{Tr} _ {L/K}1 = 0$ を利用して [$H^1 = 0$][Hilbert] 定理の系から
ある $\alpha \in L$ が存在して次を満たす：

$$
1 = \sigma(\alpha) - \alpha.
$$

$[L : K] = p$ は素数だから $L = K(\alpha).$
$a \coloneqq \alpha^p - \alpha$ とおく。

$$
\begin{aligned}
\sigma(a) &= \sigma(\alpha^p - \alpha)\\
&= \sigma(\alpha^p) - \sigma(\alpha)\\
&= (\alpha^p + 1) - (\alpha + 1)\\
&= \alpha^p - \alpha = a.
\end{aligned}
$$

$a$ は $\sigma$ で不変であるから $a \in K.$
よって $\alpha$ は $K$ 上の既約多項式 $X^p - X - a$ の零点である。
したがって $L$ は $K$ 上の既約多項式 $X^p - X - a$ の最小分解体であることが示された。
$\Box$

$\impliedby:$ 根の一つを $\alpha$ とする。上で述べたようにすべての根は次である：

$$
\def\a{ \alpha }
\a, \a + 1, \a + 2, \dotsc, \a + p - 1.
$$

$L = K(\alpha)$ であり、$[L : K] = p.$
$\sigma \in \operatorname{Aut} _ K(L)$ について

$$
\begin{array}{c}
\sigma\colon & L & \longrightarrow & L\\
& \alpha & \longmapsto & \alpha + 1
\end{array}
$$

は位数 $p$ であるから $\operatorname{Gal}(L/K) = \langle \sigma \rangle \cong Z_p.$
したがって $L/K$ は巡回 Artin-Schreier 拡大であることが示された。
$\blacksquare$

----

**定義**：Artin-Schreier 拡大 $L/K$ の Galois 群に対し
$X$ を次で定義する：

$$
X(\operatorname{Gal}(L/K)) \coloneqq \operatorname{Hom}(\operatorname{Gal}(L/K), Z_p).
$$

----

**定理（Artin-Schreier 拡大の Galois 群の同型）**：
$G \coloneqq \operatorname{Gal}(L/K)$ とすると

$$
G \cong X(G) \cong K/\wp(K).
$$

**検討**：

* 左辺の同型はすぐに出る。右辺の同型は準同型定理を使う。
* $K$ が有限体であることを忘れない。
* $G \cong X(G)$ が加法群であることを忘れない。
* 最後の $\forall \chi \in X(G)$ の逆像がわかりにくい。

**証明**：$L/K$ が Artin-Schreier 拡大であるから $G$ は
$Z_p$ のいくつかの直積に同型である。それが Abel 群であることから指標群と同型であり：

$$
G \cong Z_p^r \cong X(Z_p^r) \cong X(G).
$$

$a \in K$ を一つとる。方程式 $X^p - X - a = 0$ の根の一つを $\alpha \in \overline K$
とおくと、根のすべては次である：

$$
\alpha, \alpha + 1, \alpha +2, \dotsc, \alpha + p - 1.
$$

したがって $\sigma \in G$ に対してある
$i \in \N$ が存在して

$$
\sigma(\alpha) = \alpha + i.
$$

ここで $i$ は $\alpha$ の取り方にはよらず $\sigma$ のみにより決まる。
$a$ に対して対応 $\chi_a\colon\sigma \longmapsto i$ を定義する。
[有限次 $m$-Kummer 拡大の Galois 群定理]の証明と同様の議論により
$\chi_a \in X(G).$
これを用いて写像 $\varphi$ を

$$
\def\arraystretch{1.4}
\begin{array}{c}
\varphi\colon& K &\longrightarrow &X(G)\\
&a &\longmapsto &\chi_a%%\colon \sigma \longmapsto i
\end{array}
$$

で定めると、$\varphi$ が群の準同型写像であることも同様に示される：
$a, b \in K$ をとれば $\alpha, \beta \in L$ が存在して
$a = \alpha^p - \alpha,\;b = \beta^p - \beta$ と書ける。
このとき

$$
\begin{aligned}
a + b
&= \alpha^p - \alpha + \beta^p - \beta\\
&= (\alpha^p + \beta^p) - (\alpha + \beta)\\
&= (\alpha + \beta)^p - (\alpha + \beta) & \because \operatorname{char}K = p.
\end{aligned}
$$
となり、

$$
\sigma(\alpha) = \alpha + i,\quad
\sigma(\beta) = \beta + j
$$

とすれば $\sigma(\alpha + \beta) = \alpha + \beta + i + j.$
ゆえに

$$
\chi_{a + b}(\sigma) = i + j = \chi_a(\sigma) + \chi_b(\sigma).
$$

つまり $\chi_{a + b} = \chi_a + \chi_b$ を得る。
したがって $\varphi$ は（加法）群の準同型写像であることが示された。
$\Box$

写像 $\varphi$ の核は $\wp(K) = \operatorname{im}{\wp} = \lbrace x^p - x \,\mid\, x \in K \rbrace$ であることを示す。
$a \in K$ に対してある $\alpha$ があって $\alpha^p - \alpha = a.$
$\varphi(a) = \chi_a = \operatorname{id}$ ならば任意の
$\sigma \in G$ に対し $\sigma(\alpha^p - \alpha) = \alpha^p - \alpha.$
ゆえに $a = \alpha^p - \alpha \in \wp(K).$
したがって $\ker\varphi = \wp(K)$ であることが示された。
$\Box$

次に $\varphi$ が全射であることを示す。
任意の $\chi \in X(G)$ をとる。[$H^1 = 0$][Hilbert] 定理の系からある
$\alpha \in L$ が存在して次が成り立つ：

$$
\forall \sigma \in G(\chi(\sigma) = \sigma(\alpha) - \alpha).
$$

ゆえに $\sigma(\alpha^p - \alpha) = \alpha^p - \alpha$ だから
$\alpha^p - \alpha \in K.$ ここで
$a \coloneqq \alpha^p - \alpha$ とおけばこの $a$ に対し

$$
\chi_a(\sigma) = \sigma(\alpha) - \alpha = \chi(\sigma)
$$

が任意の $\sigma \in G$ に対して成り立つ。ゆえに $\chi_a = \chi.$
したがって $\varphi$ が全射であることが示された。
$\Box$

以上により、第一同型定理から

$$
K/\wp(K) = K/\ker\varphi \cong \operatorname{im}{\varphi} = X(G)
$$

である。したがって主張の同型が成り立つことが示された。
$\blacksquare$

**系（Artin-Schreier 拡大の条件）**：
体の拡大 $L/K$ が Artin-Schreier 拡大である $\iff$
$L$ が多項式

$$
\tag*{$\spadesuit$}
\prod_{i=1}^r(X^p - X - a_i),\;(a_i \in K)
$$

の最小分解体である

このとき次が成り立つ：

$$
\def\a{ \frac{1}{\wp} }
L = K\!\left(\a a_1, \a a_2, \dotsc, \a a_r\right)\!.
$$

**検討**：巡回 Artin-Schreier 拡大条件定理および巡回
Artin-Schreier 拡大の構造から示される。

**証明**：$\implies:$ 体の拡大 $L/K$ が Artin-Schreier 拡大であるから
$\operatorname{Gal}(L/K) \cong Z_p{}^r$ なる $r \in \N$ があり、生成元は次のような形である：

$$
\sigma \coloneqq (\sigma_1, \dotsc, \sigma_r),\;
\langle \sigma_i \rangle \cong Z_p,\;
i = 1, \dotsc, r.
$$

$\operatorname{Tr}_{L/K}1 = 0$ だからある $\alpha \in L$ が存在して

$$
1 = \sigma(\alpha) - \alpha.
$$

拡大次数 $[L : K] = \lvert \operatorname{Gal}(L/K)\rvert = p^r$ から
ある相異なる $\alpha_1, \dotsc, \alpha_r \in L$ が存在して
$L = K(\alpha_1, \dotsc, \alpha_r)$ となる。
$a_i \coloneqq \alpha_i^p - \alpha_i$ とおけば $\sigma(a_i) = a_i$ が
成り立つので $a_i \in K.$ ゆえに $\alpha_i$ は $K$ 上の既約多項式
$X^p - X - a_i$ の零点となり、$L$ は $K$ 上の既約多項式 $\spadesuit$ の最小分解体となる。
$\Box$

$\impliedby:$ $L$ が多項式 $\spadesuit$ の最小分解体であるから、
各因子 $X^p - X - a_i$ についてそれぞれの根の一つを $\alpha_i$ とする。
すると多項式 $\spadesuit$ のすべての根は

$$
\begin{aligned}
\alpha_i, \alpha_i + 1, \alpha_i + 2, \dotsc, \alpha_i + p - 1,\quad i = 1, \dotsc, r.
\end{aligned}
$$

である。ここで $i \ne j$ ならば $\alpha_i \ne \alpha_j$ とする。
したがって $L = K(\alpha_i \mid i = 1, \dotsc, r).$
$[L : K] = p^r.$

$$
\def\arraystretch{1.2}
\begin{array}{rccl}
\operatorname{Aut}_K(L) \ni \sigma_i \colon & L & \longrightarrow & L\\
& \alpha_i & \longmapsto & \alpha_i + 1
\end{array}
$$

のそれぞれは位数 $p$ であるから
$\operatorname{Gal}(L/K) = \langle \sigma_1 \rangle \times \dotsm \times \langle \sigma_r \rangle \cong Z_p{}^r$
となって $L/K$ は Artin-Schreier 拡大であることが示された。
$\blacksquare$

----

**定理（有限次 Artin-Schreier 拡大に関する一対一対応）**：
$K$ を標数 $p \ne 0$ の体とする。
$K$ の有限次 Artin-Schreier 拡大 $L$ と加法群
$K/\wp(K)$ の有限部分群は一対一対応する。

$$
\def\longmapsfrom{ \longleftarrow\!\shortmid }
\def\arraystretch{1.5}
\begin{array}{c}
\Phi & \longleftrightarrow & \Gamma\\
L & \longmapsto & (\wp(L) \cap K)/\wp(K)\\
K\!\left(\left. \dfrac{1}{\wp} a \;\right| \left. a \in \mathcal L \right.\right) & \longmapsfrom & \mathcal L/\wp(K)
\end{array}
$$

ここで、$K$ を加法群として見るときの部分群であって
$\wp(K)$ を含むものを一般的に $\mathcal L$ と書く。
また、$\Phi$ を $K$ の有限次 Artin-Schreier 拡大 $L$ からなる集合族、
$\Gamma$ を加法群 $K/\wp(K)$ の有限部分群からなる集合族とする。

**検討**：Kummer のときと似ているので比較するといい。

**証明**：$L/K \in \Phi$ とする。系 Artin-Schreier 拡大の条件よりある
$a_i\;(i = 1, 2, \dotsc, r)$ が存在して次が成り立つ：

$$
\def\a{ \frac{1}{\wp} }
L = K\!\left(\a a_1, \a a_2, \dotsc, \a a_r\right)\!.
$$

$\mathcal L \coloneqq \wp(L)\cap K$ とおいて次の拡大体を考える：

$$
\def\a{ \frac{1}{\wp}}
L^{\prime} = K\!\left(\left. \a a \;\right| \left. a \in \mathcal L \right.\right)\!.
$$

集合のとり方から $L^{\prime} \supset L.$

$a_i \in \mathcal L \subset K$ から $\dfrac{1}{\wp}a \in L^{\prime}.$
つまり $L \subset L^{\prime}.$
したがって $L = L^{\prime}$ が示された。

逆に $\mathcal L$ から考えて対応する体 $L$ を考える。
$\mathcal L/\wp(K)$ の生成系 $\overline a_1, \overline a_2, \dotsc, \overline a_r$ をとり
$\mathcal L$ における代表元を $a_1, a_2, \dotsc, a_r$ とすれば

$$
\def\a{ \frac{1}{\wp}}
L = K\!\left(\a a_1, \a a_2, \dotsc, \a a_r\right)
$$

であり $L/K \in \Phi.$

$\mathcal L^{\prime} \coloneqq \wp(L) \cap K$ とおく。
定義から $\mathcal L^{\prime} \supset \mathcal L.$
Artin-Schreier 拡大の Galois 群の同型定理から

$$
X(\operatorname{Gal}(L/K)) \cong K/\wp(K) \cong \mathcal L^{\prime}/\wp(K).
$$

$Y \coloneqq \langle \chi_a\,\mid\,a \in \mathcal L \rangle$ とおく。
これは $X(\operatorname{Gal}(L/K))$ の部分群である。
任意の $\sigma \in Y^\perp$ と任意の $a \in Y$ に対して
Galois-cohomology の理論から

$$
\def\a{ \frac{1}{\wp} }
\begin{aligned}
&0 = \chi_a(\sigma) = \sigma\!\left(\a a\right)\! - \a a.\\
&\therefore\quad \sigma\vert_L = \operatorname{id}_{L}.\\
&\therefore\quad Y^\perp = \lbrace \operatorname{id}_{L}\rbrace.
\end{aligned}
$$

したがって [指標群との一対一対応の存在補題][Kummer]より
$Y = X(\operatorname{Gal}(L/K)).$

以上により $\mathcal L = \mathcal L^{\prime}$ が示された。

したがって主張の対応は互いに他の一対一対応であることが示された。
$\blacksquare$

----

## 参考

* 桂利行著『代数学 III 体とガロア理論』
* 雪江明彦著『環と体とガロア理論』

[Hilbert]: {% post_url 2020/02/2020-02-18-galois-cohomology %}
[Kummer]: {% post_url 2020/02/2020-02-19-kummer %}
