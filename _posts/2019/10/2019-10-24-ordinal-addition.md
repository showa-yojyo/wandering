---
title: 順序数の加法復習ノート
mathjax: true
tags: math
---

順序論の復習。順序数の加法を定義し、その各種性質を証明する。

## 順序数の加法

### 整列集合による定義

$\alpha, \beta$ を順序数とする。和 $\alpha + \beta$ の定義を述べる。

1. $\alpha, \beta$ に対応する整列集合 $(A, \prec_A), (B, \prec_B)$ を次のようにとる：

   $$
   \def\ord{\operatorname{ord} }
   \ord(A, \prec_A) = \alpha,\quad
   \ord(B, \prec_B) = \beta,\quad
   A \cap B = \varnothing.
   $$

2. 直和 $A \cup B$ 上の要素の順序関係 $\prec_{A \oplus B}$ を次で定義する：

   $$
   x \prec_{A \oplus B} y \iff
   x \prec_A y \;\lor\; x \prec_B y \;\lor\; (x, y) \in A \times B.
   $$

   コメント：$A$ と $B$ の役割が反対称であることに注意。

3. 整列集合 $(A \cup B, \prec_{A \oplus B})$ の順序数は
   $(A, \prec_A), (B, \prec_B)$ のとり方に依らず一定である。

   それゆえ次の式の右辺が一意的に定まるので、それを順序数 $\alpha, \beta$ の和
   $\alpha + \beta$ として定義する。

   $$
   \alpha + \beta \coloneqq \operatorname{ord}(A \cup B, \prec_{A \oplus B}).
   $$

### 超限帰納法による定義

超限帰納法で順序数の加法を定義する。

$\alpha, \beta$ を順序数とする。このとき和 $\alpha + \beta$ を
$\beta$ に関する超限帰納法により次の Case 1-3 のように定義する：

#### Case 1: 帰納法の基点

$y = 0$ とする。和 $x + y$ を次で定義する：

$$
\alpha + 0 \coloneqq \alpha.
$$

#### Case 2: 帰納的段階

$\beta$ の後続順序数 $\beta^+$ に対して和 $x + y$ を次で定義する：

$$
\alpha + \beta^+ \coloneqq (\alpha + \beta)^+.
$$

#### Case 3: 極限順序数の場合

$y$ を極限順序数とする。和 $x + y$ を次で定義する：

$$
\alpha + \beta \coloneqq \bigcup_{\gamma \in \beta} \gamma.
$$

### 性質

順序数の加法に関する性質をいくつか挙げ、それぞれ証明を与える。

#### 有限順序数の加法は自然数の和と一致する

**証明**：$\operatorname{ord}()$ を用いた順序数の定義および $A \cap B = \varnothing$ から明らか。

#### 結合律

$$
(\alpha + \beta) + \gamma = \alpha + (\beta + \gamma).
$$

**証明**：$\alpha, \beta, \gamma$ に対応する整列集合をそれぞれ
$(A, \prec_A), (B, \prec_B), (C, \prec_C)$ とおき、
どの台集合同士の交わりをとってもそれぞれ空集合であるようにとる。

$$
\def\ord{\operatorname{ord} }
\begin{aligned}
(\alpha + \beta) + \gamma
&= \ord(A \cup B, \prec_{A \oplus B}) + \ord(C, \prec_C)\\
&= \ord(A \cup B \cup C, \prec_{(A \oplus B) \oplus C}).\\
\alpha + (\beta + \gamma)
&= \ord(A \cup B \cup C, \prec_{A \oplus (B \oplus C)}).\\
\end{aligned}
$$

だから $\prec_{(A \oplus B) \oplus C}$ と $\prec_{A \oplus (B \oplus C)}$ が同じ意味であることを示す。

$$
\begin{aligned}
x \prec_{(A \oplus B) \oplus C} y
&\iff x \prec_{(A \oplus B)} y \;\lor\; x \prec_C y \;\lor\; (x, y) \in (A \cup B) \times C\\
&\iff x \prec_A y \;\lor\; x \prec_B y \;\lor\; (x, y) \in A \times B \;\lor\; \dots.\\
\end{aligned}
$$

$\in$ の条件をみると:

$$
(x \in A \cup B \land y \in C) \;\lor\;(x \in A \land y \in B)\\
\iff (x \in A \land y \in C) \;\lor\; (x \in B \land y \in C) \;\lor\;(x \in A \land y \in B).
$$

この同値関係は $\prec_{A \oplus (B \oplus C)}$ 側を同様に調べることでも導かれる。よって結合則は成り立つ。

#### 零元の存在

$$
\alpha + 0 = 0 + \alpha = \alpha.
$$

**証明**： $\alpha = \operatorname{ord}(A, \prec_A)$ なる整列集合を一つとる。
$0 = \operatorname{ord}(\varnothing, \prec_\varnothing)$ につき左辺の順序数の定義は

