# Android and mobile: the category template, what to keep, what to make yours

Mobile apps have a stronger "default look" than the web because the platform ships one: Material 3 on Android, Human Interface Guidelines on iOS. Nearly every AI-generated Android app is the Android Studio template with the labels changed. This reference says exactly what that template is, which parts are platform convention (keep), and where a product earns its own identity.

## The Android template (what "common" looks like)
- `Scaffold` with a default `TopAppBar`, a `NavigationBar` with 3 to 5 stock Material icons, and a `FloatingActionButton`.
- `LazyColumn` of `Card`s, each with a title, a subtitle and a trailing icon. Cards for everything, including things that are not cards.
- Colours straight from the template `Color.kt` (Purple80 / Purple40 family) or from the Material Theme Builder with the seed left at default; `dynamicColor = true` so the brand is whatever the wallpaper decides.
- `Typography()` untouched: Roboto everywhere, default sizes, no display face.
- Default `Shapes`: 12 dp corners on every surface.
- Stock Material icons only; the green-robot launcher icon; no illustration or imagery of the product's own.
- No motion beyond what the components do themselves; default navigation fades.
- Copy: "Welcome to <App>", "Get started", "No items yet", lorem or `Greeting("Android")` still in the tree.
- Every screen the same density; no screen has a single thing you remember.

Run `scripts/template_signature_android.py <project>` to measure this; COMMON (40 or more) means redesign.

## Keep: platform conventions users rely on (Jakob's law)
- System back (gesture and button) always works and goes where the user expects; predictive back supported.
- Touch targets at least 48 × 48 dp; primary actions in the thumb zone (bottom third) on phones.
- System bars respected (edge-to-edge with insets), status bar legible on your surfaces.
- Text scales with the user's font size setting; layouts survive 200 % font scale.
- Standard gestures: pull to refresh where lists refresh, swipe where the platform swipes, long-press for context.
- Accessibility: content descriptions, TalkBack order, focus, contrast ≥ 4.5:1 for text, reduced motion via animator duration scale.
- Material components may be used for mechanics (sheets, dialogs, text fields, snackbars). Convention is in behaviour, not in looking stock.

## Make yours: where identity lives on mobile
| Layer | Template habit | Decision to make deliberately |
|---|---|---|
| Colour | Seed colour + dynamic colour | A role-based palette of your own (surface model, one accent with a job, status colours), contrast computed. `dynamicColor` off unless the product's job is to blend with the system. |
| Type | Roboto defaults | A display face with a voice for titles and large numbers, a text face for reading; a 6-step scale with a ratio; tabular figures for data. Licence recorded; font files bundled. |
| Shape | 12 dp everywhere | A shape system that means something: sharp for data, soft for people, one signature shape used sparingly. |
| Layout | Column of cards | Hierarchy per screen: one primary element, lists as lists (dividers, grouping by spacing), tables as tables, a hero element only where there is one thing to show. Asymmetric compositions are allowed on mobile too. |
| Navigation | Bottom bar + FAB | The structure users need: 3 destinations might want a bottom bar; 2 might want tabs; a single-task app might want none. Decide from the IA, not the template. |
| Iconography | Stock Material | Material for system actions; your own set (same grid, stroke and corner language) for product concepts. |
| Imagery | None or stock illustration | Real product content, real data, diagrams of the real thing, photography with a consistent treatment, or none. |
| Motion | Component defaults | A motion signature (`motion-standards.md`): shared-element transitions between list and detail, one emphasised easing, one duration scale, one memorable moment (first launch, task completion). Respect animator duration scale. |
| Copy | "Welcome to", "Get started" | The user's words; the first screen states the job, not a greeting. Every empty, error and loading state written. |
| Launcher icon and splash | Default robot | A mark from the brand, tested at 48 dp and in adaptive icon masks; splash screen uses the brand, not the default. |
| Density and rhythm | Same everywhere | Dense where users scan (lists, data), airy where they decide (confirmations, onboarding). |

## Psychology on a phone (apply from `layout-psychology.md`)
- Hick's law: one primary action per screen, in the thumb zone. Bottom bars with 5 items plus a FAB plus a top-bar action menu are three competing action groups.
- Fitts's law: primary action large and near the thumb; destructive actions away from it and confirmed.
- Gestalt proximity: group with spacing before you group with cards; a card is for a unit the user picks among peers.
- Progressive disclosure: onboarding asks for one thing per screen; permissions requested in context, with the reason, at the moment of use.
- Visibility of status: optimistic UI for local changes; skeletons over spinners for lists; explicit success states.
- Peak-end: design the completion moment (the "done" screen or animation) and the first launch; these are what users remember and rate.
- Serial position: first destination in the bottom bar is the primary job; last is the profile/settings.

## Research steps specific to apps
1. Install or capture at least three direct competitor apps (Play Store screenshots are acceptable when install is not possible; record the URL and date) and two adjacent apps known for distinct design; add one non-digital reference (a printed ticket, a paper form, a dashboard in a car, a game board) that solves the same job.
2. For each: navigation structure, first-screen hierarchy, type, colour, shape, iconography, motion, how empty and error states look, onboarding length, what they do well and badly.
3. Pattern map as in `design-research-method.md`; add "platform default" as a row so the Material baseline is explicitly named as part of the category template.
4. Three directions as Compose previews or static frames at 360 × 800 dp and a 200 % font-scale variant; the score table includes thumb-zone reachability and font-scale survival.

## Proving it on Android
- `template_signature_android.py` before and after.
- Screenshots (emulator or device) of each main screen at default and 200 % font scale, light and dark, plus TalkBack order notes.
- Motion table with the animator-duration-scale fallback tested at 0 ×.
- Swap test with the three competitors' screenshots, app names hidden.
- Accessibility Scanner or Compose UI test semantics checks; results pasted.
