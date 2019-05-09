---
layout: page
title: 東京 23 区内銭湯一覧
---

東京 23 区内で現在営業中の公衆銭湯（入湯料 460 円）の一覧を以下に示す。

東京銭湯（有力サイト）を scraping したデータのように見えてはまずいので、情報を一部デグレードしておく。すなわち、
* 休業日は原則として適用されるものを示す。例えば休業するはずの曜日が祝日の場合、休業日を振り替えたりそうしなかったりするのは店に依る。
* 営業時間は原則として適用されるものを示す。曜日によっては若干の変動がある場合があるので、紙幅の都合上、ここでは代表的な営業時間帯を記すものとする。
* 洗濯はコインランドリーの有無を基本的には示すが、当該銭湯とは無関係のコインランドリーが近所にあって、実際には洗濯ができる場合がある。

{% comment %}休業中の銭湯は除外しておく{% endcomment %}
{%- assign bathhouses = site.data.bathhouses | where: "open", 1 -%}
<table>
  <thead>
    <tr>
      <th>店舗名</th>
      <th>所在地</th>
      <th>休業日</th>
      <th>営業時間</th>
      <th>洗濯</th>
    </tr>
  </thead>
  <tbody>
{% for i in bathhouses %}
    <tr>
      <td>{{ i.name }}</td>
      <td>{{ i.address }}</td>
      <td>{{ i.closed-days | split: "/" | first }}</td>
      <td>{{ i.office-hours | split: "/" | first }}</td>
      <td>{{ i.laundry }}</td>
    </tr>
{% endfor %}
  </tbody>
</table>
