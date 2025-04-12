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
      {{ post.date | date: "%Y-%m-%d" }}: <a href="{{ post.url }}">{{ post.artTitle }} by {{ post.artist }} ({{ post.categories[0][0] }})</a> 
    </li>
    {% else %}
    <li>
      {{ post.date | date: "%Y-%m-%d" }}: <a href="{{ post.url }}">{{ post.artTitle }} by Unknown Artist ({{ post.categories[0][0] }})</a> 
    </li>
    {% endif %}
  {% endfor %}
</ul>

