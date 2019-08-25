---
title: 『新訂解析学』学習ノート第一回
tags: math
---

本稿を熊原啓作著『新訂解析学』の学習ノート第一回とする。

# 複素数

* 複素数の偏角を一意的に定めないことがあるので注意する。
* **Riemann 球面**とは、以下に述べる考え方のことだ：
  * 空間 $\R^3$ に原点を中心とする単位球面 $S$ をとり、点 $(0, 0, 1)$ を $N$ とする。
  * $xy$ 平面と複素平面を同一視し、二点 $z = x + iy$ と$N$ を通る直線 $l$ をとる。
  * 直線 $l$ と球面 $S$ の交点を $(x_1, x_2, x_3)$ とおき、$\Complex \cup \lbrace\infty\rbrace$
    から $S$ への写像 $\varphi$ を $\varphi(z) = (x_1, x_2, x_3)$ で定義する。
    この写像をステレオグラフという。
  * 簡単な計算により次のように表される：

    $$
    \varphi(z) =
    \begin{dcases}
    \left(
        \dfrac{2 \Re z}{\lvert z \rvert^2 + 1},
        \dfrac{2 \Im z}{\lvert z \rvert^2 + 1},
        \dfrac{\lvert z \rvert^2 - 1}{\lvert z \rvert^2 + 1}\right),
        & z \in \Complex,\\
    (0, 0, 1), & z = \infty.
    \end{dcases}
    $$

  * ステレオグラフには逆写像が存在する（球面上の点を平面に投影する）：

    $$
    \varphi^{-1}(x_1, x_2, x_3) =
    \begin{cases}
    \dfrac{x_1 + i x_2}{1 - x_3}, & (x_1, x_2, x_3) \ne N,\\
    \infty, & (x_1, x_2, x_3) = N.
    \end{cases}
    $$

* 定数を $\alpha \in \Complex, r \in \R, r > 0$ とすると、方程式 $\lvert z - \alpha \rvert = r$ は複素平面上で円を表す。
  ここに $\alpha = a + bi$ などと置いて展開すると、円は次の形に書けることがわかる：

  $$
  a \lvert z \rvert^2 + \beta z + \overline{\beta z} + d = 0,
  \quad a, d \in \R,\;
  \beta \in \Complex,\;
  \lvert \beta \rvert^2 > ad.
  $$

  * $a = 0$ のときは直線である。半径が $\infty$ な円という解釈でよい。

# 複素微分

基本からおさらいしていく。以下とうぶんの間、特に断りがなければ

$$
w = f(z) = P(x, y) + iQ(x, y)
$$

とする。

* **Cauchy-Riemann の方程式**

  $$
  \frac{\partial P(x, y)}{\partial x} = \frac{\partial Q(x, y)}{\partial y},
  \frac{\partial Q(x, y)}{\partial x} = -\frac{\partial P(x, y)}{\partial y}.
  $$

  * 意外に「どっちがどっちだっけ状態」になるので、導出方法を覚えておく。
  * まず微分可能な実関数 $f$ では次が成り立つ：

    $$
    f(x + h) = f(x) + hf^\prime(x) + o(h).
    $$

    これは微分可能な複素関数でも成り立つはずなので、実数 $x$ の代わりに
    複素数 $z = x + iy$ を、実数 $h$ の代わりに複素数 $\varDelta z = \varDelta x + i\varDelta y$ で置き換えてみる。
    さらに $f^\prime(z) = \Re f^\prime(z) + i\Im f^\prime(z)$ と置いて $f(z + \varDelta z)$ を展開する。実部と虚部を比較することで
    次の方程式が得られる：

    $$
    \def\zero{o(\sqrt{\varDelta x^2 + \varDelta y^2})}
    \begin{aligned}
    P(x + \varDelta x, y + \varDelta y) &= P(x, y) + \Re f^\prime(z)\varDelta x - \Im f^\prime(z)\varDelta y + \zero,\\
    Q(x + \varDelta x, y + \varDelta y) &= Q(x, y) + \Im f^\prime(z)\varDelta x + \Re f^\prime(z)\varDelta y + \zero.
    \end{aligned}
    $$

    最後に極限 $\varDelta x \to 0, \varDelta y \to 0$ を考えると、
    二つの式から $\Re f^\prime(z), \Im f^\prime(z)$ の二通りの表現を得られる。

* (Th 2.7) $f(z)$ が微分可能であることと、
  $P(x, y), Q(x, y)$ が全微分可能であり、かつ Cauchy-Riemann の方程式が成り立つことは同値である。

* Cauchy-Riemann の方程式が成り立つならば、その関数は $\overline z$ の関数であってはならない。

