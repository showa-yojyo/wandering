---
title: 体論学習ノート 6 代数的閉体＆閉包編
tags: math
---

Galois 論準備ノート。今回は代数的閉体と閉包を習う。

# 定義
## 代数的閉体、代数的に閉じている (algebraically closed)

**定義**：体 $K$ が**代数的に閉じている**、**代数的閉体である**とは、次の同値の条件を満たすことをいう：

* $(1)$ $K$ の代数的拡大が $K$ 自身しか存在しない
* $(2)$ $K$ 上の既約多項式のいずれも次数が $1$ である
* $(3)$ $K$ 上の多項式のいずれも正の次数の根をもつ

**検討**：
* $\mathbb Q$ には $\R$ という真の代数的拡大があるので代数的に閉じていないことになる。
* $\R$ には $\Complex$ という真の代数的拡大がある。
* $\Complex$ はまさしく代数的に閉じている。

## 代数的閉包 (algebraical closure)

**定義**：体 $K$ の**代数的閉包** $\overline K$ とは、$K$ の代数的拡大体の一つであって代数的閉体であるものをいう。

# 性質
## 代数的閉体の定義すべてが同値である

**証明**：

$(1) \implies (2)\colon$
代数的拡大体が自分自身しかない体 $K$ を仮定する。
$f$ を $K$ 上の既約多項式とする。
$K$ は単項イデアル整域であるので、既約元から生成されたイデアル $(f) \subset K$ を考えるとこれは極大イデアルである。

整域において極大イデアルによる剰余環は体になるので $L \coloneqq K/(f)$ は体である。

まず $L$ が有限体であることを示す。$L$ は $g + (f)$ の形をした要素の集合である。
体上の多項式環は Euclid 整域であるので、任意の $g \in K[X]$ に対してある
$q, r \in K[X]$ が存在して次を満たす：

$$
g(X) = f(X)q(X) + r(X),\;r(X) = 0 \lor 0 \lt \deg r(X) \lt \deg f(X).
$$

したがって $L$ を次の形に書ける：

$$
L = \{ r + (f)\,|\, r \in K[X], \deg r \lt \deg f\}.
$$

多項式環の剰余環の基底に関するある定理（未）により、$L$ の基底は

$$
\langle 1 + (f), X + (f), \dotsc, X^{\deg f - 1} + (f)\rangle
$$

である。したがって $L$ は有限体であることが示された。

次に $[L:K] = 1$ を示す。
有限な代数的拡大体は代数的であるので、$L$ は代数的である。
$K \subset L$ かつ最初の仮定により $K = L.$ すなわち
$[L:K] = 1.$ ゆえに $\deg f = 1.$

以上により $K$ は $(2)$ の意味で代数的に閉じていることが示された。
$\Box$

$(2) \implies (3)\colon$
$K$ 上の任意の既約多項式の次数が 1 ならば
$K$ 上の正の次数をもつ多項式が存在して、その根を持つことを示す。

多項式環 $K[X]$ は体を係数とするので Euclid 整域である。
すなわち一意分解整域であるので、任意の $f(X) \in K[X]$ を次の形に書ける：

$$
f = ug_1\dotsm g_r
$$

ここで $u$ は単元、各 $g_i$ は既約元である。

仮定により $1 = \deg f = \deg(ug_1\dotsb g_r)$ だから $r = 1$ であり因数定理により $g_1$ すなわち
$f$ は $K$ に根を持つ。

したがって $K$ は $(3)$ の意味で代数的に閉じていることが示された。
$\Box$

$(3)\implies(1)\colon$
$K$ を $(3)$ つまり $K[X]$ のどの多項式も正の次数の根をもつと仮定する。
$L/K$ を代数的拡大体とし、$\alpha \in L$ を一つとる。

仮定から $K$ 上の $\alpha$ の最小多項式 $\mu_\alpha$ は根を $K$ に持つ。それを $\beta \in K$ とする。
因数定理によりある $g \in K[X]$ が存在して次を満たす：

$$
\mu_\alpha(X) = (X - \beta)g(X).
$$

最小多項式の性質から $\mu_\alpha$ は既約かつ monic であるから：

$$
\mu_\alpha(X) = X - \beta.
$$

$0 = \mu_\alpha(\alpha) = \alpha - \beta$ より $\alpha = \beta.$
ゆえに $\alpha \in K.$ $\alpha \in L$ は任意であったから $L = K.$
以上により $K$ の代数的拡大体は $K$ 自身であり、$(1)$ の意味で代数的に閉じていることが示された。
$\blacksquare$

## $L/K$ が代数的ならば $L$ の代数的閉包は $K$ のそれに等しい

**定理**：$L/K$ が代数的拡大体ならば $L$ の代数的閉包は $K$ のそれに等しい。

**検討**：$L \supset K$ であることから $\overline L \supset \overline K$ が成り立つ（いちおう示す）。

$\overline L \supsetneq \overline K$ は成り立たない：
$\overline L \supsetneq \overline K$ が成り立つと仮定すると、
$\overline K$ が代数的に閉じている、つまり $K$ の代数的拡大のうち最大であるという性質に矛盾する。

ゆえに $\overline L = \overline K.$

**証明**：TBW

## 体には代数的閉包が存在する

**定理**：体には代数的閉包が存在して一意的に定まる。

**証明**：TBW

## 代数的閉体の部分体 $K$ の代数的閉包は $K$ の代数的閉包

**定理**：代数的閉体 $\Omega$ の部分体 $K$ の代数的閉包は $K$ の代数的閉包である。

**証明**：TBW

## 代数的閉体は無限集合

**定理**：代数的閉体は無限集合である。

**検討**：単純な証明のほうがいい。

**証明**：背理法で示す。代数的閉体 $K \coloneqq \lbrace a_1, \dotsc, a_n \rbrace$ とする。

ここで $f(X) \in K[X]$ を次のようにとる：

$$
f(X) \coloneqq (X - a_1) \dotsb (X - a_n).
$$

すると多項式 $g(X) \coloneqq f(X) + 1 \in K[X]$ には根が $F$ 上に一つもない。
なぜなら任意の $a \in X$ に対して $g(a) = 1 \ne 0$ だからだ。
このような $g$ の存在は $K$ が代数的閉体であることに矛盾する。
したがって $K$ は有限集合ではない。

背理法により、$K$ は任意の代数的閉体だから、一般の代数的閉体は無限集合であることが示された。
$\blacksquare$

# 参考資料

* Proof Wiki
  * [Definition:Algebraically Closed Field](https://proofwiki.org/wiki/Definition:Algebraically_Closed_Field)
  * [Definition:Algebraic Closure](https://proofwiki.org/wiki/Definition:Algebraic_Closure)
  * [Algebraically Closed Field is Infinite](https://proofwiki.org/wiki/Algebraically_Closed_Field_is_Infinite)
* [Show that an algebraically closed field must be infinite.](https://math.stackexchange.com/questions/416764/show-that-an-algebraically-closed-field-must-be-infinite) - Mathematics Stack Exchange
