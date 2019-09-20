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

**証明** 本文 **E 10.2** の公式を利用する。

$$
\begin{aligned}
\sin\pi z &= \pi z \prod_{n = 1}^\infty \left(1 - \frac{z^2}{n^2}\right)\\
&= \pi z (1 - z^2) \prod_{n = 2}^\infty \left(1 - \frac{z^2}{n^2}\right).\\
\therefore \prod_{n = 2}^\infty\left(1 - \frac{z^2}{n^2}\right) &= \frac{\sin\pi z}{\pi z (1 - z^2)}\\
&= \frac{\sin\pi z}{\pi z} \cdot \frac{1}{1 - z^2}\\
&= \frac{\sin\pi z}{\pi z} \cdot \frac{1}{(1 - z)(1 + z)}\\
&= \frac{\sin\pi(1 - z)}{\pi(1 - z)} \cdot \frac{1}{z(1 + z)} \quad \because \sin\theta = -\sin(\theta + \pi)\\
&\to \frac{1}{2} \quad(z \to 1).
\end{aligned}
$$

コメント：無限乗積の部分積を $p_n$ とおくと、次のように展開できる：

$$
\begin{aligned}
p_n &= \prod_{k = 2}^n\left(1 - \frac{1}{n^2}\right)\\
&= \prod_{k = 2}^n\left(1 - \frac{1}{n}\right)\left(1 + \frac{1}{n}\right)\\
&= \frac{1}{2}\cdot\frac{3}{2}
   \cdot \frac{2}{3} \cdot \frac{4}{3}
   \cdot \frac{3}{4} \cdot \frac{5}{4}
   \cdot \frac{4}{5} \cdot \frac{6}{5}
   \dotsm \frac{n - 1}{n}\cdot\frac{n + 1}{n}\\
&= \frac{1}{2} \cdot\frac{n + 1}{n}.\\
\end{aligned}
$$

このことからも $p_n \to \dfrac{1}{2}\;\; (n \to \infty)$ を示せる。
実は高校数学レベルの設問なのだ。

----

$$
\lvert z \rvert < 1 \implies\\
\prod_{n = 0}^{\infty}(1 + z^{2^n})
= (1 + z)(1 + z^2)(1 + z^4)(1 + z^8)\dotsm
= \frac{1}{1 - z}.
$$

**証明** コメント：等式の真ん中は左辺指数の誤植を避けるために記されたものだろう。

これも高校数学レベルの設問だ。無限乗積の部分積を $p_n$ とおく。これの括弧を外すと見慣れた級数の形になる：

$$
\begin{aligned}
    p_0 &= (1 + z^1) = 1 + z.\\
    p_1 &= (1 + z)(1 + z^2) = 1 + z^2 + z + z^3 = \sum_{k = 0}^3z^k.\\
    p_2 &= p_2(1 + z^4) = \sum_{k = 0}^7 z^k\\
    p_3 &= p_3(1 + z^8) = \sum_{k = 0}^{15} z^k.\\
    &\dots\\
    p_n &= \sum_{k = 0}^{2^{n + 1}} z^k.
\end{aligned}
$$

$n$ を発散させるので、級数の最後の添字の詳細は実は気にしないで済んだ。$\lvert z \rvert < 1$ ゆえ：

$$
\prod_{n = 0}^{\infty}(1 + z^{2^n})
= \lim_{n \to \infty}p_n = \sum_{k = 0}^{\infty} z^k = \frac{1}{1 - z}.
$$

----

$$
\begin{aligned}
\text{(1)} &\quad \frac{\varGamma(z + n)}{\varGamma(z)} = z(z + 1)(z + 2)\dotsm(z + n - 1), & z \notin \lbrace0\rbrace \cup -\N.\\
\text{(2)} &\quad \lim_{n \to \infty}\frac{\varGamma(z + n)}{\varGamma(z) n^z} = 1.
\end{aligned}
$$

**補題**：$\varGamma(z + 1) = z\varGamma(z).$

**証明**：Gauss の等式を変形する。

$$
\def\L{ \lim_{n \to \infty} }
\begin{aligned}
    \varGamma(z + 1)
    &= \L \frac{n! n^{z + 1}}{(z + 1)\dotsm(z + n)(z + n + 1)}\\
    &= \L z \cdot \frac{n! n^z}{z(z + 1)\dotsm(z + n)}\cdot\frac{n}{z + n + 1}\\
    &= z \varGamma(z) \L \cdot\frac{1}{(z + 1)/n + 1}\\
    &= z \varGamma(z).
\end{aligned}
$$

**$(1)$ の証明**：補題の等式を繰り返し適用する。

$$
\begin{aligned}
\varGamma(z + n)
&= (z + n)\varGamma(z + n - 1)\\
&= (z + n)(z + n - 1)\varGamma(z + n - 2)\\
&= \dots\\
&= (z + n)(z + n - 1)\dotsm(z + 1)z\varGamma(z).\\
\therefore \frac{\varGamma(z + n)}{\varGamma(z)}
&= (z + n)(z + n - 1)\dotsm(z + 1)z.
\end{aligned}
$$

**$(2)$ の証明**：
TBW; Weierstrass の公式を利用するのかもしれない。

----

$$
\Re p > 0 \land \Re q > 0 \implies B(p, q) = 2\int_0^{\pi/2}\!\sin^{2p - 1}\theta \cos^{2q - 1}\theta\,\mathrm d\theta.
$$

**証明**：$t = \sin^2\theta$ と変数変換。$\theta \in {[0, \pi/2]},\;\mathrm dt = 2\sin\theta\cos\theta\,\mathrm d\theta.$

$$
\begin{aligned}
B(p, q) &= \int_0^1\!t^{p - 1}(1 - t)^{q - 1}\,\mathrm dt\\
&= \int_0^{\pi/2}\sin^{2p - 2}\theta (1 - \sin^2\theta)^{q - 1} \cdot 2\sin\theta\cos\theta\,\mathrm d\theta\\
&= 2\int_0^{\pi/2}\!\sin^{2p - 1}\theta \cos^{2q - 1}\theta\,\mathrm d\theta.
\end{aligned}
$$

----

$$
\frac{\varGamma(1 - n - z)}{\varGamma(1 - z)} = \frac{(-1)^n}{z(z - 1)(z - 2)\dotsm(z - n + 1)}, \quad n \in \N.
$$

**証明** TODO: 符号が合わない？

両方の $\varGamma()$ の引数を揃えることを試みる：

$$
\begin{aligned}
\varGamma(1 - n - z)
&= \varGamma(1 - (z + n))\\
&= -(z + n)\varGamma(-(z + n)).\\
\\
\varGamma(1 - z)
&= -z\varGamma(-z)\\
&= -z\varGamma(1 - (z + 1))\\
&= z(z + 1)\varGamma(-(z + 1))\\
&= -z(z + 1)(z + 2)\varGamma(-(z + 2))\\
&= \dots\\
&= (-1)^{n-1} z(z+1)\dotsm(z + n)\varGamma(-(z + n)).
\end{aligned}
$$

これらを割って以下を得る：

$$
\begin{aligned}
\frac{\varGamma(1 - n - z)}{\varGamma(1 - z)}
&= \frac{-(z + n)\varGamma(-(z + n))}{(-1)^{n-1} z(z+1)\dotsm(z + n - 1)(z + n)\varGamma(-(z + n))}\\
&= \frac{(-1)^n}{z(z+1)\dotsm(z + n - 1)}.
\end{aligned}

$$
