---
title: 『新訂解析学』学習ノート第九回
tags: math
---

熊原啓作著『新訂解析学』の学習ノート第九回。

# Laplace 変換

* 微分方程式の解法に応用できる。
* 片側複素 Fourier 変換の形をしている。

## Laplace 変換の定義と収束

* 実関数 $f(x)$ を ${(0, \infty)}$ で定義されていて、区分的に $C^0$ 級であるとする。
* 複素数 $s = \sigma + i\tau$ とする。

この条件で次の $s$ を変数とする複素関数を $f$ の **Laplace 変換**という：

$$
\mathscr{L}[f](s) := \int_0^\infty\!f(x)\mathrm{e}^{-sx}\,\mathrm dx.
$$

* **E 13.1**: $f(x) \equiv 1$

  $$
  \mathscr{L}[f](s) = \frac{1}{s},\quad(\Re s > 0).
  $$

* **E 13.2**: $f(x) = x^n$
  * $\mathscr{L}[x^n](s)$ は $n \in \R \land n > -1$ で $\Re(s) > 0$ ならば絶対収束する。
  * $\displaystyle \int_0^\infty\! \frac{\mathrm{d}}{\mathrm{d}s}(x^n \mathrm{e}^{-sx})\,\mathrm dx$
    は $\Re(s) > 0$ 上広義一様収束する。それゆえ
    $\mathscr{L}[x^n](s)$ はそこで $s$ の正則関数である。
  * $s \in \R \land s > 0$ のときは

    $$
    \begin{aligned}
    \mathscr{L}[x^n](s)
    &= \int_0^\infty\!t^n \mathrm{e}^{-t}\,\mathrm dt \quad(sx = t;\;s\,\mathrm dx = \mathrm dt)\\
    &= \frac{\varGamma(n + 1)}{s^{n + 1}}.
    \end{aligned}
    $$

    $1/s^{n+1}$ は $\Re(s) > 0$ 上で正則だから、一致の定理により定義域を拡張できる：

    $$
    \forall s\left(\Re(s) > 0 \implies \mathscr{L}[x^n](s)
    = \frac{\varGamma(n + 1)}{s^{n + 1}}\right).
    $$

* **Th 13.1**: 収束定理
  * 関数 $f(x)$ は区間 ${(0, \infty)}$ で区分的に $C^0$ 級であるとし、
  * 変換 $\mathscr{L}[f](s)$ が点 $s_0 \in \Complex$ で収束するとする。

  このとき：

  $$
  \forall s\left(\Re(s) > \Re(s_0) \implies \mathscr{L}[f](s) \text{ converges.}\right)
  $$

  証明：

  $s_0 := \sigma_0 + i\tau_0$ とおく。
  関数 $g(t)$ を $t > 0$ に対して次のように不定積分として定義する：

  $$
  g(t) := \int_0^t\!f(x)\mathrm{e}^{-s_0 x}\,\mathrm dx.
  $$

  するとこの関数には次の性質がある：
  * $g(t)$ は $C^0$ 級
  * $g(0) = 0$
  * $g(t) \to \mathscr{L}[f](s_0)\quad(t \to \infty)$

  すなわち $t \in {[0, \infty)}$ で有界であるから：

  $$
  \exists M \forall t(t \ge 0 \implies \lvert g(t)\rvert \le M).
  $$

  次に $s = \sigma + i\tau$ が $\sigma > \sigma_0$ を満たすと仮定する。
  $g^\prime(x) = f(x)\mathrm{e}^{-s_0 x}$ であるから $\forall T > 0$ にたいして：

  $$
  \begin{aligned}
      \left\lvert \int_0^T\! f(x)\mathrm{e}^{-s x}\,\mathrm dx \right\rvert
      &= \left\lvert \int_0^T\! \mathrm{e}^{-(s - s_0)x}g^\prime(x)\,\mathrm dx \right\rvert\\
      &= \left\lvert \mathrm{e}^{-(s - s_0)T}g(T) + (s - s_0)\int_0^T\!\mathrm{e}^{-(s - s_0)x}g(x)\,\mathrm dx\right\rvert\\
      &\le \lvert \mathrm{e}^{-(s - s_0)T}g(T) \rvert
        + \lvert s - s_0 \rvert \left\lvert\int_0^T\!\mathrm{e}^{-(s - s_0)x}g(x)\,\mathrm dx\right\rvert.
  \end{aligned}
  $$

  * 第一項は $M\mathrm{e}^{-(s - s_0)T}$ で上から押さえられる。
  * 第二項の積分の絶対値は $M \dfrac{1 - \mathrm{e}^{-(\sigma - \sigma_0)T}}{\sigma - \sigma_0}$ で上から押さえられる。

  どちらも $T \to \infty$ のとき有限値に収束するので、左辺のもとの積分は絶対収束する。
  すなわち $\mathscr{L}[f](s)$ は収束する。

