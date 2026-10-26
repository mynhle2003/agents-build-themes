# Check perfect — Homepage {{theme_name}}

Ngày khởi tạo: {{date}}. Phạm vi: homepage. Trạng thái QA: chưa kiểm. Skill tiếp tục: `$qa-theme-pixel-perfect`.

## Định dạng báo cáo Google Sheet

STT | Section | Thiết bị | Thành phần | Tiêu chí | Figma | Hiện tại | Hướng xử lý | Lần fix | Trạng thái

Header hai tầng: Nội dung gộp ngang trên Figma và Hiện tại; các header còn lại gộp dọc.

{{sheet_style_snapshot}}

Các section nối liền nhau sau STT 0 — Tổng quan. Chung (Desktop, Mobile) trước Desktop rồi Mobile. Gộp STT/Section theo instance, Thiết bị theo breakpoint, Thành phần theo tiêu chí; không gộp nội dung/trạng thái/hướng xử lý. Wrap, mọi ô middle, header center/middle. Trạng thái và Lần fix là dropdown chip có màu; nền ô thường trắng. Mỗi thuộc tính một hàng so sánh, không list nhiều mục trong một ô. Thuộc tính khác đã xác minh: Figma highlight xanh, Hiện tại đỏ; trùng nhau không highlight. Hướng xử lý sát sau Nội dung, tương ứng thuộc tính cùng hàng; kế tiếp Lần fix rồi Trạng thái. Lần fix dùng Lần 1–Lần 5/Bỏ qua; QA đầu đã có hướng xử lý preset hoặc config/settings_data.json được xác minh thì tự gắn Lần 1, vẫn Chưa khớp đến khi fix + QA đạt. Ưu tiên preset/settings, chỉ custom khi đã xác minh preset không đáp ứng. Nguồn và phạm vi nằm cuối bảng. Markdown giữ chi tiết và đồng bộ với Sheet sau mỗi bước.

Ưu tiên API Google Sheets cho đọc/ghi/định dạng/merge/dropdown; Computer Use dùng kiểm tra giao diện hoặc phần API không hỗ trợ khi đã được phép. Áp mẫu style hiện hành ngay bước0 trên tab mới/trống đã được giao; giữ dữ liệu live của tab hiện có. Mẫu và workflow lấy từ qa-theme-pixel-perfect/assets/sheet-style.json và references/sheet-api-workflow.md; ghi version trong snapshot trên.

## Hồ sơ QA theo section

Tổng quan này giữ nguồn, manifest/order, điều kiện đo, style Sheet và checkpoint chung. Khi bắt đầu kiểm mỗi section, tạo hoặc cập nhật `docs/qa/homepage-<section>.md`, thêm link vào mục lục ở đây. Mỗi section một file ổn định; kết quả mới nhất ở đầu, mọi lượt QA/recheck/Fix lần N có ngày và bằng chứng nằm trong lịch sử cùng file. Không tạo file báo cáo mới theo ngày/vòng. Theo contract `qa-section/references/qa-report-files.md`; chưa kiểm thì không tạo kết quả giả.

## Kết quả QA

Chưa chạy QA. Khi bắt đầu, lập STT 0 — Tổng quan gồm Số lượng section, Thứ tự section, Width / Padding. Không đánh dấu Khớp từ kết quả build hoặc vì đã có link Figma.

## Checkpoint

{{init_checkpoint}}

### Rút gọn kết quả đã khớp trong section

Chỉ áp dụng cho section chi tiết, không áp dụng STT 0 Tổng quan page/theme: Tổng quan vẫn giữ từng dòng Số lượng section, Thứ tự section, Width / Padding như hiện tại. Trong mỗi section/breakpoint, gom các thành phần đã khớp hoàn toàn vào một dòng **Đã kiểm và khớp**, chỉ nêu tên, không lặp thông số. Ví dụ Heading đạt toàn bộ thì ghi Heading trong dòng này, không tạo các dòng Content/Typo/Màu riêng. Với thành phần có sai lệch, ví dụ Button chỉ sai màu, chỉ tách hàng Button · Màu với Figma/Hiện tại và hướng xử lý tương ứng; không liệt kê lại các thuộc tính Button đã khớp. Các thuộc tính còn lại đã kiểm có thể được xác nhận gọn trong dòng tổng hợp, không làm mất mục chưa xác minh. Mỗi sai lệch hoặc mục chưa xác minh là một hàng riêng; checklist và số đo đầy đủ giữ trong Markdown. Dòng xác nhận khớp có thể gộp ngang Figma/Hiện tại, không highlight so sánh.

## Phạm vi và nguồn

- Theme/worktree: {{theme_target}}
- Phạm vi: chỉ homepage.
- Figma Desktop: {{figma_desktop}}
- Figma Mobile: {{figma_mobile}}
- Style Guide: {{style_guide_or_inherited_source}}
- Preview: {{preview_or_not_provided}}
- Sheet QA/tab/gid: {{sheet_or_not_provided}}
