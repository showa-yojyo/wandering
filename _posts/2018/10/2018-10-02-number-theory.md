---
title: 『はじめての数論 原著第 3 版』学習ノート Part 1
tags: math
---

鈴木治郎訳『はじめての数論 原著第 3 版』第 26-29 章より。

* (p. 180) 紙幅の都合上と思われるが $25 = 0^2 + 5^2$ および $50 = 1^2 + 7^2$ が抜けている。
* 恒等式 $(u^2 + v^2)(A^2 + B^2) = (uA + vB)^2 + (vA - uB)^2$ が多重に使えることに注意。
* 練習問題 26.7. (a) $p^2 = A^2 + B^2$ を見つけるアルゴリズム「降下法」の実装例。

  ```python
  In [334]: def descent_method_p_1_mod4(A, B, p):
       ...:     assert p % 4 == 1
       ...:
       ...:     def update_multiplier(a, b):
       ...:         return (a**2 + b**2) // p
       ...:
       ...:     M = update_multiplier(A, B)
       ...:     while M > 1:
       ...:         u, v = A % M, B % M
       ...:         assert -M // 2 <= u
       ...:         assert v <= M // 2
       ...:         assert (u**2 + v**2) % M == 0
       ...:
       ...:         r = (u**2 + v**2) // M
       ...:         A, B = (u*A + v*B) // M, (v*A - u*B) // M
       ...:         assert A**2 + B**2 == r * p
       ...:         M = update_multiplier(A, B)
       ...:
       ...:     return A, B
       ...:

  In [335]: descent_method(387, 1, 881)
  Out[335]: (25, 16)

  In [336]: descent_method(557, 55, 12049)
  Out[336]: (105, 32)
  ```
* 2 平方和定理の中途半端な素因数分解 $m = p_1 p_2 \dotsm p_r M$ がおもしろい。
* 練習問題 27.7. が降下法の一般バージョンの実装。素因数分解、平方和定理、先の恒等式の多重展開を組み込めばできる。
* 平方三角数の問題「組 $(m, n)$ が平方三角数ならば組 $(1 + \underline{\quad} m + \underline{\quad} n,\ 1 + \underline{\quad} m + \underline{\quad} n)$ もまた平方三角数である」で数時間悩む。
