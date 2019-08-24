---
title: 『新訂解析学』学習ノート第六回
---

熊原啓作著『新訂解析学』の学習ノート第六回。

# Laurent 展開

内容：
* 正則でない関数に対しても Taylor 展開のようなことをしたい。
* 正則でない点における関数の振る舞いを調べる。
* 有理型関数について。

## Laurent 展開

* **Th 8.1** (Laurent)
  * $0 \le R_1 < R_2 \le \infty.$
  * $z_0 \in \Complex.$
  * $D = \lbrace z \,\mid\, R_1 < \lvert z - z_0\rvert < R_2 \rbrace.$
  * $f(z)$ は $D$ 上正則であるとする。

  に対して

  $$
  \forall r \in {(R_1, R_2)} \exists c_n\left(\\
  f(z) = \sum_{n = -\infty}^\infty c_n(z - z_n)^n,\quad
  c_n = \frac{1}{2\pi i}\int_{\lvert \zeta - z_0 \rvert = r}\!\frac{f(\zeta)}{(\zeta - z_0)^{n + 1}}\,\mathrm d\zeta.\right)
  $$

  かつこの級数は $R_1 < r_1 < r_2 < R_2$ を満たす任意の $r_1, r_2$ について
  $D_{12} = \lbrace z \,\mid\, r_1 < \lvert z - z_0 \rvert < r_2\rbrace$ 上一様収束する。

  証明：
  1. $D_{12}$ 上 $f$ は正則だから Cauchy の公式より：

     $$
     \def\cauchy#1{ \frac{1}{2\pi i}\int_{\partial #1}\!\frac{f(\zeta)}{\zeta - z}\,\mathrm d\zeta }
     \begin{aligned}
     f(z) &= \cauchy{D_{12}}\\
     &= \cauchy{D_2} - \cauchy{D_1}.
     \end{aligned}
     $$

     この外側の積分と内側の積分を $\varphi(z)$ と $\psi(z)$ とそれぞれおく。
  2. $\varphi(z)$ について次を示す：

     $$
     \begin{aligned}
     \varphi(z) &= \sum_{n = 0}^\infty \frac{\varphi^{(n)}(z_0)}{n!}(z - z_0)^n,\\
     \varphi^{(n)}(z_0) &= \frac{n!}{2\pi i}\int_{\partial D_2}\!\frac{f(\zeta)}{(\zeta - z)^{n + 1}}\,\mathrm d\zeta.
     \end{aligned}
     $$

     極限 $r_2 \to r$ を考えて一様収束であるとわかる。
  3. $\psi(z)$ 側は少し厄介だ。

     $Z = \dfrac{1}{z - z_0},\;W = \dfrac{1}{\zeta - z_0},\;\varPsi(Z) = \psi(z)$ とおく。
     $n < 0$ と $\lvert z - z_0 \rvert \ge r_1$ を「反転」して考えることになる。

     TODO: 後回し。
  4. $\lvert c_n \rvert$ の評価をする（絶対収束するので一様収束する）。

     $$
     \lvert z - z_0\rvert \le r_2 \implies \sum_{n = 0}^\infty \lvert c_n(z - z_0)^n \rvert < \infty.
     $$

## 孤立特異点
* 関数 $f(z)$ の**特異点**とは、そこで $f$ が正則でない点のことである。
* 点 $z_0$ が関数 $f(z)$ の**孤立特異点**であるとは、$f$ の特異点であって、
  ある $R > 0$ に対して $\lbrace z \,\mid\, \lvert z - z_0 \rvert < R \rbrace$ において $f$ が正則であるものをいう。
* 特異点 $z_0$ が**除去可能である**とは、次の方法で $f$ の値を定義することで $z_0$ においても $f$ を正則にできるものをいう：

  > Laurent 展開の主要部が 0 であるならば、$f(z_0) := c_0.$

