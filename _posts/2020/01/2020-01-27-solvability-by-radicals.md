---
title: 代数方程式のべき根による可解性 学習ノート
tags: math
---

代数方程式がべき根で解ける条件について学ぶノート。

## 群論の復習

Galois 理論が関係しないものについてトピックだけ記す。
これらのきちんとした復習は別途行う or 行った。

群 $G$ に対して

* 交換子 $[x, y] \coloneqq xyx^{-1}y^{-1}\;(x, y \in G).$
* 交換子群 $D(G) \coloneqq \lbrace [x, y] \,\mid\, x, y \in G\rbrace.$
  * $D(G) \triangleleft G.$
  * 剰余群 $G/D(G)$ は Abel 群である。
  * $N \triangleleft G$ に対して $G/N$ が Abel 群 $\iff D(G)\subset N.$
  * $D_1(G) \coloneqq D(G),\;D_i(G) \coloneqq D(D_{i-1}(G)), \dotsc$
  * $G = D_0(G) \supset D_1(G) \supset D_2(G) \dotsb$ において
    * $D_i(G) \triangleright D_{i + 1}(G).$
    * 剰余群 $D_i(G)/D_{i-1}(G)$ は Abel 群である。
* 可解群とは、上の交換子群列が $D_n(G) = 1_G$ の形で終わるものをいう。
  * $G$ が可解群 $\iff$ 次を満たす $H_i$ が存在する：
    * $G = H_0 \supset H_1 \supset \dotsb \supset H_m = 1_G.$
    * $H_i \triangleright H_{i - 1}.$ $H_i/H_{i-1}$ は Abel 群である。
  * $G$ が可解群 $\implies$ その部分群および剰余群も可解群である。
  * $N \triangleleft G$ に対して $G/N$ が可解群 $\implies$ $G$ は可解群である。
* 対称群 $\mathfrak S_n$ は $n \le 4$ のときに可解群であり、$n \ge 5$ のときに可解群ではない。

----

TODO: 上記の証明を Galois 理論ではないどこか別の枠で確認すること。

## 可解拡大・べき根拡大

以下基礎体 $K$ の標数を $0$ とし、多項式 $f(X) \in K[X]$ の最小分解体を
$L_f$ のように表記する。

----

**定義**：Galois 拡大 $L/K$ が**可解拡大**であるとは、
$\operatorname{Gal}(L/K)$ が可解群であることをいう。

**定義**：$f[X] \in K[X]$ の最小分解体 $L_f$ が $K$ の**べき根拡大**であるとは、
次を満たす列が存在して $L_f \subset L_r$ が成り立つことをいう：

$$
K = L_0 \subset L_1 \subset \dotsb \subset L_r,\\
L_i = L_{i - 1}(\sqrt[n_i]{\alpha_i}),\;
\alpha_i \in L_{i - 1},\;
n_i \in \N.
$$

$f(X) = 0$ が**べき根によって解ける**とは、$L_f$ が $K$ のべき根拡大であることをいう。

----

**補題（合成体の Galois 群の同型）**：
$K$ を（標数が $0$ でなくてもいい）体、
$L/K$ を Galois 拡大、
$K^{\prime}/K$ を体の拡大、
$L$ と $K^{\prime}$ の $\overline K$ における合成体を $L^{\prime}$ とする。

$$
L^{\prime} \coloneqq LK^{\prime} = K^{\prime}L \coloneqq L(K^{\prime}) = K^{\prime}(L).
$$

このとき $L^{\prime}/K^{\prime}$ も Galois 拡大であり、

$$
\operatorname{Gal}(L^{\prime}/K^{\prime}) \cong \operatorname{Gal}(L/L \cap K^{\prime}).
$$

とくに $[L^{\prime} : K^{\prime}]$ は $[L : K]$ を割り切る。

**検討**：

* $L/K$ の仮定からある分離多項式 $f(X) \in K[X]$ が存在する。
  * 先述の記法を使いたいが、基礎体が明記されていないので誤解を招くから不採用。
* $f(X) \in K^{\prime}[X]$ としても同様のことがいえるから結局
  $L^{\prime}/K^{\prime}$ も Galois 拡大であるといえる。
* その関係から $\operatorname{Hom}_K(L, \overline K) = \operatorname{Hom}_K(L, \overline L) \subset \operatorname{Aut}_K(L).$
* 以降は Galois の基本定理を用いて不変体の比較をして拡大次数を吟味する。
* 教科書には拡大体の関係グラフが図示されている。
  そこでは $L \cap K^{\prime}$ のノードが $L/K$ と $K^{\prime}/K$ の交点あたりに記されている。

**証明**：
$L/K$ が Galois 拡大であることから、$L$ はある多項式 $f(X) \in K[X]$ についての $K$ 上の最小分解体である。
そして $f(X) \in K^{\prime}[X]$ としても分離多項式であり、
$L^{\prime}$ は $K^{\prime}$ 上の $f(X)$ の最小分解体である。
したがって $L^{\prime}/K^{\prime}$ が Galois 拡大であることが示された。
$\Box$

