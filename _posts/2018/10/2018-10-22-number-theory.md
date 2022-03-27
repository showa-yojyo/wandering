---
title: 『はじめての数論 原著第 3 版』学習ノート Part 4
mathjax: true
tags: math
---

鈴木治郎訳『はじめての数論 原著第 3 版』より。

『はじめての数論』の必修章である 1-11 章を読み直す。$\gcd(a, b) = 1$ を利用した証明問題が私は苦手のようだ。
とにかく $ax + by = 1$ を満たす整数 $x, y$ があるので、この等式を変形して推論するだけなのだが。

$ax + by = \gcd(a, b)$ を解くコードを今書いたのでここに残しておく。関数 `divmod` をきっちり実装したいところだ。

```python
In [4]: abxyg??
Signature: abxyg(a, b)
Source:
def abxyg(a, b):
    """Solve ax + by = gcd(a, b) and return (x, y, gcd(a, b))"""

    def divmod(A, B):
        return A // B, A % B

    x, g, v, w = 1, a, 0, b
    while w != 0:
        q, t = divmod(g, w)
        s = x - v * q
        x, g, v, w = v, w, s, t

    y = (g - a * x) // b
    return x, y, g
File:      d:\temp\ipython_edit_fn43apny\ipython_edit_ei221mk7.py
Type:      function

In [5]: abxyg(105, 121)
Out[5]: (-53, 46, 1)
```