* **Th 13.2**: 収束座標
  * 関数 $f(x)$ は区間 ${(0, \infty)}$ で区分的に $C^0$ 級であるとする。

  このとき変換 $\mathscr{L}[f](s)$ は次のいずれか一つの性質がある：
  1. $\forall s \in \Complex( \mathscr{L}[f](s) \text{ diverges.})$
  2. $\forall s \in \Complex( \mathscr{L}[f](s) \text{ converges.})$
  3. $\exists \sigma_0 \in \R \forall s(\Re(s) > \sigma_0 \implies \mathscr{L}[f](s) \text{ converges} \land \Re(s) < \sigma_0 \implies \mathscr{L}[f](s) \text{ diverges.})$

  * この 3. の $\sigma_0$ を**収束座標**という。1. と 2. はそれぞれ $\sigma_0 = -\infty, \infty$ の場合とみなせる。
  * **絶対収束座標**とは、次の値をいう：

    $$
    \sigma_0 = \inf_{\Re(s) > 0}\{ \sigma_1 \,|\, \sigma_1 = \Re(s), \int_0^\infty\,\lvert f(x)\mathrm{e}^{-sx}\rvert\,\mathrm dx < \infty\}.
    $$

  * **絶対収束領域**とは、絶対収束座標から右の部分をいう：

    $$
    \{ s \,|\, s \in \Complex \land \Re(s) > \sigma_0\}.
    $$

* **指数 $a$ 型**

  関数 $f(x)$ が ${[0, \infty)}$ で区分的に $C^0$ 級で、
  次の条件をみたすとき、$f$ は指数 $a$ 型であるという：

  $$
  \exists T > 0 \exists M > 0 \exists a(
      \forall x > T (
          \lvert f(x) \rvert \le M \mathrm{e}^{ax}
      )
  ).
  $$

  * $a$ を明示しないときは、たんに**指数位数である**という。
* **Th 13.3**: 指数位数の関数には Laplace 変換が存在する。

  関数 $f(x)$ が ${[0, \infty)}$ で区分的に $C^0$ 級で指数 $a$ 型であるとする。
  このとき次が成り立つ：

  * $\mathscr{L}[f](s)$ が存在する。
  * その収束座標は $a$ を超えない。
  * $\displaystyle \lim_{\Re(s) > 0} \mathscr{L}[f](s) = 0.$

  証明：

  まず指数位数条件を先ほどの定義文のように表現しておく。このとき：

  $$
  \begin{aligned}
  \forall \sigma(\sigma > a \implies\\
      \int_T^\infty\! \lvert f(x) \rvert \mathrm{e}^{-\sigma x}\,\mathrm dx
      &\le M \int_T^\infty\! \mathrm{e}^{-(\sigma - a)x}\,\mathrm dx\\
      &= M \frac{\mathrm{e}^{-(\sigma - a)T}}{\sigma - a}).\\

  \therefore
  \int_0^\infty\! \lvert f(x) \rvert \mathrm{e}^{-\sigma x}\,\mathrm dx &< \infty.
  \end{aligned}
  $$

  すなわち $\forall s(\Re(s) > a \implies \mathscr{L}[f](s) \text{ absolutely converges.})$

  また、$\lvert \mathscr{L}[f](s) \rvert \le \dfrac{M}{\sigma - a}$ ゆえ、$\sigma \to \infty$ として、主張の極限が成り立つ。
* **C 13.1**:

  関数 $f(x)$ が ${[0, \infty)}$ で有界ならば $\Re(s) > 0$ で Laplace 変換 $\mathscr{L}[f](s)$ は絶対収束する。

  証明：指数ゼロ型。

* 指数 $a$ 型 $f(x)$ について、その不定積分も指数 $a$ 型である。

  関数 $f(x)$ が ${[0, \infty)}$ で区分的に $C^0$ 級で指数 $a$ 型であるとする。
  $x_0 \ge 0$ に対して、関数 $g(x)$ を次のように不定積分として定義する：

  $$
  g(x) := \int_{x_0}^x\!f(t)\,\mathrm dt.
  $$

  すると $g(x)$ も $C^0$ 級となる。
  また、$f(x)$ についての指数位数条件を先ほどの定義文のように表現しておくと、
  $x > \max \lbrace T, x_0 \rbrace$ のとき $g(x)$ は：

  $$
  \begin{aligned}
  \lvert g(x) \rvert
  &\le M\int_{x_0}^x\! \mathrm{e}^{at}\,\mathrm dt\\
  &= \frac{M}{a}(1 - \mathrm{e}^{-a(x - x_0)})\mathrm{e}^{ax}\\
  &\le \frac{M}{a} \mathrm{e}^{ax}.
  \end{aligned}
  $$

  であるので、やはり指数 $a$ 型である。
