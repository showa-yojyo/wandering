---
layout: page
title: 東京 23 区内図書館一覧
---

東京 23 区内にある区立図書館および参考施設の一覧を以下に示す。
訪問済みの図書館については、リンク先の個別ページで、開館スケジュール、営業時間、場所、入場料金などの基礎情報と各図書館の特徴を記述していく。
記載データは訪問直後のものに基づくので、現在のものとは異なる可能性が普通にあることをあらかじめ断っておく。

{%- assign libraries = site.data.libraries -%}
{%- assign num_visited = libraries | where: "visited", 1 | size -%}
現在、{{ num_visited }} 館を訪問済みだ。

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
