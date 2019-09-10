---
title: 『常微分方程式』学習ノート Part 6
tags: math
---

高崎金久著『常微分方程式』（日本評論社）ノートその六。第 7 章の前半をやる。
後半は読み飛ばしていた第 4 章を済ませた後に取り組む。

# 第 7 章 一般的な微分方程式

## §7.1 初期値問題の回の存在と一意性

まずは単独一階 ODE の初期値問題から考察する。

$$
y^\prime = f(x, y),\quad y(x_0) = y_0.
$$

* $f(x, y)$ の定義域を $\varOmega \subset \R^2$ とする。
* $f(x, y)$ は $C^0$ 級であると仮定する。実用上はこれで問題ない。
  * この条件だけでは、解の存在性はいえても一意性が一般には担保できないことが知られている（本文中の Peano の例を参照）。
* $f(x, y)$ が Lipschitz 条件を満たすと仮定することで、一意性が十分保証される。
* **Lipschitz 条件**
  * 関数 $f(x, y)$ が Lipschitz 連続であるとは、次の条件を満たすことをいう：

    $$
    \exists L \forall x \forall y_1 \forall y_2\\
    ((x, y_1) \in \varOmega \land (x, y_2) \in \varOmega
    \implies
    \lvert f(x, y_1) - f(x, y_2) \rvert \le L \lvert y_1 - y_2 \rvert).
    $$

  * Lipschitz 連続性は $C^0$ 級と $C^1$ 級の間にあるようなイメージ。
    * $C^1$ 級関数は平均値の定理により Lipschitz 連続である。

冒頭の ODE を積分方程式の形に書き直して考えると都合がいい：

$$
y(x) = y_0 + \int_{x_0}^x\!f(t, y(t))\,\mathrm dt.
$$

コメント：先に一意性を証明するようだ（どちらを先にしてもいい）。

* (Th 7.1) 関数 $f(x, y)$ は $\varOmega$ を定義域とする $C^0$ 級であり、
  $y$ について Lipschitz 連続であるとする。
  このとき $(x_0, y_0)\in\varOmega$ において初期条件

  $$
  y(x_0) = y_0
  $$

  を満たす解が存在すれば、それは $x_0$ のある近傍で一意的に定まる。

  * 証明：
    * 関数 $f$ の Lipschitz 定数を $L \ge 0$ とおく。
    * 関数 $u(x), v(x)$ が与えられた ODE の解であると仮定する。
      そして両者の差を評価する：

      $$
      \begin{aligned}
      \lvert u(x) - v(x) \rvert
      &= \left\lvert \int_{x_0}^x\!(f(t, u(t)) - f(t, v(t)))\,\mathrm dt\right\rvert\\
      &\le \int_{x_0}^x\! \left\lvert f(t, u(t)) - f(t, v(t))\right\rvert \,\mathrm dt\\
      &\le L \int_{x_0}^x\! \left\lvert u(t) - v(t)\right\rvert \,\mathrm dt.
      \end{aligned}
      $$

    * ここで $x_0$ の $\delta$ 近傍を $D = \lbrace x\,\mid\, \lvert x - x_0 \rvert < \delta\rbrace$ とおく。
    * さらに $\displaystyle m = \max_{x \in D} \lbrace \lvert u(x) - v(x) \rvert\rbrace$ とおくと、評価の続きはこうなる：

      $$
      \begin{aligned}
      \lvert u(x) - v(x) \rvert
      &\le L \int_{x_0}^x\! \left\lvert u(t) - v(t)\right\rvert \,\mathrm dt\\
      & \le L \int_{x_0}^x\! m \,\mathrm dt\\
      & \le Lm\delta.\\
      \therefore m &\le Lm\delta.
      \end{aligned}
      $$

      $\delta > 0$ を $L\delta < 1$ を満たすように十分小さくとることができるので、この不等式は $m = 0$ のときにしか成立しない。
      すなわち：

      $$
      \forall x \in D (\lvert u(x) - v(x) \rvert = 0).
      $$

    * 以上により、$x = x_0$ のある近傍においては、解が存在すれば一意であることが証明された。
      解曲線に沿ってこのような近傍を構成ができるから、一意性が担保される定義域を「接続」していくことができる。

次に存在性を証明する。

