import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
DIST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dist')
from common import icon, page_shell

body = f'''
  <section class="about-hero">
    <div class="container">
      <div class="inner">
        <div class="copy">
          <h1>About Top Notch <span class="line2">Auto Sales</span></h1>
          <p class="tagline">Driven by People. Powered by Trust.</p>
          <p class="lead">We are committed to providing quality vehicles at fair prices, with a focus on trust, transparency and excellent customer service. Whether you're buying for your family, business or personal use, we make the process simple and stress-free.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-tight">
    <div class="container">
      <div class="trust-grid">
        <div class="trust-card">
          <div class="trust-icon">{icon('target')}</div>
          <h3>Our Mission</h3>
          <p>To make quality vehicles accessible to everyone in Guyana.</p>
        </div>
        <div class="trust-card">
          <div class="trust-icon">{icon('shield')}</div>
          <h3>Our Values</h3>
          <p>Integrity, transparency and customer satisfaction.</p>
        </div>
        <div class="trust-card">
          <div class="trust-icon">{icon('handshake')}</div>
          <h3>Our Commitment</h3>
          <p>Reliable vehicles, fair pricing, ongoing support.</p>
        </div>
      </div>
    </div>
  </section>

  <section style="padding:0;">
    <div class="about-brand-cta">
      <div class="photo-side">
        <img src="images/jeep_renegade_black.jpg" alt="A vehicle from the Top Notch Auto Sales inventory">
      </div>
      <div class="panel-side">
        <h3>Guyana Drives Forward</h3>
        <p>More than cars. A stronger tomorrow.</p>
      </div>
    </div>
  </section>
'''

html = page_shell(
    title="About Us",
    description="About Top Notch Auto Sales — a trusted vehicle dealership in Georgetown, Guyana focused on quality, fair pricing and transparent service.",
    active_page="about.html",
    body=body,
)

with open(f'{DIST_DIR}/about.html', 'w') as f:
    f.write(html)

print("about.html written")
