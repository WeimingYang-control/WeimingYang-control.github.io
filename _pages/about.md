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

<!-- About -->
<section id="about-me" class="home-section">
  <h2>About Me</h2>
  <div class="about-feature">
    <div class="about-feature__media">
      <img src="{{ base_path }}/images/web_logo.jpg" alt="Flying inverted pendulum platform">
    </div>
    <div class="about-feature__content">
      <p>
        I am currently a <strong>Research Fellow at the National University of Singapore</strong>. My work sits at the intersection of <strong>control theory</strong> and <strong>robotics</strong>, with a particular emphasis on systems that are nonlinear, underactuated, and challenging to deploy reliably in real-world environments.
      </p>
      <p>
        My primary interests include <strong>aerial robotic systems</strong>, <strong>robust nonlinear control</strong>, and the full path from mathematical design to experimental deployment. Along the way, I have worked on <strong>flying inverted pendulum platforms</strong>, <strong>quadrotor-based systems</strong>, and <strong>trajectory generation methods for aggressive maneuvers</strong>.
      </p>
      <p>
        My broader goal is to develop <strong>control and planning methods that remain practical beyond simulation</strong>, especially when models are imperfect, actuation is limited, and experiments must work on physical platforms.
      </p>
    </div>
  </div>
</section>

<!-- News -->
<section id="news" class="home-section">
  <h2>News</h2>
  <ul class="home-list">
    <li><strong>2025.12:</strong> Our manuscript titled <em>Trajectory Generation and Extended High-Gain Observers Based Output Feedback Control for an Underactuated Flying Inverted Pendulum</em> has been accepted for publication in <strong>IEEE TASE</strong>.</li>
    <li><strong>2025.11:</strong> Joined the <strong>National University of Singapore</strong> as a <strong>Research Fellow</strong>.</li>
    <li><strong>2025.10:</strong> Successfully obtained my <strong>Ph.D. degree</strong> from the <strong>University of Macau</strong>.</li>
    <li><strong>Service:</strong> Reviewer for <strong>IEEE TASE</strong>, <strong>IEEE RA-L</strong>, <strong>Control Engineering Practice</strong>, and <strong>IEEE TSMC: Systems</strong>.</li>
  </ul>
</section>

<!-- Research -->
<section id="research" class="home-section">
  <h2>Research</h2>
  <div class="research-list">
    <article class="research-paper">
      <div class="research-paper__media">
        <img src="{{ base_path }}/images/web_1.jpg" alt="Robust nonlinear 3D control of an inverted pendulum balanced on a quadrotor">
      </div>
      <div class="research-paper__content">
        <h3><span class="research-paper__index">01</span> Robust nonlinear 3D control of an inverted pendulum balanced on a quadrotor</h3>
        <p class="research-paper__venue"><em>Automatica</em>, 2024</p>
        <div class="research-paper__links">
          <a class="research-link research-link--paper" href="https://www.sciencedirect.com/science/article/abs/pii/S0005109823005022"><i class="fas fa-file-alt" aria-hidden="true"></i> Paper</a>
          <a class="research-link research-link--video" href="https://www.youtube.com/watch?v=n9nVOPnf6h8"><i class="fab fa-youtube" aria-hidden="true"></i> Video</a>
        </div>
        <p>
          This work studies full three-dimensional trajectory tracking for a flying inverted pendulum balanced on a quadrotor under unknown constant disturbances. Instead of relying on linearization, it develops a robust nonlinear control strategy that coordinates pendulum translation, pendulum direction, and quadrotor attitude in a unified framework. The paper shows that the proposed controller can achieve asymptotic tracking while preserving upright balance in a highly coupled underactuated aerial system.
        </p>
      </div>
    </article>
    <article class="research-paper">
      <div class="research-paper__media">
        <img src="{{ base_path }}/images/web_2.jpg" alt="Output feedback control of an underactuated flying inverted pendulum">
      </div>
      <div class="research-paper__content">
        <h3><span class="research-paper__index">02</span> Output feedback control of an underactuated flying inverted pendulum</h3>
        <p class="research-paper__venue"><em>Control Engineering Practice</em>, 2025</p>
        <div class="research-paper__links">
          <a class="research-link research-link--paper" href="https://www.sciencedirect.com/science/article/abs/pii/S0967066125002369"><i class="fas fa-file-alt" aria-hidden="true"></i> Paper</a>
        </div>
        <p>
          This paper tackles trajectory tracking for an underactuated flying inverted pendulum when direct measurements of all state variables are not available and constant external disturbances are present. A uniformly completely observable linear time-varying model is introduced, and a Kalman filter is used to estimate angular velocity, disturbances, and noise-filtered pendulum orientation measurements. These estimates are then embedded in a nonlinear backstepping output-feedback controller, with both simulations and experiments validating the resulting tracking performance.
        </p>
      </div>
    </article>
    <article class="research-paper">
      <div class="research-paper__media">
        <img src="{{ base_path }}/images/web_3.jpg" alt="Trajectory Generation and Extended High-Gain Observers Based Output Feedback Control for an Underactuated Flying Inverted Pendulum">
      </div>
      <div class="research-paper__content">
        <h3><span class="research-paper__index">03</span> Trajectory Generation and Extended High-Gain Observers Based Output Feedback Control for an Underactuated Flying Inverted Pendulum</h3>
        <p class="research-paper__venue"><em>IEEE Transactions on Automation Science and Engineering</em>, 2025</p>
        <div class="research-paper__links">
          <a class="research-link research-link--paper" href="https://ieeexplore.ieee.org/abstract/document/11318354"><i class="fas fa-file-alt" aria-hidden="true"></i> Paper</a>
          <a class="research-link research-link--video" href="https://www.youtube.com/watch?v=iHm6r5wv8dk"><i class="fab fa-youtube" aria-hidden="true"></i> Video</a>
        </div>
        <p>
          This paper presents integrated trajectory generation and output-feedback control strategies for an underactuated flying inverted pendulum operating under unknown time-varying disturbances. It introduces two extended high-gain observers to independently estimate the pendulum's linear and angular velocities, as well as the unknown disturbances, and embeds them within a nonlinear hierarchical Lyapunov-based control framework. By exploiting the differential flatness of the system, the work also develops a trajectory generation method for aggressive window-crossing maneuvers, with both simulations and experiments validating the agility, robustness, and precision of the proposed approach.
        </p>
      </div>
    </article>
  </div>
</section>

<!-- Invited Talks -->
<section id="invited-talks" class="home-section">
  <h2>Invited Talks</h2>
  <div class="talk-card">
    <ul class="home-list home-list--talks">
      <li><strong>2025.10.26:</strong> Oral talk at <strong>Workshop on Advanced Aerial Robotics</strong>, University of Tokyo.</li>
      <li><strong>2022:</strong> Oral talk at the <strong>41st Chinese Control Conference (CCC)</strong>.</li>
    </ul>
  </div>
</section>

<!-- Visitors -->
<section class="home-section home-section--stats">
  <h2>Visitors</h2>
  <div class="stats-layout stats-layout--single">
    <article class="metric-card metric-card--map">
      <p class="metric-card__label">Visitor Locations</p>
      {% if site.clustrmaps.widget_page and site.clustrmaps.widget_image %}
      <a class="visitor-map" href="{{ site.clustrmaps.widget_page }}" aria-label="Visitor location map">
        <img src="{{ site.clustrmaps.widget_image }}" alt="Visitor location map">
      </a>
      <p class="metric-card__meta">Visitor locations from the site map.</p>
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

