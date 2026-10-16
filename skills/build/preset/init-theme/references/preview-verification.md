# Xác minh local và Theme Editor

Đọc khi đã có quyền chạy preview/deploy draft hoặc khi người dùng báo Editor khác local. Trước mutation, dùng quy trình repo/store tương ứng và đúng phạm vi đã được cấp quyền. Không save Theme Editor để ép đồng bộ.

1. Ghi tuple hiện tại: worktree tuyệt đối, branch, store, development theme ID, port, PID và thời điểm start. Đối chiếu ID từ link Editor với ID CLI trả về. Khi mở lại tab, dùng URL của phiên hiện tại, giữ query do CLI cung cấp (ví dụ `hr=<port>`) thay vì tự sửa link cũ; query này chưa chứng minh nguyên nhân lệch.
2. Đọc status và log mới nhất. Nếu status báo dừng nhưng cổng/PID còn sống, có thể phép kiểm tra process/socket bị sandbox chặn: xác minh bằng kiểm tra read-only được phép, xin escalation khi cần; không kết luận process chết hoặc khởi động thêm phiên từ một phép kiểm tra bị từ chối.
3. Kiểm tra sync riêng `config/settings_data.json`, template/group và schema section/block phụ thuộc. CLI in Preview URL/cổng listen chỉ chứng minh server chạy. Tìm lỗi upload mới nhất và evidence retry thành công; lỗi template vì block chưa được remote chấp nhận không được đánh dấu resolved chỉ vì schema local đã đúng.
4. Với lỗi dependency, validate schema/block tree local rồi, nếu có quyền upload, đồng bộ dependency trước composition bằng cơ chế repo/CLI hỗ trợ, đúng development theme ID. Không đổi allow-list hay xóa block hợp lệ chỉ để upload qua. Readback để xác nhận bản remote đã nhận thay đổi; không lặp full push hoặc tạo theme mới để né lỗi.
5. Khi truy cập được UI, so cùng path/template, viewport, locale/market và trạng thái section giữa local và Editor iframe. Xem saved/unsaved draft của Editor ở chế độ đọc; không ghi đè thay đổi chưa lưu của người dùng. Đối chiếu một giá trị vừa sửa và section liên quan để chứng minh đang xem đúng phiên. Reload chỉ là bước sau xác minh sync, không phải chẩn đoán cache mặc định.
6. Nếu browser bị tắt, auth/quyền thiếu hoặc không đọc được remote, tiếp tục kiểm tra file/log độc lập; ghi phần chưa kiểm chứng và yêu cầu đúng khả năng còn thiếu. Không dùng kết quả Theme Check thay screenshot, không tuyên bố local/Editor đã khớp.

Bàn giao: tuple preview, sync thành công/thất bại của file liên quan, kết quả desktop/mobile và giới hạn còn lại. Không ghi token, storefront password hoặc credential vào plan/log commit.
