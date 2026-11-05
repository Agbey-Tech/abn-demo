# Ascend Brand Network — full-site redesign plan

Scope update: the user clarified that this remains a curated client pitch. Six selected projects are presented; the complete original inventory is retained as reference. See `TODO.md` for the completed demo checklist.

Prepared 5 November 2026. Status: proposed design and implementation brief. This document supersedes the earlier requirement to reproduce the original website’s colours, wording, and layouts. It does not change the running demo.

## 1. The brief we are designing around

Ascend builds systems, websites, and platforms for other businesses and organisations. Churches are an important audience within that broader market. The website should help a prospective client understand what Ascend can build, see credible work, and start a useful project conversation.

Confirmed decisions:

- Redesign the entire site, with freedom to change the layouts, copy, colour system, and visual language.
- Use the newly supplied blue-and-gold Ascend logo as the identity reference.
- Use solid colours. No decorative gradients, glow effects, or gradient text.
- Keep real project assets where they provide useful proof. New imagery can support the presentation.
- Keep the Network, membership, Roundtable, and Experiences in a secondary Network area. The main company website leads with services and work. This hierarchy was explicitly selected in this conversation.
- Retain the current GitHub Pages delivery path unless a later functional requirement calls for a backend.

Primary conversion: a qualified project enquiry. Secondary conversion: exploring a relevant project or capability. Network enquiries have their own path.

## 2. Positioning and voice

Working positioning: **A digital design and development partner for businesses and organisations.**

Lead with the three known offers: websites, platforms, and business systems. Explain those in everyday language before introducing technical detail. Use sector-specific language on relevant solution pages. Church leadership imagery, pastoral language, membership recruitment, and future gatherings move into the Network or church-specific pages.

Proposed homepage copy, subject to editorial review:

> Built for the way your business works.
>
> We design and build websites, platforms, and systems for businesses and organisations—including churches.
>
> Explore our work / Start a project

The headline supplies character; the supporting sentence states the offer directly. Keep this headline stable rather than cycling through competing messages. The final wording should match the confirmed scope of the team’s actual delivery capabilities.

Voice: clear, capable, direct, and human. Write about the client’s task: enquiries, bookings, content, customer access, or internal workflows. Avoid vague transformation claims, invented performance figures, blanket AI promises, and inflated descriptions of the company’s size.

## 3. Creative direction

Recommended direction: **Precision with personality.**

Create a confident design and development company identity using an off-white canvas, deep navy typography, blue actions, a small gold accent, and large, sharply composed project screens. Use the upward shape and curved cut in the Ascend mark as a source for a restrained graphic language: ascending alignment, directional rules, and an occasional curved line. Keep the logo itself intact.

The homepage should feel composed before any animation begins. Its distinction comes from the relationship between type, space, real work, and purposeful motion. Avoid a repeated grid of interchangeable cards. Mix a strong opening composition, full-width project imagery, compact editorial rows, and one dark technical demonstration section.

Alternative directions considered:

| Direction | Character | Assessment |
| --- | --- | --- |
| Precision with personality | Light canvas, navy type, blue actions, small gold details, real interfaces | Recommended: supports both business credibility and creative craft |
| Bold blue studio | Large blue fields, oversized white type, dramatic project compositions | Useful as an occasional campaign or closing section; too much would overwhelm the work |
| Quiet corporate | White, conventional split layouts, conservative typography | Legible and familiar, but offers less distinction for a company selling design and development |

### Reference principles

These are references for specific principles, not templates to reproduce:

