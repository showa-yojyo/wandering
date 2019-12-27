---
title: 体論学習ノート 5 体の拡大編
tags: math
---

Galois 論に入る前に体の基本的な性質を理解してゆくノート。今回は体の拡大を習う。

# 定義
## 体の拡大、拡大体 (field extension)

**定義**：$K$ を体とする。体 $F$ 上の**拡大体**とは体 $L$ であって $K \subset L$ をみたすものをいう。
つまり $K$ は $L$ の部分体である。

**表し方**：
* $L$ は $K$ 上の拡大体である。
* $L/K$ は体の拡大である。

## 拡大体の次数 (degree)

**定義**：拡大体 $L/K$ の**次数**とは、$L$ を $F$ 上のベクトル空間として見るときのその次元である。
これを記号 $[L:K]$ で表す。

## 有限体 (finite field) / 無限体 (infinite field)

**定義**：
* $L/K$ は**有限拡大体**である $\iff$ 次数 $[L:K]$ が有限の値である
* $L/K$ は**無限拡大体**である $\iff$ 次数 $[L:K]$ が有限の値でない

# 例

拡大体の基本的な例を示す。

* $\Complex$ は $\R$ 上の有限拡大体であり、次数は $2$ である。
* $\mathbb Q (\sqrt{2}) \coloneqq \{a + b\sqrt{2} \,|\, a, b \in \mathbb Q\}$
  は $\mathbb Q$ 上の次数 $2$ の有限拡大体である。

# 性質

## 拡大体の次数は乗法的

**定理**：$K, L, M$ を体とし、$K/L, L/M$ を有限拡大体とする。

このとき $K/N$ は有限拡大体であり、次数に関して次が成り立つ：

$$
[K:N]=[K:M][M:N].
$$

**検討**：線形代数。

**証明**：拡大体の定義から、$K/M$ は $M$ 上の拡大体であると言える。
$m \coloneqq [K:M]$, $n \coloneqq[M:N]$ とおく。
$\alpha \coloneqq \langle \alpha_1, \dotsc, \alpha_m\rangle$ と
$\beta \coloneqq \langle \beta_1, \dotsc, \beta_n\rangle$ とをそれぞれ
$K/M,M/N$ の基底とする。

このとき $K/N$ の基底が次で与えられることを示せば十分だ：

$$
\gamma \coloneqq \langle a_i b_j \,|\, i = 1, \dotsc, m,\;j = 1, \dotsc, n\rangle
$$

$K/M$ において任意の $c \in K$ は次のような線形結合の形に書ける：

$$
\exists c_i \in M\left(c = \sum_{i = 1}^m c_i a_i\right).
$$

ここで $b \coloneqq \displaystyle \sum_{i = 1}^n b_i \in M$ を定義する。
$\beta$ はベクトル空間の基底であるから $b$ がゼロになることはない。
さらに $d_i \coloneqq c_i/b \in M$ とおく。
これを用いて $c$ を書き換えると：

$$
\begin{aligned}
    c &= \sum_{i = 1}^m c_ia_i = \sum_{i = 1}^m \left(\frac{c_i}{b}\cdot b \cdot a_i\right)\\
    &= \sum_{i = 1}^m\left(d_i \sum_{j = 1}^n b_j a_i \right)\\
    &= \sum_{i = 1}^m \sum_{j = 1}^n b_j (a_i d_i).
\end{aligned}
$$

これにより $\gamma$ はベクトル空間 $K/N$ を張ることがわかる。
以下 $\gamma$ が線形独立であることを示す。今ある $c_{ij} \in N$ が存在して
次の等式を成り立たせるとする：

$$
0 = \sum_{i = 1}^m \sum_{j = 1}^n c_{ij}a_i b_j.
$$

体の性質から各項は可換である。これによりすべての $c_{ij}$ がゼロであることを示す：

$$
\begin{aligned}
&\phantom{\implies}0 = \sum_{i = 1}^m \sum_{j = 1}^n c_{ij}a_i b_j.\\
&\implies \forall i \left(0 = \sum_{j = 1}^n c_{ij} b_j\right) && \because \alpha\\
&\implies \forall i \forall j (c_{ij} = 0) && \because \beta
\end{aligned}
$$

したがってベクトル空間 $K$ を張る集合 $\gamma$ が基底であることが示された。
ゆえに：

$$
[K:N] = \dim \gamma = mn = [K:M][M:N].
$$

これが示そうとしたものである。
$\blacksquare$

# 参考資料

* Proof Wiki
  * [Definition:Field Extension - ProofWiki](https://proofwiki.org/wiki/Definition:Field_Extension)
  * [Degree of Field Extensions is Multiplicative](https://proofwiki.org/wiki/Degree_of_Field_Extensions_is_Multiplicative)

