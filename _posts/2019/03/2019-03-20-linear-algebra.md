---
title: 『ベクトル空間』ノート
tags: math
---

竹山美宏著『ベクトル空間』より。

# ベクトル空間の直和空間

以下 $V$ を（有限次元）ベクトル空間とし、$W_1, \dotsc, W_r$ をその部分空間とする。

* $W_1 + \dotsb + W_r$ もまた $V$ の部分空間となる。
  * 群論にも似た考えがある。
* $\dim{(W_1 + W_2)} = \dim{W_1} + \dim{W_2} - \dim{(W_1 \cap W_2)}.$
  * $W_1 \cap W_2 = \lbrace 0\rbrace$ ならばこの等式は「きれい」になる。
  * $\dim{(\sum W_i)} \lt \sum \dim W_i.$
* 直和空間の意味
  * $W_1 \oplus \dotsb \oplus W_r = V$ とは「零ベクトルが零ベクトルの和としてしか表せない」ことを意味する。
* 覚えやすい性質
  * $W_1 \oplus \dotsb \oplus W_r = V \iff (W_1 + W_2) \cap W_3 = \lbrace 0\rbrace, \dotsc, (W_1 + \dotsb + W_{r-1}) \cap W_r = \lbrace0\rbrace.$
  * $W_1 \oplus W_2 = V \iff W_1 \cap W_2 = \lbrace 0\rbrace.$
  * $W_1 \oplus \dotsb \oplus W_r = V \iff \dim(\bigoplus W_i) = \sum(\bigoplus W_i).$
    * 先ほど書いた「きれいな」等式になる。
* 直和の基底について
  * $W_i$ の基底が $S_i$ であるとすると。この和集合は直和空間の基底になる。ただし $S_i \cap S_j = \varnothing (i \ne j)$ とする。
* 補空間の存在性
  * $W$ が $V$ の部分空間であるとすると、常に $W \oplus W' = V$ を満たす部分空間 $W'$ が存在する。
  * 一意的に定まるとは言っていない。
* 言い忘れたが $W_1 \oplus \dotsb \oplus W_r = V$ のとき各 $W_i$ を**直和因子**という。
* 直和空間のベクトル $v \in V$ は $v = \sum w_i\ (w_i \in W_i)$ の形に一意的に表せる。
* 射影 $p_i: V \longrightarrow W_i$ について
  * 線形写像であり、全射である。
  * 射影は直和因子のとり方（**直和分解**）による。
* ベクトル空間上の線形変換の相異なる固有値に対応する固有空間の和は直和空間である。
* 線形変換の固有値 $\lambda_i$ の多重度を $m_i$ とおくと、この線形変換が対角化できる条件は次と同値である：
  * $V = \bigoplus W_i,$
  * $\dim W_i = m_i,$
  * 表現行列 $A$ は適切な基底をとると次のような対角行列になる：

    $$
    P^{-1}AP = \operatorname{diag}(
        \underbrace{\lambda_1, \dotsc, \lambda_1}_{m_1},
        \dotsc,
        \underbrace{\lambda_r, \dotsc, \lambda_r}_{m_r}).
    $$
