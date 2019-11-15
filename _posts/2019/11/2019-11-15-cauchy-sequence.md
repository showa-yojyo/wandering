---
title: 実 Cauchy 列が収束することのくどい証明ノート
tags: math
---

すごく基本的な定理でありながらなぜか私の頭に入らない Cauchy 列の収束性を示す証明についてのノート。

<!--
# 証明フォーマット
## ～を証明する

$P$ を真と仮定して $Q$ を導く。

## 検討

戦略使用前：

| Givens | Goal |
| ------ | ---- |
| - | $P \implies Q$ |
| - | |

戦略使用後：

| Givens | Goal |
| ------ | ---- |
| - | $Q$ |
| $P$ | |

## 最終的な証明の形

仮定 $P$

* $Q$ であることの証明

したがって $P \implies Q$
-->

# 実数の完備性

## 主張

実数上の Cauchy 列 $\lbrace a_n \rbrace$ は収束する。

## 検討

| Givens | Goal |
| ------ | ---- |
| $\lbrace a_n \rbrace$ | $\lbrace a_n \rbrace$ は収束する |
| $\lbrace a_n \rbrace$ は Cauchy である | |

紙幅とタイプ量の都合上、数列 $\lbrace a_n \rbrace$ が Cauchy であること、
および数列が $\alpha$ に収束することを論理式で表しておく：

$$
\begin{aligned}
P(\lbrace a_n \rbrace) &\coloneqq [
\forall \varepsilon \gt 0 \exists N \in \N
\forall m \ge N \forall n \ge N(\lvert a_m - a_n \rvert \lt \varepsilon)
].\\
Q(\lbrace a_n \rbrace, \alpha) &\coloneqq [
\forall \varepsilon > 0 \exists N \in \N \forall n \ge N(
    \lvert a_n - \alpha \rvert < \varepsilon
)
].
\end{aligned}
$$

ただし一気に証明するのはきついので、いくつかの補題に分割して統合する。

* 補題 1: 数列の第 $m$ 項に対して集合 $A_m \coloneqq \lbrace a_m, a_{m+1}, a_{m+2}, \dots\rbrace$ を対応させる。
  集合 $A_m$ は有界である。

有界なので、特に下限が存在する。これを $\alpha_m \coloneqq \inf A_m$ とおく。

* 補題 2: 数列 $\lbrace \alpha_m \rbrace$ は上に有界な非減少列である。

これが成り立てば数列 $\lbrace\alpha_m\rbrace$ は収束する。このとき次が成り立てば元の主張が証明される：

* 補題 3: $\displaystyle \lim_{m \to \infty}\alpha_m = \lim_{m \to\infty}a_m.$

| Givens | Goal |
| ------ | ---- |
| $\lbrace a_n \rbrace$ | $\exists \alpha Q(\lbrace a_n \rbrace, \alpha)$ |
| $P(\lbrace a_n \rbrace)$ | |

## 補題 1

数列の第 $m$ 項に対して集合 $A_m \coloneqq \lbrace a_m, a_{m+1}, a_{m+2}, \dots\rbrace$ を対応させる。
集合 $A_m$ は有界である。

### 検討

| Givens | Goal |
| ------ | ---- |
| $\lbrace a_m \rbrace$ | $\exists L_m \in \R \exists U_m \in \R(\forall x \in A_m(L_m \lt x \lt U_m))$ |
| $P(\lbrace a_m \rbrace)$ | |
| $A_m \coloneqq \lbrace a_m, a_{m + 1}, \dotsc \rbrace$ | |

### 証明

$P(\lbrace a_m \rbrace)$ であることから $\forall m \ge N \forall n \ge N$ に対して

$$
\begin{aligned}
&\phantom{\iff} \lvert a_n - a_m \rvert \lt \varepsilon\\
&\iff -\varepsilon < a_n - a_m < \varepsilon\\
&\iff a_m - \varepsilon < a_n < a_m + \varepsilon.
\end{aligned}
$$

ゆえに $L_m \coloneqq a_m - \varepsilon$ とすれば $\forall n \ge m(L \lt a_n).$
番号 $N$ から先は下に有界だから、すなわち数列全体で下に有界である。上に有界であることも同様に成り立つ。

したがって集合 $A_m$ は有界である。
$\blacksquare$

## 補題 2

数列 $\lbrace \alpha_m \rbrace$ は上に有界かつ非減少列である。

### 検討

