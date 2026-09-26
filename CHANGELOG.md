# Changelog

All notable changes to this project are documented here.

## [0.0.2] — 2026-09-26

Facebook-linked inventory.

### Changed
- All "View Details" buttons and vehicle card arrows now open that vehicle's
  Facebook post in a new tab, instead of an internal detail page. The client keeps
  full details (specs, price, availability) up to date on Facebook.
- Inventory updated to 8 vehicles, each with a client-confirmed name and Facebook
  post link: Ford EcoSport, Jeep Renegade, Toyota Sienta (x2), Toyota Passo Moda,
  Toyota Corolla Axio, Mazda Axela Sedan, Nissan Clipper Mini Utility Van
- Removed spec chips (transmission / fuel) from vehicle cards — these details now
  live on Facebook rather than being duplicated on the site

### Removed
- The 9 per-vehicle detail pages (`vehicle-*.html`) and `build/page_details.py`,
  now redundant since all vehicles link out to Facebook

### Notes
- Additional vehicles are pending client photos; links for ~17 more are on file

## [0.0.1] — 2026-09-21

Initial versioned release of the premium redesign.

### Added
- Full static site: Home, Inventory, About, Request a Vehicle, Contact, and 9 individual
  vehicle detail pages (one per real vehicle in inventory)
- Shared header (utility bar + white nav + Call/WhatsApp CTAs) and footer, identical across
  every page
- Real client vehicle photography throughout — no mockup-extracted or placeholder images
- Distinct page-level hero/banner components (HomeHero, InventoryBanner, AboutHero,
  page-intro banners) rather than one reused generic header
- Responsive layouts validated at 390 / 768 / 1024 / 1280 / 1440px with zero horizontal
  overflow
- `Sold Vehicles` page built and ready, intentionally excluded from public navigation
  pending confirmed sold-stock data from the client
- Cache-busted stylesheet versioning to prevent stale-CSS deployment issues

### Notes
- No vehicle specs (transmission, fuel, seats, condition, price, year, mileage) are shown
  unless explicitly confirmed — unconfirmed fields are omitted rather than guessed
- Hero background image (`home-hero-bg.jpg`) is an AI-generated decorative atmospheric
  image, used only as a hero background, never presented as documentary/location photography
