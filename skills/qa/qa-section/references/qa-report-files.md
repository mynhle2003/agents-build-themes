# Hồ sơ QA theo section

Áp dụng khi tạo, kiểm lại, sửa theo vòng hoặc gộp tài liệu QA local. Giữ một file cho mỗi section của page, cập nhật qua mọi lượt QA; không tạo thêm file theo ngày, lượt recheck hoặc vòng Fix lần N.

## File và phạm vi

- Mặc định `docs/qa/<page>-<section>.md`, ví dụ `homepage-hotspot-gallery.md`. Tái sử dụng file theo section đã có; tên ổn định, không chứa ngày. Các instance cùng type nhưng nội dung/nguồn khác nhau cần slug hoặc instance ID riêng để không trộn kết quả. Không gộp khác theme/page.
- Một file tổng quan cho page, mặc định `docs/qa/<page>-qa.md`, giữ mục lục liên kết từng section, nguồn chung, manifest/order, điều kiện đo, checkpoint, style Sheet, validation và giới hạn toàn phạm vi. Nếu đã có `check-perfect-<page>.md` làm tổng quan thì cập nhật file đó; không tạo tổng quan thứ hai chỉ vì khác tên. Tìm cả hai quy ước trước khi hỏi lại nguồn.
- Header, Announcement bar, Footer và overlay được QA có file riêng trong phạm vi page. Không buộc số section cố định hoặc tạo file giả cho phần chưa kiểm.

## Nội dung mỗi section

Đầu file ghi theme/template/instance, nguồn desktop/mobile, preview và thời điểm kiểm gần nhất; đặt kết quả hiện hành hoặc snapshot Sheet mới nhất trước lịch sử. Nêu rõ giá trị gốc và kết quả sau fix để không đọc snapshot cũ thành tình trạng mới.

Gộp các lượt QA/recheck/Fix lần N vào lịch sử trong cùng file, có ngày, vòng, phạm vi, bằng chứng và tiêu chí được cập nhật. Giữ số đo gốc, expected/actual/status, mapping setting trước/sau và mục còn lệch/chưa xác minh; ghi rõ kết luận nào được thay thế, không gọi evidence cũ là đo mới. Dùng key page/template + instance + breakpoint + thành phần + tiêu chí, không dựa riêng số hàng Sheet. Kết quả mới chỉ thay thế tiêu chí thực sự đã kiểm lại; không mặc định toàn section đạt từ một phần pass.

Screenshot/số đo có thể nằm trong `output/qa/<run>/` theo ngày/vòng, liên kết từ file section; không nhân bản toàn báo cáo để lưu evidence. Nêu rõ nếu evidence chỉ còn local và không thuộc commit. Quy tắc tổ chức file không tự cấp quyền sửa theme, ghi Sheet, commit hoặc push.

## Khi gộp hồ sơ có sẵn

Đọc file mới nhất và các lượt cũ trước khi gộp. Tách báo cáo nhiều section và bảng kết quả fix theo đúng instance/section, giữ header bảng, nguồn và giới hạn chung trong tổng quan. Không chỉ nối toàn bộ báo cáo nhiều section vào một file section bất kỳ. Giữ đủ từng tiêu chí và kết quả các vòng, không làm mất trạng thái chưa giải quyết hoặc quyết định của người dùng.

Cập nhật mục lục và mọi liên kết tới file chuyển/gộp, tính lại đường dẫn tương đối khi đổi thư mục; chỉ bỏ file cũ thuộc phạm vi đã được gộp sau khi kiểm đủ nội dung. Kiểm đếm hàng/tiêu chí quan trọng, kết quả hiện hành, liên kết nội bộ và `git diff --check` trước bàn giao. Gộp Markdown không phải lượt visual QA mới và không tự thay đổi trạng thái trên Sheet.

Việc tổ chức hồ sơ không mặc nhiên yêu cầu commit hoặc giữ vĩnh viễn evidence. Khi hoàn tất/commit, áp dụng [quy tắc output/test](../../../../references/task-artifacts.md) (bản cài phẳng: `references/task-artifacts.md` của skill đang dùng); báo cáo kiểm tra tạm được loại khỏi commit và dọn delta của task, còn hồ sơ được yêu cầu lưu/checkpoint bắt buộc được giữ.
