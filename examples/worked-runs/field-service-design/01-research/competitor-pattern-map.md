# Competitor pattern map — field-service management tools

Role: competitive-analyst (T-008, rework for gate finding F-1). Method: homepage HTML and first linked stylesheets fetched on 2026-11-18 and parsed for the most frequent hex colours, declared font families, H1 text and button labels (`competitor-capture.json`). This captures marketing-site patterns, not product UI; product screenshots were not captured (no authenticated access). Limitation stated in the gate.

## Observed
| Company | Source (accessed 2026-11-18) | Top colours (excluding black/white) | Fonts | H1 | CTAs |
|---|---|---|---|---|---|
| Zuper | https://www.zuper.co/ | #fbd9c4, #f2400a, #fffaea | not exposed in first CSS files | The AI Operating System to Run Your Service Business | Sign in, Schedule Demo, Schedule a Demo |
| FieldEZ | https://www.fieldez.com/ | #fbf7f1, #575f6c, #06302a | not exposed in first CSS files | The unified operations platform for enterprise equipment and field operations – in the off | Request a demo, Request a demo →, Explore the platform |
| Fieldproxy | https://www.fieldproxy.com/ | #0a1628, #ea580c, #dfe3f7 | Geist Mono, Geist | Fieldproxy is AI field service software that we configure around your workflows, whatever  | Get Demo |
| Jobber | https://www.getjobber.com/ | blocked (HTTP Error 403: Forbidden) | — | — | — |
| Housecall Pro | https://www.housecallpro.com/ | #05f, #002942, #13191e | Manrope, Helvetica Neue LT Pro Condensed | Everything to run and grow your business | Login, Start free trial, Join the conversation
				&rarr; |
| ReachOut Suite | https://www.reachoutsuite.com/ | #585858, #34b2ed, #4a90e2 | Figtree, Poppins | SERVICE BUSINESS SOFTWARE | Request a Demo, Contact us for pricing, More Industries |
| FieldVibe | https://www.fieldvibe.com/ | #232427, #272424, #211f2a | Work Sans\:Bold | Simple field service software built for solo pros and small teams |  |
| FieldCamp | https://fieldcamp.ai/ | #111827, #fafafa, #ff791b | __Inter_176161, __Fraunces_dd45d0 | The AI-native field operations platform | Book a 15-minute call, Book a demo, Explore the AI Dispatcher → |

## Naming patterns
| Pattern | Examples | Frequency |
|---|---|---|
| "Field" + noun compound | FieldEZ, Fieldproxy, FieldVibe, FieldCamp, FieldServicePro | 5 of 9 |
| English service/job nouns ("Jobber", "Housecall", "ReachOut", "Zuper") | 4 of 9 | common |
| "Kaam" (work) prefix in Indian field apps | KaamCam, Kaam, KAAMS (search results) | crowded |

## Claim and messaging patterns
| Pattern | Examples |
|---|---|
| "AI operating system / AI-native / AI-first" | Zuper, Fieldproxy, FieldCamp |
| "All-in-one / everything to run and grow" | Zuper, Housecall Pro, ReachOut |
| "Unified platform" | FieldEZ |
| Demo-request CTA ("Schedule a demo", "Request a demo", "Book a demo", "Get Demo") | 6 of 7 reachable |
| Enterprise-equipment framing | FieldEZ |

## Visual patterns (marketing sites)
| Element | Common pattern | Examples |
|---|---|---|
| Accent colour | Orange (#f2400a, #ea580c, #ff791b) or saturated blue (#05f, #34b2ed, #4a90e2) | Zuper, Fieldproxy, FieldCamp / Housecall Pro, ReachOut |
| Base | Near-black navy (#0a1628, #111827, #002942) with off-white | Fieldproxy, FieldCamp, Housecall Pro |
| Typography | Geometric/neo-grotesque sans: Inter, Manrope, Poppins, Figtree, Geist, Work Sans | FieldCamp, Housecall Pro, ReachOut, Fieldproxy, FieldVibe |
| Display serif pairing | Fraunces with Inter | FieldCamp |
| Monospace accents | Geist Mono | Fieldproxy |
| Green base | Dark green #06302a with warm off-white | FieldEZ |

## Ownable signals (gaps)
- No reachable competitor uses a deep violet/aubergine accent or a yellow "marker" highlight; none uses a multi-script Indian type family.
- Every reachable competitor leads with "AI", "all-in-one" or "platform"; none leads with the dispatcher's concrete fear (a job falling through).
- All names are English compounds; an Indian-language name with a clear meaning for technicians is unoccupied in this set (but "Kaam" compounds are crowded; see naming report).

## Limits
Marketing-site colours and fonts are proxies for product UI. Product-UI screenshots must be captured (trial accounts) before the final identity is approved; recorded as rework T-012.