* (Th 2.8) 領域 $D$ 上 $C^1$ 級関数 $f(z)$ が $f^\prime(z) = 0$ を満たすならば、
  それは $D$ 上定数関数である。
  * コメント：脚注によれば、領域 $D$ が複数の連結成分からなる場合、各連結成分において定数値が異なることがある。

* **正則関数**とは、複素平面内のある領域上で微分可能な関数である。
* **整関数**とは、正則関数であり、その定義域が複素平面全体であるものである。
* 正則関数 $f(z)$ について、Cauchy-Riemann の方程式から、常に次の関係式が成り立つといえる：

  $$
  \frac{\partial P^2}{\partial x^2} + \frac{\partial P^2}{\partial y^2} = 0,\;
  \frac{\partial Q^2}{\partial x^2} + \frac{\partial Q^2}{\partial y^2} = 0.
  $$

  このように、各独立変数について二階微分をとって和を取るとゼロになる性質をもつ実関数は**調和関数**であるという。
  正則関数の実部と虚部はどちらも調和関数である。

* 整級数 a.k.a. べき級数

  とうぶんの間、単にべき級数と言ったら次のものを指す：

  $$
  f(z) = \sum_{n = 0}^\infty c_n z^n.
  $$

* ほとんど微分積分入門の復習になるが、**収束円**の概念には注意する。実数のときは区間であるものが、複素数ではほんとうに円になる。
* (Th 2.15) (Cauchy-Hadamard) べき級数の収束半径 $\rho$ は次で与えられる：

  $$
  \frac{1}{\rho} = \limsup_{n \to \infty}\sqrt[n]{\lvert c_n \rvert}.
  $$

  * 証明を残したいが、テキスト化するとわかりにくくなる。困った。
    見返すときのためにいくつか言い残しておく：
    * **上限**の定義を $\varepsilon$ 方式で書き下してみる（二つの陳述からなるだろう）。それから証明方針を検討する。
    * 次から推論していけば、収束円内でべき級数が収束することは示せる。

      $$
      \forall \delta\left(\delta > 0 \implies \left(\frac{1 - \delta}{\rho^{-1} + \delta} < \rho\right)\right).
      $$

      $$
      \forall \delta\left(\delta > 0 \implies
      \exists N\left(N \in \N \implies
      \forall n\left(n \ge N \implies
      \left(\sqrt[n]{\lvert c_n \rvert} < \rho^{-1} + \delta\right)\right)\right)\right).
      $$

      $$
      \forall \delta\left(\delta > 0 \implies
      \exists z \in \Complex\left(
      \lvert z \rvert < \frac{1 - \delta}{\rho^{-1} + \delta}\right)\right).
      $$

* (Th 2.17) べき級数は収束円内部で $C^1$ 級関数であり、導関数は項別微分で得られる。
  * この定理を再帰的に適用することができ、次がわかる：

    $$
    c_n = \frac{f^{(n)}(0)}{n!},\quad
    \therefore f(z) = \sum_{n = 0}^\infty \frac{f^{(n)}(0)}{n!}z^n.
    $$

* **解析関数**とは、ある領域上で定義された関数であり、各点でべき級数に展開可能であるものである。
* **解析接続**とは、べき級数の集まりである：各点に対応してべき級数が与えられていて（関数要素という）、それらを一体化して扱われるもののことらしい。

# 初等関数

* 指数関数
  * $\mathrm{e}^z$ を実数版 $\mathrm{e}^x$ の Taylor 展開における素直な拡張として定義する。
  * (Euler) $\mathrm{e}^{i\theta} = \cos\theta + i\sin\theta.$
  * (de Moivre) $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta.$
* 三角関数
  * $\cos z, \sin z$ を実数版 $\cos x, \sin x$ から素直に定義する。
  * $\tan z$, etc. も芋づる式に定義する。
* 双曲線関数
  * $\cosh z, \sinh z$ を指数関数により定義する：

    $$
    \cosh z := \frac{\mathrm{e}^z + \mathrm{e}^{-z}}{2},\\
    \sinh z := \frac{\mathrm{e}^z - \mathrm{e}^{-z}}{2},\\
    $$

  * $\tanh z$ は両者の商で定義する：

    $$
    \tanh z := \frac{\sinh z}{\cosh z}.
    $$

  * 注意すべきは級数展開の形だ。三角関数のそれと同じと言ってもいい。
    例として $\cosh z$ を挙げる：

    $$
    \begin{aligned}
    \cosh z &= 1 + \frac{1}{2!}z^2 + \frac{1}{4!}z^4 + \dotsb + \frac{1}{(2m)!}z^{2m} + \dotsb\\
    &= \cos iz.
    \end{aligned}
    $$

