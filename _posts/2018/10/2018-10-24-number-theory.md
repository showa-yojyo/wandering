---
title: 『はじめての数論 原著第 3 版』学習ノート Part 5
tags: math
---

鈴木治郎訳『はじめての数論 原著第 3 版』より。

# 練習問題 8.7. 合同式 $ax \equiv c \pmod{m}$ を解くプログラムを書く

途中の関数 `abxyg` については[144 日目]({{ site.baseurl }}{% post_url 2018/10/2018-10-22-diary %})を参照。

```python
def solve_ax_c_m(a, c, m):
    """Solve $ax \equiv x \pmod{m}$"""

    assert m >= 1

    g = math.gcd(a, m)
    if c % g != 0:
        raise ArithmeticError('Cannot be solved')

    # Solve $ax + my \equiv gcd(a, m)$
    u0, _, _ = abxyg(a, m)
    x0 = c * u0 // g
    #x0 %= m
    return [x0 + k * m // g for k in range(g)]
```

# 練習問題 10.3. Carmichael 数に関する考察

a) $m = 561 = 3 \cdot 11 \cdot 17$ は Carmichael 数であることを示せ。

* 合成数である：OK
* $\gcd(a, 561) = 1 \implies a^{561 - 1} \equiv 1 \pmod{561}$

     $\gcd(a, 3) = 1$ なる $a$ に対して Fermat の小定理より次が成り立つ：

     $$
     a^2 = a^{3-1} \equiv 1 \pmod{3}\\
     $$

     両辺を 280 乗する。

     $$
     a^{561 - 1} = a^{560} = (a^2)^{280} \equiv 1^{280} = 1 \pmod{3}
     $$

     同様にして $p = 11, 17$ について $\gcd(a, p) = 1$ なる $a$ に対して次が成り立つ：

     $$
     \begin{aligned}
     a^{561 - 1} &= a^{560} = (a^{10})^{56} &\equiv &1^{56} = 1 \pmod{11}\\
     a^{561 - 1} &= a^{560} = (a^{16})^{28} &\equiv &1^{28} = 1 \pmod{17}\\
     \end{aligned}
     $$

     これらの合同式から $\gcd(a, 3) = \gcd(a, 11) = \gcd(a, 17) = 1$ なる $a$ に対して
     $a^{561 - 1} \equiv 1 \pmod{561}$ が成り立つので（簡単な計算で確認できる）OK だ。

b) 合成数 $m$ が Carmichael 数であるための必要条件を絞り込む：

* 素因数の個数が奇数ある。
* すべての素因数 $p$ が $p \mid m$ のみならず $(p - 1) \mid (m - 1)$ をも満たす。

   そこで次のようなプログラムを書けばよさそうなことがわかる（素因数分解コードはできあいのものを利用した）：

   ```python
   In [117]: is_carmichael_number??
   Signature: is_carmichael_number(m)
   Docstring: <no docstring>
   Source:
   def is_carmichael_number(m):
       factors = ntheory.factorint(m).keys()
       if len(factors) == 1 or len(factors) % 2 == 0:
           return False
       return not any((m - 1) % (p - 1) for p in factors)
   File:      d:\temp\ipython_edit_kp_lcc20\ipython_edit_das96924.py
   Type:      function

   In [118]: [n for n in range(561, 10000) if is_carmichael_number(n)]
   Out[118]: [561, 1105, 1729, 2465, 2821, 3825, 6525, 6601, 8625, 8911]
   ```
