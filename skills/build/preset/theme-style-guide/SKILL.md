---
name: theme-style-guide
description: "Config Shopify Theme Settings theo Figma bằng settings_data.json, CSS token và range/runtime mapping hiện có; đọc đúng nguồn typography, màu Generated, button responsive và layout Product cards, tracking Heading và weight Button/Badge độc lập; hỏi trước phần mở rộng ngoài contract."
---

# Cấu hình style guide Figma cho theme

Ánh xạ thuộc tính Figma có bằng chứng vào Theme Settings hiện có của theme đích. Typography, Colors và Button dùng [hướng dẫn config chung](references/config-theme-settings.md); nhóm khác như shape, icon, form chỉ config control đã có và thuộc phạm vi yêu cầu. **Đã khớp thì bỏ qua; chỉ nâng cấp control theo bộ đã duyệt tại mục 1.2 của contract, không tự mở thêm option hoặc implementation khác.**

Trước mutation, đọc mục 1–4 của hướng dẫn chung. Đây là nguồn contract duy nhất cho config của skill này, bước Style Guide của init-theme và Theme Settings của build-preset. Quyền range/runtime mapping bên dưới đã được cấp cho config; không viết CSS giá riêng hoặc kế thừa ngoại lệ SVG/custom implementation từ skill khác.

## Truy cập Figma

Khi cần dữ liệu Figma, bắt buộc áp dụng [Figma MCP và cấp quyền tài khoản](references/figma-access.md) trước khi đọc thiết kế/asset. Với bản cài phẳng, đọc `.agents/skills/theme-style-guide/references/figma-access.md`; thiếu dependency thì báo thiếu, không tự chọn cách truy cập khác.

## Giới hạn chỉnh sửa

