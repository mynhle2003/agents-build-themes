# Video Figma → Shopify Files → preset/template

Đọc khi yêu cầu có video từ thiết kế và upload hoặc gắn video vào composition theme. Yêu cầu chỉ thêm/cập nhật skill không cho phép thực hiện upload. Khi người dùng đã yêu cầu upload video vào preset trong store/theme xác định, tiếp tục trong phạm vi đó; không hỏi lại chỉ vì đây là file video.

## Xác định nguồn và đích

- Ghi file/node Figma, video layer và thứ tự slide; phân biệt video thật với ảnh cover, nút Play vẽ trong thiết kế hoặc prototype animation. Screenshot và image export chỉ chứng minh hình ảnh, không phải file video.
- Dùng Figma connector hoặc UI được hỗ trợ để lấy tài nguyên video nếu có. Không giả định image export API xuất được MP4; không suy URL video từ imageRef/node ID. Nếu chỉ thấy poster mà không có file/source tải được, hỏi file gốc hoặc link video của đúng layer; giữ poster và báo slide nào thiếu video. Không tạo clip thay thế hoặc quay prototype thành video khi chưa được yêu cầu.
- Chỉ tải source đã xác định thuộc layer được yêu cầu. Không đọc cookie, token hoặc trạng thái nội bộ để tìm đường tải khác. Với manifest HLS thay vì file gốc, xác minh đó là cùng clip và dùng công cụ hỗ trợ để tải/remux khi được phép; không coi một segment riêng là toàn bộ video.
- Xác định store upload riêng với store/theme tham khảo. URL editor của theme mẫu không tự trở thành đích upload. Đọc branch hiện tại và đường dẫn section/preset/template; giữ nguyên block ID, thứ tự và tài nguyên khác.

## Kiểm tra và upload

1. Kiểm tra file thật bằng media probe/decoder: MIME, container/codec, kích thước, thời lượng và audio; xem các khung hình đầu/giữa/cuối để nhận đúng clip, không mất frame hoặc bị cắt. Giữ bản nguồn; không chuyển video sang AVIF. Chỉ transcode khi source không tương thích hoặc yêu cầu tối ưu, giữ tỷ lệ, nội dung, thời lượng và audio.
2. Đặt tên theo theme/nội dung/slide. Lưu source file/node, checksum và tên đích trong ledger dưới thư mục ignored của repo. Tra cứu video trong Shopify Files và ledger trước upload để tái sử dụng file READY phù hợp; cùng video dùng nhiều slide chỉ upload một lần.
3. Ưu tiên công cụ upload video chuyên biệt nếu hiện có. Nếu dùng GraphQL, kiểm tra schema/API version và quyền Files trước mutation. Luồng staging: `stagedUploadsCreate` với `resource: VIDEO`, MIME và byte size thật → gửi binary cùng các parameters trả về đến staged target → `fileCreate` với `contentType: VIDEO` và `originalSource` là `resourceUrl`. Không dùng endpoint chỉ hỗ trợ image; không dùng URL staging làm media lâu dài.
4. Đọc lại Video bằng ID. Chờ có giới hạn cho `fileStatus/status: READY`, kiểm tra `sources`, MIME, dimensions, preview image và media/file errors. Nếu FAILED, dừng file đó và báo lỗi; nếu quá thời gian chờ, lưu ID ở trạng thái pending để đọc tiếp, không tạo bản trùng. Nếu timeout sau mutation, đọc lại Files/ledger trước retry.
5. Ghi store, Video ID, filename, trạng thái, CDN source, duration/dimensions và đường dẫn block đích. Không ghi credential hoặc signed upload URL/parameters vào hồ sơ commit.

Tham chiếu hiện hành: [stagedUploadsCreate](https://shopify.dev/docs/api/admin-graphql/latest/mutations/stagedUploadsCreate), [fileCreate](https://shopify.dev/docs/api/admin-graphql/latest/mutations/fileCreate), [Video](https://shopify.dev/docs/api/admin-graphql/latest/objects/Video). Tra lại khi API/tool khác; không áp giới hạn file hoặc field đã cũ.

## Gắn vào preset và instance

- Đọc schema block trước khi ghi settings. Video Shopify Files dùng setting `type: video`; `video_url` dành cho YouTube/Vimeo. Không nhét MP4 CDN URL vào `video_url`, dùng ảnh preview thay video hoặc ghi GID trực tiếp vào setting khi chưa xác minh dạng tham chiếu.
- Lấy giá trị resource đã được Theme Editor lưu hoặc readback theme xác nhận. Tham chiếu thường có dạng `shopify://files/videos/<filename>`, nhưng phải xác minh filename/reference thật trong store; không đoán từ URL CDN hoặc SHA. Giữ Video ID trong ledger để đối chiếu.
- Ghi resource vào **settings của block Video** trong section schema `presets[].blocks` và instance JSON template được yêu cầu. Không thêm `default` vào định nghĩa setting `type: video`: [Shopify video settings](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings#video) không hỗ trợ thuộc tính này. Schema preset và instance đã lưu là hai cấu hình riêng, sửa một phía không cập nhật phía kia.
- Nếu yêu cầu chỉ cập nhật preset, chỉ sửa preset. Nếu yêu cầu cả homepage, cập nhật đúng instance và giữ vị trí section theo Figma. Không thay composition đang custom hoặc preset khác ngoài phạm vi.
- Với Video product carousel (custom), dùng cây **Header → Carousel → Slide → [Video, Product card: Compact]**. Video và Compact là hai block ngang hàng trong Slide, thứ tự Video trước. Không tạo block gộp `Video + Product: Compact`; product picker thuộc Compact, nguồn/poster/playback thuộc Video, gap thuộc Slide và navigation/columns thuộc Carousel.
- Trong repo hiện tại, block Video dùng `video_source: uploaded`, `video: <resource đã xác minh>`, `cover_image`, `autoplay` và `loop_video`. Giữ lựa chọn autoplay/loop hiện có nếu brief không đổi; ảnh cover không được upload lại khi đã tồn tại. Video vắng nguồn thì giữ cover fallback nếu schema hỗ trợ; không hiển thị điều khiển Play giả.
- Shopify Files upload không đồng nghĩa deploy theme. Chỉ push draft theme khi người dùng yêu cầu hoặc đã có quyền push trong phiên; không publish theme khi chỉ yêu cầu media/preset. Theme Check và customization record vẫn áp dụng theo AGENTS.md.

## Kiểm tra kết quả

- Validate schema và JSON/JSONC, Theme Check, cấu trúc block và đúng resource ở cả preset/instance trong phạm vi. Kiểm tra không có video source tạm từ Figma/staging được lưu vào theme.
- Với theme đã được đẩy theo yêu cầu, readback Video picker và preview desktop/mobile: poster → Play/Pause, crop/ratio, loop/autoplay theo setting, keyboard/focus, âm thanh và reduced motion. Add/duplicate/reorder/save/reload phải giữ media đúng slide. Không báo playback đã xác minh nếu chỉ kiểm tra JSON hoặc poster.
- Bàn giao số video upload/tái sử dụng, clip/node và Video ID tương ứng, preset/template đã sửa, trạng thái READY/pending/thiếu nguồn, kết quả validation và tình trạng deploy.
