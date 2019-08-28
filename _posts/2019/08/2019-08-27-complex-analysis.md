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

## Fourier 変換

コメント：関数 $f(x)$ の Fourier 変換とは（存在すれば）次の（変数 $\xi$ の）関数である：

$$
\mathscr{F}[f](\xi) := \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty\!f(x)\mathrm{e}^{-i\xi x}\,\mathrm dx.
$$

* **絶対積分可能**

  関数 $f(x)$ が 1-ノルムが有限であることをいう。すなわち：

  $$
  \|f\|_1 := \int_{-\infty}^\infty\! \lvert f(x)\rvert\,\mathrm dx < \infty.
  $$

* **Th 13.8**: 絶対積分可能ならば Fourier 変換は絶対収束する

  $f(x)$ を $\R$ 上区分的に $C^0$ 級であるとし、かつ絶対積分可能であるとする。
  このとき $\mathscr{F}[f](\xi)$ は $\forall \xi \in \R$ で絶対収束し：

  $$
  \lvert \mathscr{F}[f](\xi) \rvert \le \frac{1}{\sqrt{2\pi}} \|f\!\|_1.
  $$

  証明：すなおに評価する。
* **L 13.1**: Riemann-Lebesgue の定理を証明するための補題

  関数 $f(x)$ が区間 ${[a, b]}$ で区分的に $C^0$ 級であるならば：

  $$
  \def\I#1{ \lim_{\lvert \xi\rvert \to \infty}\int_a^b\! f(x){#1}\,\mathrm dx }
  \I{\sin\xi x} = \I{\cos \xi x} = 0.
  $$

  証明：

  * $\sin$ のほうがゼロであることを示す。$\cos$ の証明も同様である。
  * $f(x)$ に関する条件のうち「区分的に」は無視して構わない。
    閉区間 ${[a, b]}$ 全体で連続であるものとして、$f$ が一様連続であることを活かす。

    一様連続を定式化しておく：

    $$
    \forall \varepsilon \exists \delta \forall x_1 \forall x_2(
        \varepsilon > 0 \implies \delta > 0 \land
        \\
        \left(\lvert x_1 - x_2 \rvert < \delta \implies
        \lvert f(x_1) - f(x_2) \rvert < \frac{\varepsilon}{2(b - a)}\right)
    ).
    $$

  * 区間 ${[a, b]}$ を $(b - a) < n\delta$ をみたす $n$ で等分割する：
    $a = x_0 < x_1 < \dotsb < x_n = b.$
  * 次の等式を各細分区間で評価する：

    $$
    \def\I#1{ \int_a^b\!{#1}\,\mathrm dx}
    \I{f(x)\sin\xi x} = \I{(f(x) - f(x_0))\sin\xi x} - f(x_0)\I{\sin\xi x}.
    $$

    * 第一項

      $$
      \left\lvert \sum\int_{x_{k-1}}^{x_k}(f(x) - f(x_k))\sin\xi x\,\mathrm dx\right\rvert
      \le \frac{\varepsilon}{2(b - a)} \sum \int_{x_{k-1}}^{x_k}\mathrm dx
      = \frac{\varepsilon}{2}.
      $$

    * 第二項。$\xi > 0$ かつ $\lvert f(x) \rvert \le M$ であるとして：

      $$
      \left\lvert \sum\int_{x_{k-1}}^{x_k}f(x_k)\sin\xi x\,\mathrm dx\right\rvert
      \le M \sum\frac{\lvert \cos\xi x_k - \cos\xi x_{k-1}\rvert}{\xi}
      \le \frac{2nM}{\xi}.
      $$

    ゆえに十分大きい $\xi > \dfrac{4nM}{\varepsilon}$ に対して

    $$
    \left\lvert \int_a^b\!{\sin\xi x}\,\mathrm dx \right\rvert \le \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
    $$
