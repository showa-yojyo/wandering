---
title: Orbit-Stabilizer theorem 証明ノート
tags: math
---

コメント：経験上、検索エンジンで当定理を検索するときは上の用語を使うといい。

# 軌道・固定部分群定理（仮）

群 $G$ が空でない集合 $X$ に作用しているとき、任意の $x \in X$ に対して次が成り立つ：

$$
\tag*{$\spadesuit$}
\lvert O(x) \rvert = [G\colon G_x].
$$

## 証明 1

**証明の検討**：
主張の主要部分を検討する：

* 所与：$G \curvearrowright X$
* 所与：$x \in X$
* 目標：$\spadesuit$
  * 目標：写像 $\varphi\colon G \longrightarrow O(x)$ を（自然に）構成する。
  * 目標：写像 $\varphi$ から誘導される写像 $\bar{\varphi}\colon G/G_x \longrightarrow O(x)$ が全単射であることを示す。
    * 目標：写像 $\bar\varphi$ が全射であることを示す。
    * 目標：写像 $\bar\varphi$ が単射であることを示す。

**証明**：
$x\in X$ を固定して、写像 $\varphi\colon G \longrightarrow O(x)$ を次で定義する：

$$
\varphi(g) = g \cdot x.
$$

写像 $\varphi$ は全射である：定義から、$x$ は $G$ の要素すべてにより作用されているから。

次に、$G_x$ は部分群であるので、任意の $g, h \in G$ について次が成り立つ：

$$
\begin{aligned}
g\cdot x = h \cdot x &\iff g^{-1}h \in G_x.\\
\therefore \varphi(g) = \varphi(h) &\iff g^{-1}h \in G_x.\\
\therefore \varphi(g) = \varphi(h) &\iff gG_x = hG_x.
\end{aligned}
$$

ゆえに、well-defined な全単射 $\bar\varphi\colon G/G_x \longrightarrow O(x)$ が
$\bar\varphi(gG_x) = g\cdot x$ により定義可能である。

集合 $G/G_x$ と $O(x)$ の間に全単射が存在することが示されたので
$\spadesuit$ が成り立つ。
$\blacksquare$

## 証明 2

**証明の検討**：
証明 1 の検討を一部変えてみよう：

* 所与：（証明 1 と同様）
* 目標：$\spadesuit$
  * 目標：写像 $\varphi\colon O(x) \longrightarrow G/G_x$ を（自然に）構成する。
  * 目標（以下同様）

**証明**：
$x\in X$ を固定して、写像 $\varphi\colon O(x) \longrightarrow G/G_x$ を次で定義する：

$$
\varphi(g \cdot x) = gG_x.
$$

この写像が well-defined であることを示す。
$g\cdot x = h \cdot x$ を満たす $g, h \in G$ が存在すると仮定する。
このとき：

$$
\begin{aligned}
h^{-1}\cdot g\cdot x &= h^{-1}\cdot h\cdot x = x.\\
\therefore h^{-1}g &\in G_x.
\end{aligned}
$$

ゆえに $gG_x = hG_x.$ 以上により $\varphi$ が well-defined であることが示された。

以下、写像 $\varphi$ が全単射であることを示す。全射、単射の順に示す。

全射であることは $\varphi$ の定義から剰余類 $gG_x$ が $\varphi(g\cdot x)$ に等しいことによる。

次に $\varphi$ が単射であることを示す。
$\varphi(g_1\cdot x) = \varphi(g_2 \cdot x)$ が成り立つ $g_1, g_2 \in G$ が存在すると仮定する。
このとき：

$$
\begin{aligned}
g_1G_x &= g_2G_x.\\
\therefore g_2^{-1}g_1 &\in G_x.
\end{aligned}
$$

$G_x$ は固定部分群であることから：

$$
x = g_2^{-1}g_1 \cdot x.
$$

これを変形していくと：

$$
\begin{aligned}
g_2 \cdot x
&= g_2 \cdot (g_2^{-1}g_1 \cdot x)\\
&= (g_2g_2^{-1}g_1) \cdot x\\
&= g_1\cdot x.\\
\therefore g_2 &= g_1.
\end{aligned}
$$

$\exists g_1 \in G \exists g_2 \in G(\varphi(g_1\cdot x) = \varphi(g_2 \cdot x) \implies g_1 = g_2)$
が示された。したがって $\varphi$ は単射である。


以上により $\varphi$ は全単射であるから（以下証明 1 と同様に）、
集合 $O(X)$ と $G/G_x$ の間に全単射が存在することが示されたので
$\spadesuit$ が成り立つ。
$\blacksquare$

# 参考資料

* 川口周著『代数学入門』
* [Orbit-Stabilizer Theorem](https://proofwiki.org/wiki/Orbit-Stabilizer_Theorem) - ProofWiki