* **Th 8.2** (Riemann)

  $f(z)$ が $0 < \lvert z - z_0 \rvert < R$ で正則かつ有界ならば $z_0$ は除去可能である。

  証明：
  $\forall n \in \N,\; 0 < \forall r < R$ に対して

  $$
  \begin{aligned}
      \lvert c_{-n}\rvert
      &= \left\lvert \frac{1}{2\pi i}\int_C\!f(z)(z - z_0)^{n - 1}\,\mathrm dz\right\rvert\\
      &\le \max_{z \in C} \{\lvert f(z)\rvert\} r^n.
  \end{aligned}
  $$

  極限 $r \to +0$ を考えると $\forall n \in N (c_{-n} = 0).$
  主要部がゼロである Laurent 展開をもつ点 $z_0$ は除去可能であるので、主張が成り立つ。
* **極**：Laurent 展開の係数で、$c_{-k} \ne 0,\;c_{-n} = 0 \quad(n > k > 0)$ なる
  $k$ がある点は $f$ の $k$ 位の極であるという。
  * 点 $z_0$ が $f$ の $k$ 位の極であるとき、$\displaystyle \lim_{z\to z_0}f(z) = \infty.$
    よって $z_0$ は $\dfrac{1}{f(z)}$ の除去可能な特異点である。
* **L 8.1** 除去可能条件

  $f(z)$ を $0 < \lvert z - z_0 \rvert < R$ で正則かつ非定数関数であるとする。
  このとき、点 $z_0$ が除去可能であることと次が成り立つことは同値である：

  $$
  \def\L{ \lim_{z \to z_0} \lvert z - z_0\rvert^h \lvert f(z) \rvert }
  \begin{aligned}
      \exists a \in \R(\forall h
      &(h > a \implies \L = 0)\\
      \lor &(h < a \implies \L = \infty)).
  \end{aligned}
  $$

  証明：
  * $\implies$ $z_0$ が除去可能であり $\displaystyle f(z_0) := \lim_{z \to z_0}f(z)$ であるとする。
    これにより $f(z)$ は円盤内で正則である。
    * $f(z_0)\ne 0$ ならば $a = 0$ で上も下も成り立つ。
      * $z_0$ が $k$ 位の零点のときは $a = -k.$
      * $z_0$ が $k$ 位の極のときは $a = k.$
  * $\impliedby$
    * $h < a$ とする。$\forall m(m \ge a \implies \lim(z - z_0)^mf(z) = 0).$
      すなわち $z_0$ は $(z - z_0)^mf(z)$ の除去可能な特異点であり、除去後の正則関数の零点である。
      その位数を $k$ とすると次のような正則関数 $g$ が得られる：

      $$
      \exists g(z)((z - z_0)^m f(z) = (z - z_0)^kg(z) \land g(z_0) \ne 0).
      $$

      $z_0$ は、
      * $m \le k$ のときは除去可能特異点である。
      * $m > k$ のときは極である。
    * $h > a$ とする。$\forall m(m < a \implies \lim(z - z_0)^mf(z) = \infty).$
      すなわち $z_0$ は $(z - z_0)^mf(z)$ の極である。
      その位数を $k$ とおくと次のような正則関数 $g$ が得られる：

      $$
      \exists g(z)\left((z - z_0)^m f(z) = \frac{g(z)}{(z - z_0)^k}\right).
      $$

      $z_0$ は、
      * $m \le -k$ のときは除去可能特異点である。
      * $m > -k$ のときは極である。
