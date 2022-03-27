---
title: Jekyll ページにおける MathJax コードのマークアップ方法
mathjax: true
tags: jekyll javascript mathjax
---

次のようにして MathJax インライン数式をマークアップしたい。

```text
\( expression \)
```

そのため、私は次のような JavaScript を書いて（詳細は読書ノートを参照して欲しい）
Jekyll ブログの各ページ共通ヘッダーが `script` タグでこれをインクルードするように小細工している。

```javascript
window.MathJax = {
    tex2jax: {
        inlineMath: [['$','$'], ['\\(','\\)']],
        displayMath: [['$$','$$'], ['\\[','\\]']],
        processEscapes: true
    },
    TeX:
    {
        // ...
    }
};
```

しかし、どうしてもドルマークによるマークアップしか MathJax に認識されない。この現象について解決策を考えたい。
オフライン環境でデバッグする以上は、MathJax のソースコードをこの PC に調達する必要があるはずだ。
`git clone` は時間がかかりそうなので敬遠したいが……。
