# 3. Collection

### Tái sử dụng hoặc tạo collection theo Figma

- Khi người dùng yêu cầu setup store/bổ sung catalog để khớp Figma, audit collection hiện có bằng ID, handle, title, ảnh, membership và thứ tự sản phẩm trước khi tạo.
- Nếu không có collection tương ứng với nhóm sản phẩm trong Figma, được phép tạo collection mới trên store đích đã xác định trong phạm vi yêu cầu đó; không cần hỏi lại chỉ vì collection chưa tồn tại. Dùng manual collection khi thiết kế chọn một nhóm sản phẩm cụ thể, gắn ảnh đúng nguồn và sắp thứ tự sản phẩm theo Figma.
- Tái sử dụng collection tương ứng nếu có; không đổi membership/thứ tự của collection dùng chung cho theme khác chỉ để khớp một section. Nếu collection dùng chung không phù hợp và thay đổi sẽ ảnh hưởng theme khác, tạo collection riêng theo template trong phạm vi setup đã được yêu cầu.
- Audit chỉ đọc vẫn không cho phép tạo collection. Thiếu store đích hoặc nguồn sản phẩm/ảnh bắt buộc thì báo phần thiếu, không tự dùng store của profile minh họa. Tạo collection không bao gồm quyền push/publish theme.


### Tên, nội dung và ảnh

- Title có tên template ở cuối: `<Tên collection> <Template>`, ví dụ `Rattles Perky`, `New Arrivals Perky`.
- Collection mới dùng handle `<collection-slug>-<template-slug>`, ví dụ `rattles-perky`.
- Mỗi collection có ảnh đại diện. Ưu tiên ảnh đúng thiết kế; khi render, tham khảo sản phẩm thuộc collection để ảnh phù hợp nội dung.
- Ảnh collection ưu tiên dạng lifestyle, sản phẩm cần thấy rõ ở vùng giữa để crop không mất chủ thể. Theo tỷ lệ thiết kế; khi chưa có tỷ lệ cụ thể, dùng 1:1 hoặc 4:5 theo yêu cầu trước đây.
- Khi tạo ảnh collection dạng product life, áp dụng quy tắc đối tượng và hành động sử dụng thực tế ở mục 2; tham chiếu đúng sản phẩm thuộc collection.
- Upload ảnh vào Shopify và gắn trực tiếp vào trường ảnh collection. Không tạo bản dự phòng trùng lặp nếu không được yêu cầu.
- Viết description phù hợp nhóm sản phẩm, không thêm thông tin kỹ thuật hoặc tuyên bố chưa có nguồn.

### Membership và preset/template local

- Dùng manual collection cho nhóm được chọn thủ công trong thiết kế. Chỉ dùng smart collection khi có quy tắc rõ ràng; kiểm tra membership thực tế sau khi áp dụng.
- Chọn sản phẩm đúng category/chủ đề; không thêm sản phẩm không liên quan để đủ số lượng.
- Nếu yêu cầu có số lượng tối thiểu, đáp ứng số lượng đó. Yêu cầu cũ “ít nhất 5 sản phẩm mỗi danh mục” xuất phát từ shop trang sức; không tự áp dụng cho mọi template mới. Nếu thiếu sản phẩm phù hợp, báo thiếu và đề xuất nguồn/nội dung demo.
- Ghi handle collection vào đúng setting resource trong preset/template local; tab, thumbnail, banner, hotspot hoặc nút dùng URL/reference phù hợp schema. Không chọn rồi save picker trên store. Dùng link collection thật và ảnh collection thật.
- Nếu người dùng yêu cầu tạo collection trước, có thể để sản phẩm trống, nhưng phải báo rõ. Không báo catalog đã hoàn thành khi membership chưa được bổ sung.
- Kiểm tra trạng thái khả dụng trên Online Store theo yêu cầu và môi trường demo hiện tại.
