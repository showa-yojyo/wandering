---
layout: page
title: 札
---

{%- assign date_format = site.minima.date_format -%}
{% for tag in site.tags %}
<article>
  {%- assign name = tag[0] -%}
  {%- assign posts = tag[1] -%}
  <h2 id="{{ name }}">{{ name }}</h2>
  <ul class="posts">
    {% for post in posts %}
    <li>
      <span class="post-date">{{ post.date | date: date_format }}</span>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </li>
    {% endfor %}
  </ul>
</article>
{% endfor %}
