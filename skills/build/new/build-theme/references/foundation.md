# Foundation

## Ưu tiên option trước CSS custom

Áp dụng cho các yêu cầu build, rebuild, custom, fix, tối ưu và cập nhật giao diện theme, **không bao gồm tác vụ `build-preset`**. Build preset giữ phạm vi và ngoại lệ riêng của skill `build-preset`.

1. Đọc schema, giá trị hiện tại và mapping runtime để xác định option Theme Settings/section/block đúng owner, thuộc tính và breakpoint. Ưu tiên cấu hình option hiện có trước khi sửa CSS custom; không hard-code hoặc override thuộc tính mà option đã điều khiển được. Nếu option không hoạt động đúng, kiểm tra và sửa mapping trong phạm vi implementation được yêu cầu.
2. **Được phép mở rộng giới hạn `min`/`max` của option hiện có khi cần custom trong phạm vi người dùng yêu cầu**, không chỉ khi có Figma: hạ `min` và/hoặc nâng `max` để chứa giá trị cần dùng. Đây là một phần của quyền custom, không cần xin lại riêng cho việc mở rộng range. Tính lại `step` ngay khi đổi biên; cập nhật validation runtime tương ứng và lưu đúng giá trị vào preset/template. Giữ ID, kiểu, unit, ý nghĩa setting, default và các giá trị đã lưu hợp lệ; không đổi sang setting mới hoặc quy đổi ngầm value để né giới hạn. Quyền sửa range local không tự cấp quyền deploy/push/publish.
3. Range phải có `min < max`, `step > 0`, các thuộc tính số đúng định dạng Shopify và `(max - min) / step` là số nguyên không quá 100, tức tối đa **101 giá trị chọn được** kể cả hai đầu. `step >= (max - min) / 100` chỉ là điều kiện cần; chọn bước chia hết khoảng range và biểu diễn được giá trị Figma, default cùng các giá trị đã lưu chịu tác động: `(value - min) / step` phải là số nguyên và value nằm trong range. Không chỉ tăng max, không tự làm tròn Figma hoặc âm thầm đổi giá trị đã lưu. Ví dụ `min: 0, max: 500, step: 5` có 101 giá trị chọn được; `step: 1` có 501 và không hợp lệ. Nếu không tìm được range hợp lệ giữ các giá trị cần thiết, báo rõ gap để quyết định thay đổi contract.
4. **Không quy đổi ngầm giá trị option.** Với setting có giá trị và unit cụ thể, giá trị cấu hình phải giữ đúng ý nghĩa khi render; không lưu `100px` nhưng render `80px`, và không áp dụng thủ thuật tương tự cho bất kỳ giá trị, breakpoint hay thuộc tính nào qua Liquid, CSS hoặc JavaScript. Chuyển đơn vị tương đương được phép nếu giữ nguyên đại lượng; mapping của option ngữ nghĩa như Small/Medium theo contract không thuộc lệnh cấm này. Nếu cần 80px mà min là 100px, sửa trực tiếp min/step/max hợp lệ, validation runtime và preset/template để lưu đúng 80; không hard-code ngoại lệ cho một value để né schema hoặc lỗi đồng bộ. Schema trên store chưa cập nhật thì đồng bộ schema trước/cùng consumer trong phạm vi deploy đã được cho phép, hoặc báo chưa đồng bộ; không làm sai ý nghĩa option để né lỗi. Fallback cho dữ liệu thiếu/không hợp lệ được giữ, nhưng không được thay đổi giá trị hợp lệ.
5. Sau khi xử lý option và range, mới đọc CSS custom đang có cho các thuộc tính còn thiếu option. Chỉ thêm/sửa CSS custom cho phần không có option tương ứng và nằm trong phạm vi yêu cầu; scope selector theo component/instance, giữ token và hành vi responsive/editor. Yêu cầu chỉ cấu hình vẫn báo gap cho phần cần custom implementation.
6. Kiểm tra schema/JSON, Theme Check, giá trị đã lưu và output desktop/mobile/editor chịu tác động; thử thay đổi option để xác nhận CSS custom không vô hiệu hóa control. Báo các range đã đổi và phần còn cần custom.

Tham khảo định dạng và hành vi làm tròn/clamp của [Shopify range settings](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#range); xác minh schema với Shopify khi điều chỉnh range.

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

## Icon Figma và SVG

- Không tạo hoặc lưu SVG icon vào theme `assets/`; không tham chiếu URL Figma tạm trong theme. SVG icon được render từ snippet icon của repo.
- Kiểm tra snippet icon hiện có và các consumer trước. Nếu đã có icon khớp Figma, dùng lại đúng icon/snippet, giữ kích thước và màu theo contract hiện tại.
- Nếu chưa có bản khớp, tìm icon tương tự không được dùng trong Figma và kiểm tra callsite/preset trước khi thay bằng SVG đúng thiết kế trong snippet. Không thay một icon đang được dùng hoặc làm thay đổi consumer khác; khi không có ứng viên an toàn, bổ sung icon vào snippet hiện có.
- Render qua lựa chọn icon/style trong schema nếu có; không ép icon hay layout bằng CSS bất kể option. Giữ `currentColor`, kích thước/viewBox, accessibility và contract snippet; cập nhật option liên quan chỉ trong phạm vi được yêu cầu.
- Nếu đã thêm SVG icon vào `assets/` trong tác vụ hiện tại, chuyển consumer về snippet và xóa đúng file vừa thêm. Không xóa asset có sẵn hoặc thay đổi không liên quan.
