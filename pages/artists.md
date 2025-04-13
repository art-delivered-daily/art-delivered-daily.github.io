---
layout: page
title: Artists
permalink: /artists/
---
<ul>
  {% assign sortedArtists = site.posts | sort: 'artist' %}
  {% for post in sortedArtists %}
    <li>
      {{ post.artist }}: <a href="{{ post.url }}">{{ post.artTitle }}</a>
    </li>
  {% endfor %}
</ul>