* **E 13.3**

  $\alpha \in \Complex,;\Re(s) > \Re(\alpha)$ として：

  $$
  \mathscr{L}[\mathrm{e}^{\alpha x}](s)
  = \int_0^\infty\!\mathrm{e}^{-(s - \alpha)x}\,\mathrm dx
  = \frac{1}{s - \alpha}.
  $$

  証明： $s - \alpha \in \R \land s > \alpha$ のとき成り立つことを示す。
  次に正則性を示す。あとは一致の定理により成立領域を拡張する。
  **E 13.2**を参照。

## Laplace 変換の性質 1

* **Th 13.4**: 線形性
  関数 $f(x),\;g(x)$ にそれぞれ Laplace 変換が存在するとする。
  このとき、次が成り立つ：
  * $f(x) \pm g(x)$ にも Laplace 変換が存在し、

    $$
    \mathscr{L}[f(x) \pm g(x)](s) = \mathscr{L}[f](s) \pm \mathscr{L}[g](s).
    $$

  * $\forall k \in \R$ に対して $kf(x)$ にも Laplace 変換が存在し、

    $$
    \mathscr{L}[kf(x)](s) = k \mathscr{L}[f](s).
    $$

  証明：積分の線形性からどちらも明らかに成り立つ。
* **E 13.4**: $\cos{ax}, \sin{ax}$ の Laplace 変換
  * コメント：積分計算は三角関数を $\mathrm{e}^{iax}$ などで表すと楽。
* **Q 13.1**: $\cosh{ax}, \sinh{ax}$ の Laplace 変換
  * コメント：こちらは最初から指数関数なので迷わないだろう。
* **Q 13.2**: $\mathrm{e}^{ax}\cos{bx}, \mathrm{e}^{ax}\sin{bx}$ の Laplace 変換
  * コメント：まだ計算していないが、おそらく同時に求まる。
* **Th 13.5** スケーリング
  * $f(x)$ をこれまでどおりとし、
  * $\lambda > 0$ とする。

  このとき：

  $$
  \mathscr{L}[f(\lambda x)](s)
  = \frac{1}{\lambda} \mathscr{L}[f(x)]\left(\frac{\lambda}{s}\right).
  $$

  証明：書くほどのものでもない。$\lambda x = t$ として置換積分。
* **Th 13.6**: 導関数の Laplace 変換
  * 関数 $f(x)$ は区間 ${[0, \infty)}$ で指数 $a$ 型の $C^0$ 級関数とする。
  * $f^\prime(x)$ は
    * 区分的に $C^0$ 級、
    * 不連続点は高々有限個あり、
    * 指数位数である

  とする。このとき $f^\prime$ に関して次が成り立つ：

  $$
  \forall s(\Re(s) > a \implies
  \mathscr{L}[f^\prime](s)
  = s \mathscr{L}[f](s) - f(0)).
  $$

  証明：不連続点を丁寧に扱う必要があるが、基本的には直接計算だけで示せる。
  積分は置換積分を反復することで結論の形に変形できる。

* **C 13.2**: 高階導関数の Laplace 変換
  * $f, f^\prime, \dotsc, f^{(n - 1)}$ が **Th 13.6** における $f$ の条件を満たすとし、
  * $f^{(n)}$ が同じく $f^\prime$ の条件を満たすものとする。

  このとき次の等式が成り立つ：

  $$
  \mathscr{L}[f^{(n)}](s)
  = s^n \mathscr{L}[f](s) - s^{n-1}f(0) - s^{n-2}f^\prime(0) - \dotsb - f^{(n - 1)}(0).
  $$
* **Th 13.7**: 不定積分の Laplace 変換

  関数 $f(x)$ は区間 ${[0, \infty)}$ で指数位数かつ区分的に $C^0$ 級関数であるとする。
  このとき $x_0 \ge 0$ であれば：

  $$
  \mathscr{L}\left[\int_{x_0}^x\!f(t)\,\mathrm dt\right](s)
  = \frac{1}{s} \mathscr{L}[f](s) - \frac{1}{s}\int_0^{x_0}\!f(x)\,\mathrm dx.
  $$

  証明：

  この不定積分を $g(x)$ とおく。前述の通り $g$ も指数位数かつ $C^0$ 級関数である。
  **Th 13.6** より：

  $$
  \begin{aligned}
      \mathscr{L}[f](s) &= s \mathscr{L}[g](s) - g(0).\\
      \therefore \mathscr{L}[g](s) &= \frac{1}{s}(\mathscr{L}[f](s) + g(0)).
  \end{aligned}
  $$

----

第 13 章は後半が長いのでページを分割する。
