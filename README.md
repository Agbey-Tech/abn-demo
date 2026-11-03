# Ascend Brand Network — redesign pitch

A static, responsive presentation demo using original Ascend logos, photographs, and project imagery. The homepage is the principal design presentation; ten concise interior pages preserve the original navigation structure without rebuilding the full production website.

**Deployment:** Follow [DEPLOYMENT.md](DEPLOYMENT.md) for the one-time GitHub Pages setup and first push.

## Preview

From this folder:

```powershell
python -m http.server 4173 --bind 127.0.0.1
```

Open `http://127.0.0.1:4173/`. Use an HTTP server so folder-style page destinations work correctly. No npm install is needed.

## Brand and motion

Colours verified against the live original site's CSS on 3 November 2026: turquoise `#3ADCDD`, teal `#1F8A8C`, cyan `#2FC3D8`, dark ink `#061317`, deep teal `#0E4D51`, off-white `#F1F2F0`, and mist `#E3EFEE`. The homepage leads with dark ink and turquoise. Original typography uses Sora, Manrope, and Instrument Serif. See `assets/brand-tokens.json` for the source and values.

The opening combines masked headline entrances, a photographic reveal, an offset frame, and a staged second image. Fine-pointer devices add subtle photo and button movement. Menus, project selections, dialogs, page changes, and sections have coordinated transitions. The layout stays usable without JavaScript; reduced-motion preferences disable animation and reveal all content. Reload at the top to replay the entrance.

## Navigation

The original top-level structure is retained: Home, The Network, Ascend Studio, Experiences, Resources, About, and Let's Connect. Desktop menus group the original membership, services, audiences, process, FAQ, gathering, and resource destinations. Mobile navigation uses expandable groups. The shared footer links to those destinations too.

| Page | Path |
|---|---|
| Home | `/` |
| The Network | `/network/` |
| Ascend Studio | `/services/` |
| Churches & Ministries | `/churches-ministries/` |
| Real Estate Professionals | `/real-estate/` |
| Portfolio | `/portfolio/` |
| The Shepherd's Roundtable | `/roundtable/` |
| Experiences | `/experiences/` |
| Resource Center | `/resources/` |
| About ABN | `/about/` |
| Let's Connect | `/work-with-us/` |

Pages use relative links and assets, so the same build works under a GitHub repository subpath. There is no client-side router or rewrite requirement.

## Edit and regenerate

- `src/home.html`: homepage design source and shared demo dialog markup.
- `scripts/build.py`: shared navigation, footer, and concise interior-page content.
- `styles.css`: base visual system.
- `refinements.css`: editorial design refinements.
- `site.css`: original navigation hierarchy and interior-page layouts.
- `motion.css`: cinematic hero, responsive composition, and CSS motion.
- `motion.js`: progressive reveals, pointer effects, and page transitions.
- `app.js`: menus, service accordions, portfolio filters, project dialogs, and demo forms.
- `assets/sources.json`: original asset URLs.

After editing the source or page builder:

```powershell
python scripts/build.py
python scripts/check_site.py
```

Generated root and interior HTML files are included for immediate preview. Edit their sources rather than generated output. GitHub Actions regenerates the deployment artifact automatically, checks links, and deploys only `_site/`.

## Pitch walkthrough

1. Introduce the homepage's two distinct audience paths.
2. Open the Network and Studio menus to show the familiar information architecture.
3. Follow a service link to its actual page section.
4. Visit the portfolio, filter the selection, and open a project.
5. Explore the planned gathering formats and future resources.
6. Follow a membership or consultation link to the matching contact mode.

## Scope

All 17 original image assets are local. Fonts load from Google Fonts with system fallbacks. Portfolio work is attributed to the founding team, future events remain planned, and resources remain marked as coming soon. Supporting copy is written for this demo; no testimonials or unverified outcomes have been invented.

Forms validate locally and display a completion preview. **They do not send or store enquiries.** The old default WordPress post and unfinished media page are excluded. No GitHub repository has been created, pushed, or published automatically.

## Checks

The link checker verifies every generated page, local asset, fragment target, and duplicate ID, and rejects domain-root URLs that would break repository hosting. Browser QA covers the deployment artifact under a repository-style subpath, page navigation, service deep links, enquiry deep links, nested-page project images, and mobile menus and layouts. Motion QA additionally verifies the initial entrance, computed brand colours, responsive headline bounds from 320px to 1440px, pointer movement, and reduced-motion behavior.