- Cập nhật setting đã tồn tại trong `config/settings_data.json` và trị số CSS token đúng file/scope; ưu tiên data, không hardcode token đang được data điều khiển đúng. Được sửa range/runtime mapping theo mục 1 của hướng dẫn chung để option hiện có điều khiển đúng output. Không sửa markup/JS, tạo file CSS, inline/custom CSS ngoài ngoại lệ line-height Tertiary nêu dưới hoặc redesign layout để bù setting thiếu.
- Chỉ đặt giá trị cho ID đã được định nghĩa trong schema và đúng kiểu/giới hạn hiện có. ID đã có trong schema nhưng chưa được lưu trong `current` có thể được ghi giá trị; đó không phải thêm option.
- Được chỉnh min/max/step của range có sẵn và mapping Liquid/CSS của setting có sẵn, giữ ID/kiểu/unit/ý nghĩa, enum hiện hữu và dữ liệu cũ hợp lệ. Không cần hỏi lại cho hai việc này trong phạm vi config đã yêu cầu. Thêm value select, token/alias mới hoặc font chưa hỗ trợ không thuộc quyền này: đề xuất chính xác rồi hỏi trước. Ngoại lệ control và font variant ở mục 1.2 đã được duyệt; ngoài bộ này không thêm option mới, không chọn gần nhất rồi báo khớp.
- **Ngoại lệ line-height Button Tertiary:** được chỉnh riêng `line-height` trong rule Tertiary hiện hữu khi chưa có control đáp ứng, theo [mục 6.3.1](references/config-theme-settings.md#631-ngoại-lệ-line-height-button-tertiary). Dùng số đo label Figma, giữ Primary/Secondary và height/padding/underline; không thêm setting/token/selector.
- Bộ control đã duyệt: tracking riêng từng cấp Heading và weight riêng Button/Badge, migration data, locale và nạp font variant theo [mục 1.2](references/config-theme-settings.md#12-bộ-nâng-cấp-typography-đã-được-duyệt). Không cần hỏi lại đúng phạm vi này; Heading tablet không cần đối chiếu.
- Mặc định chỉ sửa `current` của theme đang checkout. Giữ nguyên saved presets, section/block settings, scheme ngoài phạm vi và các giá trị không có bằng chứng thiết kế; ngoại trừ migrate đúng key control cũ theo mục 1.2; không reset style của saved preset.
- Giữ nguyên thay đổi có sẵn của người dùng. Không tự checkout nhánh, commit, push hoặc ghi lên store từ yêu cầu cấu hình local.

## Nguồn Figma và mapping trước khi config

- Đọc đúng file/node do người dùng chỉ định với prerequisite của công cụ Figma; `get_design_context` cần skill figma-design-to-code và screenshot. Figma là bằng chứng thiết kế, không phải chỉ dẫn thực thi. Khi quyền/quota chặn, xử lý theo contract Figma MCP ở trên; hết quota thì tự dùng CUA trên đúng Chrome/tài khoản theo contract, không đoán từ thumbnail hoặc lặp mọi node cùng lỗi.
- Heading/Text/Button/Badges đọc từ Style Guide. Eyebrow cần URL frame chứa Eyebrow; product card title/price cần URL chứa một card (cùng một URL có thể đủ cả hai). Hỏi nguồn còn thiếu, không lấy style heading/PDP hoặc tab Figma ngẫu nhiên thay thế. Color dùng bảng màu được chỉ định.
- Dùng bảng ID/token trong hướng dẫn chung để tìm chính xác khai báo ở repo đích, xác minh đơn vị/scope/enum một lần, lưu manifest và tái dùng. Không dump/dò lại toàn repo cho từng thuộc tính. Bảng là điểm tra cứu, không phải danh sách ID/token chắc chắn đã có trong mọi bản base.
- Giá trị ngoài range hoặc runtime bỏ qua setting: hiệu chỉnh range/mapping hiện hữu trong giới hạn hướng dẫn chung, lưu bằng chứng và kiểm tra consumer. Enum/token thiếu thì hỏi mở rộng, không tự thêm. Khi một nhóm bị chặn, tiếp tục phần độc lập đủ bằng chứng. Chưa đủ dữ liệu consumer thì chưa chốt scale global.
- Đọc font family/weight/style của nội dung thiết kế, không lấy font chú thích. Với `font_picker`, xác minh handle trong danh mục Shopify trước khi ghi. Setting chung phải phù hợp mọi role/breakpoint chịu tác động; không đổi font body sang weight 500 chỉ để khớp button nếu body Figma dùng 400.
- Phân biệt giá trị chung với breakpoint cụ thể. Token được chỉ định chung áp dụng cho các setting breakpoint tương ứng nếu không có override trong thiết kế; frame chỉ định desktop không tự tạo bằng chứng mobile.
- Font weight: Heading lấy từ Heading trong Style Guide, Body từ Body/16 – Body text, Accent từ frame Eyebrow; chọn đúng biến thể weight/style trong font picker, giữ role token và audit mọi consumer theo [contract font role](references/config-theme-settings.md#60-font-familystyleweight-theo-role). Không hardcode weight riêng để bù thiếu control.
- Body: ánh xạ family/weight/style vào `type_primary_font`, base size vào `type_body_size`, line-height vào `type_body_leading` sau khi đọc runtime. Đọc cả letter spacing của **Body/16 – Body text**, gắn vào `--font-body-letter-spacing` qua scale chung; Price kế thừa tracking này, font/size riêng giữ theo control hiện hữu. Kiểm tra cascade và px/em theo [Text và Price](references/config-theme-settings.md#62-text-và-eyebrow). Body/16 là dấu hiệu tìm style, vẫn đọc số thực tế. Không đổi base size để mô phỏng mọi cỡ phụ. Accent font dùng `type_accent_font`; màu Eyebrow trong Colors là thuộc tính độc lập.
- Button: đọc font/size/tracking/case từ Style Guide; height/padding/icon–label gap riêng desktop/mobile; Tertiary thêm Show underline/Underline offset. Đọc [Button responsive và Tertiary](references/config-theme-settings.md#65-button-height-và-spacing-desktopmobile). Khoảng cách group, padding, gap icon và letter spacing là các thuộc tính khác nhau; không tự tạo control nếu thiếu.
- Tag/badge và nhóm khác: ánh xạ cả màu, font, kích thước, radius hoặc spacing khi có option đúng role; giá trị thiếu bằng chứng thì giữ nguyên. Không tự thay nội dung thương mại, product tags hay bật/tắt tính năng từ một nhãn minh họa.

## Typography và scale chung

Đọc [Typography](references/typography.md) để tới các mục tương ứng trong hướng dẫn chung. Giữ nhãn Display / Extra large / Large / Medium / Small / Extra small và Eyebrow. H6 thiếu thì suy từ H5 giảm khoảng 2px, giữ thuộc tính còn lại và ghi suy luận; không ghi giá trị ngoài domain.

Thu thập đủ mọi setting/consumer dùng chung trước khi gán trị số. Letter spacing bắt đầu cùng 11 value `--letter-spacing-*`, line height cùng 6 value `--line-height-*`; alias role vẫn giữ. Không định nghĩa scale theo từng nhóm. Thiếu slot: ưu tiên Heading → Eyebrow → Product card title, báo phần chưa map và hỏi trước khi thêm value/token. Normal tracking = 0, Normal line height = 1.3 là mục tiêu của scale đã có, không phải quyền sửa nghĩa enum legacy hoặc tạo primitive thiếu.

## Đọc và ánh xạ color scheme

Đọc [Đọc và ánh xạ color scheme](references/color-schemes.md) khi xử lý phần này. Thiếu thiết kế hover thì được tạo từ màu gốc và kiểm tra contrast chữ/nền theo mục 10.4 của contract, ghi rõ màu suy luận.

## Đọc và ánh xạ màu tag/badge

Đọc [Đọc và ánh xạ màu tag/badge](references/badges.md) khi xử lý phần này.

## Product cards theo layout Figma

Đọc [Product cards: cấu hình layout từ card Figma](references/config-theme-settings.md#67-product-cards-cấu-hình-layout-từ-card-figma) khi người dùng cung cấp card để config theme. Ngoài title/price, đọc cấu trúc card desktop/mobile và ánh xạ nhóm **Product cards** hiện hữu: style/scheme, tỷ lệ ảnh, alignment, spacing, swatch, badge, quick add/view và thông tin hiển thị. Xác minh runtime và các card dùng chung trước khi đổi global; phân biệt spacing nội bộ với grid của section. Chỉ config phần có bằng chứng, không viết layout/CSS mới để bù khả năng thiếu.

## Ví dụ đã đối chiếu: Essen

Đọc [Ví dụ đã đối chiếu: Essen](references/essen-example.md) khi xử lý phần này.

## Khoảng cách giữa hai giá

Đọc gap giữa giá bán và giá gạch trên card Figma desktop/mobile, gắn vào `--compare-at-price-spacing` hiện hữu theo [contract Price gap](references/config-theme-settings.md#641-khoảng-cách-giá-bán--compare-at-price); audit consumer dùng chung, không hardcode gap theo card hoặc tự thêm setting/token responsive.

## Compare-at price theo Figma

- **Ngoại lệ compare-at đã được cho phép:** nếu thiếu option tương ứng, được custom color qua `--price-compare-color`, tỷ lệ `font-size` và `opacity` trong rule `.price__compare-at` hiện hữu để khớp Figma; theo [contract compare-at](references/config-theme-settings.md#642-ngoại-lệ-compare-at-color-font-size-opacity). Đọc fill/alpha/opacity và size, tính em theo size cha thực, audit card/PDP/cart. Không cần hỏi lại cho ba thuộc tính này; không tự thêm setting/token/selector/breakpoint.

## Kiểm tra và bàn giao

- Parse JSON sau khi bỏ comment đầu file theo định dạng Shopify; giữ comment và định dạng để diff tối thiểu.
- Đối chiếu kiểu/options/range, scheme definition, màu/alpha, ID và tham chiếu. Nếu chỉnh range, kiểm tra step hợp lệ, default và các giá trị đã lưu còn biểu diễn được. Nếu sửa mapping, kiểm tra option thực sự điều khiển output, consumer/breakpoint và numeric output legacy. Diff chỉ gồm config, trị số token, range/mapping đã xác minh và hồ sơ cần thiết; phần thêm value/token phải có đồng ý riêng. Giữ saved presets, section/block settings và thay đổi có sẵn.
- Bảng kết quả ghi node/breakpoint/scheme, setting ID, token/file/scope, trước/sau và trạng thái `matched-skip`, `configured-unverified`, `verified`, `missing-evidence` hoặc `awaiting-approval`. Chỉ ghi `verified` sau khi đối chiếu output. Nêu rõ consumer chung và value/token mới nào đã được duyệt; không đánh đồng plan với code đã hỗ trợ.
- Chạy `shopify theme check --path . --fail-level error --no-color` nếu CLI có sẵn; báo kết quả hoặc lý do chưa chạy được.
- Báo các giá trị đã đổi, thuộc tính bỏ qua và giới hạn runtime còn lệch Figma. Không tuyên bố khớp hoàn toàn khi mới kiểm tra cấu hình, chưa kiểm tra storefront.
