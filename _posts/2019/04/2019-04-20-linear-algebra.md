----
title: 『初歩から学べる線形代数』ノート
tags: math
----

佐藤恒雄、野澤宗平著『初歩から学べる線形代数』より。

----

第 8 章発展問題を解く。

* 広義固有空間の定義では、固有値 $\lambda$ の多重度を $n$ とすると $(A - \lambda I)^n$ の核空間であるというものだが、
  この $n$ を最小多項式における根 $\lambda$ の多重度にまで下げられる。というのがわからなかった。
  たぶん Jordan 標準形を求めるときの変形行列の計算過程に関係があると思う。
* Jordan 分解可能定理。Jordan 行列が対角行列と冪零行列の「直和」の形になっていることに気づけば OK だった。
* 最終問題。次の行列を Jordan 分解する：

  $$
  A =
  \begin{pmatrix}
  1 & 0 & -1 \\
  2 & 1 & 0 \\
  1 & 0 & 3
  \end{pmatrix}
  $$

  * この問題では変換行列 $P$ が必要になるので、方程式法で解く。固有方程式を求めて根を求める。

    $$
    \varphi_A(x) =
    \begin{vmatrix}
    1 - x &     0 & -1 \\
    2     & 1 - x & 0 \\
    1     &     0 & 3 - x
    \end{vmatrix}
    = (x - 1) (x - 2)^2.
    $$

    固有値は $1, 2$ である。後者は多重度 2 だ。
  * したがって Jordan 標準形は例えば次の形になる：

    $$
    J =
    \begin{pmatrix}
    1 & 0 & 0\\
    0 & 2 & 1\\
    0 & 0 & 2
    \end{pmatrix}
    $$

  * $(A - I)\bm{p}_1 = \bm{o}$ を解いておく（基底ベクトルから勝手に一つ決める）：

    $$
    A - I \longrightarrow
    \begin{pmatrix}
    1 & 0 & 2\\
    0 & 0 & 4\\
    0 & 0 & 1
    \end{pmatrix},
    \quad
    \bm{p}_1 =
    \begin{pmatrix}
    0\\
    1\\
    0
    \end{pmatrix}
    $$

  * $(A - 2I)\bm{p}_2 = \bm{o}$ を解いておく：

    $$
    A - 2I \longrightarrow
    \begin{pmatrix}
    1 & 0 & 1\\
    0 & 1 & 2\\
    0 & 0 & 0
    \end{pmatrix},
    \quad
    \bm{p}_2 =
    \begin{pmatrix}
    -1\\
    -2\\
    1
    \end{pmatrix}
    $$

  * なので $AP = PJ = \begin{pmatrix}\bm{p}_1& 2 \bm{p}_2& \bm{p}_2 + 2 \bm{p}_3\end{pmatrix}.$
    残るのは $(A - 2I)\bm{p}_3 = \bm{p}_2$ を解くこと。
  * $(A - 2I \quad \bm{p}_3)$ を変形する：

    $$
    (A - 2I \quad \bm{p}_3) \longrightarrow
    \begin{pmatrix}
    1 & 0 & 1 & 1\\
    0 & 1 & 3 & 4\\
    0 & 0 & 0 & 0
    \end{pmatrix}
    \quad
    \bm{p}_3 =
    \begin{pmatrix}
    1\\
    4\\
    0
    \end{pmatrix}
    $$

  * $P = \begin{pmatrix}\bm{p}_1 & \bm{p}_2 & \bm{p}_3\end{pmatrix}$ が得られた。
  * まだ計算が続く。ここから逆行列 $P^{-1}$ を求める（変形手順省略）。

    $$
    P^{-1} =
    \begin{pmatrix}
    -4 & 1 & -2\\
     0 & 0 &  1\\
     1 & 0 &  1
    \end{pmatrix}
    $$

  * Jordan 分解に話を戻す。$A = S + N$ とし、$S$ を対角行列、$N$ を冪零行列とする。

    $$
    S = P \begin{pmatrix}
    1 & 0 & 0 \\
    0 & 2 & 0 \\
    0 & 0 & 2
    \end{pmatrix}
    P^{-1},
    \quad
    N = A - S
    $$

    を計算して、解答例の値を得る。
