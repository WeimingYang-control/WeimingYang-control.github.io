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
  <p class="home-hero__eyebrow">Electrical and Computer Engineering</p>
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
  <div class="research-grid">
    <article class="research-card">
      <h3>Nonlinear Control for Underactuated Aerial Systems</h3>
      <p>
        I study control strategies for aerial platforms whose dynamics are strongly nonlinear and whose inputs are inherently constrained. The goal is to obtain controllers that remain stable, robust, and implementable in realistic conditions.
      </p>
    </article>
    <article class="research-card">
      <h3>Flying Inverted Pendulum and Aggressive Maneuvers</h3>
      <p>
        A major part of my work explores the flying inverted pendulum as a demanding benchmark for aerial robotics. This line of research combines balancing, motion planning, and aggressive flight in a single experimentally challenging platform.
      </p>
    </article>
    <article class="research-card">
      <h3>Trajectory Generation and Experimental Validation</h3>
      <p>
        Beyond controller design, I am interested in building end-to-end experimental systems, including trajectory generation, path planning, and testbed implementation. I care about methods that transfer cleanly from theory to hardware.
      </p>
    </article>
  </div>
  <p class="home-section__note">
    A fuller list of publications is available on
    {% if site.author.googlescholar %}<a href="{{ site.author.googlescholar }}">Google Scholar</a>{% else %}my publication pages{% endif %}.
  </p>
</section>

<section id="invited-talks" class="home-section">
  <h2>Invited Talks</h2>
  <div class="talk-card">
    <p>
      Invited talk information is being updated. If you would like to invite me for a seminar or research discussion on aerial robotics, nonlinear control, or experimental robotic systems, please feel free to get in touch.
    </p>
  </div>
</section>

<section id="visitors" class="home-section home-section--visitors">
  <h2>Visitors by Region</h2>
  <div class="visitor-card">
    <p>
      This section is reserved for a region-level visitor widget so the homepage can show where visitors are coming from.
      Because GitHub Pages is a static site, this module needs to be connected to a third-party counter service such as Flag Counter or ClustrMaps.
    </p>
    <p class="home-section__note">
      The layout and anchor are in place here, so we can wire in a live region map or country counter next.
    </p>
  </div>
</section>
