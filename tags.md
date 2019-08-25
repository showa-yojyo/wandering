---
layout: page
title: 札
---

{%- assign date_format = site.minima.date_format -%}
{% for tag in site.tags %}
<article>
  <h2>{{ tag[0] }}</h2>
  <ul class="posts">
    {% for post in tag[1] %}
    <li>
      <span class="post-date">{{ post.date | date: date_format }}</span>
      <a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
    </li>
    {% endfor %}
  </ul>
</article>
{% endfor %}
