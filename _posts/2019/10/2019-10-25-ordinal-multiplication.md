---
title: 順序数の乗法復習ノート
tags: math
---

順序論の復習。順序数の乗法を定義し、その各種性質を証明する。

# 順序数の乗法
## 整列集合の直積に順序を入れることによる定義

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
   (x_1, y_1) \prec_{A \otimes B} (x_2, y_2)\\
   \coloneqq
   (y_1 \prec_B y_2)
   \;\lor\;
   ((y_1 = y_2) \land (x_1 \prec_A x_2)).
   $$

   コメント：順序数の和の定義のときと全然異なることに注意。

3. $(A \times B, \prec_{A \otimes B})$ は整列集合になる。これと同型な順序数を席として定義する：

   $$
   \alpha \cdot \beta \coloneqq \operatorname{ord}(A \times B, \prec_{A \otimes B}).
   $$

## 超限帰納法による定義

$\alpha, \beta$ を順序数とする。順序数の乗法 $\alpha \cdot \beta$ は以下のように超限帰納法を用いて定義される。

### Case 1: 帰納法の基点

$\beta = 0$ のときは積を 0 と定義する：

$$
\alpha \cdot \beta \coloneqq 0.
$$

### Case 2: 帰納的段階

積 $\alpha \cdot \beta^+$ は $\alpha\cdot\beta$ を用いて定義される：

$$
\alpha \cdot \beta^+ \coloneqq (\alpha \cdot \beta) + \alpha.
$$

### Case 3: 極限順序数の場合

$y$ が極限順序数であるときは次のようにして積 $\alpha\cdot\beta$ を定める：

$$
\alpha \cdot \beta \coloneqq \bigcup_{\gamma \in \beta}(\alpha \cdot \gamma).
$$

## 性質

順序数の乗法に関する性質をいくつか挙げ、それぞれ証明を与える。

### 有限順序数の乗法は自然数の通常の積に一致する

**証明**：積の定義を直積の順序数としていることと、有限順序数は自然数と順序同型であることから明らか。

### 結合律 $(\alpha \cdot \beta) \cdot \gamma = \alpha \cdot (\beta \cdot \gamma)$

**直積順序の定義での証明**：$\gamma = \operatorname{ord}(C, \prec_C)$ をみたす整列集合 $(C, \prec_C)$ を一つとる。
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

**超限帰納法による証明**：
* コメント：あらかじめ零元に関する性質と左分配律の証明が終わっている必要がある。

#### Case 1 帰納法の基点

まず $\gamma = 0$ のときに成り立つことを示す。

$$
\begin{aligned}
(\alpha\cdot\beta)\cdot0
&= 0\\
&= \alpha\cdot0\\
&= \alpha\cdot(\beta\cdot0).
\end{aligned}
$$

これで基点ケースが証明された。

#### Case 2 帰納的段階

与えられた等式が $\gamma$ について成り立てば、後続順序数 $\gamma^+$ についても成り立つことを示す：

$$
\begin{aligned}
\alpha\cdot(\beta\cdot\gamma^+)
&= \alpha \cdot (\beta \cdot \gamma + \beta)\\
&= \alpha \cdot (\beta \cdot \gamma) + \alpha\cdot\beta\\
&= (\alpha \cdot \beta)\cdot \gamma + \alpha\cdot\beta\\
&= (\alpha \cdot \beta)\cdot \gamma^+.
\end{aligned}
$$

* コメント：最初の等号と最後の等号は後続順序数に関する積の性質による。
  これが成り立つのは超限帰納法によって順序数の積を定義したことを前提とする証明だからだ。

#### Case 3 極限順序数の場合

$\gamma$ が極限順序数のとき成り立つことを、つまり次の命題を示す：

$$
\forall c(z \in \gamma \implies
(\alpha \cdot \beta) \cdot c = \alpha \cdot (\beta \cdot c)).
$$

そのためにさらに場合分けをする。$\beta = 0$ の場合と $\beta \ne 0$ の場合になる。
前者の証明は上述の Case 1 と同様なものになる（省略）。
後者の証明を以下で述べる。

