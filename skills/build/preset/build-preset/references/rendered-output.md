# Kiểm đầu ra với Figma

Áp dụng sau cấu hình preset/instance và trước bàn giao. Đối chiếu đúng section, template/resource và hai node desktop/mobile được yêu cầu. Theme Check, JSON hợp lệ, asset đúng tên hoặc cấu hình đúng tỷ lệ chỉ chứng minh từng phần; không thay thế kiểm bản render thực tế.

## So từng vùng và từng item

- Chờ font, ảnh và entrance animation ổn định; reload sau thay đổi breakpoint nếu runtime giữ kích thước cũ. Kiểm ở viewport Figma và ghi kích thước vùng nội dung thực tế nếu scrollbar làm khác nguồn.
- So tổng thể: đủ thành phần, thứ tự, header/content/media, số cột/item, căn lề, chiều rộng, padding/gap. Tiếp theo so copy, typography, line wrapping, màu, icon, border/radius và overflow. Kiểm các item trong phạm vi thiết kế; không dùng card đầu đại diện tất cả ảnh.
- Với mỗi ảnh/video, xác minh nguồn/resource và đúng slot, kích thước khung/tỷ lệ, fit/fill, crop/zoom, object-position/focal point, thứ tự và vị trí so với nội dung. So chủ thể nhìn thấy bằng mốc rõ như đầu/mũ, vai, tay, mép cầu thang; không kết luận khớp chỉ vì dùng cùng ảnh gốc hoặc cùng tỷ lệ3:2. Desktop và mobile có thể dùng cùng ảnh nhưng transform/crop khác nhau.
- Đối chiếu ảnh nguồn Figma với ảnh thực sự render (src/currentSrc và kích thước tự nhiên khi truy cập được), không chỉ ảnh Files đã upload. Article cover, product media hoặc CDN rendition có thể khác Files gốc. Đọc setting → renderer → CSS hiệu lực để phân biệt sai nguồn, sai khung và sai crop; không tự đoán focal point từ thumbnail.
- Kiểm button/navigation/pagination hiện thật, đúng vị trí và trạng thái sau initialization/chuyển item. Đọc điều kiện dữ liệu: ví dụ blog4 bài khả dụng với Max posts3 thỏa articles_count > max_posts, nhưng vẫn phải xác minh nút thực sự xuất hiện. Không thêm nội dung hoặc sửa điều kiện chỉ để tạo nút nếu chưa có quyền cho phần đó.

## Sửa và xác minh lại

Ưu tiên control hiện có, đồng bộ preset Add section và instance local rồi kiểm lại phần bị ảnh hưởng ở cả desktop/mobile. Nếu cần chỉnh resource/focal point trên store, chỉ làm trong phạm vi media được yêu cầu và có đích xác định. Không thêm CSS, setting hoặc sửa implementation ngoài quyền của build-preset để bù crop/layout. Khi thiếu control hoặc transform không biểu đạt được, ghi rõ kỳ vọng Figma, giao diện hiện tại và control/behavior còn thiếu.

## Bằng chứng bàn giao

Lưu screenshot Figma và preview ở viewport đối chiếu khi công cụ hỗ trợ, kèm mapping slot/card và các số đo cần giải thích sai lệch. Mỗi tiêu chí có một trạng thái: đã xác minh khớp, sai lệch đã xác minh, hoặc chưa xác minh (ghi lý do). Screenshot chỉ xuất hiện trong tool output không phải tệp bằng chứng đã lưu. Chỉ kết luận khớp/hoàn tất kiểm hình ảnh khi mọi tiêu chí áp dụng đã kiểm và các sai lệch đã được sửa hoặc người dùng chấp nhận. Browser/công cụ bị tắt thì tiếp tục kiểm local độc lập, ghi phần còn thiếu; không thay bằng một browser/API khác để vượt hạn chế.
