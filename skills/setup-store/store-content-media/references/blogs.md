# 4. Blog post


### Blog riêng cho từng template

- Mỗi template có một blog riêng để chứa các bài viết mới của template đó. Blog mang tên template và dùng handle `<template-slug>`; ví dụ làm template Perky thì dùng blog **Perky**, handle `perky`, rồi tạo mọi bài viết mới của Perky trong blog này.
- Kiểm tra blog theo tên, handle và ID trước khi tạo. Nếu đã có blog đúng template thì dùng lại; nếu chưa có thì tạo blog trước, lấy ID trả về rồi dùng ID đó khi tạo bài viết. Không tạo blog riêng cho từng bài hoặc tạo trùng blog mỗi lần chạy.
- Không gắn bài mới vào `News` hoặc blog của template khác chỉ vì section hiện đang chọn blog đó. Nếu người dùng chỉ định rõ một blog đích khác, ưu tiên chỉ định đó.
- Khi được yêu cầu gắn nội dung vào Theme Editor, chọn blog riêng của template trong picker của section và gắn article thuộc blog đó. Kiểm tra trang blog, link bài viết và nút View all đều dẫn đúng blog.
- Đọc lại quan hệ article → blog sau khi tạo; lưu blog ID/title/handle cùng article ID/handle vào manifest và receipt/audit. Không tự chuyển bài viết có sẵn ngoài phạm vi yêu cầu.

### Nội dung và hiển thị bài viết

- Kiểm tra bài viết đã có trong blog đích trước khi tạo để tránh trùng lặp.
- Mỗi bài có title, handle, nội dung đầy đủ, excerpt, ảnh đại diện và alt. Nội dung đúng chủ đề template, dùng cùng ngôn ngữ với thiết kế.
- Title giữ nội dung tiêu đề trong thiết kế; không tự thêm hậu tố template. Với bài mới cần phân biệt trong shop dùng chung, dùng handle `<template-slug>-<article-slug>`.
- Nội dung có phần mở đầu, các đoạn/đề mục dễ đọc và kết thúc phù hợp; excerpt là tóm tắt ngắn cho blog card, không để HTML lỗi hoặc placeholder.
- Dùng ảnh đúng thiết kế. Nếu cần ảnh demo, tạo ảnh phù hợp chủ đề, đúng tỷ lệ khung card; upload vào Shopify và gắn vào article, không đưa vào theme `assets`.
- Tác giả và ngày đăng lấy từ nguồn/yêu cầu; không giả danh tác giả hoặc tổ chức. Nếu thiếu tác giả, dùng tác giả mặc định đã xác nhận của blog/store; nếu chưa xác nhận thì ghi thiếu.
- Gắn tag phù hợp nếu có yêu cầu. Bổ sung SEO title/meta description phù hợp nội dung, không nhồi từ khóa.
- Đặt trạng thái đăng bài theo yêu cầu. Bài cần xuất hiện ngay trên homepage demo phải khả dụng ở thời điểm kiểm tra; không dùng ngày đăng tương lai khiến card trống.
- Gắn blog/article vào đúng picker mà section hỗ trợ. Nếu section lấy bài theo thứ tự blog, kiểm tra thứ tự/ngày đăng để bài featured và bài phụ hiển thị đúng; không sửa dữ liệu bài cũ ngoài phạm vi để ép thứ tự.
- Kiểm tra ảnh, title, excerpt, tác giả/ngày nếu bật, link card, trang bài viết và nút View all với dữ liệu thật.