$\beta \ne 0$ ならば $\beta \cdot \gamma$ は極限順序数だ。

次の二つの等式が成り立つ：

$$
\begin{aligned}
\alpha\cdot(\beta\cdot\gamma) &= \bigcup_{u \lt \beta\cdot\gamma} (\alpha\cdot u).\\
(\alpha\cdot\beta)\cdot\gamma &= \bigcup_{w \lt \gamma} (\alpha\cdot\beta)\cdot w.
\end{aligned}
$$

$u \lt \beta\cdot\gamma$ のとき $\exists w(w \in \gamma \land u \lt \beta \cdot w).$
これを用いて：

$$
\begin{aligned}
\alpha \cdot u
&\le \alpha \cdot (\beta \cdot w)\\
&= (\alpha \cdot \beta) \cdot w\\
&\le (\alpha \cdot \beta) \cdot \gamma.
\end{aligned}
$$

ここで等号は帰納法の仮定による。この結果をすべての $u \in \beta \cdot \gamma$ に一般化する。
順序数に対する上限不等式により：

$$
\tag*{$\spadesuit1$}
\alpha \cdot (\beta \cdot \gamma) \le (\alpha \cdot \beta) \cdot \gamma.
$$

次に逆向きの不等式を証明する。任意の $w \in \gamma$ をとる。いきなり帰納法の仮定が使えて：

$$
\begin{aligned}
  (\alpha\cdot\beta)\cdot w = \alpha\cdot(\beta\cdot w) \le \alpha\cdot(\beta\cdot\gamma).
\end{aligned}
$$

再び順序数に対する上限不等式の性質により：

$$
\tag*{$\spadesuit2$}
(\alpha\cdot\beta)\cdot\gamma \le \alpha\cdot(\beta\cdot\gamma).
$$

$\spadesuit1, \spadesuit2$ より $(\alpha\cdot\beta)\cdot\gamma = \alpha\cdot(\beta\cdot\gamma).$
以上で極限順序数の場合が証明された。

### 零元の存在 $\alpha \cdot 0 = 0 \cdot \alpha = 0$

**直積順序の定義での証明**：$0 = \operatorname{ord}(\varnothing, \prec_0)$ とする。

$$
\def\ord{ \operatorname{ord} }
\alpha \cdot 0 = \ord(A \times \varnothing, \prec_{A \otimes 0}) = \ord(\varnothing, \prec_{0}) = 0,\\
0 \cdot \alpha = \ord(\varnothing \times A, \prec_{0 \otimes A}) = \ord(\varnothing, \prec_{0}) = 0.
$$

つまり、空集合と任意集合との直積が空集合になる性質から導かれる。

### 後続順序数との積 $\alpha \cdot \beta^+ = (\alpha \cdot \beta) + \alpha$

**証明**：
$$
\def\ord{ \operatorname{ord} }
\begin{aligned}
\alpha \cdot \beta^+ &= \ord(A \times B^+, \prec_{A \otimes B^+})\\
&= \ord(A \times (B \cup \{B\}), \prec_{A \otimes B^+})\\
&= \ord((A \times B) \cup (A \times \{B\}), \prec_{A \otimes B^+})\\
&= \ord(A \times B, \prec_{A \otimes B}) + \ord(A \times \{B\}, \prec_{A \otimes \{B\}})\\
&= \alpha \cdot \beta + \alpha.
\end{aligned}
$$

4 つのめ等号で $\cup$ を $+$ にするところは $A \times B \cap A \times \lbrace B\rbrace = \varnothing$ から成り立つ。
さらに、例えば $\prec_{A \otimes B^+}\mid_{A \times B} = \prec_{A \otimes B}$ などを用いた。

### 極限順序数 $\gamma$ について $\alpha\cdot\gamma = \sup\lbrace \alpha\cdot\beta \mid \beta \lt \gamma\rbrace$

**直積順序による証明**：$\gamma = \bigcup_{c \in \gamma} c$ であるから、

$\gamma = \sup\lbrace \beta \,\mid\, \beta < \gamma\rbrace$

**超限帰納法による証明**：乗法の定義を超限帰納法で与える流儀では、この性質は乗法の定義の一部だ。

