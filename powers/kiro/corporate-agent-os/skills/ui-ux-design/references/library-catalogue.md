# Library catalogue: motion, components, icons, logos, fonts, 3D, cursors

Verified 2026-11-18 (`npm view` and GitHub licence API). Re-verify version and licence before adopting; record the choice and licence in `08-legal-oss/component-register.md`. Picking a library is a design decision made in the research record, not a default: the question is always "which tool serves this product's motion signature / component needs / iconography language", never "which is popular".

## How to choose (in this order)
1. **Need first.** From the motion table (`motion-standards.md`) and the element decisions (`page-logic-crawl.md`): what exactly must move, what components are actually needed, which icon concepts exist. No library is added for a capability no element needs.
2. **Stack fit.** React / Vue / Svelte / vanilla / Android / iOS. Bundle budget stated in the performance plan.
3. **Licence fit.** Commercial use, redistribution, attribution. Anything without a licence file is not used.
4. **Ownership of look.** Prefer unstyled or low-opinion libraries (primitives, animation engines) over styled galleries. Styled galleries are the fastest route back to the template centre (`slop-mechanics.md`). If a gallery component is used, it is re-skinned with the project's tokens and its default motion is replaced by the motion table's.
5. **Record** library, version, licence, why, and what it is used for.

## Animation engines
| Library | Version | Licence | Stack | Use for | Caution |
|---|---|---|---|---|---|
| [Motion](https://motion.dev/) (`motion`, formerly Framer Motion) | 14.14 | MIT | React, vanilla JS, Vue | Layout and shared-element transitions, gesture-driven motion, spring physics, scroll-linked progress, `AnimatePresence` for exit animations. Best default for React product UI. | Avoid its examples' default spring on everything; define two or three easings as tokens and use those. |
| [GSAP](https://gsap.com/) (`gsap`) | 3.15 | GSAP Standard "no charge" licence (free incl. commercial since the Webflow acquisition; plugins included) | Any | Orchestrated timelines (one page-load sequence), ScrollTrigger for a single explanatory scroll moment, SplitText for typographic reveals, Flip for list reorder, MorphSVG for a logo or diagram that transforms. | Read the licence text; not SPDX MIT. Scroll-scrubbed decoration is still slop; use ScrollTrigger for explanation, once. |
| [anime.js](https://animejs.com/) (`animejs`) | 4.5 | MIT | Vanilla, any framework | Lightweight timelines, SVG line drawing (stroke-dashoffset), staggered reveals, draggable. Good when React is not present or the bundle must stay small. | |
| [Lenis](https://github.com/darkroomengineering/lenis) (`lenis`) | 1.3 | MIT | Any | Smooth scroll only when the product's job is an editorial or narrative read and the owner approved; pairs with GSAP ScrollTrigger. | Breaks native scroll expectations (Jakob's law); never on tools, dashboards or forms. |
| [Lottie](https://airbnb.io/lottie/) (`lottie-web`, `lottie-react`) | 5.13 / 3.1 | MIT | Any | Designed vector animation (After Effects or Figma export): a brand moment, an empty-state illustration that moves once, a success confirmation. | Stock Lottie files from marketplaces are the template; animations must be the project's own. |
| [Rive](https://rive.app/) (`@rive-app/react-canvas`) | 4.39 | MIT (runtime; editor is a separate product) | Web, Android, iOS | Interactive state-machine animation: a mark that reacts to input, a character or control with states. | Needs the Rive editor to author. |
| CSS and Web Animations API | built in | n/a | Any | Feedback (100–200 ms), hover and press, focus, reduced-motion media queries. The right tool for most moments; libraries are for continuity, explanation and orchestration. | |
| Android: Compose `animate*AsState`, `AnimatedVisibility`, `AnimatedContent`, shared element (`SharedTransitionLayout`), `MotionLayout` for XML; Lottie Compose, Rive Android | platform | Apache-2.0 | Android | All in-app motion; honour animator duration scale. | |

## Component sources
| Source | Licence | What it is | Use |
|---|---|---|---|
| [Radix Primitives](https://www.radix-ui.com/) (`radix-ui`) | MIT | Unstyled accessible primitives (dialog, popover, menu, tabs, slider) | Default for React: accessibility done, no look imposed; every pixel comes from the project's tokens. |
| [Base UI](https://base-ui.com/) (`@base-ui-components/react`) | MIT (1.0 RC) | Unstyled primitives from the MUI/Radix/Floating UI team | Same role as Radix; check stability. |
| [Ark UI](https://ark-ui.com/) (`@ark-ui/react`, Vue, Solid) | MIT | Unstyled, state-machine-driven components, multi-framework | Vue and Solid projects. |
| [Floating UI](https://floating-ui.com/) (`@floating-ui/react`) | MIT | Positioning for tooltips, popovers, menus | When only positioning is needed. |
| [Magic UI](https://magicui.design/) | MIT (repo `magicuidesign/magicui`) | Styled, animated marketing components (shadcn-style, copy-paste) | Reference and raw material only. Any component taken is re-tokenised and its motion replaced; the default look is the exact template `template_signature.py` penalises. |
| [React Bits](https://reactbits.dev/) (repo `DavidHDev/react-bits`) | MIT + Commons Clause: use inside a product (incl. commercial) allowed; selling or redistributing the components, tools, sounds or exports themselves is not | Animated backgrounds, text effects, cursors, tools (Background Studio, Texture Lab, Sound Lab) | Allowed inside the product; record the licence in the component register. Backgrounds and text effects are decoration unless the motion table gives them a job; most will be rejected by the job test. |
| [21st.dev](https://21st.dev/) (community registry; motion collection at `/community/libraries/s/motion`) | Platform repo MIT; **each component has its own author and licence**: check per component | Registry of shadcn-style components incl. Motion-based ones | Browse for ideas and mechanics; copy only components whose individual licence allows it; re-tokenise. |
| [cursify](https://cursify.ui-layouts.com/) (repo `ui-layouts/cursify`) | **No licence file found (2026-11-18)** | Custom cursor effects | Do not copy code. Custom cursors are also a Jakob's-law break; only for a narrative site with a stated reason. |
| shadcn/ui, Tailwind UI, DaisyUI, MUI, Ant, Chakra | MIT / commercial | Styled systems | Permitted when the owner's stack already uses one; then tokens override the theme completely and the result must still re-score `DISTINCT`. Never introduced as the look. |

## Icons
| Set | Licence | Style | Use |
|---|---|---|---|
| [Lucide](https://lucide.dev/) (`lucide-react`) | ISC | 24 px stroke, 2 px | System actions. The most common AI default; use it for mechanics only and pair with a custom set for product concepts. |
| [Tabler Icons](https://tabler.io/icons) (`@tabler/icons-react`) | MIT | 24 px stroke, 5 900+ | Large coverage, same grid as Lucide. |
| [Phosphor](https://phosphoricons.com/) (`@phosphor-icons/react`) | MIT | Six weights (thin to fill, duotone) | When weight variation is part of the hierarchy. |
| [Simple Icons](https://simpleicons.org/) (`simple-icons`) | CC0-1.0 (the icons; the brands remain trademarks of their owners) | 3 300+ brand logos | Third-party brand marks (payment methods, integrations, social). Follow each brand's usage guidelines. |
| Material Symbols | Apache-2.0 | Variable (weight, fill, grade, optical size) | Android system actions. |
| Project icon set | yours | Same grid, stroke and corner language as the chosen system set | Product concepts that no generic set has. At least the five core concepts of the product get their own glyphs; this is where iconography becomes identity. |

## Logos and marks
- The product's own mark comes from `logo-design` via `creative-ideation.md` lenses and `brand-originality-auditor`; never from a generator, a template or an icon set glyph.
- Third-party logos: Simple Icons (CC0 data) or the brand's official press kit; respect clear space, colour and the brand's guidelines; record provenance in `08-legal-oss/asset-provenance.md`.
- Logo animation: GSAP MorphSVG or anime.js SVG drawing for a one-time mark reveal; Rive for an interactive mark. One moment, per `motion-standards.md`.

## Fonts
- Self-host via [Fontsource](https://fontsource.org/) (`@fontsource/<family>`, e.g. `@fontsource/fraunces` 5.3, OFL-1.1) or the foundry's files; `font-display: swap`; subset; licence recorded.
- Chosen from the direction's type pairing, not from the top of Google Fonts. Avoid as the default voice: Inter, Roboto, Arial, Helvetica, system-ui (the measured AI default, `slop-mechanics.md`). Variable fonts with optical sizes (Fraunces, Newsreader, Source Serif 4, Anek, Instrument Sans, Geist is the Vercel default so avoid it) are good raw material; the pairing must still be argued in the research record.

## 3D and canvas
| Library | Licence | Use |
|---|---|---|
| [Three.js](https://threejs.org/) / [React Three Fiber](https://r3f.docs.pmnd.rs/) (`@react-three/fiber` 9.8) | MIT | Only when the product's material truth is three-dimensional (a physical object, a space, a dataset with depth). Floating abstract 3D blobs are the template. |
| p5.js, Paper.js | LGPL / MIT | Generative or data-driven visuals derived from real product data. |

## Rejected by default (needs a written job to pass review)
Particle backgrounds, animated gradient meshes, cursor trails, typing-text effects, infinite marquees, parallax layers, glassmorphism cards, 3D tilt on hover, confetti outside a genuine completion moment, scroll-jacking. Each is available in the galleries above; each is on the slop list.
