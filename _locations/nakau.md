---
layout: page
title: 東京 23 区内なか卯店舗一覧
---

筆者が可能な限り朝食（納豆朝定食＋ライス大盛り 300 円）をとる飲食店であるなか卯。東京 23 区内の店舗所在地一覧を記す。
なお、データはブログ執筆期間当時のものであり、現在の状態は正しく表されていないことを断っておく。

{%- assign shops = site.data.nakau -%}
{%- assign num_visited = shops | where: "visited", 1 | size -%}
現在、{{ num_visited }} 軒訪問済み。

<table>
  <thead>
    <tr>
      <th>店舗名</th>
      <th>所在地</th>
      <th>訪問済</th>
    </tr>
  </thead>
  <tbody>
{% for i in shops %}
    <tr>
      <td>{{ i.name }}</td>
      <td>{{ i.address }}</td>
      <td style="text-align: center">{{ i.visited }}</td>
    </tr>
{% endfor %}
  </tbody>
</table>
