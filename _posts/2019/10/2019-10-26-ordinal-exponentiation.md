---
title: 順序数のべき乗復習ノート
tags: math
---

順序論の復習。順序数のべき乗を定義し、その各種性質を証明する。

# 定義

$\alpha, \beta$ を順序数とする。べき乗 $\alpha^\beta$ を定義する。

## 写像の集合による定義

$\alpha, \beta$ に対応する整列集合 $(A, \prec_A), (B, \prec_B)$ を次のようにとる：

$$
\def\ord{\operatorname{ord} }
\ord(A, \prec_A) = \alpha,\quad
\ord(B, \prec_B) = \beta.\quad
$$

$B$ から $A$ への写像の集合 $F$ を次のようにとる：

$$
F = \{f\,|\, f \in \operatorname{Map}(B, A),\; \forall b(b \in B \implies f(b) \ne \min A)\}.
$$

$F$ 上の二項関係 $\prec_F$ を次のように定義する：

$$
f \prec_F g \iff f \ne g \land (b = \max\{b\,|\, b \in B \land f(b) \ne g(b)\} \implies f(b) \prec_A g(b)).
$$

これは順序関係になる（練習問題）。こうして整列集合 $(F, \prec_F)$ を得る。
この整列集合は $A, B$ のとり方によらず一意的に定まる（練習問題）。

この整列集合の順序数をもって $\alpha$ の $\beta$ 乗を定義し、$\alpha^\beta$ で表す：

$$
\alpha^\beta \coloneqq \operatorname{ord}(F, \prec_F).
$$

## 超限帰納法による定義

$$
\alpha^\beta = \begin{cases}
0, & \alpha = 0,\ \beta \ne 0,\\
1, & \alpha = \beta = 0,\\
1, & \alpha \ne 0,\ \beta = 0,\\
\alpha^\gamma \cdot \alpha, & \alpha \ne 0,\ \gamma = \beta^+,\\
\displaystyle \bigcup_{\gamma \in \beta}\alpha^\gamma, & \alpha \ne 0,\ \beta : \text{limit ordinal}.
\end{cases}
$$

* コメント：$\alpha = 0$ が特別扱い。

# 性質

## どちらも有限順序数ならば $\alpha^\beta$ は自然数のべきに一致する

順序数のべき乗を写像集合で定義する流儀だと、順序数に対応する集合の要素数のべき乗に一致するから成り立つ。

超限帰納法で定義する流儀でも明らかに正しい。

## $0^0 = 1$

順序数のべき乗を写像集合で定義する流儀だと、写像 $\varnothing \longrightarrow \varnothing$ が $\varnothing$ 一つしかないので
$0^0 = 1$ と解釈する必要がある。

順序数のべき乗を超限帰納法で定義する流儀では、この性質は定義の一部だ。

## $0 \lt \beta \implies 0^\beta = 0$

順序数のべき乗を写像集合で定義する流儀だと、空集合でない整列集合 $(B, \prec_B)$ から空集合への写像は一つもないので、こうなる。

順序数のべき乗を超限帰納法で定義する流儀では、この性質は定義の一部だ。

## $\alpha^0 = 1$

順序数のべき乗を写像集合で定義する流儀の場合。空集合から任意の整列集合 $(A, \prec_A)$ への写像はちょうど一つ存在することになっている
(vaculous truth) ことから、$\alpha^0 = 1$ とする。

順序数のべき乗を超限帰納法で定義する流儀では、この性質は定義の一部だ。

## $\alpha^{\beta^+} = \alpha^\beta \cdot \alpha$

**証明**：乗法の性質を利用して超限帰納法で証明される。

**帰納法の基点**：$\beta = 0$ のとき、先述の性質を利用すれば：

$$
\begin{aligned}
\alpha^{\beta^+} &= \alpha^1 = \alpha.\\
\alpha^\beta \cdot \alpha &= \alpha^0 \cdot \alpha\\
&= 1\cdot\alpha = \alpha.
\end{aligned}
$$

両辺ともに値は $\alpha$ に等しい。よって $\beta = 0$ のとき成り立つ。

**帰納的段階**：表題の等式が成り立つと仮定すると、$\gamma \coloneqq \beta^+$ とおいて：

$$
\begin{aligned}
    \alpha^{\gamma^+} &= \alpha^\gamma \cdot \alpha\\
    &= (\alpha^\beta \cdot \alpha) \cdot \alpha\\
    &= \alpha^{\beta^+} \cdot \alpha\\
    &= \alpha^\gamma \cdot \alpha.
\end{aligned}
$$

ゆえに $\gamma$ に対して成り立つ等式が $\gamma^+$ に対しても成り立つことが示された。

