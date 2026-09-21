import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
DIST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dist')
from common import icon, page_shell, PHONE_HREF, WHATSAPP_HREF
from vehicle_data import VEHICLES, FEATURED_VEHICLE

LATEST = VEHICLES[:4]  # Jeep, Sienta(brown), Fielder, Axela — matches reference order

def vehicle_card(v):
    crop_attr = f' data-crop="{v["crop"]}"' if v["crop"] else ""
    specs = []
    if v["transmission"]:
        specs.append(f'<span>{icon("gear")} {v["transmission"]}</span>')
    if v["fuel"]:
        specs.append(f'<span>{icon("fuel")} {v["fuel"]}</span>')
    specs_html = "".join(specs)
    return f'''<div class="vehicle-card">
      <div class="thumb">
        <img src="images/{v['img']}" alt="{v['name']}" loading="lazy"{crop_attr}>
      </div>
      <div class="body">
        <h3>{v['name']}</h3>
        <div class="specs">{specs_html}</div>
        <div class="price-link-row">
          <span class="price">Contact for Price</span>
          <a href="vehicle-{v['id']}.html" aria-label="View details">{icon('arrow-right')}</a>
        </div>
      </div>
    </div>'''

fv = FEATURED_VEHICLE

body = f'''
  <section class="home-hero">
    <div class="guyana-mark"></div>
    <div class="container">
      <div class="inner">
        <div class="split">
          <div class="copy">
            <p class="eyebrow-line">Quality Vehicles. Fair Prices.</p>
            <h1>Guyana Drives <span class="accent">Forward.</span></h1>
            <p class="lead">Reliable, high-quality vehicles for families, professionals and businesses. A simpler, more transparent car buying experience in Guyana.</p>
            <div class="ctas">
              <a href="inventory.html" class="btn btn-red btn-lg">{icon('search')} Browse Inventory</a>
              <a href="{WHATSAPP_HREF}" target="_blank" rel="noopener" class="btn btn-green btn-lg">{icon('whatsapp')} WhatsApp Us</a>
            </div>
          </div>
          <div class="vehicle-side">
            <div class="featured-vehicle-card">
              <div class="photo">
                <img src="images/{fv['img']}" alt="{fv['name']} — featured vehicle">
                <div class="dots"><span class="active"></span><span></span><span></span></div>
              </div>
              <div class="info">
                <h3>{fv['name']}</h3>
                <div class="specs-row">
                  {'<span>' + icon('gear') + ' ' + fv['transmission'] + '</span>' if fv['transmission'] else ''}
                  {'<span>' + icon('fuel') + ' ' + fv['fuel'] + '</span>' if fv['fuel'] else ''}
                  {'<span>' + icon('seat') + ' ' + fv['seats'] + '</span>' if fv['seats'] else ''}
                </div>
                <div class="price">Contact for Price</div>
                <div class="cta-row">
                  <a href="vehicle-{fv['id']}.html" class="btn btn-red">{icon('search')} View Details</a>
                  <a href="contact.html" class="btn btn-outline-dark">{icon('doc')} Ask About This Vehicle</a>
                </div>
              </div>
            </div>
          </div>
          <div class="trust-strip">
            <div class="item">
              <div class="icon-circle">{icon('shield')}</div>
              <div><h5>Inspected Vehicles</h5><p>Quality you can trust</p></div>
            </div>
            <div class="item">
              <div class="icon-circle">{icon('handshake')}</div>
              <div><h5>Fair Pricing</h5><p>No hidden costs</p></div>
            </div>
            <div class="item">
              <div class="icon-circle">{icon('users')}</div>
              <div><h5>Local Support</h5><p>We're here to help</p></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head row">
        <div>
          <h2>Latest Inventory</h2>
          <p>Fresh arrivals. Quality checked. Ready for the road.</p>
        </div>
        <a href="inventory.html" class="view-all-link">View All Inventory {icon('arrow-right')}</a>
      </div>
      <div class="vehicle-grid cols-4">
        {''.join(vehicle_card(v) for v in LATEST)}
      </div>
    </div>
  </section>

  <section class="section-grey">
    <div class="container">
      <div class="cta-banner dark">
        <div class="cta-banner-inner">
          <div>
            <h3>Ready to Find Your Next Vehicle?</h3>
            <p>Browse our inventory or reach out — we're happy to help you find the right fit.</p>
          </div>
          <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <a href="{PHONE_HREF}" class="btn btn-red">{icon('phone')} Call Now</a>
            <a href="{WHATSAPP_HREF}" target="_blank" rel="noopener" class="btn btn-green">{icon('whatsapp')} WhatsApp Us</a>
          </div>
        </div>
      </div>
    </div>
  </section>
'''

html = page_shell(
    title="Home",
    description="Top Notch Auto Sales — quality vehicles at fair prices in Georgetown, Guyana. A simpler, more transparent car buying experience.",
    active_page="index.html",
    body=body,
)

with open(f'{DIST_DIR}/index.html', 'w') as f:
    f.write(html)

print("index.html written")
