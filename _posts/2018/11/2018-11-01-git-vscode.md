---
title: Git の `mergetool` として VS Code を利用する
tags: vscode git
---

Git を利用していてブランチを `merge` または `rebase` した結果、衝突が発生したときのマージツールとして VS Code を利用できる。
その方法の一例は、ファイル `~/.gitconfig` の内容に次のような部分を含めることだ：

```gitconfig
[merge]
    tool = vscode
[mergetool "vscode"]
    cmd = code --wait $MERGED
```

すると例えば次のような編集画面が表示される（画像下部がリポジトリーの内容の移り変わりをある程度は説明しているだろう）。
手動でコードを編集するもよし、画面上部の選択肢をクリックするもよし（これが使えるということは、マージコマンドのオプション指定に工夫ができたことを意味しそうだが）。

![gitconfig mergetool section]({{ "/assets/images/20181101-vscode-mergetool" | relative_url }})
