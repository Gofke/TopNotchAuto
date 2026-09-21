import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
DIST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dist')
from common import icon, page_shell, PHONE_HREF, WHATSAPP_HREF
from vehicle_data import VEHICLES

def build_detail_page(v):
    spec_rows = [
        ("Transmission", v["transmission"]),
        ("Fuel Type", v["fuel"]),
        ("Seating Capacity", v["seats"]),
        ("Condition", v["condition"]),
        ("Location", "Georgetown, Guyana"),
    ]
    spec_rows = [(label, val) for label, val in spec_rows if val]
    # Pair into two-column table rows
    rows_html = ""
    for i in range(0, len(spec_rows), 2):
        left = spec_rows[i]
        right = spec_rows[i+1] if i+1 < len(spec_rows) else None
        rows_html += "<tr>"
        rows_html += f'<td class="label">{left[0]}</td><td>{left[1]}</td>'
        if right:
            rows_html += f'<td class="label">{right[0]}</td><td>{right[1]}</td>'
        rows_html += "</tr>"

    whatsapp_prefill = f"{WHATSAPP_HREF}?text=Hi%2C%20I%27m%20interested%20in%20the%20{v['name'].replace(' ', '%20')}%20listed%20on%20your%20website."

    body = f'''
  <section class="section-tight">
    <div class="container">
      <a href="inventory.html" class="back-link">{icon('chevron-left-sm')} Back to Inventory</a>
      <div class="detail-layout">
        <div>
          <h1 style="font-size:1.7rem; margin:0 0 4px;">{v['name']}</h1>
          <div style="display:flex; align-items:center; gap:14px; margin-bottom:18px;">
            <span style="color:var(--red); font-weight:700; font-size:1.05rem;">Contact for Price</span>
            {'<span style="color:var(--ink-soft); font-size:0.85rem; display:flex; align-items:center; gap:5px;">' + icon('seat') + ' ' + v['seats'] + '</span>' if v['seats'] else ''}
          </div>

          <div class="detail-main-photo">
            <img src="images/{v['img']}" alt="{v['name']}">
          </div>

          <h2 style="font-size:1.2rem; margin:28px 0 12px;">Vehicle Overview</h2>
          <table class="spec-table-clean">
            {rows_html}
          </table>
          <p class="detail-disclaimer">Vehicle details are provided to the best of our knowledge. Please contact us to confirm specific information, availability and arrange a viewing.</p>
        </div>

        <aside class="detail-sidebar">
          <h4>Get in Touch</h4>
          <p>Interested in this vehicle? Contact us for more information or to schedule a viewing.</p>
          <div style="display:flex; flex-direction:column; gap:10px;">
            <a href="{PHONE_HREF}" class="btn btn-red btn-block">{icon('phone')} Call Now</a>
            <a href="{whatsapp_prefill}" target="_blank" rel="noopener" class="btn btn-green btn-block">{icon('whatsapp')} WhatsApp Us</a>
            <a href="request-a-vehicle.html" class="btn btn-outline btn-block">{icon('doc')} Request This Vehicle</a>
          </div>
        </aside>
      </div>
    </div>
  </section>
'''

    html = page_shell(
        title=v['name'],
        description=f"{v['name']} available at Top Notch Auto Sales in Georgetown, Guyana. Contact us for pricing and availability.",
        active_page="inventory.html",
        body=body,
    )

    filename = f"vehicle-{v['id']}.html"
    with open(f'{DIST_DIR}/{filename}', 'w') as f:
        f.write(html)
    return filename


for v in VEHICLES:
    fname = build_detail_page(v)
    print(f"{fname} written")