* **Th 13.9** (Riemann-Lebesgue)

  前定理と同じ仮定の下：

  $$
  \lim_{\lvert \xi \rvert \to \infty} \mathscr{F}[f](\xi) = 0.
  $$

  証明：

  絶対積分可能条件から

  $$
  \forall \varepsilon(
      \varepsilon > 0 \implies
      \exists T_0(
          \forall T(T \ge T_0 \implies\\
            \int_{-\infty}^{-T}\!\lvert f(x)\rvert\,\mathrm dx
            + \int_{T}^\infty\!\lvert f(x)\rvert\,\mathrm dx < \frac{\varepsilon}{2}
          ))).
  $$

  一方、**L 13.1** より

  $$
  \exists T_1(T_1 > 0 \land \forall \xi > T_1(
      \left\lvert \int_{-T_0}^{T_0}\!f(x)\sin\xi x\,\mathrm dx\right\rvert < \frac{\varepsilon}{2})
  ).
  $$

  $$
  \def\e{ \frac{\varepsilon}{2} }
  \therefore \forall \xi(\xi > T_1 \implies\\
  \left\lvert \int_{-\infty}^\infty\!f(x)\sin\xi x\,\mathrm dx \right\rvert
  < \e + \e = \varepsilon).
  $$

* **Dirichlet 核**

  $L > 0$ に対応して、次の関数を $L$ の Dirichlet 核と呼ぶ：

  $$
  \begin{aligned}
  D^L(x) &:= \int_0^L\!\cos tx\,\mathrm dt\\
  &= \begin{dcases}
  \frac{\sin Lx}{x}, & (x \ne 0),\\
  L, & (x = 0).
  \end{dcases}
  \end{aligned}
  $$

  $a < 0 < b$ のとき次が成り立つ：

  $$
  \lim_{L \to \infty}\int_a^b\!D^L(x)\,\mathrm dx = \pi.
  $$

  証明：$Lx = t$ で置換積分。途中で現れる $\displaystyle \int_{\R}\frac{\sin u}{u}\,\mathrm du$ は留数定理の応用で求まる。
* **Th 13.10**: 不連続点における値

  $f(x)$ を $\R$ 上区分的に $C^1$ 級かつ絶対積分可能な関数であるとする。このとき：

  $$
  \lim_{L \to \infty}\frac{1}{\pi}\int_{-\infty}^\infty\!f(t)D^L(t)(x - t)\,\mathrm dt
  = \frac{1}{2}(f(x - 0) + f(x + 0)).
  $$

  証明： $x=x_0$ が連続か不連続かで場合分けして示す。先に連続点の場合を示す。

  絶対積分可能条件から：

  $$
  \def\I#1#2#3{ \frac{1}{\pi}\int_{#1}^{#2}\! \lvert{#3}\rvert\,\mathrm dt }
  \begin{aligned}
  \forall \varepsilon(\varepsilon > 0 &\implies \exists T(
      T > 0 \land \\
      & \phantom{\le} \I{-\infty}{-T}{f(t)D^L(x_0 - t)} + \I{T}{\infty}{f(t)D^L(x_0 - t)}\\
      & \le \I{-\infty}{-T}{f(t)} + \I{T}{\infty}{f(t)}\\
      & < \frac{\varepsilon}{2}
  )).
  \end{aligned}
  $$

  連続点においては結論の右辺は $f(x)$ に等しい。
  以下次を示す：

  $$
  \def\I#1#2#3{ \frac{1}{\pi}\int_{#1}^{#2}\! {#3}\,\mathrm dt }
  \begin{aligned}
  \exists L(L &> 0 \land\\
  &\left\lvert \I{-T}{T}{f(t)D^L(x_0 - t)} - f(x_0)\right\rvert < \frac{\varepsilon}{2}).
  \end{aligned}
  $$

  Direchlet 核の定義により：

  $$
  \def\L{ \lim_{L \to \infty} }
  \def\I#1#2#3#4{ \L \frac{1}{\pi} \int_{#1}^{#2}\!{#3}\,\mathrm{d}{#4} }
  \begin{aligned}
      &\phantom{=} \I{-T}{T}{f(t)D^L(x_0 - t)}{t} - f(x_0)\\
      &= \I{x_0 - T}{x_0 + T}{f(x_0 - u)D^L(u)}{u} - f(x_0) \quad(t := x_0 - u)\\
      &= \I{x_0 - T}{x_0 + T}{f(x_0 - u) - f(x_0))D^L(u)}{u}\\
      &= \I{x_0 - T}{x_0 + T}{\frac{f(x_0 - u) - f(x_0)}{u}\sin Lu}{u}.
  \end{aligned}
  $$

  被積分関数の分数部分を $g(u)$ とおくと、これは $u \ne 0$ において区分的に $C^1$ 級、
  $u = 0$ で $g(\pm 0) = -f^\prime(x_0 \mp 0).$
  ゆえに区分的に $C^0$ 級。

  **L 13.1** をここで使い、

  $$
  \lim_{L \to \infty} \int_{-\infty}^\infty\!g(u)\sin Lu\,\mathrm du = 0.
  $$

  以上、連続点の場合は成り立つことを示した。

  以下、$x = x_0$ が不連続点であっても成り立つことを示す。

  $$
  \def\h#1{ \frac{1}{2}(f(x_0 + {#1}) + f(x_0 - {#1})) }
  h(x_0 + t) :=
  \begin{dcases}
  \h{t}, & t \ne 0,\\
  \h{0}, & t = 0.
  \end{dcases}
  $$

  $h$ は $C^0$ 級かつ区分的に $C^1$ 級である。すると前半の議論が適用できて：

  $$
  \def\L{ \lim_{L \to \infty} }
  \def\I#1{ \frac{1}{\pi} \int_{-\infty}^\infty\! {#1} D^L(t) \,\mathrm{d}t }
  \begin{aligned}
  h(x_0) &= \L \I{h(x_0 + t)}\\
  &= \L \I{ \frac{1}{2}(f(x_0 + t) + f(x_0 - t)) }\\
  &= \L \I{f(x_0 + t)}.
  \end{aligned}
  $$

  最後の等号は偶関数の性質による。
