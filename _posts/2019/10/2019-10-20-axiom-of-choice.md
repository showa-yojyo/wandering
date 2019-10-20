---
title: 整列可能定理を仮定して選出公理を結論する証明のノート
tags: math
---

整列可能定理を仮定して選出公理を結論する証明のノート。

# 選出公理

いろいろな表現で主張されるので、好きなものを挙げておく。

まずもっとも正統な言い回しのものを挙げる：

For any set $E$ of nonempty sets, there exists a choice function $f$ defined on $E$.
* A **choice function** is a function $f$, defined on a collection $E$ of nonempty sets,
  such that for every set $A \in E,\; f(A) \in A$.

論理記号による表現を挙げる（これが書けるようになることは、否定命題を述べることができるようになることと同じだ）：

$$
\forall X(\varnothing \notin E \implies \exists f(f \in \operatorname{Map}(E, \bigcup E)
\forall A(A \in E \implies f(A) \in A))).
$$

* コメント：集合族 $E$ が空集合を含まないとは言っていない。

## 証明

空集合を要素として持たない集合族 $E$ に対する選出関数 $f$ を構成するのに
$E$ の集合全ての和集合をとりそれを $X$ とおく。

[整列可能定理][zermelo]によれば、集合 $X$ を整列集合にできる整列順序が存在する。その一つを $\prec$ とする：
$(X, \prec)$ は整列集合。

各 $S \in E$ に、整列順序 $\prec$（の $S$ への制限）により定まる $S$ の最小元とを関連付ける関数は
$E$ に関する選出関数である。すなわち：

$$
f\colon S \longmapsto \min S.
$$

証明終わり。

* コメント：この証明のポイントは整列可能定理を $S$ に個別に適用しないことだ。

# 参考資料

* [Well-ordering theorem](https://en.wikipedia.org/wiki/Well-ordering_theorem) - Wikipedia: 証明のスケルトンをコンパクトにまとめてある。証明の見通しになる。

[zermelo]: {{ site.baseurl }}{% post_url 2019/10/2019-10-19-zermelo %}
