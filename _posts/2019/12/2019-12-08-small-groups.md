---
title: 小さい有限群を分類する学習ノート
tags: math
---

位数が 10 以下の有限群を分類する。

以下、位数 $n$ の巡回群を $Z_n$ で表し、同型 $\Z/n\Z \simeq Z_n$ を断りなく利用する。

# 分類するために利用する定理

## 有限 Abel 群の基本定理

TODO: この定理だけは別のページで取り扱う。

**定理**：自明でない有限 Abel 群はいくつかの素数べきの巡回群の直積と同型である。

特に、素数 $p_1, \dotsc, p_r$ と正の整数 $e_1, \dotsc, e_r$ とが存在して次の同型が成り立つ：

$$
G \simeq (\Z/p_1{}^{e_1}\Z) \times \dotsb \times (\Z/p_r{}^{e_r}\Z).
$$

**証明**：別のページで取り扱う。

## 定理：$p$ 群は巡回群

**定理**：位数が素数である群は巡回群に同型である。

**証明**：$G$ を位数が素数 $p$ である群とする。
今、任意に非単位元 $a \in G$ をとると $a$ が生成する $G$ の部分群
$\langle a \rangle$ の位数は Lagrange の定理により $\lvert G \rvert = p$ を割り切る必要がある。
$a \ne 1_G$ より $\lvert\langle a \rangle\rvert = p.$

$p = \lvert\langle a \rangle\rvert = \lvert G \rvert$ かつ $\langle a \rangle \subset G$ から
$\langle a \rangle = G.$
したがって $G$ 自身が $a$ が生成する巡回群である。
$\blacksquare$

## 定理：$p^2$ 群の二つの同型

**定理**：$G$ を位数が素数 $p$ の平方である群とする：$\lvert G \rvert = p^2.$
このとき $G$ は Abel 群であり、$G$ は $Z_{p^2}$ または $Z_p \times Z_p$ に同型である。

**証明**：背理法で示す。$G$ が Abel 群でないと仮定すると群の中心は群自身と等しくない。
$Z(G) \subsetneq Z.$

Lagrange の定理より $\lvert Z(G)\rvert$ は $\lvert G\rvert$ を割り切る。
$\lvert G\rvert$ が素数べきであることから $\lvert Z(G) \rvert \ne 1.$
今 $\lvert Z(G) \rvert = p$ しか可能性がない。

一方、剰余群 $G/Z(G)$ において、$\lvert G/Z(G)\rvert = p.$
前述の定理によりこれは巡回群である。これは $G$ が Abel 群であることと矛盾する：
$G$ が Abel ならば剰余群も Abel でなければならない。

背理法により、$G$ は Abel 群である。$\Box$

次に有限 Abel 群の基本定理により、ただちに次を得る：

$$
G \simeq Z_{p^2} \ \lor \ G \simeq Z_p \times Z_p.
\quad \blacksquare
$$

## 定理：$2p$ 群の二つの同型

**定理**：$p$ を 3 以上の素数とする。このとき位数 $2p$ の群は
二面体群 $D_{2p}$ か巡回群 $Z_{2p}$ と同型である。

**証明**：TBW

# 位数が 10 以下の有限群

位数が 10 以下の有限群を分類する。巡回群 $Z_n$ やいくつかの巡回群の直積に同型だという表し方をする。

## 位数が 1 の群

単位元しか含まない集合の一つしかない。

$$
G_1^1 \simeq Z_1 \simeq S_1.
$$

## 位数が 2 の群

位数が素数である群は巡回群しかない。

$$
G_2^1 \simeq Z_2.
$$

## 位数が 3 の群

位数が素数である群は巡回群しかない。

$$
G_3^1 \simeq Z_3.
$$

## 位数が 4 の群

位数が素数の平方の有限群は Abel 群であり、
巡回群と同型であるか、または位数がその素数である巡回群二つの直積に同型だ。

$4 = 2^2$ より：

$$
\begin{aligned}
    G_4^1 &\simeq Z_4,\\
    G_4^2 &\simeq Z_2 \times Z_2 \simeq K_4.
\end{aligned}
$$

ちなみに直積のほうは Klein の四元群 $K_4$ と同型だ。

## 位数が 5 の群

位数が素数である群は巡回群しかない。

$$
G_5^1 \simeq Z_5.
$$

## 位数が 6 の群

位数が素数の倍であるような有限群はすでに分類が済んでいる。
二面体群に同型なほうは Abel 群でない。

$$
\begin{aligned}
G_6^1 &\simeq D_{6} \simeq S_3,\\
G_6^2 &\simeq Z_{6} \simeq Z_3 \times Z_2.
\end{aligned}
$$

ちなみに二面体群 $D_6$ と対称群 $S_3$ は同型だ。

## 位数が 7 の群

位数が素数である群は巡回群しかない。

$$
G_7^1 \simeq Z_7.
$$

## 位数が 8 の群

位数 $8 = 2^3$ ということで、複数の同型が存在する。

Abel 群である同型から調べる。$8 = 2 \cdot 2 \cdot 2 = 4 \cdot 2.$
これに基本定理を適用する。
このタイプの同型が全部で $8, 2 \cdot 2, 4 \cdot 2$ のそれぞれに対応して存在する。

次に 非 Abel 群である同型を調べる。結論から言うと二つある。
一つはおなじみの四面体群に同型のものだ。
もう一つは四元数群 $Q_8$ というものに同型となる。
TODO: ここをしっかり述べる。

以上により、次の 5 個の同型が存在する：

$$
\begin{aligned}
G_8^1 &\simeq Z_8,\\
G_8^2 &\simeq Z_4 \times Z_2,\\
G_8^3 &\simeq D_8,\\
G_8^4 &\simeq Q_8,\\
G_8^5 &\simeq Z_2 \times Z_2 \times Z_2.
\end{aligned}
$$

## 位数が 9 の群

位数が素数の平方の有限群は Abel 群であり、
巡回群と同型であるか、または位数がその素数である巡回群二つの直積に同型だ。

$9 = 3^2$ より：

$$
\begin{aligned}
    G_9^1 &\simeq Z_9,\\
    G_9^2 &\simeq Z_3 \times Z_3.
\end{aligned}
$$

## 位数が 10 の群

位数が素数の倍であるような有限群はすでに分類が済んでいる。
二面体群に同型なほうは Abel 群でない。

$$
\begin{aligned}
    G_{10}^1 &\simeq D_{10},\\
    G_{10}^2 &\simeq Z_{10} \simeq Z_5 \times Z_2.
\end{aligned}
$$

# 参考資料

* 川口周著『代数学入門』
* [List of small groups](https://en.wikipedia.org/wiki/List_of_small_groups) - Wikipedia
