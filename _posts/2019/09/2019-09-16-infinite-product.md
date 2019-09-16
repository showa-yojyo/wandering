---
title: 『新訂解析学』学習ノート Part 15
tags: math
---

熊原啓作著『新訂解析学』第 10 章（無限乗積）章末問題を解く。

----

$$
2 \le \prod_{n = 0}^\infty \left(1 + \frac{1}{n(n + 1)}\right) \le \mathrm{e}.
$$

**証明** $a_n = \dfrac{1}{n(n + 1)}$ とおく。
まず高校数学レベルだが $\displaystyle \sum_{n = 1}^\infty a_n = 1$ を証明する。：

$$
\def\tt#1#2{ \left(\frac{1}{#1} - \frac{1}{#2}\right) }
\begin{aligned}
    \sum_{n = 1}^\infty a_n
    &= \sum_{n = 1}^\infty \left(\frac{1}{n} - \frac{1}{n + 1}\right)\\
    &= \tt{1}{2} + \tt{2}{3} + \dotsb + \tt{n}{n + 1} + \dotsm\\
    &= \lim_{n \to \infty}\tt{1}{n}\\
    &= 1.
\end{aligned}
$$

次の不等式を利用すれば証明は終わる：

$$
\lim_{n \to \infty}a_n = 0 \land a_n \ge 0 \implies
1 + \sum_{n = 1}^\infty a_n \le \prod_{n = 1}^\infty(1 + a_n)
  \le \mathrm{e}^{\sum_{n = 1}^\infty a_n}.
$$

条件 $\lim a_n \to 0$ は無限級数の収束と無限乗積の収束する条件だ。
上記の不等式が成り立つことは本文中に書いてあるが、いちおうメモ：

$$
\begin{aligned}
    x \ge 0 &\implies 1 + x \le \mathrm{e}^x.\\
    \therefore x \ge 0 \land y \ge 0 &\implies (1 + x)(1 + y) \le \mathrm{e}^x \mathrm{e}^y = \mathrm{e}^{x + y}.\\
\end{aligned}
$$

一方：

$$
x \ge 0 \land y \ge 0 \implies 1 + x + y \le 1 + x + y + xy = (1 + x)(1 + y).
$$

こちらも高校数学レベルだった。

----

$$
\prod_{n = 2}^\infty \left(1 - \frac{1}{n^2}\right) = \frac{1}{2}.
$$

**証明** TBW.

----

$$
\lvert z \rvert < 1 \implies\\
\prod_{n = 0}^{\infty}(1 + z^{2n})
= (1 + z)(1 + z^2)(1 + z^4)(1 + z^8)\dotsm
= \frac{1}{1 - z}.
$$

**証明** TBW.

----

$$
\begin{aligned}
\text{(1)} &\quad \frac{\varGamma(z + n)}{\varGamma(z)} = z(z + 1)(z + 2)\dotsm(z + n - 1), & z \notin \lbrace0\rbrace \cup -\N.\\
\text{(2)} &\quad \lim_{n \to \infty}\frac{\varGamma(z + n)}{\varGamma(z) n^z} = 1.
\end{aligned}
$$

**証明** TBW.

----

$$
\Re p > 0 \land \Re q > 0 \implies B(p, q) = 2\int_0^{\pi/2}\!\sin^{2p - 1}\theta \cos^{2q - 1}\theta\,\mathrm d\theta.
$$

**証明** TBW.

----

$$
\frac{\varGamma(1 - n - z)}{\varGamma(1 - z)} = \frac{(-1)^n}{z(z - 1)(z - 2)\dotsm(z - n + 1)}, \quad n \in \N.
$$

**証明** TBW.
