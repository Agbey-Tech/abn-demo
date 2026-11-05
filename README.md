# Ascend Brand Network — redesign demo

A curated pitch for a broader digital design and development company: websites, platforms, business systems, and the original Ascend Studio creative services. The secondary Network area retains its membership, gatherings, and resources information.

The demo features six selected founding-team projects. The complete original inventory stays in source reference files; it is not the public portfolio in this pitch.

## Preview

```powershell
python scripts/build.py
python -m http.server 4173 --bind 127.0.0.1
```

Open `http://127.0.0.1:4173/`. Reload at the top to replay the opening animation. No npm installation is needed.

## Pitch walkthrough

1. Open the homepage: broader business positioning, the actual supplied symbol, and an original illustration of connected websites, platforms, and systems.
2. Explore selected work and a project profile. Original screenshots and founding-team attribution are retained.
3. Explore Websites, Platforms, and Systems, plus the five original Studio service areas.
4. Try the labelled illustrative business workflow on the homepage.
5. Open the audience pages, About, and the project enquiry preview.
6. Visit the secondary Network, Roundtable, Experiences, and Resource Center.

## Source files

- `TODO.md`: the short working checklist, revised to reflect the curated demo scope.
- `REDESIGN-PLAN.md`: the original broader design plan. The later demo-scope decision takes precedence over full portfolio implementation.
- `src/home.html`: homepage composition.
- `scripts/content.py`: shared components and preserved service, process, and team information. `SELECTED` controls the six-project selection.
- `scripts/pages.py`: supporting page compositions and project profiles.
- `scripts/build.py`: shared navigation, footer, metadata, relative URLs, and deployment packaging.
- `design.css`: the active design system, responsive layouts, and CSS motion. All designed backgrounds use solid colours.
- `site.js`: navigation, hero illustration motion, workflow, filters, and local enquiry preview.
- `content/original-site.json`: captured original content, links, FAQs, and asset references.
- `content/projects.json`: the full 47-project source inventory for reference.
- `CONTENT-MAP.md`: what was retained and where it appears.

The earlier CSS/JS files are retained as historical source and are no longer loaded by the redesign. The deployment builder copies only active styles/scripts and image files referenced by the generated demo. Unused portfolio downloads have been moved outside the demo into the temporary audit archive. Their source content remains in the inventory.

## Design

The supplied WhatsApp-named JPEGs are the logo source. The header uses the original symbol with a live-text brand label; the footer uses the supplied horizontal logo. JPEG-derived working colours are blue `#074DA5`, navy `#000E3F`, and gold `#EABA2A`, with a light neutral canvas. Manrope and IBM Plex Mono load from Google Fonts with local fallbacks.

No generated client work, staff portraits, testimonials, or results are used. About includes a clearly captioned fictional studio setting; it does not depict Ascend staff. The system workflow is clearly labelled as illustrative. Project profiles use original descriptions and imagery, without invented case-study results.

## Validation and deployment

```powershell
node --check site.js
python scripts/check_site.py
python scripts/build.py --output _site
python scripts/check_site.py _site
python scripts/check_content.py _site
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for GitHub Pages setup. Relative links work at a domain root or repository subpath. The existing workflow builds and deploys `_site/` on pushes to `main`.

## Demo limits

The enquiry form validates locally and previews completion. It does not send requests or store personal data. A live-company contact link is provided. Real enquiry delivery and an approved privacy policy remain production launch dependencies. Planned gatherings and unpublished resources retain those labels.

No changes have been pushed or published automatically.

Hero artwork: `assets/ascend-digital-ecosystem.svg`, an original code-native vector illustration. Interfaces are illustrative, not client work.

## Motion and project-page visual

Start a Project has a dedicated illustration (`assets/ascend-project-start.svg`) and a direct link to the enquiry form. The homepage and contact artwork are rendered inline so their individual panels can move independently. The SVG files remain editable artwork sources.

Motion includes staggered headline and copy entrances, drawing connection lines, continuous layered illustration movement, stronger scroll reveals, menu-link entrances, and hover responses. Pause/Resume controls are available in the illustrated openings and footer. System reduced-motion preferences disable effects, reveal content, and keep controls usable. Enquiry-mode links continue to work when jumping to the form.

About-page image: `assets/about-studio-team.png`. Generation method and final prompt are recorded in `assets/about-studio-team.source.md`.
