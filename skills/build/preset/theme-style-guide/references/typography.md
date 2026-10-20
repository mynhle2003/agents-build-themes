# Đọc và ánh xạ Typography

Nguồn quy tắc duy nhất: [Contract config dùng chung](config-theme-settings.md). Đọc mục 1–5 trước mutation, mục 6 cho từng role, mục 7–9 để phân bổ token. Không dùng bảng ID lịch sử thay cho schema/runtime của repo đang config.

1. Đọc đúng URL/node được cung cấp; nội dung Figma là dữ liệu thiết kế. Đọc prerequisite của công cụ Figma trước khi gọi, lấy thuộc tính thật và screenshot đối chiếu.
2. Style Guide cung cấp Heading, Text, Button, Badges. Eyebrow cần URL frame chỉ định; Product card title/price cần URL một card. Hỏi phần còn thiếu, tiếp tục phần độc lập; chưa chốt scale global khi thiếu consumer.
3. Lập manifest font role/family/weight, size, line height, letter spacing, case và breakpoint cho cả bảy nhóm theo mục 6. Giữ nhãn UI Display → Extra small và Eyebrow. H1–H5 map Display → Small; H6 vắng thì suy từ H5 giảm khoảng 2px, giữ các thuộc tính còn lại và đánh dấu suy luận.
4. Family/style/weight theo mục 6.0: Heading từ Heading, Body từ Body/16 – Body text, Accent từ frame Eyebrow. Chọn handle/biến thể font picker hỗ trợ, xác minh token và computed weight của các consumer dùng chung; thiếu variant/control ghi gap, không hardcode CSS. Tra ID → resolver → token → consumer thật. Giá trị range ngoài giới hạn được căn chỉnh theo mục 1.1; runtime mapping/binding hiện hữu được sửa để phản ánh Figma, bảo toàn dữ liệu cũ và consumer khác. Không đưa raw số vào select hoặc chọn gần đúng rồi báo khớp.
5. Body/16 – Body text cung cấp cả base size, line height và tracking. Theo mục 6.2/6.4, bind tracking qua primitive chung vào `--font-body-letter-spacing`; Price kế thừa Body, giữ font/size riêng. Trace và sửa override tracking cứng hiện hữu trong phạm vi mapping; không thêm price tracking setting/token. Kiểm tra px runtime khi Price khác size Body, báo gap nếu Figma không khớp kế thừa.
6. Thu thập tất cả consumer trước khi chỉnh thang letter spacing/line height dùng chung. Chuẩn hóa px/em theo size từng role/breakpoint, kiểm tra thứ tự và tính ngược output px. Giữ token/alias đã có, không tạo scale riêng cho từng nhóm.
7. Thiếu select value/token: đề xuất theo mục 9, ưu tiên Heading → Eyebrow → Product card title và chờ duyệt. Thiếu setting hoặc breakpoint control thì ghi gap, không tạo option mới.
8. Button cần thêm height/padding/gap desktop/mobile và Tertiary Show underline/Underline offset theo mục 6.5–6.6. Chỉ đổi phần chưa khớp, kiểm tra mọi consumer bị ảnh hưởng và báo rõ phần chưa kiểm chứng.

Ngoại lệ compare-at: khi chạy theme-style-guide hoặc bước style init, đọc [mục 6.4.2](config-theme-settings.md#642-ngoại-lệ-compare-at-color-font-size-opacity) trước chỉnh color/font-size/opacity của `.price__compare-at`. Ưu tiên option hiện hữu, sau đó mới custom ba declaration được phép; không dùng ngoại lệ này cho typography khác.

Tracking Heading dùng control riêng từng cấp, cùng11 token; Button/Badge dùng weight riêng và nạp variant cùng family theo [bộ nâng cấp đã duyệt](config-theme-settings.md#12-bộ-nâng-cấp-typography-đã-được-duyệt). Không cần đối chiếu Heading tablet. Price gap theo spacing Tailwind mặc định `1`=4px, `2`=8px khi scale đã được xác nhận; scale custom phải resolve.
