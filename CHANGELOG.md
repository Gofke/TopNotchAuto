# Changelog

All notable changes to this project are documented here.

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