$$
x \prec_A y \lor x \prec_\varnothing y \lor (x, y) \in A \times \varnothing
$$

である。実際には空集合の性質からこのうちの $x \prec_A y$ だけが常に成り立つ。
$A \cup \varnothing = A$ ゆえ、$(A \cup \varnothing, \prec_{A \oplus \varnothing}) = (A, \prec_A).$
すなわち順序数 $\alpha$ に等しい。中辺の順序数の定義は次のようになり、やはり
$x \prec_A y$ だけが成り立つ。以下略。

$$
x \prec_\varnothing y \lor x \prec_A y \lor (x, y) \in \varnothing \times A
$$

**超限帰納法による証明**：
ここでは $\alpha + 0 = \alpha$ を和の定義から直ちに言えるとして、$0 + \alpha = \alpha$
がすべての順序数 $\alpha$ に対して成り立つことを超限帰納法によって証明する。

* コメント：後述する性質を前もって証明してある必要がある。

##### Case 1 帰納法の基点

$\alpha = 0$ に対して成り立つことを示す。$0 + 0 = 0.$ これは $0$ の定義から成り立つことがいえる。

##### Case 2 帰納的段階

$0 + \alpha = \alpha$ が成り立つと仮定すると、$0 + \alpha^+ = \alpha^+$ も成り立つことを示す。
右辺から左辺を導く：

$$
\begin{aligned}
\alpha^+ = (0 + \alpha)^+ = 0 + \alpha^+.
\end{aligned}
$$

##### Case 3 極限順序数の場合

最後に $\alpha$ が極限順序数であるときにも成り立つことを示す。
$\alpha$ を極限順序数であると仮定する。すなわち

$$
\forall \beta(\beta \in \alpha \implies 0 + \beta = \beta).
$$

このとき次が成り立つ：

$$
\begin{aligned}
\alpha &= \bigcup_{\beta \in \alpha}\beta\\
&= \bigcup_{\beta \in \alpha}(0 + \beta)\\
&= 0 + \alpha.
\end{aligned}
$$

最後の等号は和の定義による。

#### $\alpha + \beta^+ = (\alpha + \beta)^+$

* コメント：順序数の加法を超限帰納法で定義する流儀では、この性質は定義の一部だ。

**証明**：$\gamma = \alpha + \beta = \operatorname{ord}(A \cup B, \prec_{A \oplus B}).$
とおくと $\gamma^+ = \gamma + 1.$
一方結合律により $\alpha + \beta^+ = \alpha + (\beta + 1) = (\alpha + \beta) + 1 = \gamma + 1 = \gamma^+.$

* コメント：加法の定義が順序数ベースの場合、これは定義の一部である。

#### $\beta \lt \gamma \iff \alpha + \beta \lt \alpha + \gamma$

**証明**：順序数の大小関係は小さい方が大きい方の切片になっていることを意味する。
$A, B, C$ を順序数 $\alpha, \beta, \gamma$ と同型な、互いに素な整列集合とする。
このとき次の同値関係が成り立つ：

$$
\def\ord{ \operatorname{ord} }
\begin{aligned}
    \beta \lt \gamma
    &\iff \ord(B, \prec_B) \lt \ord(C, \prec_C)\\
    &\iff \exists c(c \in C \land B \cong s(c))\\
    &\iff \exists c(c \in A \cup C \land A \cup B \cong A \cup s(c))\\
    &\iff \ord(A \cup B, \prec_{A \oplus B}) \lt \ord(A \cup C, \prec_{A \oplus C})\\
    &\iff \alpha + \beta \lt \alpha + \gamma.
\end{aligned}
$$

#### $\beta \preceq \gamma \implies \beta + \alpha \preceq \gamma + \alpha$

**証明**：直前の性質と同様。

* コメント：なぜ $\iff$ ではなく $\implies$ なのか。

#### 一般には可換でない

**証明**：反例を一つ挙げる：

$$1 + \omega = \omega \ne \omega + 1.$$

#### $\alpha \le \beta \implies \exists \gamma(\alpha + \gamma = \beta)$

**証明**：$\alpha = \operatorname{ord}(A, \prec_A), \beta = \operatorname{ord}(B, \prec_B), A \cap B = \varnothing$ とおく。

Case 1: $\alpha \lt \beta$ ならば $\alpha \in \beta.$
$\exists x(x \in B \land A \cong s(x)).$
したがって $\gamma = \operatorname{ord}(B\setminus s(x)).$

Case 2: $\alpha = \beta$ ならば $\gamma = 0.$

## 参考文献

* [順序数](https://ja.wikipedia.org/wiki/%E9%A0%86%E5%BA%8F%E6%95%B0#%E5%AE%9A%E7%BE%A9) - Wikipedia
* [Category:Ordinal Arithmetic](https://proofwiki.org/wiki/Category:Ordinal_Arithmetic) - ProofWiki
