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
\forall a \in R \forall b \in R(b \ne 0_D \implies\\
\exists q \in R \exists r\in R(\\
    (\nu(r) \lt \nu(b) \lor r = 0_D) \land a = qb + r)).
$$

**検討**：
* 整域であって $(EF)$ 条件を満たす関数が存在するものを特に Euclid 整域と呼ぶと言っている。
* 写像 $\nu$ に次の条件を追加する流儀もあるが、Wikipedia がいうように不要。

$$
\tag*{$(EF2)$}
\forall a \in R \forall b \in R(b \ne 0_D \implies \nu(a) \le \nu(ab)).
$$

* 英語では Euclidean domain という。Euclidean integral domain みたいに冗長に書かない。
  ちなみに単数形には不定冠詞 a を用いる。

## 互いに素

**定義**：$D$ を Euclid 整域とする。$a, b \in D$ をどちらも零でない任意の元とする。

$d \coloneqq \gcd\lbrace a, b\rbrace$ が $D$ の零でない単元であるとき、かつそのときに限り、
$a$ と $b$ は**互いに素である**という。

コメント：英語では coprime だとか relatively prime だとか色々言い回しがあるようだ。
日本語では「互いに素」しかない。

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

$\nu(f(X)) \coloneqq \deg f$ が $(EF)$ を満たす。

**証明**：TBW

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

## 単項イデアル整域である

**定理**：Euclid 整域は単項イデアル整域である。

**検討**：不等式 $\nu(?) \lt \nu(?)$ に注目した最大最小パターンによる証明になる。

**証明**：$D$ を Euclid 整域とし、写像 $\nu$ を $D$ の Euclid 写像とする。
以下、$D$ の任意のイデアルが単項生成であることを示す。

$(0) \in D$ は単項イデアルである。

今 $U \subset D$ を $(0)$ ではないイデアルとする。
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

$U$ は任意の $(0)$ でないイデアルであるから、$(0)$ と合わせて、
$D$ の任意のイデアルが単項生成であることが示された。
したがって Euclid 整域は単項イデアル整域である。
$\blacksquare$

## 要素に最大公約元が存在する

**定理**：Euclid 整域の任意の二つの要素には最大公約元が存在する。

$D$ を Euclid 整域とする。このとき任意の $a, b \in D$ に対し
最大公約元 $d \coloneqq \gcd(a, b)$ が存在する。すなわち：

$$
d \mid a \land d \mid b \land (x \mid a \land x \mid b \implies x \mid d).
$$

**検討**：
$\gcd$ の存在を示すのに前定理の Euclid 整域が PID であるという性質を利用する。

**証明**：
$U \subset D$ を $a, b$ が生成するイデアルとする：$U \coloneqq (a) + (b).$
$D$ は Euclid 整域であるので、これは単項イデアルの形に表される。
すなわちある $d \in D$ が存在して $(d) = (a) + (b).$

$a, b \in U$ だから $d$ は $a$ と $b$ のどちらも割り切る。
そして $d$ 自身 $U$ の要素であるので次を満たす $s, t \in D$ が存在する：

$$
sa + tb = d.
$$

整域において、公約元は上のような線形結合で表される元を割り切る。つまり
$a$ も $b$ も割り切るような任意の $x$ について $x$ は $d$ を割り切る。
したがって $d = \gcd(a, b).$

そして $\gcd$ は一意的に定まる。$d^{\prime} \in U$ もまた
$a$ と $b$ のどちらも割り切ると仮定する。このとき $d$ は $d^{\prime}$ を割り切る。
同時に $d^{\prime}$ は $d$ を割り切る。ゆえに $d$ と $d^{\prime}$ は互いに他を割り切る。
$\blacksquare$

# 参考資料

* [ユークリッド環](https://ja.wikipedia.org/wiki/%E3%83%A6%E3%83%BC%E3%82%AF%E3%83%AA%E3%83%83%E3%83%89%E7%92%B0) - Wikipedia
  * EF2 条件についての注意は必読。
* [Category:Euclidean Domains](https://proofwiki.org/wiki/Category:Euclidean_Domains) - ProofWiki