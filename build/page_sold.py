import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
DIST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dist')
from common import icon, page_shell, PHONE_HREF, WHATSAPP_HREF

# INTENTIONALLY EMPTY: no sold-vehicle data has been confirmed by the client.
# Do NOT populate this with current inventory or unrelated photos to "fill" the page.
# Once the client supplies confirmed sold vehicles (photo + at minimum a name), add
# them here in the same shape as vehicle_data.VEHICLES and this page + component are
# ready to go. This page is intentionally left out of NAV_ITEMS / footer Quick Links
# in common.py until then — add it back there once real data lands.
SOLD_VEHICLES = []


def sold_card(v):
    crop_attr = f' data-crop="{v["crop"]}"' if v.get("crop") else ""
    return f'''<div class="vehicle-card">
      <div class="thumb">
        <span class="vehicle-badge sold">Sold</span>
        <img src="images/{v['img']}" alt="{v['name']}" loading="lazy"{crop_attr}>
      </div>
      <div class="body">
        <h3>{v['name']}</h3>
        <div class="price-link-row">
          <span class="price sold-text">Sold</span>
        </div>
      </div>
    </div>'''


cards_html = "".join(sold_card(v) for v in SOLD_VEHICLES)

body = f'''
  <section class="page-intro-banner">
    <div class="guyana-mark small"></div>
    <div class="container">
      <div class="inner">
        <h1>Recently <span class="accent">Sold</span></h1>
        <p>A selection of vehicles we've recently delivered to happy customers.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      {"<div class='vehicle-grid cols-4'>" + cards_html + "</div>" if SOLD_VEHICLES else """
      <div style="text-align:center; padding:40px 0; color:var(--ink-soft);">
        <p style="font-size:0.95rem;">Our sold-vehicle showcase is being updated. In the meantime, browse our current inventory or get in touch — we're happy to help you find your next vehicle.</p>
      </div>
      """}
    </div>
  </section>

  <section class="section-grey">
    <div class="container">
      <div class="cta-banner dark">
        <div class="cta-banner-inner">
          <div>
            <h3>Ready to Find Your Next Vehicle?</h3>
            <p>Browse our current inventory or reach out — we're happy to help.</p>
          </div>
          <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <a href="inventory.html" class="btn btn-red">{icon('search')} View Inventory</a>
            <a href="{WHATSAPP_HREF}" target="_blank" rel="noopener" class="btn btn-green">{icon('whatsapp')} WhatsApp Us</a>
          </div>
        </div>
      </div>
    </div>
  </section>
'''

html = page_shell(
    title="Sold Vehicles",
    description="Recently sold vehicles from Top Notch Auto Sales in Georgetown, Guyana.",
    active_page="sold-vehicles.html",
    body=body,
)

with open(f'{DIST_DIR}/sold-vehicles.html', 'w') as f:
    f.write(html)

print("sold-vehicles.html written (not linked in public nav — awaiting confirmed sold-stock data)")
