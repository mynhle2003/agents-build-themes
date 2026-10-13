# Theme-specific height-option calibration

Áp dụng khi section hoặc block hiện có option ảnh hưởng chiều cao (ví dụ Slideshow, Hotspot: Product callout, Hero). Đây là hiệu chỉnh cấu hình riêng của theme, **không tính là custom**, dù các giá trị cố định được khai báo trong Liquid/CSS. Không thêm hậu tố `(custom)` hoặc đưa riêng hiệu chỉnh này vào bảng Customizations.

- Chỉ áp dụng trên `theme/<slug>` hiện tại; không đổi shared `main` hoặc theme khác.
- Đo đúng phần mà option điều khiển: với Product callout là vùng media, không cộng padding section, header hoặc nội dung xếp bên dưới. Lấy chiều cao Figma desktop/mobile độc lập; không đoán viewport thiếu.
- Map chiều cao chuẩn vào option `medium` hiện hữu. Nhân toàn bộ thang cố định theo `old value × target Medium / old Medium`, làm tròn hợp lý, giữ Medium chính xác và thứ tự tăng dần. Nếu control không có Medium, dùng lựa chọn chuẩn đã có và ghi rõ mapping; không tạo option mới.
- Giữ nguyên Adapt/Full screen, IDs, labels, option values, defaults và breakpoints. Control số có sẵn thì cấu hình trực tiếp trước khi cần hiệu chỉnh mapping.
- Chỉ sửa giá trị/mapping chiều cao cố định cần thiết, scope vào section đích nếu implementation dùng chung. Không đổi markup, JavaScript, global tokens hoặc thêm custom CSS settings. Chọn option chuẩn ở cả preset và instance template.
- Lưu audit riêng trong `docs/audits/`: source node, kích thước media/frame, scale cũ/mới, file/control, viewport và kết quả QA. Khi cập nhật base, review mappings upstream và giữ scale theme đã hiệu chỉnh; phân loại không custom không có nghĩa là được ghi đè calibration.
- Chạy Theme Check, kiểm tra thứ tự thang, preset/instance và desktop/mobile preview. Báo rõ giới hạn preview. Nếu checker local còn coi mọi CSS/Liquid diff là custom, báo hạn chế phân loại đó; không thêm record custom chỉ để hợp thức hóa hoặc bỏ qua failure.

Ngoại lệ chỉ bao gồm calibration của **option chiều cao đã có**. Logic responsive mới, wrapper, thay đổi layout, option mới hoặc CSS khác vẫn theo ranh giới cấu hình và quy tắc custom của repo.
