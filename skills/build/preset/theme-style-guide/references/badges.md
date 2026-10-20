# Đọc và ánh xạ màu tag/badge

Typography Badges đọc từ Style Guide theo [contract chung, mục 6.3 và 7–9](config-theme-settings.md); dùng cùng scale với Heading/Text/Eyebrow/Button/card, không tạo bộ token riêng. Các quy tắc màu/scope bên dưới vẫn áp dụng.


- Đọc màu nền/chữ của Sale, Sold out, Custom 1/2 từ frame hoặc variables Figma, tách khỏi các property màu scheme và sale price. Nhãn “Badge 1/2” không phải yêu cầu đổi label/tag hay bật badge trong store.
- Kiểm tra scope của setting: nếu màu badge toàn cục, chỉ đổi khi các frame scheme được cung cấp cùng dùng màu đó; nếu các scheme khác màu thì báo không biểu diễn được bằng setting toàn cục. Không tự chuyển badge toàn cục thành màu theo scheme.

  | Role Figma | Setting toàn cục hiện có |
  | --- | --- |
  | Sale background / text | `badge_sale_background_color` / `badge_sale_text_color` |
  | Sold out background / text | `badge_sold_out_background_color` / `badge_sold_out_text_color` |
  | Custom 1/2 background / text | Chỉ ánh xạ vào ID đúng role nếu schema/runtime có hỗ trợ riêng |

- Đọc `snippets/badge.liquid`, `snippets/product-badges.liquid` và CSS màu `product-badge--manual` khi đối chiếu tag custom. Không dùng setting Sale/Sold out hoặc màu scheme chung để mô phỏng Custom 1/2 nếu chúng ảnh hưởng các role khác. Nếu thiếu setting, báo màu Figma cùng giới hạn; không thêm schema/CSS theo yêu cầu đồng bộ cấu hình.
- Sale price config field `sale_price` trong scheme; không lấy màu nền Sale badge gán sang Sale price. Virelle đã xóa picker global `badge_sale_price_color` dư, không tạo lại. Giữ label, collection rules, `badge_custom_enabled`, product tags và option hiển thị badge hiện tại. Dùng cùng quy tắc định dạng màu/alpha như color scheme và chỉ sửa giá trị cần đổi.
