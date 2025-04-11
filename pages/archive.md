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
      {{ post.date | date: "%Y-%m-%d" }}: <a href="{{ post.url }}">{{ post.artist }}</a> 
    </li>
    {% else %}
    <li>
      {{ post.date | date: "%Y-%m-%d" }}: <a href="{{ post.url }}">Unknown Artist</a> 
    </li>
    {% endif %}
  {% endfor %}
</ul>