### 単位元の存在 $\alpha\cdot1 = 1\cdot\alpha = \alpha$

**直積順序による証明**：$1 = \operatorname{ord}(\lbrace \varnothing \rbrace, \prec_1)$ とおく。

$$
\begin{aligned}
\def\ord{\operatorname{ord} }
\def\first{ \lbrace \varnothing \rbrace }
\alpha\cdot1 &= \ord(A \times \first, \prec_{A \otimes 1})\\
&= \ord(A, \prec_A) & \because A \simeq A \times \first\\
&= \alpha.\\
1\cdot\alpha &= \ord(\first \times A, \prec_{1 \otimes A})\\
&= \ord(A, \prec_A) & \because A \simeq \first \times A\\
&= \alpha.
\end{aligned}
$$

ゆえに $\alpha\cdot1 = 1\cdot\alpha = \alpha.$

### $0 \lt \alpha$ のとき $\beta \lt \gamma \iff \alpha\cdot\beta \lt \alpha\cdot\gamma$

**証明**：仮定から $\alpha$ は空集合の順序数ではない。したがって：

$$
\begin{aligned}
\beta \lt \gamma
\iff \beta \in \gamma
\iff \alpha \times \beta \in \alpha \times \gamma
\iff \alpha \cdot \beta \lt \alpha \cdot \gamma.
\end{aligned}
$$

### $\beta \le \gamma \implies \beta\cdot\alpha \le \gamma\cdot\alpha$

**証明**：$\beta = \gamma$ のときは右辺は等号が成り立つ。

$\beta \lt \gamma$ のときは

$$
\begin{aligned}
\beta \lt \gamma
\iff \beta \in \gamma
\implies \beta \times \alpha \in \gamma \times \alpha
\iff \beta \cdot \alpha \lt \gamma \cdot \alpha.
\end{aligned}
$$

### 交換律は一般には成り立たない

**証明**：反例を一つ挙げる：

$$
2 \cdot \omega = \omega \ne \omega \cdot 2.
$$

### 左分配律 $\alpha\cdot(\beta+\gamma)=\alpha\cdot\beta+\alpha\cdot\gamma$

**超限帰納法による証明**

#### Case 1 帰納法の基点

$\gamma = 0$ のとき成り立つことを示す。

$$
\begin{aligned}
\alpha \cdot (\beta + 0) &= \alpha \cdot \beta.\\
\alpha \cdot \beta + \alpha \cdot 0 &= \alpha \cdot \beta.
\end{aligned}
$$

ゆえに両辺は等しい。

#### Case 2 帰納的段階

$\alpha\cdot(\beta+\gamma)=\alpha\cdot\beta+\alpha\cdot\gamma$ が成り立つと仮定する。
このとき $\gamma$ を $\gamma^+$ で置き換えても成り立つことが示されれば、超限帰納法によりすべての $\gamma$ について左分配律が成り立つことになる。

$$
\begin{aligned}
\alpha\cdot(\beta+\gamma^+)
&= \alpha\cdot(\beta+\gamma)^+\\
&= \alpha\cdot(\beta+\gamma) + \alpha\\
&= \alpha\cdot\beta + \alpha\cdot\gamma + \alpha\\
&= \alpha\cdot\beta + \alpha\cdot\gamma^+.
\end{aligned}
$$

最初の等号は順序数の和の性質による（前のノート参照）。
二番目の等号は前述の性質による。
三番目の等号は超限帰納法の仮定による。
最後の等号は再び前述の性質と和の結合律による。

#### Case 3 極限順序数の場合

$\alpha = 0$ の場合とそうでない場合とで分けて証明する。
$\alpha = 0$ ならば：

$$
\alpha\cdot(\beta + \gamma) = 0 = 0 + 0 = 0\cdot\beta + 0\cdot\gamma.
$$

と書けるので成り立つ。

以下 $\alpha \ne 0$ の場合を示す。$\gamma$ が極限順序数であるので
和 $\beta + \gamma$ も積 $\beta \cdot \gamma$ もどちらも極限順序数となる。
示すべき等式の左辺と右辺をそれぞれ定義に従って書き換えると：

