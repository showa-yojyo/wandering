---
title: 『初歩から学べる線形代数』学習ノート Part 7
mathjax: true
tags: math
---

佐藤恒雄、野澤宗平著『初歩から学べる線形代数』より。第 8 章章末問題。

* $f(x)q(x) + g(x)r(x) = 1$ を利用して行列を変形する問題。本番ならこの式は文中に出てこない。
* 次の二問は肌感覚では理解済み：
  * $A(x)$ が可逆⇔$A(x) \sim I$⇔$A(x)$ は基本行列の積で表せる。
  * 正方行列とその転置行列は相似である。
* 最小多項式の計算問題。〆の $(A - \lambda I)^k$ の計算をうっかりしてはもったいない。
* Jordan 標準形の変換行列を求めるときのベクトルの組 $(\bm{p}_1, \dotsc, \bm{p}_k)$
  が一次独立であることの証明。簡単なことに気づかず立ち止まってしまう。
* 正方行列 $A$ に対する最小多項式と転置行列のそれ、相似な行列のそれがすべて一致することの証明。
  固有値が全部共通なのだから、そこから当たりをつける。
* 三角ブロック行列と最小多項式と関係。次のようにする：
  * 前章定理 7.4 より $\varphi_A(x) = \varphi_{A_{11}}(x) \varphi_{A_{22}}(x).$
  * 最小多項式の定義より $m_{A_{11}}(x) \mid \varphi_{A_{11}}(x).$
  * ゆえに $m_{A_{11}}(x) \mid (\varphi_{A_{11}}(x) \varphi_{A_{22}}(x)).\quad \therefore m_{A_{11}}(x) \mid \varphi_A(x).$
  * $A_{22}$ 側についても同様。
