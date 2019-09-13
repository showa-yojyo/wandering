---
title: 『岩波基礎講座 基礎数学 集合と位相』学習ノート Part 13
tags: math
---

彌永昌吉・彌永健一著『岩波基礎講座 基礎数学 9 集合と位相 I』より。
終章に目を通す。

# §ZF 集合論、選出公理、連続体仮説

* (S10) 正則性の公理

  $$
  \forall a(a \ne \varnothing \implies \exists b(b \in a \land a \cup b = \varnothing)).
  $$

  言いたいことは「集合はそれ自身を含むことはできない」だ。
  $x \cap \lbrace x \rbrace = \varnothing \implies x \notin x.$

* Zermelo-Fraenkel の公理系とは、とりあえず本書の (S1) から (S10) を指す。
* 実はこの 10 個は冗長だ。e.g. $\text{(S5)} \land \text{(S6)} \implies \text{(S2)}.$
  他にもこういう導出がある。
* (S6) 分出公理を仮定しないと集合の差 ($\setminus$) を定義することができない。
* Zermelo-Fraenkel の公理系とは、(S1)-(S5), (S7)-(S10) の 9 個を意味するものとする。
* **ZF 集合論の体系**とか、単に **ZF** とか呼ぶのは、ここからさらに (S8) 選出公理を取り除いたものを指す。
  取り除いていないものを **ZFC** と呼ぶ。
* 1938 Gödel:「ZF が無矛盾 $\implies$ (S8) と連続体仮説が無矛盾」を証明。
* 1963 P. Cohen: 「ZF が無矛盾 $\implies$ ZF に選出公理を否定したものを合わせた体系が無矛盾」を証明。さらに
* 「ZFC が無矛盾 $\implies$ ZFC に連続体仮説を否定したものを合わせた体系が無矛盾」を証明。
  連続体仮説の正否は ZFC の体系からは独立している。
* 1931 Gödel 不完全性定理「ZF に公理系を付け加えて得られる体系が無矛盾 $\implies$
  次のような論理的命題 $P$ が存在する： $P$ が証明不可能 $\land$ $\lnot P$ が証明不可能」
* ZF 集合論の評価
  * この体系から $\N, \Z, \mathbb{Q}, \R$ を構成できるのだから、一定の妥当性はある。
  * 数学の各種理論への影響力は無視できない。