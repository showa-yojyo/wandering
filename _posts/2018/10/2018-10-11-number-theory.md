---
title: 『はじめての数論 原著第 3 版』学習ノート Part 2
tags: math
---

鈴木治郎訳『はじめての数論 原著第 3 版』より。

----

* 第 37 章
  * Fibonacci 数列の由来は 1202 年の彼の本による。
  * mutatis mutandis の意味するところは何か？
  * Fibonacci 数列を $\bmod{p}$ で考える。ある周期性が現れる。
  * 練習問題が妙に多いのが気になる。
  * ビネだのリュカだの、スペリングがわからない人名がある。
* 第 38 章
  * なんと $O()$ 記法がトピックだ。本書ではもっぱら計算時間のオーダーを表現するのに用いる。
  * 繰り返し自乗法のオーダーは対数時間であり、愚直な計算法は線形時間だ。
  * 練習問題では $o()$ 記法、$\Omega()$ 記法と $\Theta()$ 記法を採用している。
* 第 39 章
  * 連分数による無理数の近似、連分数の漸化式。
  * 練習問題 39.2. の計算：

    {% raw %}
    ```python
    >>> list(islice(ntheory.continued_fraction_iterator(pi**2), 3))
    ... [9, 1, 6]

    >>> L = list(islice(ntheory.continued_fraction_iterator(pi**2), 6))

    >>> L[:3]
    ... [9, 1, 6]

    >>> ntheory.continued_fraction_reduce(L[:5])
    ... 227/23

    >>> (pi**2 - _).evalf()
    ... 3.91836980542710e-5

    >>> ntheory.continued_fraction_reduce(L[:6])
    ... 10748/1089

    >>> (pi**2 - _).evalf()
    ... -7.41243056440853e-7
    ```
    {% endraw %}

* 第 40 章
  * 連分数を用いて Pell 方程式の特解を得ることができる。
  * 周期的部分を特定するアルゴリズムが欲しい。
