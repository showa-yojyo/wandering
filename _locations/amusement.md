---
layout: page
title: 東京 23 区内訪問対象ゲーセン一覧
---

私の便宜のために、東京都 23 区内のゲームセンターのうち、遊戯対象となるゲームが稼動している店舗を表に示す。
併せて、各店舗ごとに実際に訪れて遊戯したかどうかを記しておく。

{%- assign shops = site.data.amusement -%}
{%- assign num_visited = shops | where: "visited", 1 | size -%}
現在、{{ num_visited }} 軒訪問済み。

## 対象ゲーセン一覧

図表中の固有名詞は、実際に用いられている表記、正式な呼称から乖離している場合がある。
なお、データはブログ執筆期間当時のものであり、現在の状態は正しく表されていないことを断っておく。

<table>
  <thead>
    <tr>
      <th>店舗名</th>
      <th>所在地</th>
      <th>MFC</th>
      <th>MJAC</th>
      <th>BM</th>
      <th>N</th>
      <th>CR</th>
      <th>訪問済</th>
    </tr>
  </thead>
  <tbody>
{% for i in shops %}
    <tr>
      <td>{{ i.name }}</td>
      <td>{{ i.address }}</td>
      <td style="text-align: center">{{ i.mfc }}</td>
      <td style="text-align: center">{{ i.mjac }}</td>
      <td style="text-align: center">{{ i.beatmania }}</td>
      <td style="text-align: center">{{ i.nostalgia }}</td>
      <td style="text-align: center">{{ i.chronoregalia }}</td>
      <td style="text-align: center">{{ i.visited }}</td>
    </tr>
{% endfor %}
  </tbody>
</table>

## 総評

チェーン店のゲーセンについては特に注意を要しないが、街のゲーセンは見落とさないように気をつけている。
また、ゲーセンではなくてもビデオゲームが稼動しているスペースがあることに最近気づく。
ラウンドワンとまではいかなくても、ボウリング場に併設されたゲームコーナーで音楽ゲームや麻雀ゲームが稼動していることが少なくない。
また、総合スーパーマーケットの入っている建物のゲームコーナーでも音楽ゲームが一通り揃っているということがある。

なお、中央区、港区、文京区はゲーセンがまったく存在しないか、隠れ家的な営業をしていて私の視界に入らない。

## 重要店舗

以下、私が特に重要視する店舗について寸評する。

TODO: いつか書く。