* **真性特異点**とは、Laurent 展開の主要部の長さが有限でない特異点をいう。
* **Th 8.3** (Weierstrass) 真性特異点は除去できない＝値を決定できない
  * $z_0$ を $f(z)$ の真性特異点であるとする。

  このとき $\displaystyle \lim_{z \to z_0}f(z)$ の値を自由に決められる：

  $$
  \forall \lambda \in \Complex \cup \{\infty\}
  \exists z_n \in \Complex
  \forall \varepsilon > 0
  \exists n \in \N
  \forall n \ge N
  (\lvert f(z_n) - \lambda\rvert < \varepsilon).
  $$

  証明：背理法による。上記の論理式を否定したものを仮定して矛盾を導く。

  $$
  \exists \varepsilon > 0 \exists \delta > 0 \forall z(
      0 < \lvert z - z_0 \rvert < \delta \implies
      \lvert f(z) - \lambda \rvert \ge \varepsilon
  )
  $$

  が成り立つとすると：

  $$
  \forall a(a < 0 \implies \lim_{z \to z_0}\lvert z - z_0\rvert^a \lvert f(z) - \lambda\rvert = \infty).
  $$

  **L 8.1** より、$z_0$ は $f(z) - \lambda$ の除去可能な特異点である。
  したがって：

  $$
  \def\F{ \lim_{z \to z_0}(z - z_0)^b }
  \begin{aligned}
  \exists b > 0(
      0 &= \F(f(z) - \lambda)\\
      &= \F f(z) - \F\lambda\\
      &= \F f(z)
      )
  ).
  \end{aligned}
  $$

  これは $z_0$ が真性特異点であることに矛盾する。
  * コメント：よくわからない。
* **有理型**とは関数であって、定義領域内に極以外の特異点がないものをいう。
* **E 8.1** 有理式は有理型
  * $P(z), Q(z)$ は多項式であり、共通の零点を持たないとする。

  このとき $\dfrac{P(z)}{Q(z)}$ は $\Complex$ 上有理型であり、その極は $Q(z)$ の零点と一致する。
* **$\infty$ まわりの Laurent 展開**とは、$f(z)$ が $\infty$ の十分近く --
  $\exists R > 0 (\lvert z \rvert > R)$ -- で正則であるときに、次の形の級数に書けることをいう：

  $$
  f(z) = \sum_{n = -\infty}^{\infty} c_n z^n.
  $$

  * $g(z) = \dfrac{1}{f(z)}$ とすると $0 < \lvert z \rvert < R$ で正則。
    $z = 0$ が $g(z)$ の
    * 除去可能な特異点であるとき、$z = \infty$ は $f(z)$ の除去可能な特異点であるという。
      $\displaystyle \lim_{z \to \infty}f(z) \ne \infty$ に対応。
    * 極であるとき、$z = \infty$ は $f(z)$ の極であるという。
      $\displaystyle \lim_{z \to \infty}f(z) = \infty$ に対応。
    * 真性特異点であるとき、$z = \infty$ は $f(z)$ の真性特異点であるという。
      $\displaystyle \lim_{z \to \infty}f(z)$ は決定できない。
  * $f$ の主要部は $\displaystyle \sum_{n = 1}^\infty c_nz^n$ であるとする。
    もしこの級数が有限の長さならば極を $\infty$ にもつ。
* **E 8.2**
  * $k$ 次多項式は $z = \infty$ を $k$ 位の極にもつ。
  * $\mathrm{e}^z$ では $z = \infty$ は真性特異点である。

## 有理型関数の級数

以下、
* $D$ を領域、
* $\lbrace f_n(z) \rbrace$ を $D$ 上の有理型関数、
* $S \subset D$ を単なる部分集合

とする。

* 級数 $\sum f_n(z)$ が **$S$ 上一様収束する**とは、$f_n$ のうち正則でないものが高々有限個しかなく、
  それら以外からなる級数が $S$ 上一様収束することをいう。
* 級数 $\sum f_n(z)$ が **$D$ 上広義一様収束する**とは、$D$ の任意の有界閉集合において、
  $D$ 上一様収束することをいう。

コメント：ある番号以降 $f_n$ は正則関数だから、それをかき集めた級数は正則関数の級数である。
以前の結果よりこれは一様収束して極限は正則関数である。これが $D$ の開集合と番号のとり方に依らないで確定すれば（する）、
その値をもって級数 $\sum f_n(z)$ の定義とする。そう言っている。
また、そのときは項別微分が可能になることに注意。

