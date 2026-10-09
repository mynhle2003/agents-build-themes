# Section Contract

## Section contract and ownership

Before creating or refactoring a section, record a compact contract with these fields:

- **Identity:** section type, role, title, owner, and supported template/group surfaces.
- **Context:** resource or data context supplied by the template or parent; the section must not infer product, collection, cart, or market context.
- **Presentation:** color scheme, background layer, width/container, section spacing, layout mode, and default content alignment.
- **Children:** block allow-list, slot purpose, capacity, default composition/order, nesting depth, app-block policy, and empty state.
- **Runtime:** Liquid render path, JavaScript owner, editor lifecycle, and loading/changing/success/error states when applicable.
- **Output:** stable root classes/data attributes and accessibility responsibility.
- **Constraints:** what the section cannot control, especially global tokens, block typography, leaf alignment, card/grid ownership, and page placement.

Ownership follows this rule: the section owns external spacing, parent grid/columns, card width and card gap, container/background, and data handoff; a block owns content and internal layout only when its Block Contract permits it; Theme Settings own reusable tokens; Shopify owns resource, localization, market-aware money, and app context.

## Section schema and placement contract

Choose placement before schema or markup:

- A **dynamic content section** belongs in a JSON template, has a meaningful preset, and may be addable, removable, and reorderable within its surface.
- A **main/resource section** is limited to the resource template that supplies its context; it is not a generic content section.
- A **section group** is rendered through `{% sections 'group-name' %}` and is reserved for a layout surface such as header, footer, aside, or another explicitly contracted group.
- A **static section** is an exception for structure that merchants must not add, remove, or reorder; do not use static rendering as a shortcut.

For every section schema:

- Keep one valid `{% schema %}` JSON object with `name`, `tag`, `class`, limits, settings, blocks, presets, and placement guards.
- Use either `enabled_on` or `disabled_on`, never both. Guard the section to the templates/groups that provide its context.
- Expose only section-level editor settings: common layout/appearance settings when the section owns them, and specialized settings only when the contract requires them. Do not expose token or CSS-editor controls already covered by Theme Settings.
- Define each setting's owner, consumer, default, allowed values, constraint, visibility rule, and translation key. Keep preset/default composition and editor order explicit.
- Respect Shopify capacity limits: a JSON template may contain at most 25 sections and a section may contain at most 50 blocks.

Keep a placement matrix for each new type: allowed surface, add/remove/reorder policy, resource context, app-block support, and default/preset behavior. Verify the JSON template, section group, or static render together with the section schema.

## Section shell and CSS contract

Use one stable shell for every section:

```liquid
<div class="section-spacing ... color-scheme ...">
  <div class="container page-width|full-width ...">
    <div class="align-content">...</div>
  </div>
</div>
```

- Separate the background/full-bleed layer from the content-width container. The section schema controls the outer class and container mode; the base owns the shared implementation.
- Map section settings to scoped custom properties for width, padding, gap, layout mode, and propagated alignment. Emit only non-default values and active mobile overrides.
- Foundation CSS owns tokens, reset, semantic typography/utilities, radius, motion, focus, and shared section primitives. Section CSS owns only its layout/appearance; block CSS owns only internal content/layout.
- Use one responsive DOM tree unless content order or interaction genuinely differs. Do not fork core block styles, duplicate global tokens, or let a child block set external section spacing or parent grid columns.
- Do not put `{{ section.shopify_attributes }}` on the section shell. Shopify supplies the outer section wrapper; only the root element of a rendered block receives `{{ block.shopify_attributes }}`.
- Shopify Custom CSS is an escape hatch scoped to the current section; it must not override Foundation tokens, the DOM contract, or accessibility states.

Changing a color scheme or spacing token should update the section through inherited variables/classes without editing its markup.

## Section skill boundaries

This skill supplies the project foundation and contract; it does not silently create a new Block Registry, replace a section contract, or broaden a section's placement. If a request requires a missing block kernel/contract, stop section implementation and resolve that dependency first. Treat schema design, section implementation, responsive/editor guard, and final standards audit as separate responsibilities; use corresponding skills only when they are available and explicitly enabled for this project. The section builder may coordinate them, but must not hide schema, runtime, accessibility, or QA decisions inside a single Liquid/CSS patch.

## Section DOM contract

Shopify already emits the outer wrapper:

```html
<div id="shopify-section-..." class="shopify-section section-...">
```

The Liquid section must not add another semantic `<section>` wrapper for the kernel. Render the section content directly as a `div`, with `section-spacing` as the first child when applicable:

```html
<div class="section-spacing ... color-scheme ...">
  <div class="container page-width|full-width ...">
    <div class="align-content">...</div>
  </div>
</div>
```

Use a section-specific schema `class` (for example `section-rich--text`) when the section needs a stable outer hook. Keep the outer class and container responsibilities separate:

- `page-width` applies the global page-width cap.
- `full-width` belongs only on the inner `.container`, not on the section root.
- `.container.full-width` removes the max-width cap but preserves the current responsive page margins with `calc(100% - (var(--page-margin-current) * 2))`.
- Background and spacing belong to `section-spacing`; content width belongs to the container.

Do not add duplicate `rich-text`, `rich-text--full-width`, or utility `full-width` wrappers around a section kernel.
