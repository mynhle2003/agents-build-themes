---
name: build-preset
description: "Configure existing Shopify sections and blocks from Figma through presets, template settings and existing global Theme Settings in local config/settings_data.json. Supports theme-specific calibration of existing section/block height choices without classifying that calibration as custom; allows replacing existing theme icon SVGs with Figma originals; otherwise keeps implementation unchanged."
---

# Build Preset

Build the closest practical match to a Figma section using section and block types already present in the target theme. Configure its existing preset composition and settings, check desktop and mobile rendering, then list the visible gaps. Existing height-option calibration and the scoped existing-icon replacement and social workflows are the implementation exceptions below; other gaps remain unimplemented.

## Preset/template local và media store

- Chỉ chỉnh preset/composition trong file repo. Không sửa hoặc lưu preset/template trực tiếp trên store qua Shopify bot, connector/API hay Theme Editor nếu chưa được người dùng cho phép rõ ràng riêng cho thao tác đó. Build preset, upload media hoặc yêu cầu gắn resource không tự cấp quyền này.
- Khi có yêu cầu media/content, dùng store để upload/tái sử dụng ảnh/video và chuẩn bị resource; gắn URL lâu dài/resource reference đúng kiểu setting hoặc handle product/collection/blog/article vào preset/template local. Không save picker trên store để tạo reference. Đọc [ranh giới store content và preset local](../../../setup-store/store-content-media/SKILL.md#ranh-giới-store-content-và-preset-local); khi đã cài skill phẳng, đọc `.agents/skills/store-content-media/SKILL.md`.
- Deploy file local cần quyền push riêng; preview/readback chỉ đọc, không lưu cấu hình trên store.

## Scope

- Áp dụng [Tên, preset Figma hiện tại và routing `(custom)`](#tên-preset-figma-hiện-tại-và-routing-custom) trước khi chọn section và ghi preset.
- Inspect and reuse existing `sections/*.liquid` and `blocks/*.liquid` types. Do not add, rename, or replace section/block implementations.
- Configuration changes may update an existing section's `presets` entries inside its `{% schema %}` and the target page's `templates/*.json` or section-group JSON composition and settings. In a preset, use only block types and setting IDs already declared by that section/block.
- Treat all other schema content as read-only: do not add settings, IDs, options, block allow-list entries, or alter limits/placement guards.
- Except for the existing height-option calibration and the scoped existing-icon replacement and social exceptions below, do not edit Liquid/HTML outside `{% schema %}`, CSS, JavaScript, snippets, custom CSS fields, to chase visual fidelity. Configure existing global Theme Settings only through the local settings-data workflow below. Do not choose or fetch products, images, or videos unless the user explicitly requests media work. Otherwise leave those references unset; use existing text-only controls for copy. If the Figma includes copy that is available, use it; otherwise write short matching copy with similar hierarchy and line length.
- Preserve unrelated working-tree changes. Limit edits to the page/template, preset and verified global Theme Settings needed for the request. Do not push, publish, or change a live store as part of this skill.

In this repository, `docs/theme-customization-policy.md` treats preset declarations and template JSON as configuration, not custom implementation. Height-option calibration is theme configuration, not custom implementation; keep a separate calibration audit for measured values and base-update review.

## Tên, preset Figma hiện tại và routing `(custom)`

- **Mặc định giữ tên gốc của section.** Build từ `Hero` thì preset là `Hero`, không phải `Essen: Hero`, `Hero 2` hay `Hero — Campaign`. Đối chiếu preset gốc trên `main` để giữ đúng tên/key dịch; nếu section không có trên `main`, dùng tên gốc trong schema. Heading Figma, tên theme, ID instance và tên chiến dịch không quyết định tên preset.
- **Một preset Figma hiện tại cho section thông thường.** Cập nhật/thay thế preset mặc định bằng composition Figma hiện tại, giữ nguyên tên gốc. Không giữ song song bản factory và bản Figma chỉ vì khác nội dung. Ví dụ `Image cards` và `Image cards — Opal edits` dùng cùng section: giữ composition Opal edits đang được yêu cầu, đặt tên `Image cards`, bỏ preset dư. Khi gộp, không làm mất composition Figma bằng cách chỉ giữ preset đầu tiên; xác định preset đang build từ yêu cầu và dữ liệu hiện tại. Không đổi/xóa instance trong template ngoài phạm vi yêu cầu.
- **Ngoại lệ tên riêng do người dùng yêu cầu.** Nếu yêu cầu rõ preset `Text width icon (custom)`, giữ chính xác tên đó. Không đổi thành `Custom section`, không thêm tiền tố theme hoặc số thứ tự. Preset tên riêng được phép tồn tại cùng preset mặc định và các preset tên riêng khác đã được yêu cầu; cập nhật cùng tên khi build lại, không tạo bản trùng.
- **Tên có `(custom)` dùng `Custom section`.** Dùng section `sections/custom-section.liquid` với các block hiện có để dựng composition, dù tên người dùng gọi là “section”. `Custom section` là section chứa, không phải một block type mới. Ví dụ `Text width icon (custom)` → preset tên `Text width icon (custom)` trong schema của `Custom section`; instance nếu được yêu cầu dùng `type: custom-section`. Không tạo section implementation riêng chỉ để mang tên preset này. Nếu các block/setting hiện có không dựng được thiết kế, báo gap theo ranh giới skill.
- **Phải xuất hiện trong Add section.** Khai báo tên riêng trong `presets[]` của section chứa để Theme Editor liệt kê preset cho template đích; kiểm tra `enabled_on`/`disabled_on`, section group và giới hạn hiện có. Không chỉ đặt `name` trong `templates/*.json`, vì thao tác đó không đăng ký preset trong Add section. Chỉ thêm instance vào template khi thuộc yêu cầu; nếu placement hiện tại chặn template đích, báo gap, không tự sửa guard/schema ngoài quyền skill.
- **Kiểm tra trước bàn giao.** Tên preset trong mỗi schema phải duy nhất; preset thường có đúng một bản Figma mang tên mặc định; các preset tên riêng phải có yêu cầu rõ ràng và dùng đúng section chứa. Không xử lý lỗi trùng tên bằng tiền tố theme, số thứ tự hoặc hậu tố tự đặt.
- **Category trong Add section.** Khi build hoặc đồng bộ composition từ template, giữ metadata `name`/`category` và áp dụng [QA category theo base `main`](../../../qa/references/section-qa-baseline.md#add-section-category-theo-base-main): dùng đúng category của preset gốc; section riêng chỉ dùng category phù hợp đã có trên base, không tạo category mới.

## Workflow

1. **Read the reference.** Identify the target Figma frame and the intended page/section. Capture or inspect both desktop and mobile frames when available, including their viewport dimensions. If using Figma `get_design_context`, first load `figma:figma-design-to-code` as its prerequisite and request a screenshot; use its design evidence for analysis, while keeping this skill's configuration-only boundary.
2. **Inspect the theme.** Read the applicable `AGENTS.md` and theme contracts. Inventory existing sections, their schema settings and presets, their allowed blocks, and the target template or section group. Check how each plausible candidate already behaves on mobile. Do not infer unsupported settings from a screenshot.
3. **Map the design to existing controls.** Make a compact mapping of each visible region to an existing section/block, the settings that can express it, and the desktop/mobile behavior those settings provide. Choose the closest semantically correct composition. Use only controls that exist today.
4. **Configure the composition.** Set the existing section/block order, preset tree, copy, alignment, layout mode, spacing, colors, and available desktop/mobile options to match the reference as closely as the current theme permits. Apply the pagination guidance and existing height-option exception below when relevant. Keep resource selectors empty unless the user explicitly requested that media work. Prefer a section with native responsive behavior over one whose desktop structure breaks on mobile.
5. **Review both viewports.** Preview the configured result at the Figma frame sizes when possible. Compare hierarchy, content order, columns, alignment, spacing, line wrapping, and overflow against each frame. If a mobile frame was not supplied, inspect the theme's mobile viewport and state that this was the comparison used. Limit implementation changes to the height and scoped icon exceptions below.
6. **Report the result.** Name the changed configuration files and selected section/block types. Summarize desktop and mobile checks. Report any calibrated height scale and its calibration audit (not a customization record). List each material mismatch with the Figma expectation, the current rendering, and the missing existing control or behavior. Mark other custom follow-up as unimplemented. State whether requested media work was completed or references remain unselected.

## Global Theme Settings trong `config/settings_data.json`

- Build preset được phép chỉnh `current` trong `config/settings_data.json` local để Theme Settings khớp Figma bằng các setting ID đã có trong `config/settings_schema.json`. Đây là cấu hình theme, không phải custom implementation; không cần xin quyền riêng cho từng giá trị trong phạm vi build preset đã yêu cầu.
- Đối chiếu Style Guide và frame desktop/mobile, đọc schema và nơi setting được sử dụng trước khi chọn giá trị. Ưu tiên giá trị có bằng chứng; không suy từ một section để thay toàn bộ typography, palette hoặc kích thước dùng chung khi chưa có căn cứ.
- Kiểm tra kiểu dữ liệu, option, min/max/step và color scheme/resource reference. Giữ nguyên header comment, `presets` đã lưu, setting không liên quan và thay đổi của người dùng. Không đổi default/schema, thêm ID/option, sửa CSS/JS/Liquid hoặc custom CSS để bù control còn thiếu.
- Ghi mapping Figma → setting ID → giá trị cũ/mới và ảnh hưởng tới các section/block dùng chung. Giá trị gần nhất hoặc chi tiết không biểu đạt được phải ghi thành gap, không tuyên bố khớp hoàn toàn khi chưa preview cả hai viewport.
- Validate JSON, schema values và Theme Check; preview chỉ đọc. Quyền sửa file local không tự cấp quyền lưu Theme Editor, ghi cấu hình qua API/bot, push hay publish theme.

## Thay SVG cho icon value có sẵn từ Figma

- Khi build preset có icon (ví dụ menu Chevron/Plus hoặc button có icon), được phép **thay SVG của icon đã tồn tại**, không thêm icon mới. Đọc schema và luồng render để tìm đúng setting → icon value hiện có → nhánh SVG trong snippet tương ứng của theme đích; chọn value đúng ngữ nghĩa rồi thay SVG trong chính nhánh đó.
- Dùng SVG gốc export từ Figma, giữ path/geometry và viewBox; bảo toàn wrapper/class, tham số kích thước, accessibility, màu theo scheme và hành vi xoay/chuyển trạng thái hiện có. Không vẽ lại hoặc dùng screenshot thay SVG. Không đổi logic, CSS/layout hay hành vi button/menu qua ngoại lệ này.
- **Đồng bộ nét giữa các value cùng option.** Khi thay một icon theo Figma, rà các value cùng nhóm có nét tương đồng (ví dụ Menu Plus/Chevron hoặc nhóm arrow của button) và đồng bộ `stroke-width`, `stroke-linecap`, `stroke-linejoin` theo SVG Figma đã xác minh. So sánh độ dày hiển thị ở kích thước render thực tế, có tính tỉ lệ viewBox; không sao chép máy móc cùng con số khi kích thước khác nhau. Giữ nguyên path, viewBox, hướng và ý nghĩa của icon anh em nếu không có SVG Figma tương ứng; chỉ hiệu chỉnh nét của SVG đã có, không vẽ lại hoặc thêm icon. Không áp stroke cho icon fill, logo hoặc social thương hiệu. Ghi rõ value nào thay SVG gốc, value nào chỉ đồng bộ nét và các consumer bị ảnh hưởng; giữ nguyên hành vi hover/xoay/đóng mở và token màu hiện có.
- Không thêm icon value, case/nhánh render, snippet, setting/option, block hoặc control mới; không đổi tên value để tạo icon riêng. Nếu chưa có value phù hợp hoặc không tìm được nhánh SVG tương ứng, ghi gap và dừng phần thay icon đó.
- Kiểm tra các nơi dùng chung value/snippet trước khi thay; ghi rõ ảnh hưởng tới các consumer trong theme đích. Preview desktop/mobile và trạng thái liên quan (ví dụ menu đóng/mở, button) để kiểm tra kích thước, màu và xoay icon; thiếu preview thì ghi chưa xác minh.
- Đây là custom riêng của theme: ghi mapping setting/value → snippet/nhánh SVG, nguồn Figma, consumer bị ảnh hưởng và quy tắc giữ khi update base trong `docs/theme-customizations/<theme>.md`. Ngoại lệ chỉ cấp quyền thay SVG hiện có, không cấp quyền push/publish hoặc lưu Theme Editor. Quy tắc social bổ sung ở mục dưới vẫn áp dụng.

## Social trong preset và icon riêng của theme

- Khi Figma có social nhưng chưa có URL thương hiệu, cấu hình các setting social hiện có bằng `#` trong `current` local để hiển thị đúng icon; không bịa tài khoản hay tự dùng homepage nền tảng. URL thật được thay sau khi có dữ liệu. Không ghi đè URL thật đang có và không sửa social của theme khác.
- Ngoại lệ implementation giới hạn cho social: được phép thay các icon social tương ứng bằng SVG gốc Figma trong snippet social-icon của **theme đích**, giữ geometry/viewBox, accessibility và màu theo scheme (`currentColor`). Giữ social text mode, các platform không thuộc thiết kế và hành vi link hiện có; chỉ đổi thứ tự icon theo Figma nếu cần. Không thêm CSS/layout/setting khác qua ngoại lệ này.
- Tải/export asset gốc, không vẽ lại, không dùng ảnh screenshot làm icon, không đặt SVG icon vào assets và không lưu URL Figma tạm. Kiểm tra trên nền sáng/tối và desktop/mobile.
- Đây là custom riêng của theme, không phải preset-only: ghi các snippet/dependency đã đổi, nguồn Figma, lý do và quy tắc giữ khi update base trong `docs/theme-customizations/<theme>.md`. Ngoại lệ này không cấp quyền sửa implementation ngoài social, push/publish hay lưu Theme Editor.

## Theme-specific height-option calibration

Khi preset có phần này, đọc [Theme-specific existing height-option calibration](references/slideshow-height.md).

## View all và điều kiện dữ liệu

Khi Figma có View all, đọc điều kiện Liquid/JS của section và đối chiếu collection, URL, label, giới hạn render và visibility desktop/mobile. Giữ nguyên điều kiện gốc; không thêm ngoại lệ theo vị trí nút. Với overflow `products_count > max_products`, số lượng phải lớn hơn giới hạn, không chỉ lớn hơn số cột. Chọn giới hạn preset để vừa có sản phẩm trượt vừa thỏa điều kiện nút, đồng bộ Add section preset và instance local. Ví dụ 4 cột / render5 / collection6 thỏa cả hai.

Khi content work đã được yêu cầu, phối hợp [Collections — View all trong thiết kế](../../../setup-store/store-content-media/references/collections.md#view-all-trong-thiết-kế) để tái sử dụng/bổ sung sản phẩm đúng nguồn và đọc lại số khả dụng trên Online Store cho từng tab. Khi chỉ có quyền preset, dùng catalog đã có hoặc báo thiếu dữ liệu; không tự mở rộng quyền tạo sản phẩm. Không đổi số lượng collection chính xác từ Figma để lấp gap. Kiểm tra nút thực sự hiện sau initialization/chuyển tab; HTML có nút nhưng `hidden` chưa phải kết quả pass. Thiếu preview thì ghi chưa xác minh.

## Pagination visibility and spacing

Khi preset có phần này, đọc [Pagination visibility and spacing](references/pagination.md).

## Section/block có hotspot

Khi section hoặc block (kể cả block lồng nhau) có hotspot, đọc [Hotspot: tọa độ, crop và focal point store](references/hotspots.md). Đo tâm chấm nhìn thấy cho desktop/mobile và đối chiếu web sau crop; focal point 50% 50% được lưu trong Shopify media khi media work đã được yêu cầu, không sửa code để thay cho setting ảnh ở store.

## Stop and report a gap

Apart from the theme-specific existing height-option exception, scoped existing-icon replacement/social exceptions and explicitly requested media work, if matching the design would require a new section/block, new setting, changed block allow-list, custom logic, markup, CSS, or JavaScript, stop at the configuration boundary. Apply the closest reasonable existing composition if it remains useful; otherwise present the mapping and explain why no existing section is a suitable fit. Include the unmet design details in the gap list and wait for a separate instruction before other custom implementation. Media requests do not authorize an unspecified upload destination or theme push.
