---
name: theme-style-guide
description: Ánh xạ style guide Figma vào mọi option Shopify Theme Settings hiện có, gồm typography, color scheme, button và tag; tạo scheme còn thiếu nhưng không thêm hoặc xóa option.
---

# Cấu hình style guide Figma cho theme

Ánh xạ mọi thuộc tính style guide Figma có option tương ứng trong Theme Settings hiện có: typography heading/body/accent, color scheme, button, tag/badge, shape, spacing, icon, form và các nhóm khác. Không giới hạn việc đồng bộ theo nhóm tính năng. Quy tắc cốt lõi: **không thêm hoặc xóa option Theme Settings**; thuộc tính có option biểu diễn được thì ánh xạ và cập nhật.

## Giới hạn chỉnh sửa

- Mặc định cập nhật giá trị trong `config/settings_data.json`. Không thêm hoặc xóa setting/option Theme Settings. Được điều chỉnh min/max/step của setting range đang có để biểu diễn giá trị Figma và sửa mapping Liquid/CSS để option hiện có điều khiển đúng output; giữ ID, kiểu và các lựa chọn select hiện có. Giữ default nếu vẫn hợp lệ, nếu cần đổi default thì báo rõ. Không tạo setting mới để bù thuộc tính thiếu. Ghi hồ sơ custom khi sửa implementation theo quy tắc repo.
- Chỉ đặt giá trị cho ID đã được định nghĩa trong schema và đúng kiểu/giới hạn hiện có. ID đã có trong schema nhưng chưa được lưu trong `current` có thể được ghi giá trị; đó không phải thêm option.
- Mặc định chỉ sửa `current` của theme đang checkout. Giữ nguyên saved presets, section/block settings, scheme ngoài phạm vi và các giá trị không có bằng chứng thiết kế; chỉ sửa saved preset khi người dùng yêu cầu rõ.
- Giữ nguyên thay đổi có sẵn của người dùng. Không tự checkout nhánh, commit, push hoặc ghi lên store từ yêu cầu cấu hình local.

## Ánh xạ mọi option hiện có

- Bắt đầu từ bằng chứng Figma và toàn bộ schema hiện tại; các bảng bên dưới là gợi ý ID, không phải danh sách cho phép đóng. Với option ngoài bảng, đọc nơi tiêu thụ Liquid/CSS/JS để xác minh ý nghĩa và ánh xạ tương tự.
- Cập nhật đúng kiểu và giá trị select. Với range có sẵn chưa chứa giá trị Figma, mở rộng min/max hoặc giảm step tối thiểu để giá trị hợp lệ, giữ các giá trị/default đã lưu hợp lệ và giới hạn Shopify. Không làm tròn sang giá trị gần nhất. Nếu runtime bỏ qua option hoặc override trái ý nghĩa option, sửa mapping hiện có và ghi hồ sơ custom; chỉ báo thiếu khi cần thêm setting/lựa chọn mới hoặc không có bằng chứng thiết kế.
- Đọc font family/weight/style của nội dung thiết kế, không lấy font chú thích. Với `font_picker`, xác minh handle trong danh mục Shopify trước khi ghi. Setting chung phải phù hợp mọi role/breakpoint chịu tác động; không đổi font body sang weight 500 chỉ để khớp button nếu body Figma dùng 400.
- Phân biệt giá trị chung với breakpoint cụ thể. Token được chỉ định chung áp dụng cho các setting breakpoint tương ứng nếu không có override trong thiết kế; frame chỉ định desktop không tự tạo bằng chứng mobile.
- Body: ánh xạ family/weight/style vào `type_primary_font`, base size vào `type_body_size`, line-height vào `type_body_leading` sau khi đọc runtime. Body role 12/14/18px có thể là token cố định, không đổi base size để mô phỏng mọi role. Accent dùng `type_accent_font` khi có bằng chứng đúng role.
- Button: đối chiếu `button_radius_style`, `button_height_desktop/mobile`, `button_padding_inline_desktop/mobile`, `button_font_size`, `button_font_size_mobile`, `button_letter_spacing`, `button_primary/secondary/tertiary_font`, `button_*_text_case`, border width, underline/offset và các option khác đang có. Màu normal/hover thuộc scheme được xử lý bên dưới. Không loại trừ size/typography button chỉ vì skill ban đầu chỉ hỗ trợ heading.
- Tag/badge và nhóm khác: ánh xạ cả màu, font, kích thước, radius hoặc spacing khi có option đúng role; giá trị thiếu bằng chứng thì giữ nguyên. Không tự thay nội dung thương mại, product tags hay bật/tắt tính năng từ một nhãn minh họa.

## Đọc và ánh xạ heading

Đọc [Đọc và ánh xạ heading](references/typography.md) khi xử lý phần này.

## Đọc và ánh xạ color scheme

Đọc [Đọc và ánh xạ color scheme](references/color-schemes.md) khi xử lý phần này.

## Đọc và ánh xạ màu tag/badge

Đọc [Đọc và ánh xạ màu tag/badge](references/badges.md) khi xử lý phần này.

## Ví dụ đã đối chiếu: Essen

Đọc [Ví dụ đã đối chiếu: Essen](references/essen-example.md) khi xử lý phần này.

## Kiểm tra và bàn giao

- Parse JSON sau khi bỏ comment đầu file theo định dạng Shopify; giữ comment và định dạng để diff tối thiểu.
- Đối chiếu giá trị sửa với kiểu, options, min/max/step của schema; với scheme, kiểm tra từng ID thuộc `definition`, định dạng màu và alpha, ID scheme duy nhất và các tham chiếu hiện có vẫn resolve được. Nếu sửa range/mapping, so sánh schema trước/sau để xác nhận không thêm/xóa ID hoặc lựa chọn select, các default và giá trị đã lưu vẫn hợp lệ; kiểm tra token đầu ra và hồ sơ custom. Giữ saved presets, section/block settings và các giá trị ngoài phạm vi, không ghi đè thay đổi đã có.
- Chạy `shopify theme check --path . --fail-level error --no-color` nếu CLI có sẵn; báo kết quả hoặc lý do chưa chạy được.
- Báo các giá trị đã đổi, thuộc tính bỏ qua và giới hạn runtime còn lệch Figma. Không tuyên bố khớp hoàn toàn khi mới kiểm tra cấu hình, chưa kiểm tra storefront.
