---
name: store-content-media
description: "Create or update Shopify store products, variants, collections, blogs, articles and content media from a theme brief or Figma; upload verified images/videos and bind requested media settings. Use for store content work, not theme layout implementation or base synchronization."
---

# Setup store và cập nhật catalog/content/media

Xử lý đúng nhóm dữ liệu người dùng yêu cầu. Audit chỉ đọc; yêu cầu tạo/cập nhật/gắn cho phép làm phần đó trên đích đã xác định. Tạo skill hoặc lập kế hoạch không cho phép ghi dữ liệu store.

## Xác định đích và tránh trùng

- Đọc branch hiện tại, `AGENTS.md`, hồ sơ theme và brief. Không tự checkout branch. Xác định template/theme slug, tên hiển thị, store domain, theme ID khi cần gắn editor, currency và inventory location trước mutation liên quan.
- Không có store mặc định dùng chung. Profile Essen của repo nguồn nằm trong [profile minh họa](references/essen-profile.md); chỉ dùng khi repo đích hoặc người dùng xác nhận.
- Dữ liệu Shopify thuộc store, không được branch cô lập. Audit ID/handle/title và manifest trước tạo; sản phẩm xuất hiện nhiều section chỉ tạo một lần. Không sửa tài nguyên theme khác.
- Khi đã được yêu cầu setup/bổ sung catalog để khớp Figma mà không có collection tương ứng, được phép tạo collection riêng theo template trên store đích đã xác định, theo [Collections](references/collections.md); không hỏi lại chỉ vì thiếu collection. Yêu cầu audit đơn thuần vẫn chỉ đọc.
- Đọc đúng Figma/node và screenshot với skill Figma bắt buộc của công cụ tương ứng. Không suy số product từ pagination hoặc biến ảnh trang trí thành product.
- Timeout sau mutation: đọc lại kết quả trước retry để tránh trùng. Nếu thiếu đích, quyền connector hoặc dữ liệu bắt buộc, hỏi phần thiếu và tiếp tục phần độc lập.

## Chọn reference theo tác vụ

- Product, variant, stock, swatch, summary, ảnh gallery: [Products](references/products.md).
- Collection, ảnh và membership: [Collections](references/collections.md).
- Blog riêng theo template, bài viết và publication: [Blogs](references/blogs.md).
- Chuyển/upload ảnh AVIF và giới hạn CDN: [Images](references/images-avif.md).
- SVG icon giao diện không phải media cần upload; xử lý bằng snippet theo [quy tắc icon của build-theme](../../build/new/build-theme/references/foundation.md#icon-figma-và-svg), không thêm SVG icon vào theme `assets/`.
- Video Figma, Shopify Files và gắn preset/instance: [Video](references/figma-video-to-preset.md).

Mặc định catalog hiện tại: ít nhất 4 ảnh mỗi product, 20 đơn vị mỗi variant demo còn hàng tại location đã xác nhận, blog riêng mang tên template. Giá gốc/khuyến mãi cần nguồn; không bịa giá thiếu. Stock/demo default không áp vào stock đang vận hành. Quy tắc mới lấy từ `docs/content-creation-workflow.md` local ngày 07/10/2026, thay mốc 100 và blog dùng hậu tố của skill cũ.

## Thực hiện và readback

Lập manifest nguồn/đích và tài nguyên có sẵn/cần tạo/thiếu. Chuẩn bị content/media, upload và chờ processing có giới hạn; dùng ID trả về cho quan hệ phụ thuộc. Ưu tiên connector Shopify; kiểm tra schema/API version hiện tại nếu dùng GraphQL.

Đọc lại publication, giá/compare-at, options/swatch, variant media, stock, summary, membership và article → blog. Khi được yêu cầu gắn editor, đọc lại cấu hình sau reload và kiểm tra preview desktop/mobile. Báo riêng phần chưa tạo, chưa gắn, pending hoặc chưa kiểm tra.

Lưu receipt/audit theo repo đích: nguồn, store, ID, handle, URL lâu dài và kết quả xác minh; không lưu credential hoặc signed staging URL. Upload content không đồng nghĩa push/publish theme. Sửa media settings/preset/template chỉ khi được yêu cầu, giữ composition khác và chạy validation theo AGENTS.md.
