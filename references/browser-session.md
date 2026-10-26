# Vòng đời tab và group Google Chrome của task

Áp dụng khi skill dùng Google Chrome cho task: Figma, preview, Theme Editor, Sheet hoặc trang tham khảo. Không tự mở Chrome nếu task không cần. Dùng công cụ được hỗ trợ và giữ nguyên ranh giới quyền truy cập của workflow.

## Nhận diện và ghi nhớ

- Trước khi tạo tab/group, đọc checkpoint của task và inventory Chrome. Tái sử dụng tab đúng profile, URL/file/node và mục đích đã ghi; group thu gọn vẫn có thể chứa tab cần dùng. Không tạo tab/group mới cho mỗi bước, section, viewport, lần retry hoặc lần khôi phục ngữ cảnh.
- Phân biệt tab/group có sẵn của người dùng với tab/group do task tạo. Không tự gom, di chuyển hay đóng tab có sẵn. Nếu cần group riêng để tổ chức nhiều tab mới, đặt tên ngắn có dấu nhận diện task; không tạo nhiều group cùng mục đích.
- Ngay sau mỗi lần tạo, đóng hoặc thay đổi tab/group, cập nhật một checkpoint local bền vững của đúng task. Dùng hồ sơ tiến trình hiện có; nếu chưa có, dùng một file riêng theo task trong thư mục trạng thái local được repo cho phép, ngoài Git (có thể dùng thư mục tạm được phép). Ghi đường dẫn tuyệt đối vào handoff/tóm tắt tiếp tục để phiên sau tìm lại được; không chỉ giữ ID trong biến REPL hay trí nhớ hội thoại.
- Checkpoint ghi: task/theme/worktree, browser và profile đã xác minh, window/tab/group ID mà công cụ cung cấp, tên group, URL/file key/node cần thiết để nhận diện, mục đích từng tab, ai tạo (`task-created` hoặc `pre-existing`), trạng thái mở/đã đóng, bước đang làm, việc tiếp theo và cleanup còn chờ. Chỉ lưu URL đã loại credential/token/tham số nhạy cảm; không lưu cookie, token hay credential. ID là dữ liệu runtime, không hardcode vào skill. Nếu công cụ không trả ID, ghi dấu nhận diện UI thực sự quan sát được, không bịa ID.

## Tiếp tục sau hết token, compact hoặc reconnect

- Đọc checkpoint và trạng thái tiến trình trước thao tác trình duyệt. Dùng inventory hiện tại để xác minh lại profile, tab/group, URL và nội dung; ID có thể đổi sau reconnect/restart, không dùng ID cũ một cách mù quáng.
- Chọn/claim lại tab cũ qua API được hỗ trợ và tiếp tục đúng bước đang dở. Binding REPL mất không có nghĩa tab đã đóng. Nếu ID không còn hợp lệ, tìm theo profile, URL/file/node và group trước khi mở mới; cập nhật ID vừa xác minh vào checkpoint.
- Chỉ mở tab thay thế sau khi xác nhận tab cũ không còn hoặc không thể dùng cho mục đích cần thiết. Chỉ tạo lại group nếu group cũ không còn và vẫn cần tổ chức tab. Nếu công cụ không cho inventory/chọn lại, ghi blocker và giữ checkpoint; không liên tục tạo bản sao để né lỗi.
- Khi đang tạm dừng, chờ đầu vào hoặc sắp bàn giao ngữ cảnh, lưu bước tiếp theo và giữ tab/group cần để tiếp tục. Hết token/compact không phải task hoàn tất. Cập nhật checkpoint theo từng mốc để vẫn khôi phục được khi bị ngắt bất ngờ.

## Cleanup khi hoàn tất

- Khi task kết thúc, lưu evidence và kết quả cần thiết trước, rồi đóng các tab `task-created` còn mở và gỡ group do task tạo. Không đóng toàn bộ cửa sổ/Chrome để dọn task. Nếu người dùng yêu cầu giữ một tab kết quả, giữ đúng tab đó và ghi ngoại lệ trong checkpoint.
- Chỉ thao tác lên tài nguyên đã đối chiếu với inventory hiện tại và xác minh do task tạo. Nếu người dùng đã thêm tab riêng vào group của task, giữ tab đó và chỉ gỡ group khi làm được mà không đóng tab của người dùng. Tab/group `pre-existing` không thuộc phạm vi cleanup, kể cả khi task đã dùng chúng.
- Kiểm tra lại inventory sau cleanup; cập nhật tab/group đã đóng/gỡ và phần còn lại. Nếu công cụ không hỗ trợ đóng/gỡ hoặc thao tác bị chặn, lưu đúng ID/dấu nhận diện còn chờ và lý do để lần tiếp tục dọn được; báo ngắn gọn, không tuyên bố đã clean khi chưa xác minh.
