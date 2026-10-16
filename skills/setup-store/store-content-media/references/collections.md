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
- Khi setup collection theo Figma và thiết kế hiển thị số product, coi số đó là mục tiêu membership chính xác của từng collection. Đọc số từ đúng card/node, audit và tái sử dụng sản phẩm phù hợp, rồi thêm vào collection để số đếm thực tế khớp Figma; ví dụ ba card ghi 4/3/5 thì cần lần lượt 4/3/5 sản phẩm, không phải mỗi collection ít nhất 5 sản phẩm.
- Nếu catalog hiện có chưa đủ, bổ sung sản phẩm đúng nguồn theo reference Products trong phạm vi setup catalog đã được cho phép. Không tự mở rộng yêu cầu chỉ upload ảnh thành tạo sản phẩm mới khi thiếu dữ liệu bắt buộc hoặc quyền tạo catalog; báo rõ collection, số mục tiêu, số hiện có và phần thiếu. Không bịa sản phẩm, giá hoặc dùng sản phẩm không liên quan để lấp số đếm.
- Sau khi gắn membership, đọc lại số product thực tế và trạng thái khả dụng trên Online Store; đối chiếu với trường count mà block đang render. Chỉ báo hoàn tất setup collection khi số hiển thị khớp thiết kế, hoặc ghi rõ phần chưa khớp và nguyên nhân. Không hardcode số đếm trong theme để thay cho membership thật.
- Nếu yêu cầu có số lượng tối thiểu, đáp ứng số lượng đó. Yêu cầu cũ “ít nhất 5 sản phẩm mỗi danh mục” xuất phát từ shop trang sức; không tự áp dụng cho mọi template mới. Nếu thiếu sản phẩm phù hợp, báo thiếu và đề xuất nguồn/nội dung demo.
- Ghi handle collection vào đúng setting resource trong preset/template local; tab, thumbnail, banner, hotspot hoặc nút dùng URL/reference phù hợp schema. Không chọn rồi save picker trên store. Dùng link collection thật và ảnh collection thật.
- Chỉ để sản phẩm trống khi người dùng yêu cầu tạo collection trước/chỉ làm ảnh hoặc khi thiếu nguồn/quyền bắt buộc, và phải báo rõ; đây không phải kết quả hoàn tất setup có số đếm theo Figma. Không báo catalog đã hoàn thành khi membership chưa được bổ sung.
- Kiểm tra trạng thái khả dụng trên Online Store theo yêu cầu và môi trường demo hiện tại.


### View all trong thiết kế

- Nếu Figma hiển thị View all, đọc điều kiện render/ẩn hiện thực tế của section/block/runtime trước khi chuẩn bị collection. Không sửa hoặc bỏ điều kiện của theme chỉ để nút xuất hiện; thay đổi hành vi cần yêu cầu custom riêng.
- Với điều kiện `collection.products_count > max_products`, mỗi tab cần hiển thị nút phải có collection hợp lệ, URL thật, label không rỗng và số sản phẩm khả dụng trên Online Store **lớn hơn** giới hạn render. Bằng giới hạn vẫn chưa đủ. Số cột chỉ quyết định số card nhìn thấy cùng lúc; không thay thế `max_products`.
- Phối hợp preset để đồng thời có nút và slide: ví dụ 4 cột, giới hạn render5 và collection6 sản phẩm thì có thể trượt và có View all. Không đặt giới hạn render bằng hoặc lớn hơn toàn bộ collection khi thiết kế cần nút theo điều kiện overflow.
- Khi setup content đã được yêu cầu, ưu tiên tái sử dụng sản phẩm đúng theme/chủ đề và thêm phần thiếu theo nguồn được phép. Không tạo trùng hoặc thêm sản phẩm không liên quan chỉ để vượt ngưỡng. Nếu Figma ghi số lượng collection chính xác, giữ số lượng đó và chọn giới hạn preset phù hợp; nếu không thể đồng thời đáp ứng, báo gap.
- Đọc lại số sản phẩm khả dụng, thứ tự, URL và trạng thái từng tab sau mutation. Kiểm tra nút sau khởi tạo/chuyển tab cùng carousel tại desktop/mobile khi preview khả dụng. Ghi riêng giới hạn render, số cột, số lượng collection và kết quả hiển thị; không coi HTML có wrapper là bằng chứng nút đã hiện. Nếu thiếu quyền tạo/bổ sung catalog, báo thiếu theo ranh giới quyền hiện có.
