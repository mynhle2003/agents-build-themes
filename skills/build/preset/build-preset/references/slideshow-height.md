# Theme-specific slideshow height calibration


When building a slideshow preset on a `theme/<slug>` branch, existing `Desktop height` and `Mobile height` fixed values may be calibrated to the supplied Figma section heights. Apply this only to the current theme, never to shared `main` or other theme branches.

- Use measured section/frame height, excluding surrounding header/footer. Map the standard reference height to the existing `Medium` choice for each supplied viewport. For example, a desktop reference of 800px makes desktop `medium` 800px. Do not guess a mobile target when no mobile reference exists.
- Adjust the entire fixed scale proportionally: `new height = old height × target Medium / old Medium`, independently for desktop and mobile. Round to practical units while keeping `Extra small < Small < Medium < Large < Extra large`; keep Medium exact. Preserve the theme's unit convention and account for its root font size when converting rem to pixels.
- Preserve `Adapt` and `Full screen` behavior. Their dynamic heights are not part of the fixed numeric ordering. Keep all existing schema IDs, option values, labels, defaults, and responsive breakpoints.
- Change only the existing slideshow fixed-height CSS mappings. Select `medium` for the matching desktop/mobile viewport in both the section preset and target template. This exception does not permit new controls, markup, JavaScript, global tokens, or unrelated visual changes.
- Before handoff, record the implementation path in `docs/theme-customizations/<slug>.md`: original and new desktop/mobile values, Figma node IDs and measured heights, rationale, and the base-update rule. Review upstream changes to the same mappings before merging; preserve the theme's calibrated scale rather than overwriting it automatically.
- Validate strict ordering and the preset/template selections, run Theme Check and `node theme-base check-custom <slug>`, and verify rendered desktop/mobile heights when a preview is available. Report preview limitations explicitly.
