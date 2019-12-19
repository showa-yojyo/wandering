---
title: Euclid 整域学習ノート
tags: math
---

代数入門レベルの Euclid 整域の学習内容をまとめる。以下、環といったら 1 を含む可換環のつもりで書かれている。

# 定義
## Euclid 整域

**定義**：$D$ を零元 $0_D$ を含む整域とする。$D$ が **Euclid 整域**であるとは、
次の条件を満たす写像 $\nu\colon D\setminus \lbrace 0_D \rbrace \longrightarrow \N$ が存在する整域のこととする：

$$
\tag*{$(EF)$}
\forall a \in D \forall b \in D(b \ne 0_D \implies\\
\exists q \in D \exists r\in D(\\
    (\nu(r) \lt \nu(b) \lor r = 0_D) \land a = qb + r)).
$$

**検討**：
* 整域であって $(EF)$ 条件を満たす関数が存在するものを特に Euclid 整域と呼ぶと言っている。
* 写像 $\nu$ に次の条件を追加する流儀もあるが、Wikipedia がいうように不要。

$$
\tag*{$(EF2)$}
\forall a \in D \forall b \in D(b \ne 0_D \implies \nu(a) \le \nu(ab)).
$$

* 英語では Euclidean domain という。Euclidean integral domain みたいに冗長に書かない。
  ちなみに単数形には不定冠詞 a を用いる。

# Euclid 整域のインスタンス

## 整数環

有理整数環 $\Z$ はもちろん Euclid 整域である。Euclid 整域は主にこれをモデルにして生じた概念なのだから。

$\nu(n) \coloneqq \lvert n \rvert$ とすれば $(EF)$ を満たす。整除の原理だ。

**検討**：整除原理を証明することになる。符号による場合分けなど。

**証明**：任意に $a, b \in \Z,\; b \ne 0$ をとる。

$b \gt 0$ のとき： $a$ の符号により場合分けを行う。

以下、これを正の整除原理と呼んで参照する。

$b \lt 0$ のとき：絶対値 $\lvert b \rvert \gt 0$ を考えることにする。

すると正の整除原理により、次が成り立つ：

$$
\exists \tilde q \in \Z \exists \tilde r \in Z(\\
  a = \lvert b \rvert \tilde q + \tilde r \land (
    \lvert \tilde r \rvert \lt \lvert b \rvert \lor \tilde r = 0)).
$$

条件中の等式を絶対値を外して書くと：

$$
a = (-b)\cdot\tilde q + \tilde r = b(-\tilde q) + \tilde r.
$$

これは $(EF)$ で $q, r$ をそれぞれ $-\tilde q, \tilde r$ と置いたものだ。
よって $b \lt 0$ のときにも $(EF)$ が成り立つ。

以上より、$\Z$ は $(EF)$ を満たすことが示された。すなわち $\Z$ は Euclid 整域である。
$\blacksquare$

## 体上の多項式環

体 $F$ を係数とする多項式環 $F[X]$ は Euclid 整域である（整域であることは問題ない）。

**証明**：$\nu(f(X)) \coloneqq \deg f$ が $(EF)$ を満たすことを示す。
任意に $f \in F[X]$ と $g \in F[X],\;g \ne 0_{F[X]}$ をとる。

このとき $q \in F[X]$ および $r \in F[X]$ が存在して次が成り立つことを示す：

$$
f = qg + r \land (r = 0_{F[X]} \lor (\deg r \lt \deg g)).
$$

TODO: 色々やり方があるので検討する。

$\blacksquare$

## Gauss 整数環

$\Z[i]$ で Gauss 整数環を表す。これは Euclid 整域である。

写像 $\nu$ のとり方は例えば次で定める：

$$
\nu(a) = \lvert a \rvert^2.
$$

**証明**：写像 $\nu$ が $(EF)$ 条件を満たすことを示す。

TODO: これは少し難しい。

写像 $\nu$ が $(EF)$ 条件を満たすことが示された。ゆえに $\Z[i]$ は
Euclid 整域である。
$\blacksquare$

# 性質

## Bézout の補題が成り立つ

**定理**：$D$ を Euclid 整域とし、$a, b \in D$ は $a$ と $b$ の少なくとも一方は $0_D$ ではないとする。
このとき次の等式を満たす $x, y \in D$ が存在する：

$$
ax + by = \gcd(a, b).
$$

**検討**：この定理がおそらくもっとも基本的 Euclid 整域の性質を述べるものだと思われる。
証明の内容は整数論における同補題と同様であり、PID の概念が少し見える。

**証明**：$b \ne 0$ を仮定する。部分集合 $S \subset D$ を次で定義する：

$$
S \coloneqq \{s\,|\,s \in D\!\setminus\!0_D, s = ax + by, x \in D, y \in D \}.
$$

まず $S \ne \varnothing$ を示す。$x = 0_D, y = 1_D$ とすることで $b \in S.$
よって $S \ne \varnothing.$

