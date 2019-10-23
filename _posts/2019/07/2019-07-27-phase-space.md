---
title: 『常微分方程式』学習ノート Part 10
tags: math
---

高崎金久著『常微分方程式』（日本評論社）ノートその十。

# 第 7 章 （続き）

## §7.2 2 次元相空間上の定性的解析

* 自由度が 3 以上の連立一階自励系は多様であり過ぎて一般論がない。
* 直線上の自励系は単純。相空間を $f(x)$ の符号で分類して（区間族に分割）時刻の極限を見ればいい。
* 2 次元相空間（自由度 1）上の自励系からして状況は複雑。しかも 3 次元以上のものと比べても異質。
  * $\dfrac{\mathrm{d}x}{\mathrm{d}t} = f(x, y),\quad \dfrac{\mathrm{d}y}{\mathrm{d}t} = g(x, y)$ として、符号の組み合わせで平面を 4 分割できる。
  * その領域の境界 $f(x, y) = 0$ と $g(x, y) = 0$ は isocline であって、交点が不動点であることはすでにやった。
    ただし、これしか情報がないのであれば、ほとんど何もわからない。
* 本節では 2 次元相空間における連立一階自励系を考える。「右辺」は初期値問題の解の存在性と一意性（例えば Lipschitz 連続性がある）が成り立つと仮定する。

### 線形化

* **線形化**とは、連立一階系に対して、右辺の関数の不動点 $(c_1, c_2)$ について
  Taylor 展開したものを、一次の項までで打ち切ったもので置き換えた連立一階系のことをいう：

  $$
  \frac{\mathrm{d}x_i}{\mathrm{d}t} = f_i(x_1, x_2),\quad i = 1, 2.
  \\
  \longrightarrow
  \\
  f_i(x_1, x_2) = a_{i1}(x_1 - c_1) + a_{i2}(x_2 - c_2) + o(\sqrt{(x_1 - c_1)^2 + (x_2 - c_2)^2}),\\
  a_{ij} = \left.\frac{\partial f_i}{\partial x_j}(x_1, x_2)\right\rvert_{(c_1, c_2)}
  \\
  \longrightarrow
  \\
  \frac{\mathrm{d}x_i}{\mathrm{d}t} = a_{i1}(x_1 - c_1) + a_{i2}(x_2 - c_2),\quad i = 1, 2.
  $$

  * 変数変換 $X_i = x_i - c_i, \quad(i = 1, 2)$ を施すと、線形連立一階系に変形する：

    $$
    \frac{\mathrm{d}X_i}{\mathrm{d}t} = \sum_{j = 1}^2 a_{ij}X_j,\quad i = 1, 2.
    $$

  * 線形化は不動点の近傍における一次近似を与えていると解釈する。

----
(E 7.3) $a_1 > 0,\,a_2 > 0,\,K_1 > 0,\,K_2 > 0,\,L > 0,\,M > 0,LM \ne 1$
として次の自励系を考える：

$$
\frac{\mathrm{d}x}{\mathrm{d}t} = a_1x \left(1 - \frac{x + Ly}{K_1}\right),\quad
\frac{\mathrm{d}y}{\mathrm{d}t} = a_2y \left(1 - \frac{Mx + y}{K_2}\right),\\
$$

まず次の 4 直線が isocline であることがただちにわかる：

$$
\begin{aligned}
x &= 0,\\
y &= 0,\\
1 - \dfrac{x + Ly}{K_1} &= 0,\\
1 - \dfrac{Mx + y}{K_2} &= 0
\end{aligned}
$$

これを利用すると $a_{ij}$ の計算が楽になる：

$$
\begin{aligned}
\frac{\partial f}{\partial x} &= a_1 \cdot 0 + a_1 x \left(-\frac{1}{K_1}\right) = -\frac{a_1}{K_1}x.\\
\frac{\partial f}{\partial y} &= -\frac{L}{K_1}a_1 x = -\frac{a_1 L}{K_1}x.\\
\frac{\partial g}{\partial x} &= -\frac{Mx}{K_2} \cdot a_2 y = -\frac{a_2 M}{K_2}y.\\
\frac{\partial g}{\partial y} &= a_2 \cdot 0 + a_2 y \left(-\frac{1}{K_2}\right) = -\frac{a_2}{K_2}y.
\end{aligned}
$$

