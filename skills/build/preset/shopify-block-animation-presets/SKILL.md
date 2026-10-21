---
name: shopify-block-animation-presets
description: Configure existing Shopify theme animation presets and delays across blocks, sections, and templates, informed by 5–6 popular themes in the same industry. Use for requests to create or tune theme animations through presets only; do not add controls or change implementation code.
---

# Shopify block animation presets

Interpret requests such as “tạo animation cho theme”, “gắn animation”, or “set animation preset” as configuring existing supported animation settings throughout the target theme. Every eligible block with an Animation group must receive an explicit non-None preset effect, except documented exclusions or a competing existing effect. Do not limit the work to two familiar block types, merely add controls, or leave eligible presets at None.

## Preset-only boundary

Allowed edits are animation setting values in block schema `presets`, section schema `presets` (including nested/static block configurations), and existing JSON template section/block settings. Liquid files may be edited only inside those preset configuration objects. Preserve unrelated settings, content, IDs, ordering, and layout.

Do not change schema setting definitions/defaults, add Animation groups or Delay controls, edit Liquid markup/snippets, CSS, JavaScript, locales, runtime logic, carousel activation, global motion controls, or accessibility behavior. Do not modify global settings or `config/settings_data.json` under this skill. Reading implementation files to determine existing support is allowed. If an effect or delay needs code changes, choose another supported preset; report the limitation instead of implementing it. A separate explicit user request is required for implementation work.

## Inspect the actual target

Read repository instructions and preserve existing working changes. Inventory all blocks and sections with an existing Animation group and their supported setting IDs, values, defaults, delay ranges/steps, and runtime constraints. Do not assume Malandra's setting names or a fixed list of content kernels apply. An authorized sibling theme may be read as a reference, never edited as part of target-theme configuration.

Distinguish neutral schema defaults from preset values: defaults may remain None/0 while actual eligible preset configurations must explicitly select effects. Traverse actual `blocks` trees, including static blocks and reusable content Header blocks; do not mistake schema declarations such as `{ "type": "text" }` for block instances.

## Research the same industry

For each theme-animation request, visit [Shopify Theme Store](https://themes.shopify.com/themes), identify the target's industry from the storefront/design brief, and research 5–6 popular relevant themes. Use official industry filters/listings and accessible official demos. The user permits read-only access to the Theme Store and its accessible demo links for this research; respect actual access restrictions and report unavailable pages.

Prefer popularity evidence exposed by the store, such as its sorting, review volume, and ratings, together with industry relevance. Do not invent an official “top” ranking. Record the selected theme names, source links, selection basis, and relevant motion observations. If fewer than five suitable references are accessible, state the actual number and limitation rather than inventing observations.

Prioritize reference effects resembling the target theme's existing supported animations and reproducible through its presets. Map the references to available fade, scale, directional slide, heading word effects, or media settings only when the target already supports them. Research guides composition; it does not authorize copying theme source or adding capabilities. Separate directly observed behavior from design inference and chosen timings. A listing alone does not establish exact delays or motion curves.

## Compose and apply

Apply explicit effects consistently to standalone block presets, all eligible section preset compositions, and existing target JSON templates. Include nested reusable content Headers. Preserve established exclusions from project instructions and existing theme contracts: for the Mara/Virelle workflow these include site Header/navigation, Footer, announcement groups, FAQ and dialog surfaces. A page containing an excluded section can still animate its other eligible sections. Keep a short inventory of exceptions and their reasons; None is acceptable only for an established exclusion or an existing effect that must take precedence.

Use varied but coherent effects and delays based on brand, industry, reading order, and the reference observations. Avoid assigning one effect everywhere or excessive delays. For a restrained clothing composition, a starting point is Eyebrow/paired icon Fade 0ms, Heading Slide from bottom 50ms, Text Fade 100ms, Button Fade 150ms; vary supported effects where the composition benefits. These are design choices, not measured reference-theme timings. Use only the target's actual supported delay range, step, and effective runtime limit; do not change them.

Respect existing Editorial scroll reveal precedence: retain entrance None when scroll reveal is enabled. Preserve card staggering and component-owned carousel/media motion; avoid double animation of the same content. Hero presets may use only existing supported media effects and must obey documented image/video and stacked-layout constraints. Never change runtime or schema to enforce a new Hero rule under this skill.

## Verify and report

Audit all eligible preset/template instances: no missing or None animation outside recorded exceptions; values supported by the actual schema/runtime; delays valid for the actual range and step. Confirm only allowed preset/template setting values changed and schema defaults/implementation remain untouched by this task. Distinguish existing working changes from this task's edits.

Parse changed schema/JSON, run relevant existing tests and full `shopify theme check --fail-level error`, and review `git diff --check`. Do not add implementation tests or repair runtime as part of this preset-only task. Check desktop/mobile and Theme Editor behavior when an accessible preview exists; report unavailable visual checks separately. If verification exposes an implementation defect, report it and use a supported safe preset where possible.

Report the reference themes, chosen effect/delay approach, coverage, exceptions, and actual validation results. This skill does not authorize commit, push, deployment, or publication.
