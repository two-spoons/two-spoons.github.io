---
layout: page
title: casting
permalink: /casting/
description: i like talking to my friends about games. you could be that friend. we could build that  parasocial rapport.
nav: true
nav_order: 2
display_categories: [work, fun, nonsense]
horizontal: false
---

<div class="social">
  <div class="contact-icons" style="display: flex; flex-direction: column; align-items: center; gap: 3rem; margin-top: 3rem;">
    <a href="https://www.twitch.tv/twospoonstv" title="Twitch" target="_blank" rel="noopener noreferrer" style="display: flex; flex-direction: column; align-items: center; gap: 0.25rem;">
      <svg class="social-svg-icon" role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="64" height="64"><title>Twitch</title><path fill="currentColor" d="M11.571 4.714h1.715v5.143H11.57zm4.715 0H18v5.143h-1.714zM6 0L1.714 4.286v15.428h5.143V24l4.286-4.286h3.428L22.286 12V0zm14.571 11.143l-3.428 3.428h-3.429l-3 3v-3H6.857V1.714h13.714Z"/></svg>
      <span style="font-size: 1rem;">twitch</span>
    </a>
    <a href="https://discord.gg/YJrpQD2T" title="Discord" target="_blank" rel="noopener noreferrer" style="display: flex; flex-direction: column; align-items: center; gap: 0.25rem;">
      <i class="fa-brands fa-discord"></i>
      <span style="font-size: 1rem;">discord</span>
    </a>
  </div>
</div>

{%comment%}

<!-- pages/projects.md -->
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->

{% assign sorted_projects = site.projects | sort: "importance" %}

  <!-- Generate cards for each project -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>
{%endcomment%}


[twitch]: https://www.twitch.tv/twospoonstv
[discord]: https://discord.gg/YJrpQD2T