不動点を $(x_*, y_*)$ とすると、線形化は：

$$
\begin{aligned}
f(x, y) &\approx f_x(x_*, y_*)(x - x_*) + f_y(x_*, y_*)(y - y_*)\\
&= -\frac{a_1}{K_1}x_*(x - x_*) -\frac{a_1 L}{K_1}x_*(y - y_*),\\
g(x, y) &\approx g_x(x_*, y_*)(x - x_*) + g_y(x_*, y_*)(y - y_*)\\
&= -\frac{a_2 M}{K_2}y_*(x - x_*) + -\frac{a_2}{K_2}y_*(y - y_*).
\end{aligned}
$$

### 不動点の分類

ベクトル場を導入して連立一階系を次の形に書き換える：

$$
\frac{\mathrm{d}\bm X}{\mathrm{d}t} = A\bm X,\quad
\bm X = \begin{pmatrix}
    X_1\\
    X_2
\end{pmatrix},
\quad
A = \begin{pmatrix}
    a_{11} & a_{12}\\
    a_{21} & a_{22}
\end{pmatrix}.
$$

係数行列 $A$ の固有方程式を判別式 $\Delta \coloneqq p^2 - 4q$ の符号で分類することを考える。

$$
\varPhi(A) = \det(\lambda I - A) = \lambda^2 - p\lambda + q = 0,\\
p \coloneqq \operatorname{tr}A,\,q \coloneqq \det A.
$$

この根を $\alpha_1, \alpha_2$ とおく。

* $\Delta > 0$ の場合（実根）：
  * $A = P \operatorname{diag}(\alpha_1, \alpha_2) P ^{-1}$ とおく。
  * $\bm X = S \bm Y$ なる基本行列 $S$ が存在する：

    $$
    \begin{aligned}
    \frac{\mathrm{d}\bm Y}{\mathrm{d}t} &= \operatorname{diag}(\alpha_1, \alpha_2)\bm Y.\\
    \therefore \frac{\mathrm{d} Y_i}{\mathrm{d}t} &= \alpha_i Y_i,
    \quad i = 1, 2.
    \end{aligned}
    $$

  * $q \ne 0$ を仮定すると、$\alpha_i \ne 0.$ これならば $\lvert Y_i \rvert$ の大きさの変化が指数関数的であるとわかる。
    まとめると：

    1. $\alpha_1 > 0 \land \alpha_2 > 0 \implies \lvert Y_i \rvert \to \infty.$
    2. $\alpha_1 < 0 \land \alpha_2 < 0 \implies \lvert Y_i \rvert \to 0.$
    3. $\alpha_1 \alpha_2 < 0 \implies \lvert Y_i \rvert \to \infty \land \lvert Y_j \rvert \to 0 \quad (i \ne j).$

  * 固有値の符号が一致する ($q > 0$) 不動点（上の 1. と 2.）を**結節点**という。
    * 発散するもの (1.) を**不安定**結節点といい、
    * 収束するもの (2.) を**安定**結節点という。
  * 固有値の符号が異なる ($q < 0$) 不動点を**鞍部点**という。

* $\Delta = 0$ の場合（重根）：

  * $A$ が単位行列のスカラー倍であるタイプと、Jordan ブロック型の場合が相当する。
  * さきほどと同じように考えて：

    1. $p > 0 \implies \lvert \bm X \rvert \to \infty:$ 不安定結節点
    2. $p < 0 \implies \lvert \bm X \rvert \to 0:$ 安定結節点

