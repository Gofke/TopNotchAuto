import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
DIST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dist')
from common import icon, page_shell

body = f'''
  <section class="request-section">
    <div class="container">
      <h1 style="font-size:1.7rem; margin:0 0 6px;">Request a Vehicle</h1>
      <p style="color:var(--ink-soft); margin:0 0 28px; font-size:0.95rem;">Looking for something specific? Let us know what you need and we'll help source it for you.</p>

      <div class="request-layout">
        <div class="request-form-card">
          <form class="form-stack" data-demo-form data-success-message="Request sent! We'll be in touch soon.">
            <div class="form-field"><label>Full Name <span class="req">*</span></label><input type="text" required></div>
            <div class="form-field"><label>Email Address <span class="req">*</span></label><input type="email" required></div>
            <div class="form-field"><label>Phone Number <span class="req">*</span></label><input type="tel" required></div>
            <div class="form-field"><label>Vehicle Make (Optional)</label><input type="text" placeholder="e.g. Toyota, Ford, Nissan"></div>
            <div class="form-field"><label>Vehicle Model (Optional)</label><input type="text"></div>
            <div class="form-field"><label>Year Range (Optional)</label><input type="text" placeholder="e.g. 2015 - 2020"></div>
            <div class="form-field">
              <label>Additional Details</label>
              <textarea rows="4" placeholder="Tell us more about what you're looking for..."></textarea>
            </div>
            <button type="submit" class="btn btn-red btn-lg">{icon('send')} Submit Request</button>
          </form>
        </div>

        <div class="request-side-card">
          <h4>How It Works</h4>
          <p class="intro">Getting your next vehicle is simple.</p>
          <div class="request-steps">
            <div class="step"><div class="num">1</div><div><h5>Send Your Request</h5><p>Fill out the form with your preferred vehicle details.</p></div></div>
            <div class="step"><div class="num">2</div><div><h5>We Search for You</h5><p>Our network sources options that match what you need.</p></div></div>
            <div class="step"><div class="num">3</div><div><h5>We Get in Touch</h5><p>We contact you with available options and next steps.</p></div></div>
          </div>
          <div style="display:flex; flex-direction:column; gap:10px;">
            <a href="tel:+5926742844" class="btn btn-red btn-block">{icon('phone')} Call Now</a>
            <a href="https://wa.me/5926742844" target="_blank" rel="noopener" class="btn btn-green btn-block">{icon('whatsapp')} WhatsApp Us</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section-grey">
    <div class="container">
      <div class="cta-banner with-photo" style="background-image:url('images/toyota_sedan_white.jpg');">
        <div class="cta-banner-inner">
          <div>
            <h3>Can't Find It? We'll Help You Get It.</h3>
            <p>Our network gives us access to a wide range of vehicles. Tell us what you need.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
'''

html = page_shell(
    title="Request a Vehicle",
    description="Looking for a specific vehicle? Request it from Top Notch Auto Sales in Georgetown, Guyana and we'll help source it for you.",
    active_page="request-a-vehicle.html",
    body=body,
)

with open(f'{DIST_DIR}/request-a-vehicle.html', 'w') as f:
    f.write(html)

print("request-a-vehicle.html written")
