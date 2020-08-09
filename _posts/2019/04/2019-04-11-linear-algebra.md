---
title: 線形代数の答え合わせ
tags: math python sympy
---

[きのう]({% post_url 2019/04/2019-04-10-diary %})の問題を PC で検証する。

まずべき零行列の問題。インターネットによると Cayley-Hamilton の定理を使って「固有値がすべてゼロであること」を示してから $A^n = O$ を推論するものが多いようだ。
私も試行錯誤してその手順にたどり着いたが、これだとこの教科書的には (3)⇒(1) になる。

二次形式の問題はおそらく誤植。$y^2$ の項の符号を入れ替えると回答例と一致する。

```python
In [12]: from sympy import Matrix, S, factor, symbols

In [15]: x = symbols('x')

In [32]: A = Matrix([[S.One, S.Half], [S.Half, S.One]])

In [34]: B = Matrix([[S.One, S.Half], [S.Half, -S.One]])

In [37]: A.charpoly(x)
Out[37]: PurePoly(x**2 - 2*x + 3/4, x, domain='QQ')

In [38]: B.charpoly(x)
Out[38]: PurePoly(x**2 - 5/4, x, domain='QQ')

In [39]: factor(Out[37])
Out[39]: (2*x - 3)*(2*x - 1)/4

In [40]: factor(Out[38])
Out[40]: (4*x**2 - 5)/4
```

[SymPy](https://docs.sympy.org/) の便利さを再確認できた。