**極限順序数の場合**：$\beta$ を極限順序数とする。帰納法の仮定から：

$$
\forall b(b \in \beta \implies \alpha^{b^+} = \alpha^b\cdot\alpha).
$$

したがって

$$
\begin{aligned}
    \bigcup_{b \in \beta}\alpha^{b^+} &= \bigcup_{b \in \beta}(\alpha^b\cdot\alpha).\\
\end{aligned}
$$

この左辺と右辺はそれぞれ指数が極限順序数のときのべき乗の定義と帰納法の仮定から次のように書けるので、極限順序数の場合についても成り立つ。

$$
\begin{aligned}
\bigcup_{b \in \beta}\alpha^{b^+} &= \bigcup_{b \in \beta^+}\alpha^b = \alpha^{\beta^+}.\\
\bigcup_{b \in \beta}(\alpha^b\cdot\alpha) &= \bigcup_{b \in \beta}\alpha^{b^+}.
\end{aligned}
$$

## 指数が極限順序数のべきは $\sup$ で与えられる

$0 \lt \alpha$ で $\gamma$ が極限順序数のとき、

$$
\alpha^\gamma = \sup\{ \alpha^\beta \,\mid\, \beta \lt \gamma \}.
$$

**証明**：次の通り？：

$$
\begin{aligned}
    \alpha^\gamma
    &= \bigcup_{\beta \in \gamma}\alpha^\beta\\
    &= \bigcup_{\beta \lt \gamma}\alpha^\beta\\
    &= \sup\{ \alpha^\beta \,\mid\, \beta \lt \gamma \}.
\end{aligned}
$$

## $1 \lt \alpha \implies (\beta \lt \gamma \iff \alpha^\beta \lt \alpha^\gamma)$

**証明（十分条件）**：$\gamma$ に関する超限帰納法で証明する。

**帰納法の基点**：$\beta < 0$ は空集合の定義に矛盾する。よって $\gamma = 0$ のとき正しい。

**帰納的段階**：$\beta \lt \gamma \implies \alpha^\beta \lt \alpha^\gamma$ を仮定する。
このとき $\beta \le \gamma^+ \implies \beta = \gamma \lor \beta \lt \gamma.$

----

$\alpha^\beta \lt \alpha^\beta \cdot \alpha$ であることから
$\alpha^\beta \lt \alpha^{\beta^+}$ が成り立つことを以下で利用する。

----

$(1)$ $\beta = \gamma$ のときは $\alpha^\beta \lt \alpha^{\gamma^+}.$

$(2)$ $\beta \lt \gamma$ のときは帰納法の仮定と上記事実を利用して：
$\alpha^\beta \lt \alpha^\gamma \lt \alpha^{\gamma^+}.$

$(1)$, $(2)$ いずれの場合でも帰納的段階は正しい。

**極限順序数の場合**：示すべきことは次の命題だ：

$$
\forall c(c \in \gamma \land \beta \lt c \implies \alpha^\beta \lt \alpha^c).
$$

任意の $\beta \lt \gamma$ をとる。極限順序数の性質から

$$
\exists c(c \in \gamma \land \beta \lt c).
$$

帰納法の仮定により $\alpha^\beta \lt \alpha^c.$ $c \in \gamma$ であるので：

$$
\begin{aligned}
\alpha^\beta \lt \alpha^c \le \bigcup_{c \in \gamma}\alpha^c = \alpha^\gamma.
\end{aligned}
$$

これにより極限順序数の場合にも成り立つことが示された。

**証明（必要条件）**：
十分条件の証明で示されたのは $\beta \lt \gamma \implies \alpha^\beta \lt \alpha^\gamma$ だ。
これは $\beta \in \gamma \implies \alpha^\beta \in \alpha^\gamma$ と同値だ。
特に次が言える： $\beta = \gamma \implies \alpha^\beta = \alpha^\gamma.$
$\in$ が強順序であることから $\beta \notin \gamma \implies \alpha^\beta \notin \alpha^\gamma.$
これの対偶をとって $\in$ を $\lt$ とすれば必要条件が示されたことになる。

## $\beta \le \gamma \implies \beta^\alpha \le \gamma^\alpha$

**証明**：$\alpha$ に関する超限帰納法で証明する。

**帰納法の基点**：$\alpha = 0$ のときは $\beta^0 = 1$, $\gamma^0 = 1$ となり
与えられた不等式は等号が成立することで正しい。

**帰納的段階**：与えられた不等式が成立するとき、$\alpha$ を $\alpha^+$ に置き換えた不等式に対しても成り立つことを示す。

