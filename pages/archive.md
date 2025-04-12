---
layout: default
title: Archive
permalink: /archive
---
<div class="rounded mb-5 hero" style="background: #BFACC8">
  <div class="row align-items-center justify-content-between">
    <div style="text-align:left">
      <h2 class="font-weight-bold mb-4 serif-font">Explore the Archive</h2>
      <p>Below is a complete archive of daily art reverse chronologically:</p>
    </div>
  </div>
</div>

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

