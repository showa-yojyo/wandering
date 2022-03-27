---
title: 体論学習ノート 5 体の拡大編
mathjax: true
tags: math
---

Galois 論に入る前に体の基本的な性質を理解してゆくノート。今回は体の拡大を習う。

## 定義

### 体の拡大、拡大体 (field extension)

**定義**：$K$ を体とする。体 $F$ 上の**拡大体**とは体 $L$ であって $K \subset L$ をみたすものをいう。
つまり $K$ は $L$ の部分体である。

**表し方**：

* $L$ は $K$ 上の拡大体である。
* $L/K$ は体の拡大である。

### 拡大体の次数 (degree)

**定義**：拡大体 $L/K$ の**次数**とは、$L$ を $F$ 上のベクトル空間として見るときのその次元である。
これを記号 $[L:K]$ で表す。

### 有限体 (finite field) / 無限体 (infinite field)

**定義**：

* $L/K$ は**有限拡大体**である $\iff$ 次数 $[L:K]$ が有限の値である
* $L/K$ は**無限拡大体**である $\iff$ 次数 $[L:K]$ が有限の値でない

### 代数的 (algebraic) / 超越的 (transcedent)

**定義**：$K/L$ を拡大体とする。$\alpha \in K/L$ とする。

* $\alpha$ が $L$ 上**代数的**であるとは、$L$ 上のゼロでないある多項式 $f(X)$ が存在してその根であることをいう：

  $$
  \exists f(X) \in L[X]\!\setminus\!\{0\}\:(f(\alpha) = 0).
  $$

* $K/L$ が**代数的拡大体**であるとは、$K$ のすべての要素が $L$ 上代数的であることをいう。
* $\alpha$ が $L$ 上**超越的である**とは、$\alpha$ が $L$ 上代数的ではないことをいう。
* $K/L$ が**超越的拡大体**であるとは、$K/L$ が代数的拡大体でないことをいう。

### 生成された拡大体 (generated field extension)

**定義**：$K/L$ を拡大体とし、$S \subset K$ とする。

$S$ により**生成された拡大体** $L[S]$ は $S$ を含むような $K$ の拡大体のうち最小のものである。
つまり $L[S]$ は $K$ の $S$ と $L$ を含むような部分体すべての交差である。

$S$ が $L[S]$ の**生成集合**であるとは、$L[S]$ が $S$ を含むような真の部分体を含まないことをいう。

### 単拡大 (simple field extension)

**定義**：$K/L$ を拡大体とする。$K$ が $L$ の**単拡大**であるとは、
ある $\alpha \in K$ が存在して $L[\alpha] = K$ が成り立つことをいう。
つまり、単一要素の集合による生成された拡大体であることをいう。

## 例

### 拡大体

拡大体の基本的な例を挙げる。

* $\Complex$ は $\R$ 上の有限拡大体であり、次数は $2$ である。
* $\mathbb Q (\sqrt{2}) \coloneqq \{a + b\sqrt{2} \,|\, a, b \in \mathbb Q\}$
  は $\mathbb Q$ 上の次数 $2$ の有限拡大体である。

### 代数的数

代数的数の基本的な例を挙げる。

* $\sqrt{2} \in \R/\mathbb{Q}$ は $X^2 - 2 \in \mathbb{Q}[X]$ の根であるから代数的数である。
* 虚数単位 $i \in \Complex/\mathbb{Q}$ は $X^2 + 1 \in \mathbb{Q}[X]$ の根であるから代数的数である。

## 性質

### 拡大体の次数は乗法的

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

### 有限生成された代数的拡大体は有限

**定理**：$L/K$ を拡大体とし、$\alpha_1, \dotsc, \alpha_n \in L$ は $K$ 上代数的であるとする。

このとき $K(\alpha_1, \dotsc, \alpha_n)/K$ は有限拡大体である。

**検討**：

* $n$ に関する数学的帰納法による。
* 直前の定理を利用するために、拡大をバラす。

**証明**：$S \coloneqq \lbrace \alpha_1, \dotsc, \alpha_n \rbrace$ とおく。

$K(S)/K$ が有限拡大体であることを $n$ についての数学的帰納法により示す。

$n = 0$ のとき、$K$ を $K$ 自身の上の拡大体であるとみなすことで成り立つ。

今、$T \subset K$ は $n - 1$ 個の $K$ 上代数的な元からなる部分集合であると仮定する。
$K(T)/K$ は有限生成拡大体である。

$$
K(S) = K(\alpha_1, \dotsc, \alpha_{n - 1})(\alpha_n)
$$

である。

帰納法の仮定により $K(\alpha_1, \dotsc, \alpha_{n - 1})/K$ は有限である。

単純代数的拡大体の性質（未）により $K(S)/K(\alpha_1, \dotsc, \alpha_{n - 1})$ は有限である。

したがって、前述定理の体の拡大が乗法的であることから $K(S)/K$ は有限である。

以上により、任意の $n$ について $K(\alpha_1, \dotsc, \alpha_n)/K$ は有限である。
$\blacksquare$

## 参考資料

* Proof Wiki
  * [Definition:Field Extension - ProofWiki](https://proofwiki.org/wiki/Definition:Field_Extension)
  * [Definition:Algebraic Field Extension](https://proofwiki.org/wiki/Definition:Algebraic_Field_Extension)
  * [Definition:Simple Field Extension](https://proofwiki.org/wiki/Definition:Simple_Field_Extension)
  * [Degree of Field Extensions is Multiplicative](https://proofwiki.org/wiki/Degree_of_Field_Extensions_is_Multiplicative)
