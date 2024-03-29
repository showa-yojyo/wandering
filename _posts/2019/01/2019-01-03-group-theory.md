---
title: 『代数入門 群と加群』学習ノート Part 2
mathjax: true
tags: math
---

堀田良之著『代数入門 群と加群』より。第二章加群の続きを読み進める。

* 自由加群の概念を学ぶ。一次独立な生成系（もちろん基底と呼ぶ）を有する加群のことだ。
  その基底の濃度のことを階数と呼ぶ。
* 単因子論。単項イデアル整域上の有限生成加群の形を調べる。
  以降は $R$ を単項イデアル整域と仮定する。
* 基本行列は記号 $E_{ij}(\alpha, \beta, \delta, \gamma)$ で表す。添字と変数が多くて使いにくそうだが。
* 基本変形と初等変形。基本変形は有限回であるものとする。
* 単項イデアル整域上の行列は初等変形を施すと、成分が「単因子」とゼロからなる対角行列に変形できる。
* **単因子は単元倍を除いて一意的に定まる。**
* 行列式因子の定義。同サイズの小行列式の $\gcd$ をとった列。
* **単因子と行列式因子の関係式から単因子を求めるアルゴリズムがある。**
* 有限生成加群の構造定理

  $$
  M \cong \bigoplus_{i=1}^{r} R/Rd_i \oplus R^l
  $$

  * $d_1 \vert d_2 \vert \dotsb \vert d_r,\ d_1 \notin R^\times,\ d_r \neq 0.$
  * $(d_1, d_2, \dots, d_r, 0, \dots, 0)$ （ゼロは $l$ 個）は**単因子型**という。
* Abel 群の基本定理「有限生成 Abel 群と巡回群有限個の直積とが同型である」