* **Th 13.11**: 不連続点と Fourier 展開の関係

  $f(x)$ を前定理と同じように仮定する。このとき：

  $$
  \frac{1}{2}(f(x - 0)) + f(x + 0))
  = \lim_{L \to \infty}\frac{1}{\sqrt{2\pi}}\int_{-L}^L\!\hat{f}(\xi)\mathrm{e}^{i\xi x}\,\mathrm d\xi.
  $$

  証明：右辺を直接計算する。$\sin$ は期間数なので $\cos$ 側が残って：

  $$
  \begin{aligned}
      \lim_{L \to \infty}\int_0^L\!\int_{-T}^T\!f(u)\cos\xi(x - u)\,\mathrm du \mathrm d\xi
      &= \int_0^L\int_{-\infty}^\infty\!f(u)\cos\xi(x - u)\,\mathrm du \mathrm d\xi.
  \end{aligned}
  $$

  左辺に対しては積分の順序交換により：

  $$
  \def\F{ f(u)\cos\xi(x - u) }
  \begin{aligned}
      \dots &= \int_{-T}^T\int_0^L\!\F\,\mathrm d\xi\mathrm du\\
      \therefore \int_0^L \int_{-\infty}^\infty\! \F\,\mathrm du \mathrm d\xi
      &= \int_{-\infty}^\infty\! \int_0^L \F \,\mathrm d\xi\mathrm du.
  \end{aligned}
  $$

  前定理より OK となる。
* **Fourier 逆変換**

  関数 $g(\xi)$ に対して次の変換を $g$ の Fourier 逆変換と呼ぶ：

  $$
  \mathscr{F}^{-1}[g](x) := \frac{1}{2\pi}\int_{-\infty}^\infty\!g(\xi)\mathrm{e}^{i \xi x}\,\mathrm d\xi.
  $$

* $f$ が区分的に $C^1$ 級関数かつ絶対積分可能かつ $C^0$ 級ならば

  $$\mathscr{F}^{-1}[\mathscr{F}[f]](x) = f(x).$$

