# Top Notch Auto Sales — Website

Static marketing website for Top Notch Auto Sales, a vehicle dealership in Georgetown, Guyana.

**Live site:** https://topnotch.178.105.181.88.nip.io

## Project type

This is a **static HTML/CSS/JS site** with no backend, no database, and no server-side code.
Pages are generated from Python templates (`build/`) into plain static HTML (`dist/`), which is
deployed as-is to any static file host or web server.

## Structure

```
build/            Python page templates — the actual "source code" of the site
  common.py       Shared header, footer, page shell, icon set, nav config
  vehicle_data.py Vehicle inventory data (name, image, specs — no unverified fields)
  page_*.py       One script per page; each writes its HTML into dist/
  main.py         Runs every page_*.py in order — the single build entry point

dist/             Generated static site — this is what gets deployed
  *.html          15 pages: home, inventory, about, request, contact, sold-vehicles,
                  and one detail page per vehicle
  css/style.css   Single stylesheet (design system: colors, components, responsive rules)
  js/main.js      Mobile nav toggle, toast notifications, demo form handling
  images/         Real vehicle photos supplied by the client, plus one hero background image
```

## Building

Requires Python 3 only, no dependencies.

```bash
python3 build/main.py
```

This regenerates every file in `dist/` from the templates in `build/`. Run it after changing
`common.py`, `vehicle_data.py`, or any `page_*.py`.

## Deploying

`dist/` is the entire deployable site. Copy its contents to the web root of any static host
(nginx, Apache, CloudPanel, Netlify, etc.) — no build step is needed on the server, since `dist/`
already contains the final HTML/CSS/JS.

Current deployment: CloudPanel + nginx on a shared VPS. The stylesheet is cache-busted via a
timestamp query string (`css/style.css?v=...`) set in `build/common.py`; bump this value on every
deploy that changes `style.css` so browsers don't serve a stale cached copy.

## Data honesty notes

- Vehicle specs (transmission, fuel, seats, condition) are only shown when confirmed by the
  client. Unconfirmed fields are `None` in `vehicle_data.py` and are omitted from the rendered
  page entirely — never guessed or filled with placeholder values.
- All vehicle photos in `dist/images/` are real photos supplied by the client, not extracted or
  cropped from design mockups.
- The "Sold Vehicles" page exists and is fully built (`build/page_sold.py`) but is intentionally
  left out of the site navigation until the client supplies confirmed sold-inventory data. See
  the comment at the top of that file before re-enabling it.
- `images/home-hero-bg.jpg` is an AI-generated atmospheric background image, used only as a
  decorative hero background on the Home and About pages. It is not presented as, and must not
  be used as, a real photo of the dealership or its location.

## License

Proprietary — all rights reserved by Top Notch Auto Sales.