* **Th 8.4** 極限操作の順序変更定理
  * $f_n(z)$ が $D$ 上広義一様収束するとする。

  このとき、
  * $\sum f_n^\prime(z)$ は$D$ 上広義一様収束する。
  * 項別微分が許される。
* **E 8.3**

  $$
  \begin{aligned}
      f(z) &= \sum_{n = -\infty}^\infty \frac{1}{(z - n)^2},\quad n \in \Z.\\
      g(z) &= \frac{\pi^2}{\sin^2 \pi z}.
  \end{aligned}
  $$

  $f(z)$ は $\Complex$ 上広義一様収束する。

  両者ともに $z = n \in \Z$ を 2 位の極とする。
  そして Liuville の定理または一致の定理により、$f = g$ が実は成り立つ。

  $$
  \frac{\pi^2}{\sin^2 \pi z} - \frac{1}{z^2} = \sum_{n \ne 0}\frac{1}{(z - n)^2}.
  $$

  右辺は $z = 0$ で正則であるので、左辺の極限 $n \to 0$ を考える。
  左辺は $\dfrac{\pi^2}{3}$ に収束し、右辺は $\displaystyle 2 \sum_{n = 1}^\infty\dfrac{1}{n^2}$ である。
  よって次の等式が得られる：

  $$
  \sum_{n = 1}^\infty\frac{1}{n^2} = \frac{\pi^2}{6}.
  $$

* **E8.4**

  $$
  \pi\cot\pi z = \frac{1}{z} + \sum_{n = 1}^\infty\frac{2z}{z^2 - n^2}.
  $$

  $\displaystyle f(z) = \frac{1}{z} + \sum_{n \ne 0}\left(\frac{1}{z - n} + \frac{1}{n}\right)$ は $z = n$ に 1 位の極をもつ。

* **Th 8.5**
  * $0 \le R_1 < R_2 \le \infty.$
  * $D$ をこのリングの内側の領域とする。

  このとき、級数 $\displaystyle \sum_{n = -\infty}^\infty c_n(z - z_0)^n$ が $D$ 上関数 $f(z)$ に収束するならば、
  この級数は $f(z)$ の $z_0$ を中心とする Laurent 級数展開に一致する。

  証明：

  1. 級数の「主要部」でない部分は $\lvert z - z_0 \rvert < R_2$ で広義一様収束する。
  2. 級数の「主要部」は $Z = \dfrac{1}{z - z_0}$ の整級数であり、$\lvert Z \rvert < R_1$ で、
     つまり $\lvert z - z_0 \rvert > R_1$ で広義一様収束する。
  3. ゆえに $\forall m \in \Z$ に対して

     $$
     \frac{f(\zeta)}{(\zeta - z)^{m+1}} := \sum_{n = -\infty}^\infty c_n(z - z_0)^{n - m - 1}
     $$

     とおくと、これは $D$ 上広義一様収束し、$\forall r \in {(R_1, R_2)}$ に対して
     閉集合 $C: \lvert z - z_0 \rvert = r$ 上一様収束する。
     積分すれば項別積分が可能なのでそうする：

     $$
     \begin{aligned}
         \int_C\!\frac{f(\zeta)}{(\zeta - z)^{m + 1}}\,\mathrm d\zeta
         &= \sum_{n = -\infty}^\infty c_n\int_C\!(\zeta - z_0)^{n - m - 1}\,\mathrm d\zeta\\
         &= 2\pi i \cdot c_m.
     \end{aligned}
     $$

     これは級数が $f$ の Laurent 展開であることを示している。

     コメント：円周上の多項式の積分の計算は既出だった：

     $$
     \int_C\!(z - z_0)^n\,\mathrm dz =
     \begin{cases}
     2\pi i, & n = -1,\\
     0, & n \ne -1.
     \end{cases}
     $$

# 留数定理

## 留数定理

----

以上で第 8 章と第 9 章。
