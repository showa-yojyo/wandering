---
layout: page
title: なか卯東京 23 区内店舗一覧
---

筆者が可能な限り朝食（納豆朝定食＋ライス大盛り 300 円）をとる飲食店であるなか卯。東京 23 区内の店舗所在地一覧を記す。2019.2.10 時点。

<table>
  <thead>
    <tr>
      <th>店舗名</th>
      <th>所在地</th>
    </tr>
  </thead>
  <tbody>
{% for i in site.data.nakau %}
    <tr>
      <td>{{ i.name }}</td>
      <td>{{ i.address }}</td>
    </tr>
{% endfor %}
  </tbody>
</table>
