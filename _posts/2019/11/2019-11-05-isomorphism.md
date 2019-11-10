---
title: 群の同型定理復習ノート
tags: math
---

同型定理三兄弟の復習をする。

# 同型定理

正規部分群は、ある群から別の群への準同型写像の核で表される。基本。

$G, G^\prime$ を群とし、$H \triangleleft G$ を正規部分群とする。
自然な射影 $\pi\colon G \longrightarrow G/H$ の核 $\ker \pi$ は準同型写像
$f\colon G \longrightarrow G^\prime$ の核 $\ker f$ の部分集合である：
$\ker\pi \subset \ker f.$ これも基本。

## 第一定理

$$
G/\ker f \cong \operatorname{im} f.
$$

上述の基本的命題から直ちに証明できる。

## 第二定理

ここでは $H$ は（単なる）部分群、$K \triangleleft G$ は正規部分群とする。

$$
H/H \cap K \cong KH/K.
$$

$f\colon H \rightarrow HK \rightarrow HK/K$ をとり、
$\pi\colon H \longrightarrow H/K$ について第一同型定理を適用すると証明できる。

* これの応用が $S_3/S_3 \cap V_4 = S_3 \cong S_4/V_4.$
  $S_n$ は対称群、$V_4$ は Klein の四元群。

## 第三定理

$H \triangleleft G$, $K \triangleleft G$ かつ $K \subset H$ とする。

$$
(G/K)/(H/K) \cong G/H.
$$

これは $f\colon G/K \longrightarrow G/H$ を恒等写像（全射準同型）とみなして、
$\pi\colon G/K \longrightarrow (G/K)/(\ker f)$ に対して $\ker f = H/K$ を示せば証明が終わる。
