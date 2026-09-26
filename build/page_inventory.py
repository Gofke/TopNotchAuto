import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
DIST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dist')
from common import icon, page_shell
from vehicle_data import VEHICLES

def vehicle_card(v):
    crop_attr = f' data-crop="{v["crop"]}"' if v["crop"] else ""
    specs = []

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
          <a href="{v['fb']}" target="_blank" rel="noopener" aria-label="View details on Facebook">{icon('arrow-right')}</a>
        </div>
      </div>
    </div>'''

body = f'''
  <section class="inventory-banner">
    <div class="guyana-mark small"></div>
    <div class="container">
      <div class="inner">
        <h1>Our <span class="accent">Inventory</span></h1>
        <p>Quality vehicles at fair prices. Find the right car for your needs.</p>
      </div>
    </div>
  </section>

  <section class="filter-row-wrap">
    <div class="container">
      <div class="filter-row">
        <select><option>All Makes</option><option>Ford</option><option>Jeep</option><option>Toyota</option><option>Mazda</option><option>Nissan</option></select>
        <select><option>All Body Types</option><option>SUV</option><option>Sedan</option><option>MPV / Van</option></select>
        <select><option>All Price Ranges</option><option>Contact for Price</option></select>
        <button class="btn btn-red">{icon('search')} Search</button>
      </div>
    </div>
  </section>

  <section style="padding: 26px 0 56px;">
    <div class="container">
      <div class="section-head row" style="margin-bottom:20px;">
        <div></div>
        <p style="color:var(--ink-soft); font-size:0.88rem;">Showing {len(VEHICLES)} vehicles</p>
      </div>
      <div class="vehicle-grid">
        {''.join(vehicle_card(v) for v in VEHICLES)}
      </div>
    </div>
  </section>
'''

html = page_shell(
    title="Inventory",
    description="Browse Top Notch Auto Sales' inventory of quality vehicles in Georgetown, Guyana.",
    active_page="inventory.html",
    body=body,
)

with open(f'{DIST_DIR}/inventory.html', 'w') as f:
    f.write(html)

print("inventory.html written")