$$
\begin{aligned}
\beta^{\alpha^+} &= \beta^\alpha \cdot \beta\\
&\le \beta^\alpha \cdot \gamma && \because \beta \le \gamma\\
&\le \gamma^\alpha \cdot \gamma && \because \text{induction}\\
&= \gamma^{\alpha^+}.
\end{aligned}
$$

よって $\beta^\alpha \le \gamma^\alpha \implies \beta^{\alpha^+} \le \gamma^{\alpha^+}$ が示された。

**極限順序数の場合**：示すべきことは極限順序数 $\alpha$ に関する次の不等式だ：

$$
\beta \le \gamma \implies \forall a(a \in \alpha \implies \beta^a \le \gamma^a)
$$

それには次のようにする：

$$
\begin{aligned}
&\phantom{\therefore}\forall a(a \in \alpha \implies \beta^a \subset \gamma^a).\\
&\therefore \bigcup_{a \in \alpha} \beta^a \subset \bigcup_{a \in \alpha}\gamma^a.\\
&\therefore \beta^\alpha \le \gamma^\alpha.
\end{aligned}
$$

これで極限順序数の場合も成り立つことが示された。

* コメント：この性質の注意点は $\beta \lt \gamma \implies \beta^\alpha \le \gamma^\alpha$ にある。
  例えば $2 \lt 3$ に対して $\omega^2 = \omega^3 = \omega$ が成り立つ。

## $\alpha^{\beta + \gamma} = \alpha^\beta\cdot\alpha^\gamma$

**証明**：$\gamma$ についての超限帰納法による。

**帰納法の基点**：すべての $\alpha$ に対して $\alpha^0 = 1.$

$$
\therefore \alpha^\beta \cdot \alpha^0 = \alpha^\beta \cdot 1 = \alpha^\beta = \alpha^{\beta + 0}.
$$

帰納法の基点について与えられた等式は真である。

**帰納的段階**：与えられた等式が成り立つと仮定する。このとき：

$$
\begin{aligned}
\alpha^\beta \cdot \alpha^{\gamma^+}
&= \alpha^\beta \cdot (\alpha^\gamma \cdot \alpha)\\
&= (\alpha^\beta \cdot \alpha^\gamma) \cdot \alpha\\
&= \alpha^{\beta + \gamma} \cdot \alpha\\
&= \alpha^{\beta + \gamma^+}.
\end{aligned}
$$

途中の等号はこれまで示した乗法やべき乗の各性質による。
帰納的段階において、与えられた等式は真である。

**極限順序数の場合**：極限順序数 $\gamma$ に対して次が成り立っていると仮定する：

$$
\forall c(c \in \gamma \implies \alpha^{\beta+c} = \alpha^\beta\cdot\alpha^c).
$$

$c \in \gamma$ であるから：

$$
\begin{aligned}
    \alpha^\beta \cdot \alpha^c &\le \alpha^\beta \cdot \alpha^\gamma.\\
    \therefore \bigcup_{c \in \gamma}(\alpha^\beta \cdot \alpha^c) &\le \alpha^\beta \cdot \alpha^\gamma.\\
\end{aligned}
$$

反対に、$c \in \alpha^\beta \cdot \alpha^\gamma$ に対して：

$$
\exists u\exists v(v \in \gamma \land u \in \alpha^v \land c \in \alpha^\beta \cdot u).
$$

ところだこれだとある $v \in \gamma$ が存在して $u$ を上から押さえていることになる。したがって：

$$
\exists v(v \in \gamma \land c \le \alpha^c \cdot \alpha^v).
$$

順序数に対する上限不等式および帰納法の仮定により：

$$
\tag*{$\spadesuit0$}
\begin{aligned}
\alpha^\beta \cdot \alpha^\gamma
&= \bigcup_{c \in \gamma}(\alpha^\beta \cdot \alpha^c)\\
&= \bigcup_{c \in \gamma}(\alpha^{\beta + c}).
\end{aligned}
$$

$$
\begin{aligned}
&\forall c(c \in z \implies \beta + c \le \beta + \gamma \implies \alpha^{\beta + c} \le \alpha^{\beta + \gamma}).\\
\tag*{$\spadesuit1$}
&\therefore \bigcup_{c \in \gamma}(\alpha^{\beta + c}) \le \alpha^{\beta + \gamma}.
\end{aligned}
$$

反対に、$c \in \alpha^{\beta + \gamma}$ に対して：

$$
\exists u\exists v(v \in \gamma \land u \in \beta + v \land c \in \alpha^u).
$$

それゆえある $v \in \gamma$ が存在して $\beta + v$ が $u$ を上から押さえている。
したがって $\alpha^u \le \alpha^{\beta + v}.$

いつもの順序数に対する上限不等式により：

