# Khởi tạo và cập nhật Google Sheet QA qua API

Đọc reference này ở bước QA đầu, khi khởi tạo báo cáo hoặc khi cập nhật bảng đã có. Mẫu style có một nguồn chính: [sheet-style.json](../assets/sheet-style.json); quy tắc nội dung ở [sheet-report.md](sheet-report.md).

## Áp dụng style ngay bước đầu QA

- Tái sử dụng đúng Sheet/tab/gid người dùng đã chỉ định và nguồn trong file tổng quan QA hiện có (`docs/qa/<page>-qa.md` hoặc `check-perfect-<page>.md`) và file section tương ứng. Chưa có Sheet thì lưu hồ sơ local, chỉ hỏi thông tin thiếu; không tự tạo tài liệu cloud thay thế khi chưa được yêu cầu.
- Khi bắt đầu QA trên tab mới/trống đã được giao, áp dụng style hiện hành ngay cùng bước0 Tổng quan. Không chờ kiểm xong cả page hoặc xin chốt lại các lựa chọn style đã được người dùng chấp nhận. Lưu version/path hoặc snapshot JSON và link Figma/preview/Sheet trong hồ sơ page để lần sau tiếp tục dùng.
- Bảng10 cột A:J: STT, Section, Thiết bị, Thành phần, Tiêu chí, Figma, Hiện tại, Hướng xử lý, Lần fix, Trạng thái. Header2 tầng, F1:G1 gộp Nội dung; header khác gộp dọc. Arial10 dữ liệu/11bold header #1F4E78; mọi ô middle, header center/middle; wrap. Width56/141/151/191/221/300/300/301/100/140px.
- Dropdown Lần fix một lựa chọn: Lần 1–Lần 5, Bỏ qua; chip xanh dương/tím/cam/vàng/xanh lá/xám theo JSON. Trạng thái dùng dropdown màu hiện hành. Chỉ chip có màu, ô thường không nền. Figma xanh/Hiện tại đỏ chỉ ở lỗi chưa khớp đã xác minh; khi Khớp bỏ nền cả hai, giữ giá trị lịch sử trong chu kỳ fix.
- Các section liền mạch sau Tổng quan; nguồn/phạm vi ở cuối. Không tạo bảng/section mẫu có kết quả QA giả. QA đầu: sau hướng xử lý cụ thể đã xác minh dùng preset hoặc config/settings_data.json, gắn Lần 1 và giữ Chưa khớp cho đến khi fix + QA đạt.
- Với tab đã có nội dung/style được chỉnh, đọc live trước; chỉ áp phần người dùng yêu cầu hoặc sửa sai lệch so với mẫu đã chấp nhận. Không reset cả bảng, không ghi đè ghi chú hoặc cờ người dùng bằng snapshot local cũ.

## API là đường xử lý mặc định

1. Tìm connector/API Google Sheets được kết nối và đọc schema công cụ hiện tại. Đọc skill Google Sheets của connector nếu có. Không lấy công cụ Spaces/artifact chưa bound Google Sheet làm API cho Google Sheets.
2. Đọc metadata để xác định spreadsheetId, sheetId, tên tab và grid/merge hiện có. Đọc CellData trong phạm vi cần đổi: value/formula, validation, format, chip metadata khi có. Snapshot trước ghi, map key lỗi ổn định sang vị trí live; không dùng số hàng làm identity.
3. Chuẩn bị batch có phạm vi rõ: giá trị literal, insert/merge, format, width, dropdown. Chỉ ghi field cần đổi; giữ công thức, Hướng xử lý, chip/màu, thứ tự và merge ngoài phạm vi. Không tái tạo toàn bảng từ bản local. Chèn dòng lỗi đúng section, cập nhật các range liên quan và giữ nguồn cuối.
4. Với chip có màu, dùng capability được API hỗ trợ thực sự; ưu tiên giữ/copy native validation từ exemplar/template đã xác minh. Không bịa trường option-color không có trong schema; không tự đổi cấu trúc merge sang table chỉ để có chip. Nếu API không thể biểu diễn phần giao diện cần thiết, nêu đúng giới hạn và chỉ dùng Computer Use cho phần đó khi người dùng đã cho phép.
5. Đọc lại tất cả vùng vừa ghi và lân cận bằng API: values, rule/dropdown, format/merge, nguồn và thứ tự. Khi có giao diện truy cập được, dùng Computer Use để kiểm style ở zoom đọc được và lưu ảnh; thao tác dữ liệu/định dạng hàng loạt vẫn ưu tiên API.
6. Đồng bộ Markdown/checkpoint cùng lượt. Ghi rõ range đã ghi/đọc lại; không gọi một batch thành công là đã hoàn tất nếu chưa xác minh. API không khả dụng thì giữ kế hoạch local và báo phần chưa đồng bộ; không dùng credential/tokens hoặc endpoint không được cung cấp để vượt quyền.

Bảo trì skill hoặc ghi nhớ style không tự cấp quyền tạo tài liệu cloud, thay sharing, gửi thông báo, sửa theme hay chạy lại QA. Không coi việc đã áp style là tiêu chí giao diện theme đã Khớp.
