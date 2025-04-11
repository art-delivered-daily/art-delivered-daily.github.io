---
layout: page
title: Archive
permalink: /archive
---

## Blog Archive

Here is a complete archive of my blog posts chronologically:
<ul>
  {% for post in site.posts %}
    <li>
      {{ post.date | date: "%Y-%m-%d" }}: <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

