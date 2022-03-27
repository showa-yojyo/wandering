---
title: 平方剰余の相互法則
mathjax: true
tags: math
---

平方剰余の相互法則をまとめておく。以下、定数や変数はすべて整数とする。

* まず**平方剰余**、**平方非剰余**の概念を理解すること（本書では省略して QR, NR とそれぞれ呼んでいるが）。
  * $x^2 \equiv a \pmod m$ が解を持つか否かを表す概念。

* $\gcd(a, m) = 1$ なる $a$ が $m$ を法とする平方剰余である条件を導出できるようにすること。
  * これは少し記憶しにくい。

* Legendre の記号の定義を覚えること。

  $$
  \left(\dfrac{a}{p}\right) = \begin{cases}
       1 & \text{if } a \text{ is a QR } \bmod p\\
      -1 & \text{if } a \text{ is a NR } \bmod p
  \end{cases}
  $$

* Euler 規準を理解すること。
* Legendre の記号の相互法則を理解すること、その成果として記号の値を計算できるようにすること。
* SymPy の関連関数を調査すること（モジュール `sympy.ntheory` にある）。
