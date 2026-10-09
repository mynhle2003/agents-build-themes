# Blocks And Runtime

## Block slots and runtime lifecycle

Define each slot before rendering it: purpose, allowed block types from the Block Registry, min/max capacity, default order, nesting depth, app-block policy, and empty/fallback state. Do not open every block type to every section, and do not use literal block IDs as runtime logic.

Render blocks in Shopify's configured order and keep `block.shopify_attributes` on each block root. Handle removed defaults, missing resource data, unavailable content, and app removal with a safe empty state.

Interactive sections must scope all DOM queries, state, and listeners to their section instance. Initialize and destroy idempotently and handle the relevant Theme Editor events (`shopify:section:load`, `shopify:section:unload`, `shopify:section:select`, `shopify:section:deselect`, plus block select/deselect when applicable). Do not use a global observer, listener, or mutable state that allows one instance to affect another. Preserve focus, open state, and accessibility after add/remove/duplicate/reorder/save/reload.

## Alignment inheritance

Section alignment is owned by the section or parent composition. A section maps its desktop setting to `--flex-align` and, only when `Customize for mobile` is enabled, maps the mobile setting to `--flex-align-mobile`.

The shared content wrapper follows this contract:

```css
.align-content {
  --text-align: var(--flex-align, start);
  display: flex;
  flex-direction: column;
  align-items: var(--flex-align, start);
  text-align: var(--text-align);
}

@media (max-width: 767.98px) {
  .align-content {
    --text-align: var(--flex-align-mobile, var(--flex-align, start));
    align-items: var(--flex-align-mobile, var(--flex-align, start));
  }
}
```

Heading, Text, Eyebrow, and Header blocks must inherit this context rather than owning an alignment setting. Text-like blocks use `text-align: var(--text-align-default, inherit)`. Header uses `align-items: var(--flex-align, start)` on desktop and the mobile token inside the mobile media query. A missing mobile override falls back to desktop alignment.

## Kernel block and schema conventions

- Use schema headers to separate groups such as `Content`, `Size`/`Layout`, `Appearance`, `Gap`, and `Padding`.
- Keep visual typography independent from semantic HTML. Heading visual size is a token/role; `html_tag` alone selects `div`/`h1`–`h6`. Text has no HTML-tag setting.
- Block alignment is inherited from the section or compound parent. Do not add per-block alignment controls unless the user explicitly changes this contract.
- Use `block.shopify_attributes` directly on the rendered block element. Avoid an extra wrapper solely to carry editor attributes.
- Emit inline CSS custom properties only when a value is non-default or an active mobile override differs from desktop. Default zero padding and default width/alignment should not appear in the `style` attribute.
- Keep `fit`, `fill`, and `custom` width modes consistent. Show max-width only for `custom`; show mobile width/custom values only when `Customize for mobile` is enabled.
- Shared Header is a compound block with at most one Eyebrow, Heading, and Text child, in the recommended order Eyebrow → Heading → Text. It owns child flow/gap/padding, not child typography or alignment.
- Eyebrow background is opt-in. When enabled, its default surface padding is `1rem 1.4rem`; its icon choices are the contract-defined decorative shapes (circle, square, triangle, diamond). Radius options use the shared presets `Square`, `Slightly rounded`, `Rounded`, and `Pill` rather than an ad-hoc range.

Rich text-style sections use static kernel blocks when the composition is fixed:

```liquid
{% content_for "block", type: "eyebrow", id: "eyebrow" %}
{% content_for "block", type: "heading", id: "heading" %}
{% content_for "block", type: "text", id: "text" %}
```

Static blocks may be customized or hidden in the editor, but their fixed order and presence are controlled by the section implementation. Keep the section schema allow-list aligned with the static block calls.

## Mapping blocks into sections

Choose one mapping pattern per composition and keep the schema, Liquid calls, and JSON template in sync:

- **Merchant-managed composition:** the section schema declares the allowed block types and Liquid uses `{% content_for 'blocks' %}`. The merchant can add, remove, reorder, duplicate, and configure those blocks according to the allow-list and limits.
- **Fixed composition:** the section schema declares the permitted block types and Liquid calls each static block with a stable ID using `{% content_for 'block', type: ..., id: ... %}`. The template JSON lists those blocks with `"static": true` and keeps their order in the section `order`/block structure. Static blocks can be customized or hidden, but are not freely reordered or removed.
- **Compound block:** a block such as Header declares its own child allow-list and limits, renders `{% content_for 'blocks' %}`, and must reject nesting itself when the contract disallows it. The parent section still owns the outer width, alignment, and background context.

When adding a section/block relationship, verify all three surfaces together: the section schema, the Liquid rendering call, and the relevant `templates/*.json` entry. A block type that is allowed but never rendered, rendered but absent from the allow-list, or marked static without a matching stable ID is an incomplete mapping.
