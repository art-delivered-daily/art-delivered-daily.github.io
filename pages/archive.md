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
      {{ post.date | date: "%Y-%m-%d" }}: <a href="{{ post.url }}">{{ post.artist }} ({{ post.category[0] }})</a> 
    </li>
    {% else %}
    <li>
      {{ post.date | date: "%Y-%m-%d" }}: <a href="{{ post.url }}">Unknown Artist ({{ post.category[0] }})</a> 
    </li>
    {% endif %}
  {% endfor %}
</ul>

