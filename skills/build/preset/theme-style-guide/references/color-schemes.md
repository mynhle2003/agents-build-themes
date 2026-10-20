# Đọc và ánh xạ color scheme

Áp dụng [contract dùng chung](config-theme-settings.md), đặc biệt mục 1, 10 và 11; reference này bổ sung quy tắc bảo toàn scheme.


1. Đọc bảng màu và frame mẫu tương ứng từng scheme bằng công cụ Figma. Với `get_design_context`, dùng `figma-design-to-code` và screenshot như phần heading. Frame mẫu button cung cấp cả màu thuộc scheme và các thuộc tính hình dạng/typography có thể ánh xạ vào option hiện có. Nếu cần đọc variable/mode/alias bằng `use_figma`, đọc `figma-use` trước và chỉ thực hiện truy vấn; không sửa thiết kế Figma.
2. Lập bảng bằng chứng gồm node nguồn, tên/số scheme, property, RGB và opacity. Với `Generated/N` hoặc `from Generated/N`, tra đúng cấp N bằng Layouthub Generate Color, nhập Heading HEX của palette vào Insert a Hex color theo mục 11 của contract; không coi N là opacity. Variable/alias khác phải resolve đúng mode/scheme trước khi ghi. Không đoán mã màu từ tên token, không lấy pixel gần đúng từ ảnh và hover không có thiết kế thì tạo từ màu gốc theo mục10.4 của contract và ghi derived-hover, không giả là màu Figma. Nếu bảng màu là ảnh, chỉ dùng mã/opacity được ghi rõ trong ảnh; token chưa resolve được thì bỏ qua và báo.
3. Đọc `color_scheme_group.definition`, `role`, `current.color_schemes` và CSS/Liquid tiêu thụ để đối chiếu ý nghĩa. Ánh xạ theo property thực tế, không chỉ theo màu đang giống nhau:

   | Property Figma | ID trong scheme (nếu schema định nghĩa) |
   | --- | --- |
   | Background | `background` |
   | Heading | `heading` |
   | Text | `text` |
   | Heading highlight | `heading_highlight` |
   | Eyebrow (nhãn cũ Accent / Eyebrow text; có thể dùng chung link/icon) | `accent` |
   | Border | `border` |
   | Shadow | `shadow` |
   | Sale price | `sale_price` |
   | Primary button background / label / outline | `button_primary_background` / `button_primary_text` / `button_primary_border` |
   | Secondary button background / label / outline | `button_secondary_background` / `button_secondary_text` / `button_secondary_border` |
   | Tertiary button color | `button_tertiary_text` |
   | Button hover property | ID `button_*_hover_*` tương ứng; dùng nguồn hover nếu có, nếu thiếu thì tạo palette theo mục10.4 |

   `Overlay`, `Bg Bar`, `Bg Component` không mặc nhiên là `shadow`, `background` hay button background. Chỉ ánh xạ khi schema/runtime có setting đúng ý nghĩa. Không lấy màu badge làm sale price hay text thuộc scheme.
4. Giữ ID scheme đã tồn tại để bảo toàn tham chiếu từ section/block/template. Với bảng đánh số rõ `Color scheme N`, dùng `scheme-N` nếu repository sử dụng quy ước đó và không có mapping riêng trái ngược. Nếu tên/mapping mơ hồ và ảnh hưởng scheme đang được sử dụng, hỏi mapping; vẫn có thể xử lý scheme đã xác định. Không tự đổi `default_color_scheme` hoặc lựa chọn scheme của bất kỳ section/block nào.
5. Cập nhật scheme đã có bằng cách chỉ sửa các ID có bằng chứng. Tạo scheme còn thiếu dưới `current.color_schemes` bằng ID ổn định và object `{ "settings": {...} }`; khởi tạo các ID có default trong `definition`, rồi phủ các màu Figma đã xác minh. Không clone scheme khác để suy ra màu chưa được thiết kế chỉ định. Default schema chỉ là fallback cho scheme mới, phải báo rõ và không tuyên bố đã khớp Figma. Giữ scheme dư; chạy lại không tạo ID trùng hoặc đổi thứ tự/tham chiếu không cần thiết.
6. Màu đặc dùng `#RRGGBB`; màu có opacity dùng `rgba(R, G, B, A)` khi setting `color` cho phép alpha. Giữ alpha thay vì blend với background. Ví dụ trắng 80% là `rgba(255, 255, 255, 0.8)`. Nếu schema không biểu diễn được opacity/gradient, bỏ qua; không đổi schema/CSS hay thêm ID lạ.
7. Báo scheme đã cập nhật/tạo, màu bị bỏ qua, token chưa resolve, và default dùng cho scheme mới. Kết quả kiểm tra cấu hình không phải xác nhận storefront khớp toàn bộ.
