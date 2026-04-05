---
permalink: /
title:
excerpt: "Weiming Yang"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

<div class="home-hero">
  <h1 class="home-hero__title">Weiming Yang</h1>
  <p class="home-hero__lead">
    I am a researcher working on nonlinear control, underactuated aerial systems, and experimental validation for robotic platforms. My current work focuses on robust control design, trajectory generation, and aggressive maneuvering for unmanned aerial vehicles and flying inverted pendulum systems.
  </p>
  <div class="home-hero__actions">
    <a class="btn btn--primary" href="{{ base_path }}/cv/">CV</a>
    <a class="btn btn--inverse" href="{{ base_path }}/publications/">Publications</a>
    {% if site.author.googlescholar %}<a class="btn btn--light-outline" href="{{ site.author.googlescholar }}">Google Scholar</a>{% endif %}
    {% if site.author.researchgate %}<a class="btn btn--light-outline" href="{{ site.author.researchgate }}">ResearchGate</a>{% endif %}
  </div>
</div>

<section id="about-me" class="home-section">
  <h2>About Me</h2>
  <p>
    I am currently a <strong>Research Fellow at the National University of Singapore</strong>. My work sits at the intersection of <strong>control theory</strong> and <strong>robotics</strong>, with a particular emphasis on systems that are nonlinear, underactuated, and challenging to deploy reliably in real-world environments.
  </p>
  <p>
    My primary interests include <strong>aerial robotic systems</strong>, <strong>robust nonlinear control</strong>, and the full path from mathematical design to experimental deployment. Along the way, I have worked on <strong>flying inverted pendulum platforms</strong>, <strong>quadrotor-based systems</strong>, and <strong>trajectory generation methods for aggressive maneuvers</strong>.
  </p>
  <p>
    My broader goal is to develop <strong>control and planning methods that remain practical beyond simulation</strong>, especially when models are imperfect, actuation is limited, and experiments must work on physical platforms.
  </p>
</section>

<section id="news" class="home-section">
  <h2>News</h2>
  <ul class="home-list">
    <li><strong>2025.10:</strong> Successfully obtained my <strong>Ph.D. degree</strong> from the <strong>University of Macau</strong>.</li>
    <li><strong>2025.11:</strong> Joined the <strong>National University of Singapore</strong> as a <strong>Research Fellow</strong>.</li>
    <li><strong>Service:</strong> Reviewer for <strong>IEEE TASE</strong>, <strong>IEEE RA-L</strong>, <strong>Control Engineering Practice</strong>, and <strong>IEEE TSMC: Systems</strong>.</li>
    <li><strong>2025.12:</strong> Our manuscript titled <em>Trajectory Generation and Extended High-Gain Observers Based Output Feedback Control for an Underactuated Flying Inverted Pendulum</em> has been accepted for publication in <strong>IEEE TASE</strong>.</li>
  </ul>
</section>

<section id="research" class="home-section">
  <h2>Research</h2>
  <div class="research-feature">
    <div class="research-feature__media">
      <img src="{{ base_path }}/images/weiming_yang_profile.jpg" alt="Weiming Yang research profile">
    </div>
    <article class="research-feature__content">
      <h3>Robust Nonlinear Control and Aerial Robotics</h3>
      <p>
        My research centers on nonlinear control design for underactuated aerial systems, especially platforms that must operate under strong coupling, limited actuation, and real-world uncertainties.
      </p>
      <p>
        One major direction of my work is the flying inverted pendulum, which serves as a demanding benchmark for balancing, planning, and aggressive maneuvering on quadrotor-based systems. I am interested not only in theoretical stability guarantees, but also in controllers that can be implemented and validated on physical hardware.
      </p>
      <p>
        I also work on trajectory generation, path planning, and experimental system integration, with the broader goal of making advanced control methods more reliable in practice.
      </p>
    </article>
  </div>
</section>

<section id="invited-talks" class="home-section">
  <h2>Invited Talks</h2>
  <div class="talk-card">
    <ul class="home-list home-list--talks">
      <li><strong>2025.10.26:</strong> Oral talk at <strong>Workshop on Advanced Aerial Robotics</strong>, University of Tokyo.</li>
      <li><strong>2022:</strong> Oral talk at the <strong>41st Chinese Control Conference (CCC)</strong>.</li>
    </ul>
  </div>
</section>

<section class="home-section home-section--stats">
  <h2>Statistics</h2>
  <div class="stats-layout">
    <article class="metric-card metric-card--scholar">
      <p class="metric-card__label">Google Scholar</p>
      {% if site.data.scholar and site.data.scholar.citations %}
      <p class="metric-card__value">{{ site.data.scholar.citations }}</p>
      <p class="metric-card__meta">Total citations{% if site.data.scholar.updated %} | Updated {{ site.data.scholar.updated }}{% endif %}</p>
      {% elsif site.author.scholar_citations and site.author.scholar_citations != "" %}
      <p class="metric-card__value">{{ site.author.scholar_citations }}</p>
      <p class="metric-card__meta">Total citations</p>
      {% else %}
      <p class="metric-card__value metric-card__value--link"><a href="{{ site.author.googlescholar }}">View profile</a></p>
      <p class="metric-card__meta">{{ site.author.scholar_note }}</p>
      {% endif %}
    </article>
    <article class="metric-card metric-card--map">
      <p class="metric-card__label">Visitor Locations</p>
      {% if site.clustrmaps.widget_page %}
      <div class="visitor-map">
        <iframe src="{{ site.clustrmaps.widget_page }}" title="Visitor location map" loading="lazy"></iframe>
      </div>
      <p class="metric-card__meta">Visitor locations and map view.</p>
      <p class="metric-card__meta"><a href="{{ site.clustrmaps.widget_page }}">Open full visitor map</a></p>
      {% else %}
      <div class="visitor-map visitor-map--placeholder">
        <p class="visitor-map__placeholder-title">ClustrMaps widget ready</p>
        <p class="metric-card__meta">{{ site.clustrmaps.note }}</p>
      </div>
      {% endif %}
    </article>
  </div>
</section>