$L/K$ が Galois 拡大であることから、
$L$ から $\overline K$ の中への $K$ 準同型写像は $L$ の $K$ 自己同型写像である。

----

TODO: ここに教科書のように拡大関係を説明する図式が入るとベスト。
特に $L/L\cap K^{\prime}/K$ の鎖が重要。

* いちいち断られなくなっているが Galois 拡大は「上」に伝わるので $L/L \cap K^{\prime}$ も Galois 拡大である。
* $L/L\cap K^{\prime}$ と $L^{\prime}/K^{\prime}$ が「平行」になっている。
  これはあとで示す拡大次数が一致することをよく示している。

----

$G^{\prime} \coloneqq \operatorname{Gal}(L^{\prime}/K^{\prime}),$
$G \coloneqq \operatorname{Gal}(L/L \cap K^{\prime})$ とおく。

$\sigma \in G^{\prime}$ の $L$ への制限写像 $\sigma\mid_L$ は $L$ はもとより $L \cap K^{\prime}$ の元を固定する。
したがって次の写像 $\varphi$ を得る：

$$
\begin{aligned}
    \varphi\colon & G^{\prime} && \longrightarrow && G\\
                  & \sigma     && \longmapsto     && \sigma|_L.
\end{aligned}
$$

$\sigma\mid_L$ が $L$ 上恒等写像ならば $\sigma$ は $K \cap L^{\prime}$ 上で恒等写像になる。
したがって $\varphi$ は単射である。

また $L^{\prime}$ に対する $G^{\prime}$ の不変体は $K^{\prime}$ に等しいから次の三者は同値である：

* $x \in L$ が $\operatorname{im}{\varphi}$ で不変
* $x \in L$ が $G^{\prime}$ で不変
* $x \in L \cap K^{\prime}$

したがって $\operatorname{im}{\varphi}$ の $L$ に対する不変体、
$G$ の $L$ に対する不変体、$L \cap K^{\prime}$ はすべて等しい。

また、$\operatorname{im}{\varphi} \subset G$ より
Galois の基本定理から $\operatorname{im}{\varphi} = G.$
したがって $G^{\prime} \cong G.$
$\Box$

$$
[L^{\prime} : K^{\prime}] = [L : L \cap K^{\prime}]
$$

であるから $[L^{\prime} : K^{\prime}]$ は $[L : K]$ を割り切る。
$\blacksquare$

----

**定理（代数方程式がべき根によって解ける条件）**：
$f(X) = 0$ がべき根によって解ける $\iff$ $L_f/K$ が可解拡大である。

**検討**：巡回 Kummer 拡大の性質を応用できる形にもっていく。

**証明**：
$\implies:$
$L_f/K$ をべき根拡大とする：次のような体の列が存在して $L_f \subset L_r$ をみたすものとする：

$$
\begin{aligned}
    K &= L_0 \subset L_1 \subset \dotsb \subset L_r.\\
    L_i &= L_{i - 1}(\sqrt[n_i]{\alpha_i}),\;
    \alpha_i \in L_{i - 1},\;
    n_i \in \N.
\end{aligned}
$$

$m \coloneqq n_1n_2\dotsm n_r$ とし、$K^{\prime} \coloneqq K(\zeta_m)$ とする。
さらに次のように合成体をとる：

$$
L_1^{\prime} \coloneqq L_1K^{\prime} = K^{\prime}(\sqrt[n_1]{\alpha_1})
$$

$\zeta_m \in K^{\prime}$ だから $L_1^{\prime}$ は $X^{n_1} - \alpha_1$ の
$K^{\prime}$ 上の最小分解体である。[巡回 Kummer 拡大定理][kummer]から
$L_1^{\prime}/K^{\prime}$ は巡回拡大である。

----

またしても図式を入れたい。$L_2^{\prime}$ 以降の定義が意外なので。

----

$L_2/K$ は Galois 拡大ではない（とは限らない？）から
$\alpha_2$ の $K$ 上の共役全部（有限個）を $\alpha_{21}, \dotsc, \alpha_{2s}$ として次で定義する：

$$
L_2^{\prime}\coloneqq L_1^{\prime}(\sqrt[n_2]{\alpha_{21} }, \dotsc, \sqrt[n_2]{\alpha_{2s} }).
$$

$L_2^{\prime}$ は $K$ 上の多項式

$$
(X - 1)(X - \alpha_{21})(X - \alpha_{22})\dotsb(X - \alpha_{ns}) \in K[X]
$$

の最小分解体だから $L_2^{\prime}/K$ は Galois 拡大である。これにともなう体の列

$$
\def\gen#1{ \sqrt[n_{#1}]{\alpha_{2#1} } }
L_1^{\prime} \subset L_1^{\prime}(\gen 1) \subset L_1^{\prime}(\gen 1, \gen 2)
\subset \dotsb \subset L_2^{\prime}
$$

の各ステップ（包含関係）は[巡回 Kummer 拡大定理][kummer]より巡回拡大である。
この操作を繰り返せば次を得る：

