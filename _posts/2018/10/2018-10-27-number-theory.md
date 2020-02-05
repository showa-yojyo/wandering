---
title: 『はじめての数論 原著第 3 版』学習ノート Part 6
tags: math
---

鈴木治郎訳『はじめての数論 原著第 3 版』より。

* Euler 関数が乗法的であることを証明するのに中国剰余定理を利用していることに注意。
* 20-32 章（原始根、平方剰余の相互法則、平方数の和、Pell 方程式、Diophantus 近似）を復習しよう。

## 練習問題 20.1. Liouville の lambda 関数

```python
def liouville_lambda(n):
    if n == 1:
        return 1
    return pow(-1, sum(ntheory.factorint(n).values()))
```

* (a) たとえば $60750 = 2^1 \cdot 3^5 \cdot 5^3$ だから $\lambda(60750) = (-1)^{1 + 5 + 3} = -1.$
* (b) $G(n) = \displaystyle \sum_{d_i \mid n}\lambda(d_i)$ に対して次のようになる：

  | $n$  | $G(n)$ |
  |-----:|-------:|
  |  1   |      1 |
  |  2   |      0 |
  |  3   |      0 |
  |  4   |      1 |
  |  5   |      0 |
  |  6   |      0 |
  |  7   |      0 |
  |  8   |      0 |
  |  9   |      1 |
  | 10   |      0 |
  | 11   |      0 |
  | 12   |      0 |
  | 13   |      0 |
  | 14   |      0 |
  | 15   |      0 |
  | 16   |      1 |
  | 17   |      0 |
  | 18   |      0 |

* (c) $n$ が平方数ならば $G(n) = 1$ で、そうでなければ $G(n) = 0$ であるように予想できる。それゆえ：

  $$
  \begin{aligned}
  G(62141689) &= 1\\
  G(60119483) &= 0
  \end{aligned}
  $$

* (d) (c) の予想を証明する。
  * $n$ が平方数であれば $G(n) = 1$ が成り立つことは直接計算で示せる。
  * $G(n) = 1$ であれば、$\lambda(n)$ の個数は奇数であること、
    言い換えると数 $n$ の約数の個数が奇数である。これは $n$ が平方数であることを意味する。

## 練習問題 20.2 乗法的関数

* (a) $\lambda(n)$ は乗法的関数である。

  今、数 $m, n$ を $\gcd(m, n) = 1$ であるようにとり、
  それぞれの素因数分解を次のように置く：

  $$
  \begin{aligned}
  m &= p_1^{e_1} \dots p_r^{e_r},\\
  n &= q_1^{f_1} \dots q_s^{f_s}
  \end{aligned}
  $$

  あとは $p_i \neq q_j$ を用いて直接計算で示せる。

* (b) 仮定をまとめる：

  * $f(n)$: 乗法的関数
  * $d_1, \dotsc, d_r$: 数 $n$ の約数
  * $g(n) = \displaystyle \sum_{i = 1}^r f(d_i)$

  数 $m, n$ を
  * $\gcd(m, n) = 1$
  * $m$ の約数を $d_1 = 1, \dotsc, d_r = m$
  * $n$ の約数を $e_1 = 1, \dotsc, e_s = n$

  のようにとる。このとき積 $mn$ の約数は $\lbrace d_i e_j\rbrace$ である。

  $$
  \begin{aligned}
  g(mn)
  &= \sum_{i, j}^{r, s} f(d_i e_j)\\
  &= \sum_{i, j}^{r, s} f(d_i) f(e_j)\\
  &= \sum_i^r f(d_i) \sum_j^s f(e_j)\\
  &= g(m)g(n)
  \end{aligned}
  $$