* (Th 7.2) (Th 7.1) と同じ仮定の下、初期条件 $y(x_0) = y_0$ を満たす解が
  $x = x_0$ の近傍で存在する。
  * 証明：
    * 次のように定義域の部分集合（閉集合）、正の定数をとっておく：

      $$
      \begin{aligned}
      a &> 0,\\
      b &> 0,\\
      \varOmega_0 &= \{(x, y)\,|\,\lvert x - x_0 \rvert \le a \land \lvert y - y_0 \rvert \le b \} \subset \varOmega,\\
      M &= \max_{(x, y) \in \varOmega_0} \{\lvert f(x, y)\rvert\}.
      \end{aligned}
      $$

      ただし $Ma \le b$ が成り立つように $a$ を（小さく）とるものとする。
    * Picard の逐次近似法を適用する。

      関数列 $\lbrace u_k(x)\rbrace$ を次の漸化式により定義する：

      $$
      \begin{aligned}
      u_0(x) &= y_0,\\
      u_{k+1}(x) &= y_0 + \int_{x_0}^x\!f(t, u_k(t))\,\mathrm dt.
      \end{aligned}
      $$

      * 定義から、各 $u_k(x)$ はある $x_0$ の $a$ 近傍 $D_0$ において $C^1$ 級である。
      * 関数列が収束することを示すわけだが、そのために階差を $v_k(x)$ とおいて、これを評価していく：

        $$
        \begin{aligned}
        \lvert v_{k+1}(x)\rvert
        &= \lvert u_{k+1}(x) - u_k(x)\rvert\\
        &\le \left\lvert \int_{x_0}^x\!(f(t, u_k(t)) - f(t, u_{k-1}(t)))\,\mathrm dt \right\rvert\\
        &\le \int_{x_0}^x\! \left\lvert f(t, u_k(t)) - f(t, u_{k-1}(t))\right\rvert \,\mathrm dt \\
        &\le L \int_{x_0}^x\! \left\lvert u_k(t) - u_{k-1}(t)\right\rvert \,\mathrm dt\\
        &= L \int_{x_0}^x\! \left\lvert v_k(t)\right\rvert \,\mathrm dt.\\
        \\
        \therefore \lvert v_{k+1}(x)\rvert &\le \int_{x_0}^x\! \left\lvert v_k(t)\right\rvert \,\mathrm dt.
        \end{aligned}
        $$

    * $u_k(x) = u_0(x) + \sum v_j(x)$ であるので、この式中の級数の収束性を示せば、関数列も収束することが示される。

      $$
      \begin{aligned}
      \lvert v_1(x) \rvert
      &= \lvert u_1(x) - u_0(x) \rvert\\
      &= \left\lvert \int_{x_0}^x\!f(t, y_0)\,\mathrm dt\right\rvert\\
      &\le \int_{x_0}^x\!\lvert f(t, y_0)\rvert\,\mathrm dt\\
      &\le M \lvert x - x_0\rvert,\\
      \\
      \lvert v_2(x) \rvert
      &\le L\int_{x_0}^x\!\lvert v_1(t)\rvert\,\mathrm dt\\
      &\le L\int_{x_0}^x\! M \lvert t - x_0 \rvert\,\mathrm dt\\
      &= \frac{ML}{2}\lvert x - x_0 \rvert^2.\\
      \\
      &\dotsc,\\
      \\
      \lvert v_k(x) \rvert &\le \frac{ML^{k-1}}{k!}\lvert x - x_0\rvert^{k},\quad(k = 1, 2, \dotsc).\\
      \\
      \therefore \sum_{k=1}^\infty \lvert v_k(x)\rvert
      &\le \sum_{k=1}^\infty \frac{ML^{k-1}}{k!}\lvert x - x_0\rvert^{k}\\
      &= \frac{M}{L}(\mathrm{e}^{L\lvert x - x_0\rvert} - 1).
      \end{aligned}
      $$

      これで $\sum v_k(x)$ が $D_0$ 上で一様に絶対収束することがわかった。
      * コメント：この議論がわからない場合は微分積分の教科書を参照すること。

    * 一様収束性により、極限の順序交換が成り立ち、関数列での連続性が保存される。
      $\displaystyle u(x) := \lim_{k\to\infty} u_k(x)$ とすると次が成り立つ：

      $$
      \begin{aligned}
      u(x) &= \lim_{k \to \infty}u_k(x) = u_0(x) + \sum_{j = 1}^\infty v_j(x)\\
      &= \lim_{k \to \infty}\left(y_0 + \int_{x_0}^x\!f(t, u_k(t))\,\mathrm dt\right)\\
      &= y_0 + \int_{x_0}^x\! \lim_{k \to \infty}f(t, u_k(t))\,\mathrm dt\\
      &= y_0 + \int_{x_0}^x\! f(t, u(t))\,\mathrm dt.
      \end{aligned}
      $$

      この第二項の不定積分は微分可能であるので、全体 $u(x)$ として微分可能である。
      この積分方程式は元の ODE における初期値問題の解そのものである。

次に連立一階系について述べる。

$$
\begin{alignedat}{}
y_1^\prime &= f_1(x, y_1, \dotsc, y_n), & y_1(x_0) &= y_{10},\\
&\dotsc, & &\dotsc,\\
y_n^\prime &= f_n(x, y_1, \dotsc, y_n), & y_n(x_0) &= y_{n0}.\\
\end{alignedat}
$$

* これらの組をベクトル化し、ノルムを導入する（最大値ノルムが良い）。

  $$
  \bm y^\prime = \bm f(x, \bm y), \quad \bm y(x_0) = \bm y_0.
  $$

  * 単独方程式問題はこの形に一般化できる。
  * Lipschitz 条件は次の形になる。ノルムで書けるというところが本質的だ。

    $$
    \lVert \bm f(x, \bm y_1) - \bm f(x, \bm y_2) \rVert \le L \lVert \bm y_1 - \bm y_2 \rVert.
    $$

* (E 7.2) $\bm y = A(x)\bm y + \bm b(x)$ においては、

  $$
  \exists M \forall x(
      x \in \varOmega \implies \lVert A(x) \rVert \le M)
  $$

  が成り立てば、$\bm y$ に無関係に Lipschitz 条件が満たされる。

  * $A(x)$ がある区間で $C^0$ 級かつ有界であれば、そこで ODE は解が一意的に存在する。

以上で§7.1 のノートを終わる。
