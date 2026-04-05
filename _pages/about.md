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
    I am a Ph.D. candidate in Electrical and Computer Engineering at the University of Macau and a Research Assistant in the SCORE Lab. My research sits at the intersection of control theory and robotics, with an emphasis on systems that are nonlinear, underactuated, and difficult to operate reliably in the real world.
  </p>
  <p>
    I am especially interested in aerial robotic systems, robust nonlinear control, and the full path from mathematical design to experimental deployment. Along the way, I have worked on flying inverted pendulum platforms, quadrotor-based systems, and trajectory generation methods for aggressive maneuvers.
  </p>
  <p>
    My broader goal is to develop control and planning methods that remain practical when models are imperfect, actuation is limited, and experiments need to work beyond simulation.
  </p>
</section>

<section id="news" class="home-section">
  <h2>News</h2>
  <ul class="home-list">
    <li><strong>2024:</strong> Co-authored the Automatica paper <em>Robust nonlinear 3D control of an inverted pendulum balanced on a quadrotor</em>.</li>
    <li><strong>2021-present:</strong> Working as a Research Assistant in the SCORE Lab, Faculty of Science and Technology, University of Macau.</li>
    <li><strong>Service:</strong> Reviewer for IEEE TASE, IEEE RA-L, Control Engineering Practice, and IEEE TSMC: Systems.</li>
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
    <p>
      Invited talk information is being updated. If you would like to invite me for a seminar or research discussion on aerial robotics, nonlinear control, or experimental robotic systems, please feel free to get in touch.
    </p>
  </div>
</section>

<section class="home-section home-section--stats">
  <h2>Statistics</h2>
  <div class="metrics-grid">
    <article class="metric-card">
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
    <article class="metric-card">
      <p class="metric-card__label">Site Visits</p>
      <p class="metric-card__value"><span id="busuanzi_value_site_pv">--</span></p>
      <p class="metric-card__meta">Total page views</p>
    </article>
    <article class="metric-card">
      <p class="metric-card__label">Visitors</p>
      <p class="metric-card__value"><span id="busuanzi_value_site_uv">--</span></p>
      <p class="metric-card__meta">Unique visitors</p>
    </article>
  </div>
</section>
