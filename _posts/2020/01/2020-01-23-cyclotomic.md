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

**定義**：$m \in \N$ に対して $1, \dotsc, m$ のうち $m$ と互いに素な数の個数を対応させる関数を $\varphi\colon\N\longrightarrow\N$ とし、これを **Euler の関数**という。

$$
\varphi(m) \coloneqq \sum_{\substack{1 \le n \le m\\(n, m) = 1}}1.
$$

便宜上 $\varphi(1) = 1$ とする。

**補題**：
$\varphi(m) = \lvert Z_m^\times\rvert.$
$(p, m) = 1$ ならば $\varphi(m)$ は $1$ の原始 $m$ 乗根の個数に等しい。

**証明**：最初の等式の右辺は既約剰余類の全ての個数、$Z_m$ の単数群の元の個数を意味する。
$p$ がその元である条件はまさに $(p, m) = 1$ であるので、この等式は正しい。

$(p, m) = 1$ であるから原始 $m$ 乗根 $\zeta_m$ が存在する。先ほどと同様の推論をすると：

$\zeta_m^s$ が原始根でない
$\iff$ ある整数 $1 \le d \lt m$ が存在して $(\zeta_m^s)^d = 1$
$\iff$ ある整数 $1 \le d \lt m$ が存在して $m$ は $sd$ を割り切る
$\iff$ $(m, s) \ne 1.$

対偶を考えると $\zeta_m^s$ が原始根 $\iff$ $(m, s) = 1.$

$\iff$ $(m, s) = 1$ を満たす $s$ の個数とはすなわち $\varphi(m)$ である。
$\blacksquare$

----

**定義**：多項式 $\varPhi_m(X)$ が**円周等分多項式**であるとは、
* 最高次の係数が $1$ で
* 根のすべての集合が $1$ の原始 $m$ 乗根すべての集合と等しい

ものをいう。

**円周等分方程式**とは方程式 $\varPhi_m(X) = 0$ のことをいう。

* 複素平面でいうと、単位円の上に $1$ の $m$ 乗根が等分点に位置して正 $m$ 角形を構成している。

$\Omega$ を代数的閉体、$P \subset \Omega$ を素体とする。

* $\operatorname{Aut}(\Omega)$ は素体の元を固定する：
  $\sigma \in \operatorname{Aut}(\Omega)$ をとる。
  $\sigma$ によって動かない $\Omega$ の元すべてを $P^\sigma$ と書くと、これは当然 $P$ の部分である：$P \subset P^\sigma \subset \Omega.$
  しかも $P^\sigma$ は体である。

* $\varPhi_m(X)$ は $\operatorname{Aut}(\Omega)$ の元により不変：
  $\zeta_m$ は $P$ 上の方程式 $X^m - 1 = 0$ の原始根であるから、
  $\sigma(\zeta_m)$ も同様である：$\sigma$ は $1$ の原始 $m$ 乗根の置換を引き起こす。

  よって $\varPhi_m(X)$ は $\operatorname{Aut}(\Omega)$ の元で不変であり
  $\varPhi_m(X) \in P[X].$

以上の議論と $1$ の $m$ 乗根が $m$ の約数 $d$ に対して
$1$ の原始 $d$ 乗根でもあることを踏まえて次を得る：

$$
\begin{aligned}
    X^m - 1 &= \prod_{d \mid m}\varPhi_d(X),\\
    m &= \sum_{d \mid m}\varphi(d).
\end{aligned}
$$

----

以降、体の標数を $0$ とする。$\varPhi_m(X) \in \mathbb Q[X].$

$\varPhi_m(X) = 0$ の任意の根が $1$ の原始 $m$ 乗根であり、そのうちの一つを $\zeta_m$ として扱う。

----

**例（次数の低い円周等分多項式）**：

$$
\begin{aligned}
    \varPhi_1(X) &= X - 1.\\
    \varPhi_2(X) &= X + 1.\\
    \varPhi_3(X) &= X^2 + X + 1.\\
    \varPhi_4(X) &= X^2 + 1.\\
    \varPhi_5(X) &= X^4 + X^3 + X^2 + X + 1.\\
    \varPhi_6(X) &= X^2 - X + 1.\\
    \varPhi_7(X) &= X^6 + X^5 + X^4 + X^3 + X^2 + X + 1.\\
    \varPhi_8(X) &= X^4 + 1.
\end{aligned}
$$

$m$ が素数 $p$ のときは $\varPhi_p(X)$ は $X^p - 1$ 既約元分解から $X - 1$ を除いたものに等しい。

$$
\varPhi_p(X) = X^{p-1} + X^{p - 2} + \dotsb + X + 1.
$$

$m = 4$ のときは $X^4 - 1 = (X - 1)(X - i)(X + 1)(X + i).$
根のうち $4$ 乗して初めて $1$ になるのは $\pm i$ しかない。これに対応する因子を残すと上を得る。
公式を使うと $4$ を割り切るのは $1, 2, 4$ だから

