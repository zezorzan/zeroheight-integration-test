# Hero Offer

Hero Offer is the highest-visibility **promotional** card in the Magic App home hero slot. It presents a single strategic product opportunity—upsell eligibility, a major relaunch, or a market-differentiator limited-time offer—with a full-bleed visual asset, title, description, tap action, and dismiss control. It replaces the legacy **NBA** (Next Best Action) promotional slot and is temporary by design: awareness is the primary goal.

Keywords: hero offer, promotional banner, magic app, home hero slot, upsell, limited time offer, nba replacement

## Anatomy

1. **Container:** Groups all elements. Fixed height 192px at default text scale (240px from 160%–190% text scaling). Full width minus outer horizontal padding. Corner radius `border.radius.geometry.xlarge` (24). Border 1px `color.border.default`. Elevation `[Magic] Elevation / Default`. Clips overflow.
2. **Asset:** Full-bleed background media at **21:9** aspect ratio. Supports static image (V3.0), Rive animation (V3.1), and video (V3.2 — not shipped). Progressive blur starts at 50% image height and reaches **12dp / 6px** at the bottom edge. Decorative — excluded from screen readers.
   - **Fallback asset:** Static image shown while the primary asset loads or after playback failure (required for Rive/video).
3. **Scrim:** Gradient and inner-shadow overlay that tints with `scrimColor` and blends the asset into the content zone for text contrast.
   - **Bottom gradient:** Linear, 180°. Stops: 0% and 30% = `scrimColor` at 0% opacity; 60% = `scrimColor` at 100%.
   - **Inner shadow:** X 0, Y −12, blur 20, spread −4, color `scrimColor`, type inner.
4. **Content BB:** `BB / Hero Offer Content BB` — title + description text stack anchored to the bottom content zone.
5. **Dismiss Button:** `[Magic] Icon Action` with `close_mini` icon, absolute top-right. Tap target 48×48 (inherited). Gives the customer control to permanently opt out of the specific offer.

## Properties

**Type / Light Background | Dark Background**

Defines the starting point for the banner's color scheme, along with the Icon Action dismiss variant. **Default: Dark Background.**

- **Light Background** — Starting scrim: lighter decorative surface (e.g. `color.surface.decorative.05.subtle`). Starting content: darker decorative token (e.g. `color.content.decorative.05`). Dismiss: Icon Action **Type = Secondary**, Container = True.
- **Dark Background** — Starting scrim: saturated decorative surface (e.g. `color.surface.decorative.05`). Starting content: `color.content.on.color`. Dismiss: Icon Action **Type = On Color**, Container = True.

After choosing `Type`, pick **Scrim** and **Content** colors in Figma Selection Colors using **primitive tokens** so they visually match the asset.

**Scrim Color / primitive color token (required)**

Tints both scrim layers (bottom gradient + inner shadow). Choose a primitive token that visually matches the bottom edge of the asset so the scrim blends seamlessly into the content zone.

**Content Color / primitive color token (required)**

Applied to both Title and Description in the Content BB. Description renders at **80% opacity** of this token. Default starting points by `Type`:

- Light Background → `color.content.decorative.05`
- Dark Background → `color.content.on.color`

**Content / BB / Hero Offer Content BB (required)**

Title and description text stack. Refer to **Content BB** for nested text properties.

- **Title** — Style: `[Magic] Subtitle / Medium / Strong` (18px). Max **2 lines**, ellipsis.
- **Description** — Style: `[Magic] Label / Small / Default` (14px). **80% opacity**. Max **2 lines** at default scale (max **3 lines** from 110% text scaling), ellipsis.

**Asset / image | Rive | video (required)**

Full-bleed background at **21:9** aspect ratio. V3.0 = static image. V3.1 = Rive animation. V3.2 = video (rolled back; future).

**Fallback Asset / image (required when Asset is Rive or video)**

Static 21:9 image for loading and failure states. Show immediately if the primary asset is not ready on first paint.

**Loop Count / 1 | 3 | null (optional)**

Rive playback loops. `null` = loop indefinitely. Default: loop indefinitely.

**On Pressed / callback (required)**

Opens the offer destination (marketing screen, flow, etc.). The entire card body except dismiss is tappable.

**On Dismiss / callback (required)**

Permanent opt-out for this specific offer. Triggers governance suppression (see Usage).

## Usage

Hero Offer occupies the **hero slot** on Magic App Home — priority **#2** in that slot. When an active **Hero Callout** (critical alert) exists, Hero Offer is suppressed until the callout is cleared or dismissed.

