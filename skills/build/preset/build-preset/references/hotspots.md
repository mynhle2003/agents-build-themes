# Hotspot trong section hoặc block

Áp dụng cho mọi section/block có hotspot, kể cả hotspot nằm trong block lồng nhau. Phân biệt hai nhóm setting: tọa độ hotspot thuộc preset/template local; focal point thuộc ảnh trong Shopify Files/media của store.

## Ảnh và focal point tại store

- Với media của section/block hotspot đang được setup, dùng focal point **50% 50%** làm mặc định, trừ khi người dùng chỉ định vị trí khác. Lưu tại Shopify Files/media, không thêm `object-position`, CSS, Liquid hoặc setting giả trong code để thay cho focal point store.
- Build preset đơn thuần hoặc audit chỉ cho phép đọc media. Chỉ lưu focal point khi yêu cầu đã bao gồm setup/cập nhật media của ảnh đó trên store đích xác định. Không tự chỉnh ảnh dùng chung ngoài phạm vi; nếu ảnh đang được dùng ở nơi khác, kiểm tra ảnh hưởng trước khi thay focal point.
- Xác minh đúng file ID/tên ảnh và reference desktop/mobile. Nếu hai viewport dùng hai ảnh, kiểm tra focal point từng ảnh. Sau khi save, reload/readback focal point đã lưu và kiểm tra `object-position` hiệu lực trên web. Click gần giữa hoặc ảnh nhìn có vẻ cân không đủ để kết luận chính xác 50% 50%.
- Lưu media không phải save preset trong Theme Editor hay deploy theme. Giữ ranh giới quyền của skill gọi workflow này.

## Đo và cấu hình tọa độ

- Đọc đúng frame desktop/mobile và ảnh thực sự hiển thị. Chỉ lấy các chấm nhìn thấy trên thiết kế: kiểm tra hierarchy, lớp che, clipping và screenshot; không lấy một layer Hotspot bị ảnh che chỉ vì nó có tọa độ trong inspector.
- Đo **tâm chấm**, không lấy left/top của hộp hotspot làm tâm. Tính cả padding, border và kích thước khác nhau giữa trạng thái active/default. Quy đổi tọa độ về khung ảnh chứa hotspot, kể cả khi layer Figma đặt dưới parent khác.
- Dùng setting tọa độ desktop/mobile hiện có; bật override mobile khi cần. Tuân thủ min/max/step của schema, làm tròn ở bước cuối và ghi nhận sai số. Không thêm setting, CSS hoặc logic ngoài phạm vi preset để ép khớp.
- So sánh crop Figma với web sau khi focal point được xác minh: source image, aspect ratio, `cover`/`contain`, vùng ảnh thực, offset và scale. Khi crop khác nhau, quy đổi tâm từ Figma về vị trí trên ảnh nguồn rồi chiếu vào vùng ảnh web; không sao chép phần trăm Figma nếu làm chấm trượt khỏi vật thể.
- Với ảnh nguồn `(Iw, Ih)` được render `cover` vào khung `(W, H)`, scale `s = max(W/Iw, H/Ih)`. Nếu ảnh ở giữa 50% 50%, offset là `((W - s*Iw)/2, (H - s*Ih)/2)`. Tâm trên ảnh nguồn `(u, v)` chiếu thành `(s*u + offsetX, s*v + offsetY)`; chia cho `(W, H)` để ra phần trăm setting. Phép quy đổi từ Figma về ảnh nguồn dùng chính scale/offset đo trong Figma, không dùng hằng số bù crop từ một section cũ.
- Chọn aspect ratio bằng control sẵn có theo thiết kế/brief. Không mặc định đổi mọi ảnh thành vuông. Nếu `fill_height` khiến khung thay đổi theo nội dung hoặc viewport, đo các kích thước liên quan; báo giới hạn khi tọa độ phần trăm cố định không giữ được điểm neo bằng control hiện có.
- Khi cần chỉnh cả preset mặc định và instance template được yêu cầu, giữ tọa độ/resource nhất quán giữa hai nơi, bảo toàn composition khác. Nếu thiếu media hoặc reference, ghi phần chưa xác minh thay vì khẳng định chấm đã đúng trên ảnh.

## Kiểm tra và bằng chứng

- Soi web desktop/mobile tại kích thước frame: ảnh tải đúng, focal point đúng, tâm từng chấm nằm trên đúng vật thể và không bị che/cắt. Đo vùng ảnh thực tế; tính cả phần chiều rộng bị scrollbar chiếm.
- Bấm từng hotspot để kiểm tra product/card/link tương ứng, nhất là sau khi bỏ layer ẩn hoặc đổi thứ tự. Không suy quan hệ product từ vị trí ảnh trang trí.
- Audit ghi node nguồn, file/reference ảnh, focal point readback, tọa độ trước/sau, cách bù crop, ảnh chụp desktop/mobile và các giới hạn. Báo riêng media store đã lưu, preset/template local đã sửa và trạng thái preview/deploy; không gọi “đúng Figma” khi chưa soi web hoặc còn sai số/gap đáng kể.