$$
\def\gen#1#2{ \sqrt[n_{#1}]{\alpha_{ {#1} {#2} } } }
\begin{aligned}
    K \subset K^{\prime} &\subset L_1^{\prime} \subset
      L_1^{\prime}(\gen 2 1) \subset L_1^{\prime}(\gen 2 1, \gen 2 2) \subset
      \dotsb \subset L_2^{\prime}\\
    &\subset L_2^{\prime}(\gen 3 1) \subset L_2^{\prime}(\gen 3 2, \gen 3 3) \subset
      \dotsb \subset L_3^{\prime}\\
    &\subset \dotsb\\
    &\subset L_r^{\prime}.
\end{aligned}
$$

$L_r^{\prime}/K$ が Galois 拡大であり、その間の各ステップは巡回拡大である。$L_f \subset L_r^{\prime}.$

この列に Galois 対応する群の包含関係を次とする：

$$
H_0 = \operatorname{Gal}(L_r^{\prime}/K)
\supset H_1 \supset \dotsb \supset 1.
$$

こちらは基本定理から正規部分群であり、構成から Abel 正規列を得る。
したがって $\operatorname{Gal}(L_r^{\prime}/K)$ は可解群であることが示された。

$L_r/K$ は Galois 拡大であるから、$\operatorname{Gal}(L_f/K)$ は
$\operatorname{Gal}(L_r^{\prime}/K)$ の商群であり、したがって
$\operatorname{Gal}(L_f/K)$ は可解群である。
$\Box$

$\impliedby:$
拡大体の次数を $m \coloneqq [L_f : K]$ とおく。
体 $L_0 \coloneqq K(\zeta_m)$ をとる。

このとき「合成体の Galois 群の同型」補題から

* $L_fL_0/L_0$ は可解拡大である：

  同補題からまず $L_fL_0/L_0$ は Galois 拡大である。
  $\operatorname{Gal}(L_fL_0/L_0) \cong \operatorname{Gal}(K/K \cap L_0)$
  であり右辺は可解群 $\operatorname{Gal}(L/K)$ の部分群だから可解群。
  したがって $L_fL_0/L_0$ が可解拡大であることが示された。

* $[L_fL_0 : L_0]\mid m.$

$\operatorname{Gal}(L_fL_0/L_0)$ の交換子群列を細分した組成列を考える：

$$
\begin{aligned}
    \operatorname{Gal}(L_fL_0/L_0)
    &= H_0 \supset H_1 \supset \dots \supset H_r = 1,\\
    H_i &\triangleright H_{i + 1},\\
    [H_i \colon H_{i + 1}] & \text{ is prime.}
\end{aligned}
$$

これに Galois 対応する中間体の列を次のようにとる：

$$
L_0 \subset L_1 \subset \dotsb \subset L_r = L_fL_0.
$$

このとき各 $L_i/L_{i-1}$ は Galois 拡大、$p_i \coloneqq [L_i : L_{i - 1}]$ は素数で
$p_i \mid m$ となる。

$L_0 = K(\zeta_m)$ は $1$ の原始 $p_i$ 乗根を含むので
$L_{i-1}$ が $1$ の原始 $p_i$ 乗根を含む。
$\operatorname{Gal}(L_i/L_{i-1}) \cong Z_p$ だからこの Galois 群は巡回群である。
[巡回 Kummer 拡大定理][kummer]から $\operatorname{Gal}(L_i/L_{i-1})$ は巡回 Kummer 拡大であり
次の関係が成り立つ：

$$
\exists \alpha_i \in L_{i-1}(L_i = L_{i-1}(\sqrt[p_i]{\alpha_i})).
$$

また $L_0 = K(\zeta_m)$ であるから $L_fL_0$ の部分体 $L_f$ は定義によりべき根拡大である。
したがって $f(X) = 0$ がべき根によって解けることが示された。
$\blacksquare$

## 結論

$n$ 次方程式がべき根によって解ける $\iff$ $n \le 4.$

**証明**：[対称式は基本対称式の有理式で表せる][galois]で示したことから
$n$ 次対称群 $\mathfrak S_n$ を考えることになる。

$K \coloneqq k(s_1, \dotsc, s_n)$ に係数をもつ $n$ 次方程式

$$
f(X) \coloneqq X^n - s_1X^{n-1} + \dotsb + (-1)^ns_n = 0
$$

の Galois 群 $\operatorname{Gal}(L_f/K)$は $\mathfrak S_n$ と同型である。

群論によると $\mathfrak S_n$ は $n \le 4$ であるときしか可解群ではない。
したがって「代数方程式がべき根によって解ける条件」定理から
$n$ 次方程式がべき根によって解けることと $n \le 4$ が同値であることが示された。
$\blacksquare$

----

すなわち、5 次以上の代数方程式には根の公式が存在しないことが示される。

## 参照

* 桂利行著『代数学 III 体とガロア理論』
* 堀田良之著『岩波講座 現代数学の基礎 環と体 2』

[galois]: {% post_url 2020/01/2020-01-20-galois %}
[kummer]: {% post_url 2020/01/2020-01-26-kummer %}