$$
\tag*{$\spadesuit2$}
\alpha^{\beta + \gamma} \le \bigcup_{c \in \gamma} \alpha^{\beta + c}.
$$

$\spadesuit0, \spadesuit1, \spadesuit2$ より極限順序数 $\gamma$ に対して：

$$
\alpha^{\beta + \gamma} = \alpha^\beta \cdot \alpha^\gamma.
$$

以上で極限順序数の場合について成り立つことが示された。

## $(\alpha^\beta)^\gamma = \alpha^{\beta\cdot\gamma}$

**証明**：超限帰納法による。

**帰納法の基点**：次のように式変形ができることから $\gamma = 0$ のときは正しい。

$$
(\alpha^\beta)^0 = 1 = \alpha^0 = \alpha^{\beta \cdot 0}.
$$

**帰納的段階**：与えられた等式が成り立つと仮定する。このとき

$$
\begin{aligned}
(\alpha^\beta)^{\gamma^+}
&= (\alpha^\beta)^\gamma\cdot(\alpha^\beta)\\
&= \alpha^{\beta\cdot\gamma}\cdot\alpha^\beta\\
&= \alpha^{\beta\cdot\gamma + \beta}\\
&= \alpha^{\beta\cdot\gamma^+}.
\end{aligned}
$$

ゆえに帰納的段階が証明された。

**極限順序数の場合**：$\gamma$ が極限順序数であるとき、次が成り立つこと示す：

$$
\forall c(c \in \gamma \implies (\alpha^\beta)^c = \alpha^{\beta\cdot c}).
$$

任意の順序数 $c \in \gamma$ をとる。このとき：

$$
\begin{aligned}
&\phantom{\therefore}(\alpha^\beta)^c = \alpha^{\beta\cdot c}.\\
&\therefore \bigcup_{c \in \gamma}(\alpha^\beta)^c = \bigcup_{c \in \gamma}\alpha^{\beta\cdot c}.\\
&\therefore (\alpha^\beta)^\gamma = \bigcup_{c \in \gamma}\alpha^{\beta\cdot c}.\\
\end{aligned}
$$

上記右辺が $\alpha^{\beta\cdot\gamma}$ に等しいことを示せば証明は終わる。
$\beta$ による場合分けになる。

$\beta = 0$ のときは問題ない（練習問題）。

$\beta \ne 0$ ならば、$c \in \gamma$ に対する次の不等式に注意する：

$$
\begin{aligned}
     \beta \cdot c \le \beta \cdot \gamma.\\
     \therefore \alpha^{\beta \cdot c} \le \alpha^{\beta \cdot \gamma}.
\end{aligned}
$$

順序数に対する上限不等式により：

$$
\tag*{$\bigstar1$}
\bigcup_{c \in \gamma}\alpha^{\beta \cdot c} \le \alpha^{\beta \cdot \gamma}.
$$

逆に任意の $v \in \beta \cdot \gamma$ について

$$
\exists c(c \in \gamma \land v \in \beta \cdot c).\\
\therefore \alpha^v \le \alpha^{\beta\cdot\gamma}.
$$

再び順序数に対する上限不等式により：

$$
\tag*{$\bigstar2$}
\begin{aligned}
\bigcup_{v \in \beta\cdot\gamma}\alpha^v
&\le \bigcup_{c \in \gamma}\alpha^{\beta\cdot c}\\
&= \alpha^{\beta\cdot\gamma}.
\end{aligned}
$$

$\bigstar1$ と $\bigstar2$ より、極限順序数についても成り立つことが示された。

## $(\beta\cdot\gamma)^\alpha = \beta^\alpha\cdot\gamma^\alpha$ は一般には成り立たない

例えば $\alpha = \gamma = 2, \beta = \gamma$ を考える。
$(\omega \cdot 2)^2 = \omega \cdot 2 \cdot \omega \cdot 2 = \omega^2\cdot2 \ne \omega^2\cdot2^2.$

# 参考資料

* [順序数](https://ja.wikipedia.org/wiki/%E9%A0%86%E5%BA%8F%E6%95%B0#%E5%AE%9A%E7%BE%A9) - Wikipedia
* [Ordinal arithmetic](https://en.wikipedia.org/wiki/Ordinal_arithmetic#Multiplication) - Wikipedia
  * 簡単な概念に対しても例示を与えているので、わかりやすい印象がある。
* [Definition:Ordinal Exponentiation](https://proofwiki.org/wiki/Definition:Ordinal_Exponentiation) - ProofWiki
* [Category:Ordinal Arithmetic](https://proofwiki.org/wiki/Category:Ordinal_Arithmetic) - ProofWiki
  * 証明中に参照した定理をリンク付きで明示してあるのが特徴。こちらでかってに依存グラフを描きたい。

