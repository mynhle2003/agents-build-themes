# File output/test: loại khỏi commit và dọn sau task

Áp dụng cho mọi skill khi kiểm tra, QA hoặc chạy test tạo/sửa file local, kể cả khi người dùng yêu cầu commit sau đó. Yêu cầu commit code không mặc nhiên bao gồm file phục vụ kiểm tra.

## Trước khi tạo file

- Ghi nhận trạng thái Git ban đầu (tracked, untracked và staged) cùng nội dung/diff cần giữ của các file sắp bị công cụ thay đổi. Ưu tiên lưu output/test tạm ngoài working tree, trong thư mục tạm riêng của task.
- Theo dõi chính xác file do task tạo và phần task sửa trong file có sẵn. Không suy quyền xóa từ tên thư mục `output/`, `test/` hay `docs/qa/`.
- File phục vụ kiểm tra gồm screenshot, video, log, dump, snapshot, báo cáo QA/validation, cache, build output và script/fixture/test tạm do task tạo. Mã theme, cấu hình thực tế, test lâu dài được yêu cầu và tài liệu bàn giao/customization/checkpoint bắt buộc không tự bị xem là file tạm chỉ vì có chữ “test” hoặc “output”. Nếu người dùng yêu cầu lưu hoặc commit một artifact cụ thể thì giữ đúng phần đó.

## Khi được yêu cầu commit

- Kiểm tra diff và staged diff; stage bằng danh sách file/hunk thuộc sản phẩm bàn giao, loại trừ output/test và báo cáo phát sinh chỉ để kiểm tra. Không dùng `git add .` hoặc `git add -A` để gom tất cả thay đổi.
- Nếu task đã stage artifact tạm, chỉ unstage đúng phần task đã stage trước commit; giữ nguyên staging có sẵn của người dùng. Không tự tạo commit nếu chưa được yêu cầu hoặc workflow chưa cấp quyền.
- Tóm tắt kết quả kiểm tra trong chat hoặc nội dung commit phù hợp; không commit file test/kết quả test chỉ để chứng minh đã kiểm. Không tự sửa `.gitignore` để che file phát sinh.

## Dọn dẹp sau khi hoàn tất

- Sau khi kiểm tra xong và commit thành công nếu có yêu cầu commit, xóa đúng file tạm do task tạo; với file có sẵn bị task/công cụ sửa chỉ để kiểm tra, bỏ đúng delta của task và phục hồi nội dung cùng trạng thái staged/unstaged ban đầu. Không restore về `HEAD` nếu file đã có thay đổi trước task.
- Không dùng `git reset --hard`, `git clean -fd` hoặc restore cả thư mục để dọn. Nếu file có thay đổi mới của người dùng hoặc không tách được delta an toàn, giữ file, loại phần tạm khỏi commit và báo rõ phần chưa dọn; không ghi đè/xóa theo suy đoán.
- Trước khi xóa evidence còn được báo cáo/checkpoint tham chiếu, giữ kết luận và số đo cần bàn giao, cập nhật trạng thái evidence đã dọn để không còn liên kết như thể file vẫn tồn tại. Khi task còn bị chặn hoặc chờ tiếp tục, giữ checkpoint/evidence cần resume; dọn khi hoàn tất. Không xóa deliverable hoặc hồ sơ người dùng yêu cầu lưu.
- Kiểm tra lại `git status --short`, diff và staged diff để xác nhận output/test tạm đã hết, thay đổi sản phẩm và thay đổi có sẵn vẫn nguyên vẹn. Bàn giao ngắn kết quả kiểm tra và phần còn giữ/chưa dọn nếu có; không tuyên bố working tree sạch khi vẫn còn thay đổi hợp lệ.