| Givens | Goal |
| ------ | ---- |
| $A_m \coloneqq \lbrace a_m, a_{m + 1}, \dotsc \rbrace$ | $\exists u_m \in \R(\alpha_m \le u_m)$ |
| $\exists L_m \in \R \exists U_m \in \R(\forall x \in A_m(L_m \lt x \lt U_m))$ | $\forall m(\alpha_m \le \alpha_{m + 1})$ |
| $\lbrace \alpha_m\rbrace \coloneqq \lbrace \inf A_m \rbrace$ | |

### 証明

数列の有界性は $A_m$ の有界性と数列の定義から次のようにしてわかる：

$$
\begin{aligned}
    &(\forall x \in A_m (x \le U_m)) \land (\forall n \ge m(\alpha_n \le a_n))\\
    &\implies \forall n \ge m (\alpha_n \le a_m \le U_m).\\
    &\implies \forall n \ge m (\alpha_n \le U_m).\\
\end{aligned}
$$

数列 $\lbrace \alpha_m \rbrace$ は上から $U_m$ で押さえられている。上に有界である。

非減少性を示す。場合分けによりわかる：

* $a_m < a_{m+1} \implies \inf A_m < \inf A_{m+1}$
* $a_m = a_{m+1} \implies \inf A_m = \inf A_{m+1}$
* $a_m > a_{m+1} \implies \inf A_m = \inf A_{m+1}$

ゆえに $\alpha_m \le \alpha_{m+1}$ となり数列 $\lbrace \alpha_m \rbrace = \lbrace \inf A_m \rbrace$ は非減少列である。

以上により、数列 $\lbrace \alpha_m \rbrace$ は有界な非減少列である。
$\blacksquare$

## 補題 3

$\displaystyle \lim_{m \to \infty}\alpha_m = \lim_{m \to\infty}a_m.$

### 検討

| Givens | Goal |
| ------ | ---- |
| $\lbrace a_m \rbrace$ | $Q(\lbrace a_m \rbrace, \alpha)$ |
| $P(\lbrace a_m \rbrace)$ | |
| $A_m \coloneqq \lbrace a_m, a_{m + 1}, \dotsc \rbrace$ | |
| $\lbrace \alpha_m\rbrace \coloneqq \lbrace \inf A_m \rbrace$ | |
| $\alpha \coloneqq \lim \alpha_m$ | |

「有界かつ単調な数列は収束する」を適用してある。
数列 $\lbrace \alpha_m \rbrace$ が補題 2 の仮定を満たせば収束する。

### 証明

$\alpha = \displaystyle \lim_{m \to \infty}\alpha_m$ より

$$
\begin{aligned}
&\forall \varepsilon \gt 0
\exists M_1 \in \N
(\forall m \gt M_1 \implies \lvert \alpha_m - \alpha \rvert \lt \varepsilon).\\

&\implies \alpha - \varepsilon \lt \alpha_m \lt \alpha + \varepsilon.\\
\end{aligned}
$$

$P(\lbrace a_m \rbrace)$ であることより

$$
\begin{aligned}
&\exists M_2 \in \N
(\forall m \forall n(m \ge M_2 \land n \ge M_2 \implies \lvert a_m - a_n \rvert \lt \varepsilon)).\\

&\implies a_m - \varepsilon \lt a_n \lt a_m + \varepsilon
\end{aligned}
$$

$M \coloneqq \max\lbrace M_1, M_2\rbrace$ に対して上の二つが同時に成り立つ。
$a_m - \varepsilon < a_n$ より $a_m - \varepsilon$ は $A_M$ の下界である。
よって

$$
\begin{aligned}
a_m - \varepsilon \le \alpha_M \lt \alpha + \varepsilon.\\
\therefore \alpha - \varepsilon < \alpha_m \le a_m < \alpha + 2\varepsilon.
\end{aligned}
$$

$\varepsilon > 0$ は任意だから $\alpha_m, a_m$ はどちらも $\alpha$ に収束する。
つまり $Q(\lbrace a_m \rbrace, \alpha)$ が成り立つ。
$\blacksquare$

## 総合

補題 1 $\implies$ 補題 2 $\implies$ 補題 3 $\implies (P(\lbrace a_m \rbrace) \implies \exists\alpha Q(\lbrace a_m \rbrace, \alpha)).$

----

以前見たのはもっとわかりにくい証明だった。本ノートのは（私には）だいぶ見通しやすい。
