---
layout: page
title: 東京 23 区内図書館一覧
---

東京 23 区内にある区立図書館および参考施設の一覧を以下に示す。
訪問済みの図書館については、リンク先の個別ページで、開館スケジュール、営業時間、場所、入場料金などの基礎情報と各図書館の特徴を記述していく。
記載データは訪問直後のものに基づくので、現在のものとは異なる可能性が普通にあることをあらかじめ断っておく。

## 区立図書館一覧

{% assign libraries = site.data.libraries %}
{% assign num_visited = libraries | where: "visited", 1 | size %}

当ブログ責任者は現在 {{ num_visited }} 館を訪問済みだ。

<table>
  <thead>
    <tr>
      <th>図書館</th>
      <th>所在地</th>
      <th style="text-align: center;">訪問済</th>
    </tr>
  </thead>
  <tbody>
{% for i in libraries %}
    <tr>
      <td>
      {%- if i.path -%}
        {% capture path %}{{ i.path | prepend: "libraries/" | append: ".html" | relative_url }}{% endcapture %}
        <a href="{{ path }}">{{ i.area }}{{ i.name }}</a>
      {%- else -%}
        {{ i.area }}{{ i.name }}
      {%- endif -%}
      </td>
      <td>{{ i.address }}</td>
      <td style="text-align: center;">{{ i.visited }}</td>
    </tr>
{% endfor %}
  </tbody>
</table>

## 区立図書館トップページ集

* [千代田区](https://www.library.chiyoda.tokyo.jp/)
* [中央区](https://www.library.city.chuo.tokyo.jp/)
* [港区](https://www.lib.city.minato.tokyo.jp/)
* [新宿区](https://www.library.shinjuku.tokyo.jp/)
* [文京区](https://www.lib.city.bunkyo.tokyo.jp/)
* [台東区](https://www.city.taito.lg.jp/index/library/)
* [墨田区](https://www.library.sumida.tokyo.jp/)
* [江東区](https://www.koto-lib.tokyo.jp/)
* [品川区](https://library.city.shinagawa.tokyo.jp/)
* [目黒区](https://www.meguro-library.jp/)
* [大田区](https://www.lib.city.ota.tokyo.jp/)
* [世田谷区](https://libweb.city.setagaya.tokyo.jp/)
* [渋谷区](https://www.lib.city.shibuya.tokyo.jp/)
* [中野区](https://library.city.tokyo-nakano.lg.jp/)
* [杉並区](https://www.library.city.suginami.tokyo.jp/)
* [豊島区](https://www.library.toshima.tokyo.jp/)
* [北区](https://www.library.city.kita.tokyo.jp/)
* [荒川区](https://www.library.city.arakawa.tokyo.jp/)
* [板橋区](https://www.lib.city.itabashi.tokyo.jp/)
* [練馬区](https://www.lib.nerima.tokyo.jp/)
* [足立区](https://www.city.adachi.tokyo.jp/chiikibunka/toshokan/)
* [葛飾区](https://www.lib.city.katsushika.lg.jp/)
* [江戸川区](https://www.library.city.edogawa.tokyo.jp/)