$$
\begin{aligned}
  \alpha\cdot(\beta + \gamma) &= \bigcup_{w \in \beta + \gamma}(\alpha \cdot w).\\
  \alpha\cdot\beta + \alpha\cdot\gamma &= \bigcup_{v \in \alpha\cdot\gamma} \alpha\cdot\beta + v.
\end{aligned}
$$

$w \in \beta + \gamma$ を一つとる。順序数の性質から次が成り立つ：

$$
w \in \beta \;\lor\; (w \subset y \;\land\; w \in \beta + \gamma)
$$

このとき $\exists u(u \in \gamma \ \land\ w \in \beta \ \lor\ w = \beta + u).$

$w \in \beta$ の場合は $\alpha\cdot w \in \alpha\cdot\beta \subset \alpha\cdot\beta + v.$

$w = \beta + \gamma$ の場合は帰納法の仮定を使って $\alpha\cdot w = \alpha\cdot(\beta + u) = \alpha\cdot\beta + \alpha\cdot u.$
この第二項は： $\alpha \cdot u \in \alpha \cdot \gamma = \alpha\cdot\beta + v.$

したがって順序数に対する上限不等式により：

$$
\tag*{$\clubsuit1$}
\alpha\cdot(\beta+\gamma) \subset \alpha\cdot\beta + \alpha\cdot\gamma.
$$

以下、逆向きの包含関係を示す。

$$
\forall v \exists w(v \in \alpha\cdot\gamma \implies (w \in \gamma \;\land\; v \in \alpha\cdot w)).\\
\begin{aligned}
  \therefore \alpha \cdot \beta + v
  &\le \alpha \cdot \beta + \alpha \cdot w\\
  &= \alpha \cdot(\beta + w).
\end{aligned}
$$

* コメント：最初の不等号は両辺それぞれ左から $\alpha + \beta$ を加えたことから。次の等号は帰納法の仮定から。

再び順序数に対する上限不等式により：

$$
\tag*{$\clubsuit2$}
\begin{aligned}
\bigcup_{v \in \alpha\cdot\gamma} (\alpha \cdot \beta + v)
&\subset \bigcup_{w \in \gamma}\alpha \cdot(\beta + w).\\
\therefore \alpha\cdot\beta + \alpha\cdot\gamma &\subset \alpha \cdot (\beta + \gamma).
\end{aligned}
$$

$\clubsuit1, \clubsuit2$ より $\alpha\cdot\beta + \alpha\cdot\gamma = \alpha \cdot (\beta + \gamma).$
以上により極限順序数の場合が成り立つことが示された。


### 右分配律は一般には成り立たない

**証明**：$(\beta + \gamma) \cdot \alpha \ne \beta\cdot\alpha + \gamma\cdot\alpha$ なる $\alpha, \beta, \gamma$ として
$\alpha = \omega, \beta = 1, \gamma = 1$ を反例として挙げる。

$$
\begin{aligned}
(\beta + \gamma) \cdot \alpha
&= (1 + 1) \cdot \omega\\
&= 2 \cdot \omega\\
&= \omega.\\
\beta\cdot\alpha + \gamma\cdot\alpha
&= 1\cdot\omega + 1\cdot\omega\\
&= \omega + \omega.
\end{aligned}
$$

### 任意の順序数 $\alpha$ と順序数 $\delta \ne 0$ に対して $\alpha = \delta\cdot\beta + \gamma$ かつ $\gamma \lt \delta$ をみたす順序数の組 $(\beta, \gamma)$ がただ一組存在する

**証明**：
順序数の性質から $\alpha \lt \delta$ または $\delta \le \alpha$ のどちらか一方のみが成り立つ。

$\alpha \lt \delta$ ならば $(\delta, \gamma) = (\alpha, 0).$
$\delta \ne 0$ より順序関係 $\gamma = 0 \lt \delta$ も成り立っている。

$\delta \le \alpha$ の場合、$\beta = \bigcup \lbrace v\,\mid\,\delta \cdot v \le \alpha\rbrace$ とおく。
$\gamma$ を $\delta\cdot\beta + u = \alpha$ を満たす唯一の $u$ で定義する。
前述の 1 の乗算に関する性質により $1 \le \beta.$

