---
name: store-content-media
description: "Create or update Shopify store products, variants, collections, blogs, articles and content media from a theme brief or Figma; upload verified images/videos and bind requested resources in local preset/template files. Use for store content work, not theme layout implementation or base synchronization."
---

# Setup store và cập nhật catalog/content/media

Xử lý đúng nhóm dữ liệu người dùng yêu cầu. Audit chỉ đọc; yêu cầu tạo/cập nhật/gắn cho phép làm phần đó trên đích đã xác định. Tạo skill hoặc lập kế hoạch không cho phép ghi dữ liệu store.

## Truy cập Figma

Khi cần dữ liệu Figma, bắt buộc áp dụng [Figma MCP và cấp quyền tài khoản](../../build/preset/theme-style-guide/references/figma-access.md) trước khi đọc thiết kế/asset. Với bản cài phẳng, đọc `.agents/skills/theme-style-guide/references/figma-access.md`; thiếu dependency thì báo thiếu, không tự chọn cách truy cập khác.

## Ranh giới store content và preset local

- Preset/composition chỉ được chỉnh trong file repo: `presets` của section schema, `templates/*.json` hoặc section-group JSON đúng phạm vi. Không tạo luồng chỉnh/lưu preset hay template trực tiếp trên store bằng Shopify bot, connector/API hoặc thao tác Theme Editor nếu chưa có cho phép rõ ràng của người dùng dành riêng cho thao tác đó.
- Quyền tạo/cập nhật content, upload media, build preset hoặc “gắn vào preset” không phải quyền sửa cấu hình theme trên store. Dùng Shopify tools cho content/media đã được yêu cầu; sau đó ghi tham chiếu vào file preset/template local. Không save Theme Editor để lấy reference, không mutation theme/settings/template qua bot, không tự pull/đồng bộ cấu hình từ store để thay thế file local.
- Ảnh/video: tái sử dụng hoặc upload vào Shopify Files/content của store đích, chờ xử lý và đọc lại URL CDN lâu dài hoặc resource reference. Gắn giá trị đúng kiểu setting vào preset/template local: URL cho trường URL, Shopify file reference đã xác minh cho image/video picker. Không dùng URL Figma/staging, không ép URL CDN vào picker không hỗ trợ.
- Product/collection/blog/article: tạo hoặc cập nhật content chỉ trong phạm vi đã yêu cầu, đọc lại handle; gắn handle/resource reference đúng định dạng setting vào preset/template local, không ghi GID thay handle. URL điều hướng dùng link thật theo schema. Không chọn resource rồi lưu cấu hình bằng picker trên store.
- Push file theme local là bước deploy riêng, chỉ thực hiện khi người dùng đã cho phép; quyền push không cho phép sửa preset trực tiếp bằng bot/API hoặc Theme Editor. Kiểm tra preview/readback có thể chỉ đọc và không được save thay đổi cấu hình. Báo riêng content/media đã upload, file local đã sửa và trạng thái deploy.

## Xác định đích và tránh trùng

- Đọc branch hiện tại, `AGENTS.md`, hồ sơ theme và brief. Không tự checkout branch. Xác định template/theme slug, tên hiển thị, store domain, theme ID khi cần preview/deploy được cho phép, currency và inventory location trước mutation liên quan.
- Không có store mặc định dùng chung. Profile Essen của repo nguồn nằm trong [profile minh họa](references/essen-profile.md); chỉ dùng khi repo đích hoặc người dùng xác nhận.
- Dữ liệu Shopify thuộc store, không được branch cô lập. Audit ID/handle/title và manifest trước tạo; sản phẩm xuất hiện nhiều section chỉ tạo một lần. Không sửa tài nguyên theme khác.
- Khi đã được yêu cầu setup/bổ sung catalog để khớp Figma mà không có collection tương ứng, được phép tạo collection riêng theo template trên store đích đã xác định, theo [Collections](references/collections.md); không hỏi lại chỉ vì thiếu collection. Yêu cầu audit đơn thuần vẫn chỉ đọc.
- Đọc đúng Figma/node và screenshot với skill Figma bắt buộc của công cụ tương ứng. Không suy số product từ pagination hoặc biến ảnh trang trí thành product.
- Timeout sau mutation: đọc lại kết quả trước retry để tránh trùng. Nếu thiếu đích, quyền connector hoặc dữ liệu bắt buộc, hỏi phần thiếu và tiếp tục phần độc lập.

