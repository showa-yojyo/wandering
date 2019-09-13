---
title: Python と Bash の小ノート
tags: python bash
---

Python の非同期プログラミングの続き。きのう書いたような関数は**ブロック関数である**という。
複数のブロック関数を非同期的に呼び出す方法を探したら、そのものずばりがあった：

* [python - How to use asyncio with existing blocking library? - Stack Overflow][41063331]

  投稿にあるコードを簡素化して実行したところ理想的な挙動を示した。さっそく自作スクリプトに取り込もう。
  このあとは Semaphore を Thread に置き換えて、`YouTube()` のブロッキングダウンロードに `asyncio.sleep()` で重み付けする。
  `pytube` 自身が死んでいる件は後で考える。

* [bash - Calling shell functions with xargs - Stack Overflow][11003418]

  長年困っていた問題が解消された。たとえばクリップボードに YouTube の URL を行方向に並べたテキストがあるとする。
  それを複数個の URL をコマンドライン引数に取る自作シェル関数の `download_mp4` に渡すという場合はこう入力できる：

  ```shell
  bash$ export -f download_mp4
  bash$ getclip | xargs -I {} bash -c "download_mp4 {}"
  ```

[11003418]: https://stackoverflow.com/questions/11003418/calling-shell-functions-with-xargs
[41063331]: https://stackoverflow.com/questions/41063331/how-to-use-asyncio-with-existing-blocking-library
