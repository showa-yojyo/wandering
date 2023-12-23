---
layout: page
title: 札
---

{%- assign date_format = site.minima.date_format -%}
{% for tag in site.tags %}
  {%- assign name = tag[0] -%}
  * <a href="{{ '/archives/tag/' | append: name | relative_url }}">{{ name }}</a>
{% endfor %}