## Chọn reference theo tác vụ

- Product, variant, stock, swatch, summary, ảnh gallery: [Products](references/products.md).
- Tag sản phẩm phải khớp đúng Figma theo [Products — Tên và phân loại](references/products.md#tên-và-phân-loại); không tự gắn tag mặc định hoặc tag nội bộ khi tạo sản phẩm.
- Collection, ảnh và membership: [Collections](references/collections.md). Nếu Figma có View all, áp dụng mục “View all trong thiết kế” để chuẩn bị dữ liệu đủ điều kiện render gốc của theme, không nới điều kiện để bù catalog thiếu. Khi setup theo Figma có hiển thị số product của collection, phải bổ sung sản phẩm phù hợp và xác minh số đếm thực tế khớp thiết kế; không chỉ upload ảnh rồi để collection trống.
- Blog riêng theo template, bài viết và publication: [Blogs](references/blogs.md).
- Chuyển/upload ảnh AVIF và giới hạn CDN: [Images](references/images-avif.md).
- Section/block có hotspot: đọc [Hotspot: tọa độ, crop và focal point store](../../build/preset/build-preset/references/hotspots.md). Khi setup media trong phạm vi được yêu cầu, lưu focal point ảnh mặc định 50% 50% tại Shopify Files/media (trừ chỉ định khác), reload/readback và đối chiếu web desktop/mobile; tọa độ hotspot thuộc preset/template local. Khi cài skill phẳng, đọc `.agents/skills/build-preset/references/hotspots.md`.
- SVG icon giao diện không phải media cần upload; xử lý bằng snippet theo [quy tắc icon của build-theme](../../build/new/build-theme/references/foundation.md#icon-figma-và-svg), không thêm SVG icon vào theme `assets/`.
- Social có trong Figma nhưng thiếu URL: áp dụng quy tắc [`Social trong preset và icon riêng của theme`](../../build/preset/build-preset/SKILL.md#social-trong-preset-và-icon-riêng-của-theme): dùng `#` trong cấu hình local, giữ URL thật đã có; icon social Figma là custom của theme và phải ghi custom record, không upload như media.
- Video Figma, Shopify Files và gắn preset/instance local: [Video](references/figma-video-to-preset.md).

Mặc định catalog hiện tại: ít nhất 4 ảnh mỗi product, 20 đơn vị mỗi variant demo còn hàng tại location đã xác nhận, blog riêng mang tên template. Giá gốc/khuyến mãi cần nguồn; không bịa giá thiếu. Stock/demo default không áp vào stock đang vận hành. Quy tắc mới lấy từ `docs/content-creation-workflow.md` local ngày 07/10/2026, thay mốc 100 và blog dùng hậu tố của skill cũ.

## Thực hiện và readback

Lập manifest nguồn/đích và tài nguyên có sẵn/cần tạo/thiếu. Chuẩn bị content/media, upload và chờ processing có giới hạn; dùng ID trả về cho quan hệ phụ thuộc. Ưu tiên connector Shopify; kiểm tra schema/API version hiện tại nếu dùng GraphQL.

Đọc lại publication, giá/compare-at, options/swatch, variant media, stock, summary, membership và article → blog. Khi được yêu cầu gắn vào preset/template, đọc lại file local; chỉ kiểm tra cấu hình theme đã deploy và preview desktop/mobile ở chế độ đọc khi có đích phù hợp. Báo riêng phần chưa tạo, chưa gắn, pending hoặc chưa kiểm tra.

Lưu receipt/audit theo repo đích: nguồn, store, ID, handle, URL lâu dài và kết quả xác minh; không lưu credential hoặc signed staging URL. Upload content không đồng nghĩa push/publish theme. Sửa media settings/preset/template trong file local chỉ khi được yêu cầu, theo ranh giới trên; giữ composition khác và chạy validation theo AGENTS.md.
