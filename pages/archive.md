---
layout: page
title: Archive
permalink: /archive
---

Here is a complete archive of daily art reverse chronologically:
<ul>
  {% for post in site.posts %}
    {% if post.artist %}
    <li>
      {{ post.date | date: "%Y-%m-%d" }}: <a href="{{ post.url }}">{{ post.artTitle }}</a> by {{ post.artist }}
    </li>
    {% else %}
    <li>
      {{ post.date | date: "%Y-%m-%d" }}: <a href="{{ post.url }}">{{ post.artTitle }}</a> by Unknown Artist 
    </li>
    {% endif %}
  {% endfor %}
</ul>