* コメント：上のパラグラフの最後がわからない。

順序数の和集合は最小上界であるので、$\beta$ が $\bigcup \lbrace v\,\mid\,\delta \cdot v \le \alpha\rbrace$ の最小上界である。
任意の $u \in \beta$ をとる。このときある $\delta \cdot v \le \alpha$ に対して $u \in v$ が存在する。
ところが、Membership is Left Compatible with Ordinal Multiplication より、
$\delta \cdot u \le \alpha$ が成り立つ。
すなわち $\beta$ は順序数のクラスの推移的部分集合であるから、順序数である。

$\beta \ne 0$ より、極限順序数の定義によりある $u$ に対して $\beta = u^+$ か、
または $\beta$ が極限順序数であるかのどちらかが成り立つ。

* コメント：上の一行はたいしたことを言っていない。

$\beta = u^+$ を仮定する。$u < \beta \land \delta\cdot u \le \alpha.$
その上さらに、ある $\delta \cdot v \lt \alpha$ について $u \lt v.$
これは No Ordinal Between Set and Successor 則により $v \not\lt \beta$ を意味する。
ゆえに $\beta < v.$ ゆえに $\delta \cdot \beta \le \alpha.$

$\beta$ を極限順序数と仮定する。
$\forall u(u \in \beta \implies \delta\cdot u \le \alpha)$
に注意すると：

$$
\begin{aligned}
\delta \cdot \alpha
&= \bigcup_{u \in \beta}(\delta \cdot \beta)\\
&\le \bigcup_{u \in \beta}(\alpha)\\
&= \alpha.
\end{aligned}
$$

以上より、$\beta$ がどちらの順序数のタイプであるにせよ $\delta \cdot \beta \le \alpha.$

その上、$\delta\cdot \beta^+ \le \alpha$ を仮定する。
すると $\beta$ は集合 $\lbrace v \,\mid\, \delta\cdot v \le \alpha\rbrace$ の上界ではなく、矛盾である。

ゆえに（順序数の加法の性質の最後の項目に相当する） Ordinal Subtraction when Possible is Unique より

$$
\exists \gamma(\gamma \in \delta \land \alpha = \delta \cdot \beta + \gamma).
$$

**一意性**：
$\alpha = \delta\cdot\beta_1 + \gamma_1$ かつ $\gamma_1 \lt \delta_1$ および
$\alpha = \delta\cdot\beta_2 + \gamma_2$ かつ $\gamma_2 \lt \delta_2$ を仮定する。

このとき、$\beta = \beta_1, \beta = \beta_2$ の両者に対して次の不等式成り立つ：

$$
\begin{aligned}
\delta\cdot\beta
&\le \alpha\\
&\lt \delta \cdot \beta + \delta \quad \because \gamma \lt \delta\\
&= \delta \cdot \beta^+.
\end{aligned}
$$

つまり $\delta\cdot\beta_1 \lt \delta\cdot\beta_2^+$ と
$\delta\cdot\beta_2 \lt \delta\cdot\beta_1^+$ であるといえる。
再び Membership is Left Compatible with Ordinal Multiplication により
$\beta_1 \lt \beta_2^+ \land \beta_2 \lt \beta_1^+.$
前者と後者はそれぞれ $\beta1 \le \beta_2$, $\beta_2 \le \beta_1$ を意味する。
したがって $\beta_1 = \beta_2.$ ゆえに $\beta$ は一意的に定まる。

$\beta$ が一意的であるので（順序数の加法の性質の最後の項目に相当する）Ordinal Subtraction when Possible is Unique により
$\delta$ は一意的である。

# 参考資料

参考資料第というかカンニングペーパーだ。

* [順序数](https://ja.wikipedia.org/wiki/%E9%A0%86%E5%BA%8F%E6%95%B0#%E5%AE%9A%E7%BE%A9) - Wikipedia
* [Ordinal Multiplication is Left Distributive](https://proofwiki.org/wiki/Ordinal_Multiplication_is_Left_Distributive) - ProofWiki
