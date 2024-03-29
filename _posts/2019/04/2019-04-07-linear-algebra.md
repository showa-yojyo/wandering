---
title: 『初歩から学べる線形代数』学習ノート Part 1
mathjax: true
tags: math
---

佐藤恒雄、野澤宗平著『初歩から学べる線形代数』より。

* 固有値・固有ベクトルの定義
* 固有値を求める方法（固有値をどの体の上で得るかが大事）
* 固有多項式、固有方程式の定義 $\varphi_A(x) = \lvert A - xI \rvert = 0$
* 固有値の多重度 $n_i$
* 固有空間 $W(\lambda)$
* 固有空間の幾何学的意味付け（伸縮方向と比率）
* 固有値すべての和および積は容易に求まる
  * $\operatorname{tr}{A}, \det{A}$
* 正方行列の正則性と固有値との関係（オールゼロ）
* 分割行列の固有値の求め方
* 相似な行列同士の固有値は一致する
* 相異なる固有値に属する固有ベクトルは一次独立
* 相異なる固有値の固有空間 ($W(\lambda_i)$) の和は直和である
* 「三角化可能」の定義（三角行列と相似）
* 正方行列は三角化可能（対角成分に固有値が並ぶ形になる）
* 行列の多項式の定義
* Cayley-Hamilton の定理 $\varphi_A(A) = O$
  * 証明に注意。$P^{-1}\varphi_A(A)P$ を考える。
* Frobenius の定理（多項式の固有値）
  * $P^{-1}g(A)P$ を考える。
* 「対角化可能」の定義
* 対角化可能の十分条件（十分条件だが「固有値がすべて異なる」というものなので使いやすい）
* 対角化可能 ⇔ $\dim{W(\lambda_i)} = n_i$ ⇔ $n$ 個からなる一次独立な固有ベクトルの組が存在する
* 実対称行列の固有値・固有ベクトルの性質
* 実正方行列の固有値がすべて実数ならば、この行列はある直交行列により三角化可能
* 実対称行列はある直交行列により対角化可能
* 実対称行列を対角化するアルゴリズム
  1. 固有値を求める
  2. 固有空間の基底を求める
  3. Gram-Schmidt 法により正規直交基底を得る
  4. これらの基底ベクトルを束ねて $P$ とする。$P^{-1}AP$ は対角行列となる。
* 二次形式の定義 $Q(x_1, \dotsc, x_n) = Q(\bm{x})$
* 二次曲線の標準形（曲線を分類するだけならば $P$ を求めなくて済む）
