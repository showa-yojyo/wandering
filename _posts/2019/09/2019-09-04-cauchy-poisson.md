---
title: Caucy と Poisson の各積分公式に関するノート
mathjax: true
tags: math
---

このノートでは Caucy の積分公式の応用手順と Poisson の積分公式の証明を記す。
以下のどこかに間違いがあり、そのことに私が気付くことがあるならば、そのときに限り修正するものとする。

## （基本）Cauchy の積分公式を応用する

先に問題を示す。積分の計算問題だ：

$$
\begin{aligned}
    \text{(1)} &\quad \int_{\lvert z \rvert = 1}\!\frac{\mathrm{e}^{2z}}{(2z + 1)^3}\,\mathrm dz\\
    \text{(2)} &\quad \int_{\lvert z \rvert = 2}\!\frac{\mathrm{e}^z}{z^2 + 1}\,\mathrm dz
\end{aligned}
$$

これらを解くために、Cauchy の積分公式を次のように見ないといけなかった：

$$
\int_{\partial D}\!\frac{f(\zeta)}{(\zeta - z)^n}\,\mathrm d\zeta
= \frac{2\pi i}{(n - 1)!}f^{(n - 1)}(z).
$$

これを頭に叩き込んで (1) を計算する：

$$
\begin{aligned}
    \int_{\lvert z \rvert = 1}\!\frac{\mathrm{e}^{2z}}{(2z + 1)^3}\,\mathrm dz
    &= \frac{1}{8}\int_{\lvert z \rvert = \varepsilon}\!\frac{\mathrm{e}^{2z}}{\left(z + (1/2)\right)^3}\,\mathrm dz.
\end{aligned}
$$

まず $z = -1/2$ で元の被積分関数が正則でないので、積分路を移動した（この理屈はさすがに理解している：
半径 1 の円の内側からある十分小さい半径 $\varepsilon > 0$ の円の内側部分を除いた領域で正則となる。
その領域の境界における積分はゼロになる。このことからの帰結だ）。

ここで $f(z) = \dfrac{1}{8}\mathrm{e}^{2z}$ と見るのが本質的だ。
$f^{\prime\prime}(z) = \dfrac{1}{2}\mathrm{e}^{2z}$ ゆえ：

$$
\begin{aligned}
    \frac{1}{8}\int_{\lvert z \rvert = \varepsilon}\!\frac{\mathrm{e}^{2z}}{\left(z + (1/2)\right)^3}\,\mathrm dz
    &= \frac{2\pi i}{2!}f^{\prime\prime}\!\left(-\frac{1}{2}\right)\\
    &= \frac{\pi i}{2 \mathrm{e}}.
\end{aligned}
$$

(2) もまずは積分経路の調整から行う。$z = \pm i$ で被積分関数の正則性がないので、
十分小さな半径 $\varepsilon$ をとってそれらを中心とする円を描き、それらの線積分の和が元の積分と一致する：

$$
\begin{aligned}
    \int_{\lvert z \rvert = 2}\!\frac{\mathrm{e}^z}{z^2 + 1}\,\mathrm dz
    &= \frac{1}{2i}\left(
        \int_{\lvert z - i \rvert = \varepsilon}\!\frac{\mathrm{e}^z}{z - i}\,\mathrm dz
        - \int_{\lvert z + i \rvert = \varepsilon}\!\frac{\mathrm{e}^z}{z + i}\,\mathrm dz\right)\\
\end{aligned}
$$

書き忘れたが、途中で部分分数展開をした。
括弧内のどちらの項も公式で $f(z) = \mathrm{e}^z$ と当てはめる。
第一項は次のようになる：

$$
\begin{aligned}
    \int_{\lvert z - i \rvert}\!\frac{\mathrm{e}^z}{z - i}\,\mathrm dz
    &= 2\pi i \left.\frac{\mathrm{d}}{\mathrm{d}z}\mathrm{e}^z\right|_{z = i}\\
    &= 2\pi \mathrm{e}^i i.
\end{aligned}
$$

同様に二項目の積分の値は $2\pi \mathrm{e}^{-i} i$ とわかる。よって元の積分の値は：

$$
\begin{aligned}
\frac{1}{2i}(2\pi \mathrm{e}^i i - 2\pi \mathrm{e}^{-i} i)
&= \pi(\mathrm{e}^i - \mathrm{e}^{-i})\\
&= 2\pi \sin 1.
\end{aligned}
$$

## Poisson の積分公式を証明する

Poisson の積分公式とは、だいたい次のようなものだ：

原点を中心とする半径 $R$ の円内で関数 $u(R\cos\theta, R\sin\theta)$ が調和関数ならば、
円内部にある点 $(r\cos\phi, r\sin\phi)\quad(r < R)$ について次が成り立つ：