* 対数関数
  * 複素数版の $\log$ は厄介なことに無限多価関数である。これは偏角がそうであることからくる。

    $$
    \log z = \log \lvert z \rvert + i\arg z.
    $$

  * 多価関数であることを避けたい場合、方法は二つある。主値を採用する場合と、Riemann 面を採用する場合がある。
  * **主枝**を次のようにとり、対数関数の虚部の値をここに制限するようにしたものを $\operatorname{Log}$ で表す。

    $$
    \{z \in \Complex\!\setminus\!\{0\}\,|\, \arg z \in {(-\pi, \pi)}\}
    $$

  * (Th 3.1) $\operatorname{Log}$ のべき級数表示

    $$
    \operatorname{Log}(1 + z) = \sum_{n = 1}^\infty (-1)^{n - 1}\frac{z^n}{n!},\quad \lvert z \rvert < 1.
    $$

  * **Riemann 面**は考える多価関数によって異なるものである。
    数学的オブジェクトの名前というよりは手法の呼び名と思ったほうがいい。
    ここでは $\log$ についてのそれを説明する。

    * 関数 $\log z$ の Riemann 面とは、次のような集合 $\bm D$ である：

      $$
      \bm D := \bigcup_{n \in \N} D_n,\\
      D_n := \{z \in \Complex\!\setminus\!\{0\}\,|\,\arg z \in {((2n - 1)\pi, (2n + 1)\pi]}\}.
      $$

    * まず $\bm z \in \bm D$ と極座標表示 $(r, \theta)$ との間に全単射が得られる。
      それをもとに $\log\colon\bm D \longrightarrow \Complex$ を
      $\log(\bm z) = \log r + i\theta$ で定義すれば一価関数になる。

    * **射影**：写像 $p\colon\bm D \longrightarrow \Complex$ を $p(\bm z) = z$ で定義すると、これは全射である。
    * この $\log$ は $\bm D$ 上正則関数である。$\bm z \in \bm D$ のある近傍に対して、
      $p(\bm z)$ のある近傍が一対一対応して、ここでは正則関数であるという意味である。

* 累乗関数 a.k.a. べき関数
  * 特に指数が整数でない場合は $\log$ を用いて定義することになる：

    $$
    \alpha \in \Complex,\; z \ne 0 \implies
    z^\alpha := \mathrm{e}^{\alpha \log z}.
    $$

  * $\alpha \in \Z$ ならば関数 $z^\alpha$ は一価である。実数の場合と同じ計算規則が成立する。
  * $\alpha \in \mathbb{Q}\setminus\Z$ の場合。$\alpha = m/n$ と既約分数に書き直しておくと：
    $z^\alpha = z^{m/n}$ だから、先に $n$ 乗根を議論する。

    * $z^{1/n}\;\;(n \in \N)$ は多価である。Riemann 面を構成すれば一価になる：

      $$
      \begin{aligned}
      \bm D &:= C_0 \cup \bigcup_{n \in \N}C_n;\\
      C_0 &:= \{z \in \Complex\,|\, \arg z \in {[0, 2\pi]}\},\\
      C_n &:= \{z \in \Complex\,|\, \arg z \in {[2nk\pi, 2nk\pi + 2\pi]}\}.
      \end{aligned}
      $$

      これにより $\bm z \longmapsto z^{1/n}$ は一価関数となり、原点を除いて正則である。
  * $\alpha \in \R\setminus\mathbb{Q}$ の場合、べき関数は無限多価になる。
    $\mathrm{e}^{\alpha \operatorname{Log}z}$ を $z^\alpha$ の主値という。
  * $z^\alpha$ は $z \ne 0$ において正則であり、導関数は次のように（よく知られた結果に）なる：

    $$
    \begin{aligned}
    \frac{\mathrm{d}}{\mathrm{d}z} z^\alpha
    &= \frac{\mathrm{d}}{\mathrm{d}z} \mathrm{e}^{\alpha \log z}\\
    &= \mathrm{e}^{\alpha \log z} \frac{\mathrm{d}}{\mathrm{d}z}(\alpha\log z)\\
    &= z^\alpha \cdot \frac{\alpha}{z}\\
    &= \alpha z^{\alpha - 1}.
    \end{aligned}
    $$
* 逆三角関数
  * 対数関数・べき関数で定義することになる。一例を挙げると：

    $$
    \begin{aligned}
    w &= \arcsin z\\
    z &= \sin w = \frac{\mathrm{e}^{iw} - \mathrm{e}^{-iw}}{2i}\\
    \mathrm{e}^{2iw} - 2iz\mathrm{e}^{iw} - 1 &= 0\\
    e^{iw} &= iz + (1 - z^2)^{1/2}\\
    \therefore w &= -i \log(iz + (1 - z^2)^{1/2}).
    \end{aligned}
    $$

* 逆双曲線関数
  * やっていない。

----

第二回へ続く。
