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

コメント：英語では Euclidean domain という。Euclidean integral domain みたいに冗長に書かない。
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

**証明**：TBW

# 性質

## 要素に最大公約元が存在する

TBW

## 単項イデアル整域である

TBW

# 参考資料

TBW
