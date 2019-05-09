---
layout: page
title: 重要地点一覧集
permalink: /locations/
---

このページは東京 23 区をうろつくときに私が知っているべきスポット一覧を集積するものだ。

<ul class="post-list">
  {%- for i in site.locations -%}
  <li>
    <h2><a class="post-link" href="{{ i.url | relative_url }}">{{ i.title | escape }}</a></h2>

    {{ i.excerpt | truncate: 80 }}
  </li>
  {%- endfor -%}
</ul>