* $\Delta < 0$ の場合（虚根）：

  $$
  \alpha = \frac{p}{2} \pm \omega i,\quad
  \omega = \frac{\sqrt{4q - p^2}}{2}.
  $$

  今度は根が複素数になるので、座標変換は考えられない。

  $$
  \begin{aligned}
  \bm X &= P\operatorname{diag}(\mathrm{e}^{\alpha_1}t, \mathrm{e}^{\alpha_2}t)P ^{-1} \bm c,
  \quad P \coloneqq \begin{pmatrix}\bm p_1 & \bm p_2\end{pmatrix}, \;\bm c \text{ is constant}\\
  &= C_1 \mathrm{e}^{\alpha_1 t} + C_2 \mathrm{e}^{\alpha_2 t}.\\
  \end{aligned}
  $$

  ここで定数 $C_1, C_2$ は $P ^{-1}\bm c$ の成分である。
  さらに変形して：

  $$
  \begin{aligned}
  \bm X &= C_1 \bm q_1 \mathrm{e}^{\frac{pt}{2}}\cos\omega t
        + C_2 \bm q_2 \mathrm{e}^{\frac{pt}{2}}\sin\omega t,\\
  \bm q_1 &\coloneqq \bm p_1 + \bm p_2,\,\\
  \bm q_2 &\coloneqq i(\bm p_1 - \bm p _2).
  \end{aligned}
  $$

  ここで定数 $C_1, C_2$ は上のものとは異なる。
  こう書かれると $p$ の符号で $\lvert \bm X \rvert$ の評価を分類できることがわかる。
  指数関数的に変化し、円運動みたいなものも混ざっている。

  1. $p > 0$ ならば、不動点（原点）の周りを周りながら無限の彼方へ発散する。
  2. $p < 0$ ならば、不動点の周りを周りながら原点に収束する。
  3. $p = 0$ はあてにならない。

  * $p \ne 0$ の不動点を**渦状点**といい、発散するものは不安定、収束するものは安定であるという。
  * $p = 0$ の不動点を**渦心点**という。

----

(E 7.4): (E 7.3) における不動点の分類。
係数行列の固有方程式の判別式を計算して符号で分類する。
結局 $q$ の符号は $1 - LM$ のそれで決まる。
$q > 0$ ならば安定結節点、$q < 0$ ならば鞍部点である。

コメント：図 7.4 をよく見ておくこと。
安定結節点はブラックホールみたいにベクトルを吸い込む点であり、
鞍部点は、そこを通過しない限りベクトルを反らす点である。

### 解軌道の安定性

不動点とは縮退した解軌道とみなせる。逆に考えて、不動点の分類を解軌道に一般化して定義する。

* 軌道 $C$ が**安定である**とは、$C$ 上の点 $P$ の近傍にある任意の点 $Q$ から出発する解
  $Q(t)$ が、$C$ の近くに「留まる」ものをいう：

  $$
  \forall \varepsilon(\varepsilon > 0 \implies
    \exists \delta(\delta > 0 \implies
      \forall Q(
          d(P, Q) < \delta \implies \forall t(
              t \ge 0 \implies d(Q(t), C) < \varepsilon
          )
      ))).
  $$

* 上の文で「留まる」を「$C$ に限りなく近づく」に置き換えた軌道は**漸近安定である**という。
* 安定結節点および安定渦状点は漸近安定である。
* 渦心点は安定軌道（が一点につぶれたもの）である。
* 解軌道の安定性は、初期条件の微小な変化を微小にしか受けないことを意味する。
* 二次元相空間では漸近安定な閉軌道が存在し得る。これを**極限閉軌道**という。
  * コメント：周囲のベクトルを吸い込むイメージ。
* E.g. van del Pol 方程式

----

(E7.5) 余裕があったらプロットする。

$$
\begin{aligned}
\frac{\mathrm{d}x}{\mathrm{d}t} &= y + x(c - a(x^2 + y^2)),\\
\frac{\mathrm{d}y}{\mathrm{d}t} &= -x + y(c - a(x^2 + y^2)),\quad a > 0, c > 0.
\end{aligned}
$$

極座標で考える。

$$
\frac{\mathrm{d}r}{\mathrm{d}t} = r(c - ar^2),\quad \frac{\mathrm{d}\theta}{\mathrm{d}t} = -1.
$$

* 符号を調べる：
  * $0 < r < \sqrt{c/a}$ で発散、
  * $\sqrt{c/a} < r$ で収束。
* ここでは円 $c - a(x^2 + y^2) = 0$ が極限閉軌道である。

### Poincaré 指数 a.k.a. 回転数

ベクトル場 $\bm F = (f(x, y), g(x, y))$ の観点から考える。
* $\bm X$ の零点はすべて孤立しているものとする。
  * コメント：孤立零点というのはつむじのようなもの。
  * ベクトル場の零点は対応する自励系の不動点と対応する。
