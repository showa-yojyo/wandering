---
layout: page
title: 訪問済図書館
permalink: /libraries/
---

これまでに私が訪問した図書館のすべてを紹介する。
開館スケジュール、営業時間、場所、入場料金などの基礎情報と各図書館の特徴を記述していく。

<ul class="post-list">
  {%- for lib in site.libraries -%}
  <li><a href="{{ lib.url | relative_url }}">{{ lib.name | default: lib.title }}</a></li>
  {%- endfor -%}
</ul>
