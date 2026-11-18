# Motion specification

| Animation | Information conveyed | Duration | Easing | Reduced motion |
|---|---|---|---|---|
| Status chip change | state changed | `motion.fast` 140 ms colour/label swap | standard | instant swap |
| Toast appear / dismiss | action saved, undo available | `motion.base` 220 ms slide 8 px + fade | standard / exit | fade only, 100 ms |
| Sheet open (picker) | context layered | `motion.base` 220 ms | standard | fade only |
| Skeleton shimmer | loading | continuous, subtle | — | static grey |
| Board drag | spatial move | follows pointer | — | select-based alternative, no animation |

No decorative motion. No auto-animated data updates (data changes show a "Updated" status text).
