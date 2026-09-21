import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
DIST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dist')
from common import icon, page_shell, PHONE, PHONE_HREF, WHATSAPP_HREF, EMAIL

body = f'''
  <section class="page-intro-banner">
    <div class="guyana-mark small"></div>
    <div class="container">
      <div class="inner">
        <h1>Get in <span class="accent">Touch</span></h1>
        <p>We're here to help. Contact us for inquiries, vehicle information or to schedule a viewing.</p>
      </div>
    </div>
  </section>

  <section class="contact-section">
    <div class="container">
      <div class="contact-cards-layout">
        <div class="contact-info-card">
          <div class="contact-info-list">
            <div class="info-row">
              <div class="info-icon">{icon('phone')}</div>
              <div><h4>{PHONE}</h4><p>Call or WhatsApp</p></div>
            </div>
            <div class="info-row">
              <div class="info-icon">{icon('mail')}</div>
              <div><h4>{EMAIL}</h4><p>Email us anytime</p></div>
            </div>
            <div class="info-row">
              <div class="info-icon">{icon('pin')}</div>
              <div><h4>Georgetown, Guyana</h4><p>By appointment</p></div>
            </div>
            <div class="info-row">
              <div class="info-icon">{icon('clock')}</div>
              <div><h4>Mon - Sat: 9:00 AM - 6:00 PM</h4><p>Sunday: By appointment</p></div>
            </div>
          </div>
        </div>

        <div class="contact-form-card">
          <form class="form-stack" data-demo-form data-success-message="Message sent! We'll get back to you shortly.">
            <div class="form-field"><label>Full Name <span class="req">*</span></label><input type="text" required></div>
            <div class="form-field"><label>Email Address <span class="req">*</span></label><input type="email" required></div>
            <div class="form-field"><label>Phone Number <span class="req">*</span></label><input type="tel" required></div>
            <div class="form-field">
              <label>Message <span class="req">*</span></label>
              <textarea rows="5" placeholder="How can we help you?" required></textarea>
            </div>
            <button type="submit" class="btn btn-red btn-lg">{icon('send')} Send Message</button>
          </form>
        </div>
      </div>
    </div>
  </section>

  <section class="section-grey" style="padding-top:0;">
    <div class="container">
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 0; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow);">
        <div style="min-height:280px; background:#dfe6ea;">
          <iframe title="Georgetown, Guyana area map" src="https://www.google.com/maps?q=Georgetown,Guyana&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" style="border:0; width:100%; height:100%;"></iframe>
        </div>
        <div style="background:linear-gradient(135deg, #08131c, #102333); color:#fff; padding:36px; display:flex; flex-direction:column; justify-content:center;">
          <h3 style="margin:0 0 8px;">Find Us in Georgetown</h3>
          <p style="color:rgba(255,255,255,0.7); font-size:0.9rem; margin:0;">We operate by appointment in the Georgetown area. Contact us to arrange a convenient time and location to view a vehicle.</p>
        </div>
      </div>
    </div>
  </section>
'''

html = page_shell(
    title="Contact Us",
    description="Contact Top Notch Auto Sales in Georgetown, Guyana. Call, WhatsApp, email or send us a message.",
    active_page="contact.html",
    body=body,
)

with open(f'{DIST_DIR}/contact.html', 'w') as f:
    f.write(html)

print("contact.html written")
