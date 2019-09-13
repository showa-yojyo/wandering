---
title: 『初歩から学べる線形代数』学習ノート Part 5
tags: math
---

佐藤恒雄、野澤宗平著『初歩から学べる線形代数』より。
第 8 章の小問を順番に解いていく。

* $x$-行列を基本変形して単因子 $e_k(x)$ を得る問題は、いつもの計算ミスを除けば問題ない（理解は問題ない）。
* 行列式因子 $d_k(x)$ を計算する問題も同様。どうやら $d_0(x) = 1$ はいつでも明記するようだ。
* $x$-行列の階数など、単因子が関係する性質が問われる場合、その標準形を調べればよい。
* 固有 $x$-行列の単因子を求める問題も計算ミスが怖い。
* Cayley-Hamilton の定理を固有多項式と最小多項式の性質から証明する。
  この証明方法は余因子行列と因数定理（の類似）しか用いていない。
  1. 正方行列 $A$ の固有多項式を $\varphi_A(x)$ とおくと $\varphi_A(x)I = \lvert A - xI \rvert\,I = (xI - A)\operatorname{adj}(xI - A).$
  2. 補題 8.10 の $Q(x)$ に $\operatorname{adj}(xI - A)$ を当てはめれば左向きの矢印が成り立つから $\varphi_A(A) = O$
* $\lambda$ が固有値であるときに限り $\varphi_A(\lambda) = m_A(\lambda) = 0.$
* 最小多項式を問う問題。まず固有多項式を求める。そして全因数を一つは含む多項式 $f(X)$ から始めて $f(A) = O$ になるものを見つける。それが $m_A(x)$ だ。
* 与えられた固有多項式と最小多項式から考えられる Jordan 標準形を挙げる問題。
  1. 固有多項式の次数から行列のサイズがわかる。
  2. 最小多項式の形から標準形の右下部分がわかる。
  3. $\dfrac{\varphi_A(x)}{m_A(x)} = e_1(x)e_2(x)\dotsm e_?(x)$ から標準形の左上部分が検討できる。
