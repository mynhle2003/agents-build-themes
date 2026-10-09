# Ảnh AVIF


- Tải ảnh gốc, chuyển thật sang **AVIF**, kiểm tra file bằng decoder hỗ trợ AVIF. Không chỉ đổi đuôi PNG/JPG thành `.avif`.
- Tên file mô tả theme/nội dung, alt text phù hợp. Upload bằng công cụ Shopify rồi dùng URL CDN lâu dài; không dùng URL Figma tạm thời làm ảnh.
- Với ảnh render variant, kiểm tra màu, kiểu dáng và khung ảnh trước khi chuyển AVIF/upload.
- Kiểm tra ảnh trả về sau khi tạo, gồm định dạng nguồn và Content-Type khi cần. Đuôi `.avif` không chứng minh CDN luôn trả AVIF vì Shopify có thể negotiate định dạng theo client.
- **Giới hạn đã gặp:** Shopify chuyển ảnh bìa article sang JPG khi nhận URL AVIF qua API. Xác minh ở lần chạy hiện tại; nếu xảy ra, giữ bản AVIF gốc trong Files và báo rõ ảnh bìa bị chuyển. Không nói mọi ảnh đã là AVIF, không đổi đuôi URL hoặc thêm ảnh trùng vào body để che giới hạn.
- Nếu bắt buộc hiển thị ảnh bìa AVIF, nêu phần còn thiếu và giải pháp dùng ảnh Files AVIF trong theme; chỉ chỉnh theme khi người dùng yêu cầu công việc giao diện đó.
