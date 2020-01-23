---
title: 円周等分多項式・円分体学習ノート
tags: math
---

ガロア論に絡んで 1 のべき乗根、原始べき乗根、円周等分多項式、円分体に関するノート。

# 円分体など

まずは roots of unity 各種の定義を確認。整数論と同じだ。

**定義**
* $1$ の $m$ 乗根とは $\zeta^m = 1$ を満たす数 $\zeta$ をいう。
* $1$ の原始 $m$ 乗根とは、$1$ の $m$ 乗根であって
  $1 \le d \lt m$ なる $d \in \Z$ について $\zeta^d \ne 1$ となるものをいう。

感覚としては「$m$ 乗して初めて $1$ になる数」と覚えていてよいだろう。

定義に従えば $m$ が何であっても $1$ 自身は原始 $m$ 乗根ではない。

----

整数論が苦手なので掲載されている補題を真面目にやる。

**補題**：代数的閉体 $\Omega$ の標数を $p$ とすると次は同値である：
* $(1)$ $1$ の $m$ 乗根全体は位数 $m$ の巡回群をなす。
* $(2)$ $1$ の原始 $m$ 乗根が存在する。
* $(3)$ $(p, m) = 1.$

**証明**：
$(1) \implies (2):$ 巡回群の定義なので成り立つ。
正確に言うと～の全体に $1$ を加えた集合が位数 $m$ の巡回群になると言いたい。
$\Box$

$(2) \implies (3):$ 互いに素でなければ原始根が存在しないことを示す。

$n \in \N$ として $m = pn$ であると仮定する。$\zeta^m = 1$ から
$1 = (\zeta^n)^p$ ゆえに $\zeta^n = 1.$
$1 \lt n \lt m$ であるからこれは原始 $m$ 乗根ではない。
$\Box$

$(3) \implies (1):$ $f(X) \coloneqq X^m - 1$ とおく。

$f(X) = 0$ と $f^{\prime}(X) = mX^{m - 1} = 0$ には共通根がないから
$f(X) = 0$ には重根がない（分離拡大のノートを思い出せ）。
したがって $f(X) = 0$ の相異なる $m$ 個の根が位数 $m$ の Abel 群をなす（群論）。

$m$ を割り切るような $d \in \N$ についても同様にして
$G \coloneqq \lbrace a \in \Omega \,\mid\, a^d = 1\rbrace \subset \Omega$ は位数 $d$ の Abel 群である。
したがって $G \cong Z_m.$
$\blacksquare$

----

拡大体 $K(\zeta_m)/K$ についての基本的な性質か？

**定理（$K(\zeta_m)/K$ は Abel 拡大）**：
$K$ を体とする。$\zeta_m \in \overline K$ とすると
* $K(\zeta_m)/K$ は Abel 拡大であり、
* $\operatorname{Gal}(K(\zeta_m)/K) \subset Z_m^\times.$

**証明**：まず、前の補題の証明で言及したことから $K(\zeta_m)/K$ は分離拡大である。

次に $X^m - 1 = 0$ の根は $\zeta_m^j$ の形の元で尽くされるから
$K(\zeta_m)$ は $X^m - 1$ の分解体であり、したがって $K(\zeta_m)/K$ は正規拡大である。
したがって $K(\zeta_m)/K$ は Galois 拡大であることが示された。

最後に $G \coloneqq \operatorname{Gal}(K(\zeta_m)/K)$ が Abel 群であることを示す。
$\sigma \in G$ について次をみたす $s \in \Z$ が法を $m$ として決まる。

$$
\sigma(\zeta_m) = \zeta_m^s.
$$

この対応を写像 $\pi\colon G \longrightarrow Z_m^\times$ と考えると群の準同型写像であることを示す。

* $\sigma, \tau \in G$ に対して $\sigma(\zeta_m) = \zeta_m^s,$ $\tau(\zeta_m) = \zeta_m^t$ とすると

  $$
  \tau\sigma(\zeta_m) = \tau(\zeta_m^s) = (\zeta_m^s)^t
  = (\zeta_m^t)^s = \sigma\tau(\zeta_m).
  $$

* $\sigma(\zeta_m) = \zeta_m \implies \sigma = \operatorname{id}_{K(\zeta_m)}$ だから $\pi$ は単射。

したがって $G \subset Z_m^\times$ であり $G$ が Abel 群であることが示された。
$\blacksquare$


----

TODO: Euler 関数に関して

----

TODO: 円分多項式・方程式

さらに細かく。

* 例。
* $\varPhi_m(x)$ はどういう多項式であるのか。
* 円分多項式は既約である。

----

TODO: 最後に円分体の定義など

# 参照
