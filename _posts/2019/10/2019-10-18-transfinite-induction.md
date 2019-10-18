---
title: 超限帰納法証明ノート
tags: math
---

超限帰納法の証明ノート。Wikipedia の証明を持ってくる。

# 超限帰納法

[元ネタ](https://ja.wikipedia.org/wiki/%E6%95%B0%E5%AD%A6%E7%9A%84%E5%B8%B0%E7%B4%8D%E6%B3%95#%E8%B6%85%E9%99%90%E5%B8%B0%E7%B4%8D%E6%B3%95)

## 主張

$(A, \le)$ を整列集合とし、$P(x)$ を $A$ 上で定義された命題関数とする。
もし次の条件が成立するならば、任意の $x \in A$ について $P(x)$ は真である。

条件：
$a$ を $A$ の任意の元とする。
$x < a$ を満たす $A$ の全ての元 $x$ について $P(x)$ が真ならば、$P(a)$ も真である。

$$
\tag*{$\bigstar$}
\forall a(\forall x(x < a \implies P(x))) \implies P(a)
$$

ただし、$\lt$ は

$$
a < b \iff (a \le b \land a \ne b)
$$

と読み替えるものとする。

## 証明

$\bigstar$ の $\forall a(\dots)$ 部分の括弧内の文を $Q(a)$ とおく：

$$
Q(a) := \forall x(x < a \implies P(x)).
$$

主張はこう書き換えられる：

$$
\forall a Q(a) \implies P(a).
$$

### (i) 整列集合の最小元について成り立つことを証明する

$A$ は整列集合であるから、その全順序について最小元 $a_0$ がある。
これについて $Q(a_0)$ の真偽を考える。示したいことは：

$$
\tag*{$\bigstar\bigstar$}
Q(a_0) \implies P(a_0).
$$

最小元の性質により $x < a_0$ を満たす $A$ の元は存在しない。
それゆえ直ちに命題 $Q(a_0)$ は真である。従って、$\bigstar\bigstar$ が真であるには
$P(a_0)$ も真である必要がある。

コメント： $Q(a_0)$ を真であるとする vaculous truth の考え方に注意。

### (ii) 最小元でない元について背理法で証明する

条件 $Q(\cdot)$ を満たしても $P(\cdot)$ が偽となる元 $y \in A$ が存在すると仮定する：

$$
\exists y(Q(y) \implies \lnot P(y)).
$$

そのような元全ての集合を $A_f$ とする：

$$
A_f := \lbrace y \in A \,\mid\, Q(y) \implies \lnot P(y)\rbrace.
$$

$A_f \subset A$ も整列集合の性質から最小元を持つ。これを $a$ とする。当然 $P(a)$ は $a \in A_f$ だから偽である。

条件 $Q(\cdot)$ を満たしている限り $A$ の最小元 $a_0$ について $P(a_0)$ は真であるから
$a_0 \notin A_f$ であり $a \ne a_0.$
従って、

$$
A_a := \{x \,\mid\, x < a\}
$$

と置けば、$A_a$ は空ではない (少なくとも $a_0 < a$ だから $a_0 \in A_a$ だ)。

$a$ は $P(\cdot)$ が偽となる $A$ の最小元であるから、
$x \in A_a$ であれば、$P(x)$ は真である。
従って、定理の条件 $\bigstar$ により $P(a)$ は真とならねばならないが、これは前言と矛盾する。

ゆえに $A_f = \varnothing$ であり、超限帰納法の主張は正しい。