* $F$ の零点を含まないような、向きづけられた閉曲線 $C$ があるとする。

この条件で、$C$ の各点で角度

$$
\tau \coloneqq \arctan\frac{g(x, y)}{f(x, y)}
$$

を考え、その総変量を考える。

* $I_C$ を $\tau$ の総変量を $2\pi$ で割った値で定義する。
  * この値を **Poincaré 指数**という。
  * これはベクトル $\bm F$ が原点の周りを何回転するかを表す。
  * $I_C \in \Z.$

* (Th 7.3)

  $I_C$ は次の式で得られる：

  $$
  I_C = \frac{1}{2\pi}\int_C\!
    \frac{f(x, y)\,\mathrm dg(x, y) - g(x, y)\,\mathrm df(x, y)}{f(x, y)^2 + g(x, y)^2}.
  $$

  * 証明：$C$ 上、被積分関数の分母はゼロにならないと仮定されている。
    $\tau$ の定義により：

    $$
    I_C = \frac{1}{2\pi}\int_C\!\mathrm d\tau
    $$

    であるが、全微分 $\mathrm d\tau$ はまさに被積分関数そのものである。

* $C$ が零点を通らない限り $\bm F$ や $C$ を連続的に変化しても $I_C$ は不変である。
  * コメント：位相幾何的な考え方をしている。
* ベクトル場 $\bm F$ の孤立零点 $P$ における Poincaré 指数 $I_P$ を次のように定義する：

  $$
  I_P \coloneqq I_C
  $$

  ここで $I_C$ は次の条件を満たす任意の閉曲線 $C$ の Poincaré 指数である：
  * 閉曲線 $C$ の内側に孤立零点 $P$ があり、$P$ 以外の零点がない。

* (E 7.7) 本編の各図からベクトルの変位を観察することで納得できる。
* (Th 7.4) $I_C$ の簡単な導出法

  $$
  I_C = \frac{n_+ - n_-}{2}.
  $$

  ここで $n_{\pm}$ は $C$ 上を一周する間に $\tan\tau$ が連続的に
  $\mp$ から $\pm$ に変わる（複号同順）回数を表すものとする。

  * 証明：$n_+ - n_-$ が総回転数の倍であることを示す。

* (E 7.8) $\bm F = (y, -x)$ における原点の Poincaré 指数は

  $$
  I_{(0, 0)} = 2 - 0 = 1.
  $$

  * コメント：円を描いて、どこで符号の入れ替えが起こるかを考えろ。

* (Th 7.5) 閉曲線の指数と零点の指数の関係
  * $C$ を閉曲線で、ベクトル場の零点を通過しないものとする。
  * 点 $P_i$ をベクトル場の孤立零点であって、$C$ から見て内側にあるもの全部とする。

  このとき次の等式が成り立つ：

  $$
  I_C = \sum_{i}I_{P_i}.
  $$

  証明：
  * 閉曲線 $C_i$ を、点 $P_i$ を内側に囲み、それ以外の $P_j$ を通過もしないし囲みもしないものとする。
  * 領域 $\varOmega$ を、$C$ の囲む領域から $C_i$ の囲む領域を除外したものとする。

  領域 $\varOmega$ の境界において $\mathrm d\tau$ を積分すると Stokes の定理により：

  $$
  \begin{aligned}
  \int_{\partial\varOmega}\!\mathrm d\tau
  &= \int_\varOmega\!\mathrm d(\mathrm d\tau)\\
  &= 0 \quad(\because \mathrm d \circ \mathrm d = 0).
  \end{aligned}
  $$

  一方左辺は：

  $$
  \int_{\partial\varOmega}\!\mathrm d\tau
  = \int_C\!\mathrm d\tau - \sum_i \int_{C_i}\!\mathrm d\tau.\\
  \therefore \int_C\!\mathrm d\tau = \sum_i \int_{C_i}\!\mathrm d\tau.\\
  $$

  あとはこの等式の両辺を $\dfrac{1}{2\pi}$ 倍すれば、主張の結論を得る。

* Poincaré 指数の応用例として、閉軌道の内側には不動点が必ず存在することなど、色々なことが言える。

----
第 7 章ノートは以上。これまでの仕上げとして演習問題をやりたい。