* **E 13.5**: 指示関数の Fourier 変換

  $$
  f(x) =
  \begin{cases}
      1, & x \in {[-L, L]},\\
      0, & x \notin {[-L, L]}.
  \end{cases}
  $$

  $$
  \begin{aligned}
  \mathscr{F}[f](\xi) &= \frac{1}{\sqrt{2\pi}}\int_{-L}^L\!\mathrm{e}^{-i\xi x}\,\mathrm dx\\
  &= \frac{1}{\sqrt{2\pi}}\frac{\mathrm{e}^{iL\xi} - \mathrm{e}^{-iL\xi}}{i\xi}\\
  &= \sqrt{\frac{2}{\pi}}\cdot\frac{\sin L \xi}{\xi},\quad(\xi \ne 0).\\
  \mathscr{F}[f](0) &= \frac{1}{\sqrt{2\pi}}\int_{-L}^L\!\mathrm dx\\
  &=\frac{2L}{\sqrt{2\pi}}\\
  &= \sqrt{\frac{2}{\pi}}L.
  \end{aligned}
  $$

* **E 13.6**: $\mathrm{e}^{-x^2/2}$ の Fourier 変換

  $$
  \mathscr{F}[\mathrm{e}^{-x^2/2}](\xi)
  = \frac{1}{2\pi} \mathrm{e}^{-\xi^2/2}\int_{-\infty}^\infty\! \mathrm{e}^{-(x + i\xi)^2/2}\,\mathrm dx.
  $$

  * 積分路：$\xi > 0$ とすると点 $-R$, $R + i\xi$ を対角線に持つ矩形を正の向きにとる。
  * 虚軸に平行な積分路上では、評価の結果積分はゼロである。
  * 結果的に（係数部分を除いた）積分部分は Gauss より $\sqrt{2\pi}$ であるから、
    求める Fourier 変換は：

    $$
    \def\f{ \mathrm{e}^{-x^2/2} }
    \mathscr{F}[\f](\xi) = \f.
    $$

## Laplace 逆変換

* **Th 13.12**: **Laplace 反転積分** a.k.a. **Bromwich** 積分
  * 関数 $f(x)$ を ${(0, \infty)}$ 上区分的に $C^1$ 級であるとし、
  * $f(x) \mathrm{e}^{-\sigma_0 x}$ が絶対積分可能であるとする。

  $$
  \begin{aligned}
  \forall \sigma(\sigma &> \sigma_0 \implies\\
      &\frac{1}{2}(f(x - 0) + f(x + 0))
      = \frac{1}{2\pi i}\int_{\sigma - i\infty}^{\sigma + i\infty}
       \mathscr{L}[f](s)\mathrm{e}^{sx}\,\mathrm ds
  ).
  \end{aligned}
  $$

  証明：

  $$
  F(x) = \begin{cases}
  \sqrt{2\pi}f(x),& x > 0,\\
  0, & x < 0.
  \end{cases}
  $$

  とおく。$s = \sigma + i\tau$ に関して

  $$
  \mathscr{L}[f](s) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty\!F(x)\mathrm{e}^{-\sigma x}\mathrm{e}^{-i\tau x}\,\mathrm dx
  = \mathscr{F}[F(x)\mathrm{e}^{-\sigma x}](\tau).
  $$

  このとき $F(x)\mathrm{e}^{-\sigma x}$ は $\sigma > \sigma_0$ のとき絶対積分可能であり、
  $f$ の条件から区分的 $C^1$ 級関数。これに **Th 13.11** を適用する：

  $$
  \def\m{ (F(x + 0) + F(x - 0)) }
  \def\I#1{ \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty\! \mathscr{L}[f](\sigma + i\tau)\mathrm{e}^{#1}\,\mathrm dx }
  \begin{aligned}
      \frac{\mathrm{e}^{-\sigma x}}{2}\m
      &= \I{i\tau x}.\\
    \therefore \frac{1}{2}\m
      &= \I{\sigma + i\tau x}.\\
  \end{aligned}
  $$

* **C13.3**: $C^0$ 級関数 $f, g$ が $\mathscr{L}[f] = \mathscr{L}[g] \implies f = g.$

----

以上。