- [Work & Co](https://work.co/): direct design-and-technology positioning, with work and expertise as central routes. Apply that clarity to Ascend’s own offer.
- [Instrument](https://www.instrument.com/): clear Work / Services navigation and a recent-work presentation. Apply the close connection between capabilities and evidence.
- [Linear](https://linear.app/): showing interfaces and workflows to explain an abstract system. Apply this only in a clearly labelled Ascend capability illustration, using our own visual language.

These references were reviewed for their published content and information structure. Their palettes, effects, copy, and client claims are not part of this proposal.

## 4. Identity and visual system

### Logo audit

The four supplied files are in `assets/`:

- `WhatsApp Image 2026-11-05 at 3.55.41 PM.jpeg`: blue-and-gold symbol on black.
- `WhatsApp Image 2026-11-05 at 3.55.41 PM (1).jpeg`: blue-and-gold symbol on white.
- `WhatsApp Image 2026-11-05 at 3.55.40 PM.jpeg`: navy horizontal wordmark on black.
- `WhatsApp Image 2026-11-05 at 3.55.40 PM (1).jpeg`: blue-and-gold symbol with a white horizontal wordmark on black.

The navy-on-black file has poor contrast for a site header. The isolated symbol files also contain substantial blank margins. Keep all source images untouched. Prepare cropped, optimised logo derivatives for the header, footer, social preview, and favicon. Prefer a faithful vector master if available; do not use generative imagery to recreate the logo. Any vector reconstruction must be checked against the supplied geometry and lettering.

### Working colour tokens

Values below are proposed web tokens. The first three approximate sampled logo colours; they are not claimed to be an official brand specification. Masked pixel sampling across the JPEGs found blue near `#074DA5`–`#074DA6`, gold near `#EAB829`–`#EABA2A`, and the navy wordmark near `#000E3F`.

| Token | Value | Intended use |
| --- | --- | --- |
| Brand blue | `#074DA5` | Primary actions, active states, selected graphic fields |
| Brand navy | `#000E3F` | Main text, header identity, dark feature sections |
| Brand gold | `#EABA2A` | Small directional details and selected emphasis |
| Paper | `#F7F8FA` | Main canvas |
| White | `#FFFFFF` | Interface surfaces and image frames |
| Pale blue | `#EDF2F8` | Quiet capability and solution backgrounds |
| Secondary text | `#566174` | Supporting copy, subject to contrast checks |
| Rule | `#D9DFE8` | Dividers and nonessential boundaries |

Most of the screen stays neutral. Blue establishes hierarchy; gold is scarce. Gold should carry dark navy text when used as a filled control, and should not be used for small text on white. Meaning must remain clear without colour. Verify actual text and control contrast during implementation.

No linear, radial, or conic gradients. Avoid photographic gradient overlays too: place text in solid caption areas or adjacent columns. Photography retains its natural lighting.

### Typography and composition

Use Manrope for both display and body text, with deliberately different weights and spacing. Its clean forms give us a coherent system without a large font payload. Use IBM Plex Mono sparingly for project indices and small diagram labels. Test the combination in the opening composition before extending it through the site.

- Large, sentence-case headings with controlled line breaks; approximately 72–104px on wide desktop and 40–52px on mobile.
- Body copy around 17–19px with comfortable line height and a readable measure.
- A 12-column desktop grid with generous outer margins, a compact tablet adaptation, and a genuinely composed single-column mobile layout.
- Corners mostly square or gently rounded. Save rounded pills for small categories, where useful.
- Fine rules, consistent spacing, and subtle image framing replace ornamental shadows and excessive panels.
- A single icon family with consistent stroke weight. Label actions rather than relying on abstract icons alone.

## 5. Information architecture

Primary navigation: **Work · Services · Solutions · About**, with **Start a project** as the principal action. The logo returns home. Place **Network** as a smaller, visible secondary link in the desktop header and as a distinct secondary group in mobile navigation. Include Insights in the footer until there is enough real material to justify a primary link.

Keep dropdowns compact. Services contains the actual offer; Solutions contains audiences and their needs. Use click, keyboard, and touch interaction consistently. The mobile menu should expose this same structure without a dense mega-menu.

| Area | Pages and purpose |
| --- | --- |
| Home | Positioning, selected work, core capabilities, practical process, project enquiry |
| Work | Curated portfolio index with real categories and complete project pages |
| Project detail | Brief, verified scope and role, screens, design decisions, outcome where substantiated, related work |
| Services | Overview plus Websites; Platforms & Web Applications; Business Systems & Integrations |
| Solutions | Business & Professional Services; Property & Real Estate; Churches & Ministries |
| About | Company approach, actual team and roles, values demonstrated through working practices |
| Contact | Start-a-project form, general enquiries, verified contact details |
| Network | Overview, membership, Roundtable, Experiences, and Network-specific enquiry |
| Insights | Only publish real, useful articles or resources; no empty article library |
| Legal | Privacy and any other policies required by the final form, analytics, or service setup |

Service categories are based on the user’s brief. Specific examples such as portals, booking flows, admin tools, integrations, and maintenance need to match actual delivery capacity before they become published promises. Existing branding, content, marketing, video, and church-media offerings should be inventoried: retain confirmed active services in a supporting category, rather than silently deleting them or letting them dilute the lead offer.

Industry pages describe relevant needs, examples, and suitable work. They should not invent sector expertise or use the same copy with a different heading. New sector pages can be added once there is enough evidence and substance.

## 6. Homepage, section by section

### Opening screen

A crisp light header, the actual Ascend identity, and a large navy headline on off-white. Pair the headline and two clear actions with a generous project stage that shows a genuine business project. A small project caption identifies the client and the verified type of work.

On desktop the text takes roughly five columns and the project stage seven. A thin gold directional line adds character without becoming a second logo. On mobile, keep the proposition and primary action immediately visible; a recognisable portion of the project stage should follow in the first screen on common devices. Test rather than force a fixed hero height.

The stage can offer manual project selection using three clearly labelled controls. Initial candidate order: Rengovtech Dubai, Cire Homes, and Springs Gate Chapel, subject to asset quality and permission checks. This introduces business breadth immediately and includes church work within the selection. No automatic carousel or movement that interrupts reading.

### Selected work

Show three or four well-edited projects early. Use large imagery and varied composition rather than six identical thumbnails. Every entry links to a real project page. Keep categories factual: a website screenshot demonstrates website work, not an undocumented enterprise platform build.

### What we build

Three substantial editorial rows: Websites; Platforms & Web Applications; Business Systems. Each explains the problem addressed, likely scope, and next step. Link to a detailed service page and suitable work where it exists. Additional services sit beneath this primary offer.

### How the pieces connect

One dark navy section uses a small interactive workflow to make “systems” concrete: an enquiry enters a queue, is assigned, and appears in an operational view. Build this as accessible HTML/SVG with three deliberate states, solid fills, and optional interaction. Label it **Illustrative workflow**. It must never appear to be a live client system or a completed project.

On mobile the steps become a readable stack. A static representation works without animation or JavaScript.

### Built around your organisation

A concise, equally weighted set of routes for businesses, property companies, and churches/ministries. Use plain descriptions of their tasks. The homepage remains useful to a business owner with no church affiliation.

### How we work

Four steps: Understand; Define; Design & Build; Launch & Support. Show what the client contributes and receives at each step. Describe post-launch support only to the extent actually offered. Avoid unsupported turnaround guarantees.

### About and trust

A brief, concrete company introduction with genuine team imagery if available. Verified testimonials, approved client logos, or documented outcomes can strengthen this section. Without those, use transparent project scope and clear delivery practices. Do not fill the gap with invented numbers or generic partner badges.

### Close

A direct invitation: **What do you need to build?** Link to the project brief. A modest Network introduction can appear near the footer, with its own purpose and destination. The footer groups company, services, solutions, Network, and verified contact details.

## 7. Interior-page depth

Every major template should have its own composition while sharing navigation, type, spacing, and controls.

- **Work index:** large first project, useful filters only if the inventory supports them, visible categories, and normal links to case studies.
- **Case study:** project identity; brief; Ascend/founding-team role; scope; screen gallery; decisions; supported results; related work; enquiry. Short factual project profiles are acceptable when interviews or results are unavailable.
- **Service:** client problem; what is included; example interfaces or real relevant work; delivery approach; service-specific FAQ; enquiry.
- **Solution:** recognisable sector tasks; applicable services; relevant work; enquiry. Church-specific services and vocabulary belong here.
- **About:** company story, actual people, method, and values expressed through practice. No generated staff portraits.
- **Contact:** a single working project-intake flow. Collect name, organisation, email, project type, and brief; budget band and timing can be optional with an “unsure” option. Link to privacy information and show useful success/failure states.
- **Network:** a coherent secondary area using the shared brand with more human photography. Preserve the membership and gathering content after validating its status. Dates, seats, prices, and application claims from the old demo are not automatically current.

## 8. Asset and content strategy

Retain original project pixels when showing delivered work. Improve their presentation through framing, scale, crops, captions, and responsive device context. A proposed redesign of a client project must be explicitly labelled as a concept and kept separate from the delivered-work gallery.

Current assets include website captures for Rengovtech Dubai, The Base Marketing, Springs Gate Chapel, Cire Homes, Recharge Global, and Faircross. They support a broader portfolio than the previous church-led opening suggested. Existing demo attribution identifies them as founding-team work; preserve that distinction until authorship and company attribution are confirmed. Do not repeat the older “47 websites” claim without verification.

Priorities:

1. Prepare faithful logo assets and accessible light/dark applications.
2. Inventory project dimensions, attribution, usage permissions, available URLs, and genuine scope.
3. Obtain higher-resolution project captures where possible. The inspected Rengovtech and Cire images are 880px wide: useful previews, but limited for large, highly detailed presentation.
4. Build original browser/device frames in HTML/CSS and use vector diagrams for system explanations.
5. Use team and workplace photographs only when authentic and relevant.
6. Generate supporting editorial imagery only when it adds meaning. Never generate client proof, testimonials, project screens presented as delivered work, or company staff.
7. Optimise image sizes, provide alt text, prioritise the hero image, and lazy-load lower content.

No image generation is needed to approve the direction. The first design pass can be distinctive using the logo, real work, typography, and a custom workflow illustration.

## 9. Motion and interaction

Motion should explain the composition and respond to intent. Keep the page readable immediately.

- Opening: headline lines settle into place, the real project screen reveals cleanly, and one gold directional stroke draws once. Target a composed entrance within roughly 1.2 seconds, with no loading gate.
- Project selection: a short crossfade or directional slide, triggered manually. Labels remain stable and controls work with a keyboard.
- Work cards: restrained image movement and a clear action on hover and focus.
- Service rows: reveal detail on selection using controls that expose their expanded state.
- Workflow: user-triggered step changes, with a static equivalent and a clear illustrative label.
- Menus: quick, predictable entry; Escape closes and focus returns to the trigger.
- Scrolling: a small number of section reveals. Reading and scrolling remain native.
- Reduced motion: remove entrance transforms, parallax, path drawing, and transitions; preserve all content and controls.

Avoid cursor replacements, continuous logo marquees, autoplay video, constant floating panels, scroll-jacking, and decorative particle fields. These would compete with project evidence and add cost to the mobile experience.

## 10. Build approach and migration

Continue in the current `demo` repository. Preserve the existing pitch through Git history before substantial implementation. Replace the current visual layers with an intentional token/component structure rather than stacking more overriding styles on top.

The existing static Python generator and GitHub Pages workflow can deliver this marketing site. Keep shared page templates and move project/service content into structured data so repeated pages are easy to maintain. Framework migration is unnecessary unless editing requirements, integrations, or authenticated platform features justify it. The website markets systems; it does not need to contain the clients’ systems.

A static front end can host on GitHub Pages, but a real enquiry form requires an agreed external delivery service or backend. Keep credentials out of browser code. Test receipt and failure handling before describing the form as live. If a content-management interface becomes a requirement, choose that approach before implementing the article library.

Keep a route migration table. Proposed primary routes include `/work/`, `/work/project-slug/`, `/services/`, `/solutions/`, `/about/`, `/contact/`, and `/network/`. Existing demo URLs such as `/portfolio/`, `/work-with-us/`, church/property pages, and old service fragment links must resolve to useful destinations or explicit compatibility pages. GitHub Pages cannot provide arbitrary server-side HTTP redirects; use static compatibility pages there. Production-domain redirects depend on the final host.

Do not replace or publish the original live site as part of this planning task.

## 11. Delivery sequence

| Stage | Concrete deliverable | Completion condition |
| --- | --- | --- |
| 1. Content and evidence | Asset inventory, confirmed service list, project facts, route map | Every planned section has real content or a clearly identified dependency |
| 2. Design foundation | Logo applications, colour/type tokens, header, buttons, desktop/mobile hero | First screen communicates the broader offer and establishes the new identity |
| 3. Core presentation | Complete homepage, Work index, one real case-study template, one service template | The main visitor journey works end to end with convincing content |
| 4. Full site | Remaining projects, services, solutions, About, Contact, and secondary Network | Every navigation destination has complete, relevant content |
| 5. Motion and finish | Coordinated interactions, responsive imagery, reduced-motion treatment | Effects strengthen the composition without blocking access or reading |
| 6. Launch preparation | Functional enquiry delivery, SEO metadata, route compatibility, accessibility and performance checks | Production checks pass and hosting/contact decisions are resolved |

Implement motion alongside the relevant components, then refine its timing in stage 5. No need to build the entire old site before establishing whether the new design foundation works.

## 12. Acceptance criteria

- A first-time visitor can identify websites, platforms, and systems as the main offer from the opening screen.
- Business work is immediately visible; churches receive a relevant, dedicated path.
- The new supplied logo is used legibly, with blue/navy/gold working consistently.
- There are no decorative gradients in backgrounds, text, overlays, borders, or illustrations.
- Every visible navigation item, project link, filter, and enquiry action works.
- Every project is attributed accurately. Concept imagery is distinguishable from delivered work.
- Network membership and Experiences are reachable without dominating the company message.
- Keyboard navigation, visible focus, useful headings, alternative text, form labels, contrast, and reduced-motion behavior are verified.
- Layouts are checked from 320px mobile through wide desktop, including long headings, navigation, diagrams, and case-study images.
- The hero uses appropriately sized media and stable layout dimensions; target Core Web Vitals of LCP ≤2.5s, CLS ≤0.1, and INP ≤200ms. These are implementation targets, not current measured results.
- Root-domain and repository-subpath links work. Any old routes retained by the redesign have an explicit destination.
- The production enquiry flow is verified through actual delivery before launch.

## 13. Items to resolve during content preparation

These do not block the proposed visual direction:

- Which platform/system capabilities and supporting creative services the team currently delivers.
- Which existing projects can be published, the exact scope and authorship of each, and whether higher-resolution captures are available.
- Actual company/team details, approved contact channels, and any verifiable testimonials.
- Current membership and event status, including whether old planned dates still apply.
- Enquiry destination, final production host, analytics needs, and content-editing responsibility.

The first implementation milestone is a complete new homepage plus one business case study and one service page, at desktop and mobile sizes. This gives the full-site design a concrete foundation before it is extended across the remaining pages.