$$
u(r\cos\phi, R\sin\phi)
= 2\pi\int_0^{2\pi}\frac{R^2 - r^2}{R^2 - 2Rr\cos(\theta - \phi) + r^2}
  u(R\cos\theta, R\sin\theta)\,\mathrm d\theta.
$$

証明：

複素平面に置き換えて考える。対応する円を含む領域において、実部が $u(x, y)$ である正則関数をとりそれを $f(z)$ とする。

また、円周上の点と内部の点をそれぞれ $R\mathrm{e}^{i\theta},\;r \mathrm{e}^{i\phi}$ で表す。

1. Cauchy の積分公式で $z = r \mathrm{e}^{i\phi}$, $\zeta = R\mathrm{e}^{i\theta}$ と置換する。
   $\mathrm d\zeta = iR\mathrm{e}^{i\theta}\,\mathrm d\theta$ ゆえ：

   $$
   \def\zz{ r \mathrm{e}^{i\phi} }
   \def\zzeta{ R\mathrm{e}^{i\theta} }
      f(\zz)
     = \frac{1}{2\pi i}\int_0^{2\pi}\!
       \frac{f(\zzeta)}{\zzeta - \zz} iR\mathrm{e}^{i\theta}\,\mathrm d\theta.
   $$

2. 唐突なようだが、次の等式も成り立つ：

  $$
  \def\zz{ r \mathrm{e}^{i\phi} }
  \def\zzeta{ R\mathrm{e}^{i\theta} }
     0
     = \frac{1}{2\pi i}\int_0^{2\pi}\!
     \cfrac{f(\zzeta)}{\zzeta - \cfrac{R^2}{r}\mathrm{e}^{i\phi}} iR\mathrm{e}^{i\theta}\,\mathrm d\theta.
  $$

  このことは、点 $\dfrac{R^2}{r}\mathrm{e}^{i\phi}$ が積分路である円の外部にあることからいえる。
  わからなければ教科書の回転数の説明を参照。

  3. ここがわかりにくかった。1. の等式から 2. の等式を引けば次が成り立つ：

  $$
  \def\zz{ r \mathrm{e}^{i\phi} }
  \def\zzeta{ R\mathrm{e}^{i\theta} }
  \begin{aligned}
  f(\zz)
  &= \frac{1}{2\pi i}\int_0^{2\pi}\!f(\zzeta)\left(
     \frac{1}{\zzeta - \zz}
     - \cfrac{1}{\zzeta - \cfrac{R^2}{r}\mathrm{e}^{i\phi}}
     \right)iR\mathrm{e}^{i\theta}\,\mathrm d\theta\\
  &= \frac{1}{2\pi}\int_0^{2\pi}\!f(\zzeta)\left(
     \frac{1}{1 - \cfrac{r}{R} \mathrm{e}^{i(\phi - \theta)}}
     - \cfrac{1}{1 - \cfrac{R}{r}\mathrm{e}^{i(\phi - \theta)}}
     \right)\,\mathrm d\theta.
  \end{aligned}
  $$

  括弧の中身を見ていくと：

  $$
  \begin{aligned}
  &\phantom{=}\cfrac{- \cfrac{R}{r}\mathrm{e}^{i(\phi - \theta)} + \cfrac{r}{R} \mathrm{e}^{i(\phi - \theta)}}
       {1 - \cfrac{R}{r}\mathrm{e}^{i(\phi - \theta)} - \cfrac{r}{R} \mathrm{e}^{i(\phi - \theta)} + \mathrm{e}^{2i(\phi - \theta)}}\\
  &= \frac{- R^2\mathrm{e}^{i(\phi - \theta)} + r^2\mathrm{e}^{i(\phi - \theta)}}
       {rR - R^2\mathrm{e}^{i(\phi - \theta)} - r^2\mathrm{e}^{i(\phi - \theta)} + rR\mathrm{e}^{2i(\phi - \theta)}}\\
  &= \frac{- R^2 + r^2}
       {rR\mathrm{e}^{-i(\phi - \theta)} - R^2 - r^2 + rR\mathrm{e}^{i(\phi - \theta)}}\\
  &= \frac{- R^2 + r^2}
       {- R^2 + rR\mathrm{e}^{-i(\phi - \theta)} + rR\mathrm{e}^{i(\phi - \theta)} - r^2}\\
  &= \frac{- R^2 + r^2}
       {- R^2 + 2rR\cos(\phi - \theta) - r^2}.
  \end{aligned}
  $$

  計算に手間取った理由は $\mathrm{e}^{i(\phi - \theta)}$ の処理だった。
  手で書いたときに $\mathrm{e}^{-i(\phi - \theta)}$ を $\mathrm{e}^{i(\theta - \phi)}$
  としてしまい、三角関数への渡りが見えづらくなってしまった。

  4. 最後に実部をとれば所望の等式を得る。