$$
\begin{aligned}
X^4 - 1 &= \varPhi_1(X)\varPhi_2(X)\varPhi_4(X).\\
\varPhi_4(X) &= \dfrac{X^4 - 1}{\varPhi_1(X)\varPhi_2(X)}\\
&= \frac{(X - 1)(X - i)(X + 1)(X + i)}{(X - 1)(X + 1)}\\
&= (X - i)(X + i)\\
&= X^2 + 1.
\end{aligned}
$$

$m = 6$ のものを計算する（分子の因数分解がだんだん面倒になる）。

$$
\begin{aligned}
\varPhi_6(X) &= \dfrac{X^6 - 1}{\varPhi_1(X)\varPhi_2(X)\varPhi_3(X)}\\
&= \dfrac{(X - 1)(X^2 + X + 1)(X + 1)(X^2 - X + 1)}{(X - 1)(X + 1)(X^2 + X + 1)}\\
&= X^2 - X + 1.
\end{aligned}
$$

SymPy に `cyclotomic_poly()` という関数がある。これを利用すると便利だ。

----

次の定理は $m$ が素数でなくても既約だと主張していることに注意：

**定理（円周等分多項式は $\mathbb Q$ 上既約）**：$\varPhi_m(X) \in \mathbb Q[X]$ は既約である。

**検討**：示したいことは、$1$ の原始 $m$ 乗根のすべてが、原始 $m$ 乗根の一つ $\zeta$ の最小多項式 $f$ の根であることだ。
このとき $\varPhi_n(X)$ のすべての一次の因子が $f$ の因子となり、
したがって $\varPhi_n\mid f$ で $f = \varPhi_n$ を結論でき、最小多項式だから既約であることが示される。

**証明**：$\zeta \coloneqq \zeta_m$ の $\mathbb Q$ 上の最小多項式を $f(X)$ とする。
$f(X)$ が $\varPhi_m(X)$ の因子であると仮定して矛盾を導く。

$\varPhi_m(X)$ は $\Z$ 係数なので $f(X)$ もそうである。

$f(X) = 0$ の根ではない $1$ の原始 $m$ 乗根 $\zeta^r$ のうち、$r \ne 0$ が最小のものをとる。

素数 $p$ を $r$ の約数とする。$(m, r) = 1$ であることから $(p, m) = 1.$

$\zeta_1 \coloneqq \zeta^{r/p}$ は $f(X) = 0$ の根である。

$\zeta_1^p = \zeta^r$ の最小多項式を $g(X)$ とする。
$(f(X), g(X)) = 1$ だから $f(X)g(X) \mid \varPhi_m(X).$
したがって $f(X)g(X) \mid (X^m - 1).$

$g_1(X) \coloneqq g(X^p)$ とおけば

$$
g_1(\zeta_1) = g(\zeta_1^p) = g(\zeta^r) = 0.
$$

したがってある $h(X) \in \Z[X]$ が存在して $g_1(X) = f(X)h(X).$

これを $p$ を法として考えて次を得る：

$$
g(X)^p \equiv g(X^p) \equiv g_1(X) = f(X)h(X) \pmod p.
$$

（最初の $\equiv$ は何？）

この式は多項式を $\mathbb F_p[X]$ 上で考えると
$\bar f(X) = 0$ と $\bar g(X) = 0$ に共通根があることを意味する。

ところが $\mathbb F_p[X]$ において

$$
\bar f(X) \bar g(X) \mid (X^m - 1)
$$

であり、$(p, m) = 1$ であることから $X^m - 1 = 0$ は $\overline\mathbb F_p$
において重根を持たない。すると
$\bar f(X) = 0$ と $\bar g(X) = 0$ に共通根がなく、上記に矛盾する。

背理法により $\varPhi_m(X) = f(X)$ であり
$\varPhi_m(X)$ は $\mathbb Q$ 上既約であることが示された。
$\blacksquare$

**系**：$\operatorname{Gal}(\mathbb Q(\zeta_m)/\mathbb Q) \cong Z_m^\times.$

**証明**：「円周等分多項式は $\mathbb Q$ 上既約」定理から

$$
\lvert \operatorname{Gal}(\mathbb Q(\zeta_m)/\mathbb Q) \rvert = [\mathbb Q(\zeta_m) : \mathbb Q] = \varphi(m).
$$

一方「$K(\zeta_m)/K$ は Abel 拡大」定理からこの Galois 群は Abel 群であり

$$
\lvert \operatorname{Gal}(\mathbb Q(\zeta_m)/\mathbb Q) \rvert
\le \lvert Z_m^\times\rvert = \varphi(m).
$$

したがって $\operatorname{Gal}(\mathbb Q(\zeta_m)/\mathbb Q) \cong Z_m^\times.$
$\blacksquare$

----

**定義**：
* **円の $m$ 分体**とは、体 $\mathbb Q(\zeta_m)$ のことをいう。
* **円分体**とは、ある円の $m$ 分体の部分体のことをいう。

円分体 $K$ について $\mathbb Q/K$ は Abel 拡大である。拡大次数は $K$ が $m$ 分体の部分体ならば $\varphi(m)$ に等しい。
実はこの逆が成り立ち、$\mathbb Q$ 上の Abel 拡大はすべて円分体である (Kronecker)。

# 参照

* 桂利行著『代数学 III 体とガロア理論』
* 松坂和夫著『代数系入門』

以上
