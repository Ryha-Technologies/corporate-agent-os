# WCAG 2.2 Level AA checklist

Default accessibility target for every user-facing interface and document. Source: W3C WCAG 2.2 (https://www.w3.org/TR/WCAG22/). This checklist is an operational summary for review; the W3C text is normative. Record each criterion as PASS / FAIL / NOT_TESTED / NOT_APPLICABLE with evidence.

## Perceivable
| SC | Name | Check |
|---|---|---|
| 1.1.1 | Non-text content | Images, icons and controls have text alternatives; decorative images are hidden from AT. |
| 1.2.x | Time-based media | Captions for prerecorded and live audio; audio description or alternative where required. |
| 1.3.1 | Info and relationships | Headings, lists, tables, form labels and landmarks are programmatic. |
| 1.3.2 | Meaningful sequence | Reading and focus order match visual order. |
| 1.3.3 | Sensory characteristics | Instructions do not rely on shape, colour or position alone. |
| 1.3.4 | Orientation | Content works in portrait and landscape. |
| 1.3.5 | Identify input purpose | Autocomplete attributes on common fields. |
| 1.4.1 | Use of colour | Colour is not the only means of conveying information. |
| 1.4.2 | Audio control | Auto-playing audio can be paused or stopped. |
| 1.4.3 | Contrast (minimum) | Text 4.5:1; large text 3:1. |
| 1.4.4 | Resize text | 200% zoom without loss. |
| 1.4.5 | Images of text | Avoided except logos. |
| 1.4.10 | Reflow | No two-dimensional scrolling at 320 CSS px width. |
| 1.4.11 | Non-text contrast | UI components and graphical objects 3:1. |
| 1.4.12 | Text spacing | Content survives increased spacing. |
| 1.4.13 | Content on hover or focus | Dismissible, hoverable, persistent. |

## Operable
| SC | Name | Check |
|---|---|---|
| 2.1.1 | Keyboard | All functionality via keyboard. |
| 2.1.2 | No keyboard trap | Focus can always leave. |
| 2.1.4 | Character key shortcuts | Can be turned off or remapped. |
| 2.2.1 | Timing adjustable | Time limits can be extended. |
| 2.2.2 | Pause, stop, hide | Moving or auto-updating content controllable. |
| 2.3.1 | Three flashes | No content flashes more than three times per second. |
| 2.4.1 | Bypass blocks | Skip links or landmarks. |
| 2.4.2 | Page titled | Descriptive titles. |
| 2.4.3 | Focus order | Logical. |
| 2.4.4 | Link purpose | Clear from text or context. |
| 2.4.5 | Multiple ways | More than one way to find pages. |
| 2.4.6 | Headings and labels | Descriptive. |
| 2.4.7 | Focus visible | Visible focus indicator. |
| 2.4.11 | Focus not obscured (minimum) | Focused element not entirely hidden by other content. |
| 2.5.1 | Pointer gestures | Single-pointer alternatives to multipoint or path gestures. |
| 2.5.2 | Pointer cancellation | Down-event does not trigger actions irreversibly. |
| 2.5.3 | Label in name | Visible label is in the accessible name. |
| 2.5.4 | Motion actuation | Alternatives to device motion. |
| 2.5.7 | Dragging movements | Single-pointer alternative to dragging. |
| 2.5.8 | Target size (minimum) | At least 24×24 CSS px or sufficient spacing. |

## Understandable
| SC | Name | Check |
|---|---|---|
| 3.1.1 | Language of page | `lang` set. |
| 3.1.2 | Language of parts | Changes marked. |
| 3.2.1 | On focus | No unexpected context change. |
| 3.2.2 | On input | No unexpected context change. |
| 3.2.3 | Consistent navigation | Same order across pages. |
| 3.2.4 | Consistent identification | Same function, same label. |
| 3.2.6 | Consistent help | Help mechanisms in the same relative place. |
| 3.3.1 | Error identification | Errors described in text. |
| 3.3.2 | Labels or instructions | Provided for inputs. |
| 3.3.3 | Error suggestion | Correction suggested where known. |
| 3.3.4 | Error prevention (legal, financial, data) | Reversible, checked or confirmed. |
| 3.3.7 | Redundant entry | Previously entered information auto-populated or selectable. |
| 3.3.8 | Accessible authentication (minimum) | No cognitive function test without alternative. |

## Robust
| SC | Name | Check |
|---|---|---|
| 4.1.2 | Name, role, value | Custom controls expose them. |
| 4.1.3 | Status messages | Announced without focus change. |

## Method requirements
- Automated scan plus manual keyboard pass is the minimum; screen-reader pass where tooling is available.
- Record tool, version, date and environment.
- Automated output alone is never reported as conformance.
