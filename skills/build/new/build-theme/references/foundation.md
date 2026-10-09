# Foundation

## Architecture layers

Build the theme in four deliberate layers. A lower layer provides tokens and context; a higher layer composes them. Do not move a responsibility upward merely to make one component convenient.

### 1. Theme Settings — global contract

- `config/settings_schema.json` is the merchant-facing global contract. Every setting needs a stable semantic ID, supported type/options, default, constraint, and clear token mapping.
- `config/settings_data.json` contains the current theme values; do not treat it as the place to invent new setting definitions.
- `snippets/css-variables.liquid` translates global settings and color schemes into CSS custom properties. It is the bridge from Theme Editor values to the CSS foundation.
- `assets/critical.css` consumes those tokens and owns resets, primitives, responsive behavior, and shared utilities. Components should read tokens with `var(...)`, not recreate global values.
- Keep global settings global: page width/margins, typography roles, schemes, radius presets, motion, button/form contracts, prices, and shared commerce tokens belong in Theme Settings. Section and block schema settings are for composition or local overrides.
- For every new setting, trace the complete path: `settings_schema.json` → `css-variables.liquid` or section/block mapping → CSS custom property → consuming component. Add locale keys when the schema label is translatable.

### 2. Block — reusable content kernel

Each reusable block lives in `blocks/<name>.liquid` and owns only its role:

1. Normalize and validate `block.settings` in Liquid, including fallback values.
2. Capture only non-default local CSS custom properties for the rendered element.
3. Render the smallest useful markup and put `block.shopify_attributes` directly on that element.
4. Keep block-local CSS and schema together; use schema headers for editor groups.
5. Read parent context and foundation tokens; do not own section layout, brand colors, or a duplicate global token system.

Heading, Text, Eyebrow, and Header are Basic kernel blocks. Heading separates semantic `html_tag` from visual typography role. Text is rich text without an HTML-tag control. Eyebrow uses the Accent role and optional background/icon. Header composes child blocks and owns child flow/gap/padding, but not child typography or alignment.

### 3. Section — composition and context owner

Each section in `sections/<name>.liquid` owns composition-level concerns:

- section schema settings for width, alignment/context, appearance/background, and section spacing;
- the section-specific outer schema class;
- the `section-spacing` surface and background layer;
- the `container` width mapping;
- the block allow-list or fixed static block calls;
- responsive section overrides and fallback behavior.

Sections must not reimplement global typography, button, form, radius, or color logic. They map section settings to local custom properties such as `--flex-align`, `--flex-align-mobile`, and section padding tokens, then let blocks consume the context.

### 4. Section base/kernel — shared implementation

The base layer is the contract shared by every new section:

- `assets/critical.css` provides `.container`, `.page-width`, `.container.full-width`, `.align-content`, focus rules, responsive breakpoints, and foundation token consumers.
- `snippets/css-variables.liquid` provides the global variables consumed by that base layer.
- A new section should compose the base DOM and utilities instead of adding section-specific versions of them.
- If a new primitive is genuinely reusable, add it to the base layer first and then consume it from sections/blocks. Do not hide a global primitive inside one section's stylesheet.

## Mapping section, base, and blocks

The dependency direction is:

```text
Theme Editor settings
  -> css-variables.liquid / section Liquid mapping
  -> global CSS foundation and semantic tokens
  -> section surface/container/context
  -> block markup and local presentation
```

For a section, map settings in this order:

1. Resolve and validate section settings in Liquid.
2. Set the section color scheme and inherited context on `section-spacing`.
3. Select exactly one container mode: `page-width` or `full-width`.
4. Apply `.align-content` to the composition wrapper when the section contains stacked blocks.
5. Render blocks through the section's allow-list or static block contract.
6. Let each block read inherited alignment and global tokens; only pass a local override when the block contract explicitly provides one.

The section controls the parent context; the block controls its content role; the base controls the shared implementation. A block must remain usable in another compatible section without copying section CSS.

## Foundation and settings decisions

- Components consume semantic color, typography, radius, motion, button, form, price, and layout tokens; do not hard-code brand colors or section-specific dimensions.
- The Layout settings expose page width plus desktop/tablet/mobile page margins. There is no `Minimum page margin` setting or hidden minimum-margin clamp.
- Radius controls use the shared preset vocabulary. Do not switch one component to a numeric range unless the contract explicitly requires it.
- Keep the current badge scope: do not reintroduce the removed generic status-color group; collection badges and custom product-card tags are separate concerns.
- Button Tertiary remains the third button level and follows its own label/hover-label contract; do not add unrelated outline/subtle naming.
