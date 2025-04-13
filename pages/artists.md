---
layout: page
title: Artists
permalink: /artists/
---
<ul>
  {% assign sortedArtists = site.posts | sort: 'artist' %}
  {% for post in sortedArtists %}
  {% if post.artist %}
    <li>
      {{ post.artist }}: <a href="{{ post.url }}">{{ post.artTitle }}</a>
    </li>
  {% endif %}
  {% endfor %}
</ul>