$D$ に対する $(EF)$ 条件の定める写像を $\nu$ とおく。$\nu(S) \subset \N$ である。
整列原理により $\nu(S)$ には最小元が存在する。それを $d \in S$ とおく：$\nu(d) = \min\nu(S).$

すると $S$ は $d$ によって生成される単項イデアルになる $(\because)$。

----
$(\because)$
任意に $s \in S$ をとる。Euclid 整域の性質からある $q, r \in D$ が存在して
$s = qd + r$ かつ
* $r = 0$
* または $\nu(r) \lt \nu(d)$

と書ける。$d$ のとり方から後者は成り立たない。よって $s = qd.$
$s$ は任意だから $S$ のすべての要素は $d$ の倍元である。$S = (d).$
$\Box$

----

$ax + by$ の式で $x = 1_D, y = 0_D$ とすれば $a \in S.$ 先に述べたように $b \in S.$
したがって $a, b$ はどちらも $d$ の倍元であり、$d$ は $a, b$ の公約元である。
すなわち

$$
\tag*{$\spadesuit1$}
d \le g.
$$

一方、$a, b$ は $g \coloneqq \gcd(a, b)$ の倍元であるから、ある $a^{\prime}, b^{\prime} \in S$ が存在して
$a = a^{\prime}g,\;b = b^{\prime}g.$ すると

$$
\begin{aligned}
ax + by &= a^{\prime}gx + b^{\prime}gy\\
&= (a^{\prime}x + b^{\prime}y)g.
\end{aligned}
$$

となり、$S$ のすべての要素は $\gcd(a, b)$ の倍元である。
特に $d \in S$ もそうであるから

$$
\tag*{$\spadesuit2$}
g \le d.
$$

$\spadesuit1, \spadesuit2$ より $d = g.$
したがって $ax + by = g = \gcd(a, b).$
以上により、任意の $a \in D, b (\ne 0_D) \in D$ に対して
$ax + by = \gcd(a, b)$ を満たす $x \in D, y \in D$ が存在することが示された。
$\blacksquare$

## Euclid の補題が成り立つ

**定理**：$D$ を Euclid 整域とし、$a, b, c \in D$ とする。
$a$ が $bc$ を割り切るとする。かつ $a$ と $b$ は互いに素であるとする。

このとき $a$ は $c$ を割り切る。

**検討**：これも基本的だ。整数論における互いに素の性質を一般化したものだ。

ここで Bézout の補題を利用する。

**証明**：$a$ と $b$ が互いに素、すなわち $\gcd(a, b) = 1_D$ であることから、
Bézout の補題により次が成り立つような $x, y \in D$ が存在する：

$$
ax + by = 1_D.
$$

このとき

$$
\begin{aligned}
c &= c \cdot 1_D\\
&= c(ax + by)\\
&= ac x + bc y.
\end{aligned}
$$

$a$ は $ac$ も $bc$ も割り切るので、それらの倍元の和である $acx + bcy$ をも割り切る。
この値はすなわち $c$ であるので、$a$ は $c$ を割り切る。
$\blacksquare$

## 単項イデアル整域である

**定理**：Euclid 整域は[単項イデアル整域][pid]である。

**検討**：不等式 $\nu(?) \lt \nu(?)$ に注目した最大最小パターンによる証明になる。

**証明**：$D$ を Euclid 整域とし、写像 $\nu$ を $D$ の Euclid 写像とする。
以下、$D$ の任意のイデアルが単項生成であることを示す。

$(0_D) \in D$ は単項イデアルである。

今 $U \subset D$ を $(0_D)$ ではないイデアルとする。
このとき $\nu(d)$ の値が $U$ の中で最小である $d \in U$ が存在する
（これは $\N$ またはその部分集合に対する整列原理による）。

要素 $a \in U$ を一つ任意にとる。$D$ が Euclid 整域であることから
次の条件が成り立つ $q, r \in D$ が存在する：

$$
a = qd + r \land (\nu(r) \lt \nu(d) \lor r = 0).
$$

ここで $r \ne 0$ は成り立たない。なぜなら $r = 0$ だとすると
$\nu(r) \lt \nu(d)$ が成り立つが、これは $d$ のとり方に反する。

よって $r = 0.$
すると $a = qd.$ $a$ は $d$ の倍元である。

$a \in U$ は任意であったから、$U$ のすべての要素は $d$ の倍元である。
つまり $U$ は $d$ によって生成されるイデアルである。

$U$ は任意の $(0_D)$ でないイデアルであるから、$(0_D)$ と合わせて、
$D$ の任意のイデアルが単項生成であることが示された。
したがって Euclid 整域は[単項イデアル整域][pid]である。
$\blacksquare$

# 参考資料

* [ユークリッド環](https://ja.wikipedia.org/wiki/%E3%83%A6%E3%83%BC%E3%82%AF%E3%83%AA%E3%83%83%E3%83%89%E7%92%B0) - Wikipedia
  * EF2 条件についての注意は必読。
* [Category:Euclidean Domains](https://proofwiki.org/wiki/Category:Euclidean_Domains) - ProofWiki

[pid]: {{ site.baseurl }}{% post_url 2019/12/2019-12-19-pid %}
