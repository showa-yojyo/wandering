---
title: 順序数の積復習ノート
tags: math
---

順序論の復習。順序数の積を定義し、その各種性質を証明する。

# 順序数の積
## 定義

$\alpha, \beta$ を順序数とする。積 $\alpha \cdot \beta$ の定義を述べる。

1. $\alpha, \beta$ に対応する整列集合 $(A, \prec_A), (B, \prec_B)$ を次のようにとる：

   $$
   \def\ord{\operatorname{ord} }
   \ord(A, \prec_A) = \alpha,\quad
   \ord(B, \prec_B) = \beta.\quad
   $$

   コメント：$A, B$ のとり方に一意性はない。

2. 整列集合の台集合の直積 $A \times B$ に次のように順序を定義する：

   $$
   (x_1, y_1) \prec_{A \otimes B} (x_2, y_2) \coloneqq
   (y_1 \prec_B y_2)
   \;\lor\;
   ((y_1 = y_2) \land (x_1 \prec_A x_2)).
   $$

   コメント：順序数の和の定義のときと全然異なることに注意。

3. $(A \times B, \prec_{A \otimes B})$ は整列集合になる。これと同型な順序数を席として定義する：

   $$
   \alpha \cdot \beta \coloneqq \operatorname{ord}(A \times B, \prec_{A \otimes B}).
   $$

## 性質

順序数の積に関する性質をいくつか挙げ、それぞれ証明を与える。

### 有限順序数の積は自然数の通常の積に一致する

**証明**：積の定義を直積の順序数としていることと、有限順序数は自然数と順序同型であることから明らか。

### 結合律 $(\alpha \cdot \beta) \cdot \gamma = \alpha \cdot (\beta \cdot \gamma)$

**証明**：$\gamma = \operatorname{ord}(C, \prec_C)$ をみたす整列集合 (C, \prec_C) を一つとる。
左辺は整列集合 $((A \times B) \times C, \prec_{(A \otimes B) \otimes C})$ の順序数である。
順序関係を詳しく調べる：

$$
\begin{aligned}
&\phantom{\iff}((x_1, y_1), z_1) \prec_{(A \otimes B) \otimes C} ((x_2, y_2), z_2)\\
&\iff z_1 \prec_C z_2 \;\lor\; (z_1 = z_2 \land (x_1, y_1) \prec_{A \otimes B} (x_2, y_2))\\
&\iff z_1 \prec_C z_2 \;\lor\; (z_1 = z_2 \land (y_1 \prec_B y_2 \;\lor\; (y_1 = y_2 \;\lor\; (x_1 \prec_A x_2)))).
\end{aligned}
$$

一方、右辺は整列集合 $(A \times (B \times C), \prec_{A \otimes (B \otimes C)})$ の順序数である。
順序数を詳しく調べる：

$$
\begin{aligned}
&\phantom{\iff}(x_1, (y_1, z_1)) \prec_{A \otimes (B \otimes C)} (x_2, (y_2, z_2))\\
&\iff (y_1, z_1) \prec_{B \otimes C} (y_2, z_2) \;\lor\; ((y_1, z_1) = (y_2, z_2) \land x_1 \prec_A x_2)\\
&\iff z_1 \prec_C z_2 \;\lor\; (z_1 = z_2 \land y_1 \prec_B y_2) \;\lor\;
  ((y_1, z_1) = (y_2, z_2) \land x_1 \prec_A x_2).
\end{aligned}
$$

面倒だから書かないが、論理記号 $\land, \lor$ に分配律を適用すれば両者は一致するだろう。

### 零元の存在 $\alpha \cdot 0 = 0 \cdot \alpha = 0$

**証明**：TODO

### $\alpha \cdot \beta^+ = (\alpha \cdot \beta) \cdot \alpha$

**証明**：TODO

### 極限順序数 $\gamma$ について $\alpha\cdot\gamma = \sup(\lbrace \alpha\cdot\beta \mid \beta \lt \gamma\rbrace)$

**証明**：TODO

### 単位元の存在

**証明**：TODO

### $0 \le \alpha$ のとき $\beta \le \gamma \iff \alpha\beta \lt \alpha\gamma$

**証明**：TODO

### $\beta \le \gamma \implies \beta\cdot\alpha \le \gamma\alpha$

**証明**：TODO

### 一般には可換でない

**証明**：反例を一つ挙げる：

$$
2 \cdot \omega \omega \ne \omega \cdot 2.
$$

### 左分配律

**証明**：TODO

### 右分配律は一般には成り立たない

**証明**：TODO

### 任意の順序数 $\alpha$ と順序数 $\delta \ne 0$ に対して $\alpha = \delta\cdot\beta + \gamma$ かつ $\gamma \lt \delta$ をみたす順序数の組 $(\beta, \gamma)$ がただ一組存在する

**証明**：TODO
