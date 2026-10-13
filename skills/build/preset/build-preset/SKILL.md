---
name: build-preset
description: "Configure existing Shopify sections and blocks from Figma through presets and template settings. Supports theme-specific calibration of existing section/block height choices without classifying that calibration as custom; otherwise keeps implementation unchanged."
---

# Build Preset

Build the closest practical match to a Figma section using section and block types already present in the target theme. Configure its existing preset composition and settings, check desktop and mobile rendering, then list the visible gaps. Existing height-option calibration is the narrow implementation exception below; other gaps remain unimplemented.

## Preset/template local và media store

- Chỉ chỉnh preset/composition trong file repo. Không sửa hoặc lưu preset/template trực tiếp trên store qua Shopify bot, connector/API hay Theme Editor nếu chưa được người dùng cho phép rõ ràng riêng cho thao tác đó. Build preset, upload media hoặc yêu cầu gắn resource không tự cấp quyền này.
- Khi có yêu cầu media/content, dùng store để upload/tái sử dụng ảnh/video và chuẩn bị resource; gắn URL lâu dài/resource reference đúng kiểu setting hoặc handle product/collection/blog/article vào preset/template local. Không save picker trên store để tạo reference. Đọc [ranh giới store content và preset local](../../../setup-store/store-content-media/SKILL.md#ranh-giới-store-content-và-preset-local); khi đã cài skill phẳng, đọc `.agents/skills/store-content-media/SKILL.md`.
- Deploy file local cần quyền push riêng; preview/readback chỉ đọc, không lưu cấu hình trên store.

## Scope

- Inspect and reuse existing `sections/*.liquid` and `blocks/*.liquid` types. Do not add, rename, or replace section/block implementations.
- Configuration changes may update an existing section's `presets` entries inside its `{% schema %}` and the target page's `templates/*.json` or section-group JSON composition and settings. In a preset, use only block types and setting IDs already declared by that section/block.
- Treat all other schema content as read-only: do not add settings, IDs, options, block allow-list entries, or alter limits/placement guards.
- Except for the existing height-option calibration below, do not edit Liquid/HTML outside `{% schema %}`, CSS, JavaScript, snippets, custom CSS fields, or global theme settings to chase visual fidelity. Do not choose or fetch products, images, or videos unless the user explicitly requests media work. Otherwise leave those references unset; use existing text-only controls for copy. If the Figma includes copy that is available, use it; otherwise write short matching copy with similar hierarchy and line length.
- Preserve unrelated working-tree changes. Limit edits to the page/template and preset explicitly needed for the request. Do not push, publish, or change a live store as part of this skill.

In this repository, `docs/theme-customization-policy.md` treats preset declarations and template JSON as configuration, not custom implementation. Height-option calibration is theme configuration, not custom implementation; keep a separate calibration audit for measured values and base-update review.

## Workflow

1. **Read the reference.** Identify the target Figma frame and the intended page/section. Capture or inspect both desktop and mobile frames when available, including their viewport dimensions. If using Figma `get_design_context`, first load `figma:figma-design-to-code` as its prerequisite and request a screenshot; use its design evidence for analysis, while keeping this skill's configuration-only boundary.
2. **Inspect the theme.** Read the applicable `AGENTS.md` and theme contracts. Inventory existing sections, their schema settings and presets, their allowed blocks, and the target template or section group. Check how each plausible candidate already behaves on mobile. Do not infer unsupported settings from a screenshot.
3. **Map the design to existing controls.** Make a compact mapping of each visible region to an existing section/block, the settings that can express it, and the desktop/mobile behavior those settings provide. Choose the closest semantically correct composition. Use only controls that exist today.
4. **Configure the composition.** Set the existing section/block order, preset tree, copy, alignment, layout mode, spacing, colors, and available desktop/mobile options to match the reference as closely as the current theme permits. Apply the pagination guidance and existing height-option exception below when relevant. Keep resource selectors empty unless the user explicitly requested that media work. Prefer a section with native responsive behavior over one whose desktop structure breaks on mobile.
5. **Review both viewports.** Preview the configured result at the Figma frame sizes when possible. Compare hierarchy, content order, columns, alignment, spacing, line wrapping, and overflow against each frame. If a mobile frame was not supplied, inspect the theme's mobile viewport and state that this was the comparison used. Limit implementation changes to the height exception below.
6. **Report the result.** Name the changed configuration files and selected section/block types. Summarize desktop and mobile checks. Report any calibrated height scale and its calibration audit (not a customization record). List each material mismatch with the Figma expectation, the current rendering, and the missing existing control or behavior. Mark other custom follow-up as unimplemented. State whether requested media work was completed or references remain unselected.

## Theme-specific height-option calibration

Khi preset có phần này, đọc [Theme-specific existing height-option calibration](references/slideshow-height.md).

## Pagination visibility and spacing

Khi preset có phần này, đọc [Pagination visibility and spacing](references/pagination.md).

## Stop and report a gap

Apart from the theme-specific existing height-option exception and explicitly requested media work, if matching the design would require a new section/block, new setting, changed block allow-list, custom logic, markup, CSS, or JavaScript, stop at the configuration boundary. Apply the closest reasonable existing composition if it remains useful; otherwise present the mapping and explain why no existing section is a suitable fit. Include the unmet design details in the gap list and wait for a separate instruction before other custom implementation. Media requests do not authorize an unspecified upload destination or theme push.