### When to use

Use only for **highly relevant promotional opportunities** approved under [Hero Offer Governance](https://nubank.atlassian.net/wiki/spaces/FCB/pages/265015759544/Hero+Offer+-+Governance+Definition):

- First-time upsell eligibility (Ultraviolet, Nu+, regular Credit Card republish, PJ Account)
- Major product relaunch with structural journey changes
- Market-differentiator **Limited Time Offers** approved by BR Segments PF / CLOs & Marketing

Primary role is **awareness** of strategic products. Conversion is secondary.

### When not to use

- Critical alerts, recommended actions, onboarding blockers → **Hero Callout**
- Behavioral insights or advisory content → **AIPB Hub** / **AIPB 2nd/3rd Levels**
- Routine retargeting, cross-sell, brand delight, marketplace, B2B ecosystem, or non-proprietary Nubank products
- Always-on or overlapping campaigns (max **1 Hero Offer campaign per customer per month**)

### Placement

- Single instance in the **home hero slot**, above the widget grid
- Never coexists with an active Hero Callout in the same session

### Hierarchy

Hero Callout (#1) always wins the hero slot. Hero Offer appears only when no Hero Callout is active.

### Picking Scrim and Content colors

1. After defining the **Asset**, choose **Scrim** and **Content** colors in Figma **Selection Colors** using **primitive tokens**.
2. Colors should visually match the asset so the scrim appears to blend seamlessly into the content zone.
3. Apply the same **Content Color** token to both Title and Description (description renders at 80% opacity).

### Checking contrast

1. Every Scrim + Content pair must meet **WCAG AA** (minimum **4.5:1** contrast ratio).
2. Always test **Content at 80% opacity** — this is the worst case (description).
3. Use Figma's color picker contrast check (Normal Text ✓ AA).
4. If it fails, choose a more contrasting primitive for Scrim or Content until it passes.

### Safe defaults

- Pairs with **≥5 shade steps** between scrim and content usually pass (e.g. scrim `color.purple.30` + content `color.teal.80` at 80%).
- Light scrim (shade ≤30): content `color.gray.100` at 80%.
- Dark scrim (shade ≥60): content `color.white.alpha.white` at 80%.

### Campaign lifecycle (governance)

| Rule | Value |
| --- | --- |
| Campaigns per customer per month | **1** |
| Max impressions (sessions) per campaign | **5** |
| Campaign duration from first exposure | **7 days** |
| Dismiss | Permanent suppression for that specific offer |
| Awareness signal (click, dismiss, omnichannel interaction, downstream product screen view) | Permanent removal for that offer |
| Conversion | Permanent removal |

These rules will be reviewed in **H2 2026** through A/B testing on saturation before day 7 or the 5-session limit.

## Do's and Don'ts

**Do:**

- Match scrim and content colors to the asset palette using primitive tokens
- Test contrast at **80% description opacity** before handoff
- Use for first-time upsell eligibility or approved LTO campaigns only
- Provide **fallbackAsset** whenever using Rive (or video in future)
- Respect **1 campaign / month** and **5-session / 7-day** caps
- Let Hero Callout take the slot when a critical alert is active

**Caution:**

- Rive assets — stream from S3 at runtime; include a feature flag to fall back to static image
- Custom color pairs — validate in Figma even when runtime contrast resolution exists in engineering builds
- Long copy — title and description truncate with ellipsis; keep copy concise

**Don't:**

- Use for routine cross-sell, brand moments, marketplace, or non-proprietary products
- Pick scrim/content tokens unrelated to the asset (breaks the seamless blend)
- Test title-only contrast at full opacity (description at 80% is the worst case)
- Force Hero Offer above an active Hero Callout
- Ship Rive without a static fallback asset

## Behavior

### Interactions

- **Card tap** — fires `onPressed`; opens offer destination. Standard card press feedback.
- **Dismiss tap** — fires `onDismiss`; Icon Action press feedback. Permanent opt-out for the offer. No card-level dismiss animation.

### Animations

- **Rive load failure → fallback:** opacity crossfade, **350ms**, easing `cubic-bezier(0.26, 0.82, 0.53, 0.98)`.
- **Entry / exit** — governed by campaign orchestration (Purple Hub), not component-level motion tokens.

### Scrolling

Hero Offer lives in the fixed hero region on Home; it scrolls with the page layout like other hero-slot content.

### Responsiveness

- **Asset loading** — show `fallbackAsset` immediately if primary asset (Rive) is not ready. Prioritize TTFD < 1s on Home. No continuous retry after failure.
- **Pull-to-refresh (cached Rive)** — render Rive immediately; skip fallback to avoid flicker.
- **Suppressed states** — not rendered when Hero Callout is active or governance exit criteria are met.

### Contrast validation (runtime)

Teams may pass any primitive tokens for `scrimColor` and `contentColor`. At runtime, the component validates the pair against WCAG AA (≥ 4.5:1):

- **Valid pair** — renders as configured.
- **Invalid pair** — logs an error with actual ratio, required minimum, and suggested safe color.

Safe color resolution walks the content color palette toward a passing step; if none pass, falls back to `color.white.alpha.white` or `color.black.alpha.black` (whichever yields highest contrast). See handoff **Contrast Validation** for the full algorithm.

**Information missing:** Whether invalid pairs are auto-corrected at runtime or log-only in current production builds — confirm with Engineering.

## Content

- **Title** — One clear line explaining the offer. Write for **awareness**, not hard conversion.
- **Description** — Who the offer is for and why it matters **now**. Optional but recommended.
- **Voice** — Direct, helpful, customer-centric. Avoid jargon.
- **Length** — Design for truncation: title max **2 lines**, description max **2 lines** (3 from 110% text scaling). Purple Hub enforces character limits at campaign setup.

**Information missing:** Exact Purple Hub character caps for title and description in the current production API — confirm with Purple Hub / CLO Horizontals.

## Accessibility

### Color contrast

- Title + description on scrim must meet **≥ 4.5:1** (WCAG AA). Always test description at **80% opacity**.
- Do not rely on asset contrast alone; scrim + content color carry readability.
- Validate pairs in Figma before handoff using the Usage contrast workflow.

### Text wrapping

- **Title:** max 2 lines, ellipsis.
- **Description:** max 2 lines at default scale; max **3 lines** from 110% text scaling; ellipsis; 80% opacity.

### Text scaling

Component adapts starting at **110%** system text scale:

- **110%–150%:** Description max lines increased to **3**. Container height stays **192px**.
- **160%–190%:** Container **height** increased to **240px**.

### Screen reader labeling

- **Focus order 1 — Card:** Merged semantics `{Title} + {Description}`. Trait: **button**. Announcement: `"{Title}. {Description}. Button."` Asset is **excluded** (decorative).
- **Focus order 1.1 — Dismiss:** Label **"Dismiss"**. Trait: **button**. Announcement: `"Dismiss. Button."`
- Card body and dismiss each have independent tap targets. Dismiss meets **48×48** minimum via Icon Action.

Standards: WCAG 2.2 — **1.4.3** (contrast), **2.5.5** (target size 48dp).

## Internationalization

- Copy is authored per locale in Purple Hub / campaign tooling; the component displays whatever strings are passed to Content BB.
- Plan for **text expansion** in longer locales — truncation rules still apply (ellipsis after max lines).
- Numeric or date content in descriptions should follow locale formatting at the content source, not inside the component.

**Information missing:** RTL layout behavior and locale-specific asset swap rules — confirm if Hero Offer ships in RTL markets.

---

**Sources**

- Figma component: [NuDS v3 — `[Magic] Hero Offer`](https://www.figma.com/design/RxzAEZlmQX8Outs7RYQWw2/-WIP--NuDS-V3-%E2%80%93%C2%A01st-Level?node-id=8141-487)
- Figma usage: [Picking scrim/content, contrast, safe defaults](https://www.figma.com/design/RxzAEZlmQX8Outs7RYQWw2/-WIP--NuDS-V3-%E2%80%93%C2%A01st-Level?node-id=8306-574)
- Figma handoff: [NuDS Magic App — Hero Offer](https://www.figma.com/design/bgOjXshhmdDwyio21Pd7pa/NuDS-Magic-App-%E2%80%93-Handoff?node-id=26152-2237)
- Governance: [Hero Offer — Governance Definition](https://nubank.atlassian.net/wiki/spaces/FCB/pages/265015759544/Hero+Offer+-+Governance+Definition) (APPROVED, Feb 2026)
- Draft author: Zé Zorzan · Skill: nuds-component-properties v0.2.0 · 2026-08-19

**Note:** The Handoff **Overview** frame still contains Hero Callout copy in error. This page follows **Anatomy, Properties, Usage (Figma), Accessibility, and Governance** as canonical sources for Hero Offer intent.
