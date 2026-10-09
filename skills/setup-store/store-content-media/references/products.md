# 2. Sản phẩm


### Quy tắc đã được người dùng chốt

| Thành phần | Yêu cầu |
| --- | --- |
| Ảnh | Tối thiểu 4 ảnh cho từng sản phẩm. Nếu design chỉ có 1 ảnh: ảnh 1 là ảnh sản phẩm, ảnh 2 là product life, ảnh 3 và 4 là các góc nhìn khác của cùng sản phẩm. Dùng ảnh gốc làm tham chiếu để render phần thiếu. |
| Description | Có mô tả đầy đủ, phù hợp đúng sản phẩm. |
| Giá | Có giá gốc và giá khuyến mãi. |
| Tồn kho | Số lượng trung bình 20; không lấy mặc định 100 từ receipt cũ. |
| Summary | Có metafield summary. |
| Tag | Có `New` hoặc `Bestseller`. |
| Variant | Bắt buộc có `Color`, dùng dữ liệu màu liên kết metafield. Chuẩn hóa option về `Color` và `Size` khi có kích thước thực tế. |

### Tên và phân loại

- Title giữ tên sản phẩm trong thiết kế, không thêm tên template phía sau theo quy trình template hiện có.
- Sản phẩm mới dùng handle `<template-slug>-<product-slug>`, ví dụ `perky-rocking-horse`. Không đổi handle tài nguyên đã có nếu không cần thiết.
- Chọn product category đúng loại sản phẩm; mô tả và collection membership phải phù hợp với category.
- Gắn ít nhất một tag `New` hoặc `Bestseller` theo vị trí thiết kế. Nếu thiết kế không chỉ định, dùng `New` cho sản phẩm demo mới; không tự tuyên bố sản phẩm thực tế bán chạy.

### Giá và tồn kho

- Shopify `price` là giá bán/khuyến mãi; `compareAtPrice` là giá gốc và phải lớn hơn giá bán khi cần hiển thị giảm giá.
- Chép đúng giá và tiền tệ từ thiết kế. Nếu thiết kế chỉ có một giá, không tự bịa giá còn thiếu hoặc tỷ lệ giảm; ghi thiếu và lấy thông tin từ người dùng.
- Với dữ liệu demo mới không có yêu cầu khác, áp dụng **20 đơn vị cho mỗi variant có hàng** tại location đã xác nhận. Đây là cách áp dụng mặc định của quy trình cho yêu cầu “số lượng trung bình 20”.
- Giữ đúng trạng thái sold out hoặc tồn kho cụ thể trong thiết kế/yêu cầu. Không tự ghi đè tồn kho đang vận hành của sản phẩm có sẵn khi chỉ bổ sung nội dung.

### Description và summary

- Description gồm giới thiệu, đặc điểm có căn cứ và thông tin sử dụng/chăm sóc khi có nguồn. Không chỉ lặp title hoặc để placeholder.
- Summary là đoạn tóm tắt ngắn, phù hợp description và dùng đúng metafield mà theme đang đọc.
- Kiểm tra definition, namespace/key và kiểu dữ liệu summary hiện có trước khi ghi. Không tự tạo thêm một field tương tự chỉ vì chưa tìm đúng field.

### Color, Size và swatch

- Tạo `Color` theo màu sản phẩm thực tế; sản phẩm một màu vẫn có giá trị Color phù hợp.
- Liên kết màu bằng category metafield/metaobject mà Shopify và theme sử dụng, theo contract hiện có (ví dụ `shopify.color-pattern`); không chỉ nhập tên option dạng text rồi coi đã hoàn thành.
- Khi chuẩn hóa sản phẩm có option `Birthstone` hoặc `Material`, đối chiếu giá trị với màu thực tế để đổi thành `Color`. Không đổi tên hàng loạt nếu làm mất thông tin hoặc tạo tổ hợp trùng; giữ thông tin chất liệu/đá có căn cứ trong mô tả hoặc field phù hợp.
- Chỉ thêm `Size` khi có kích thước hợp lý và có nguồn. Không bịa size cho đồ chơi, phụ kiện hoặc sản phẩm không có lựa chọn kích thước.
- Kiểm tra mọi tổ hợp variant, giá, tồn kho và hình swatch sau khi tạo hoặc đổi option.

### Ảnh sản phẩm và ảnh variant

- Khi dùng trình tạo ảnh để tạo hoặc bổ sung ảnh sản phẩm (catalog, ảnh variant và product life), dùng **model `gpt-6-luna` với reasoning effort `max`** cho agent thực hiện tác vụ. Đây là cấu hình model của agent gọi công cụ tạo ảnh; không phải tham số model của công cụ tạo ảnh. Nếu môi trường không hỗ trợ cấu hình này, báo rõ giới hạn, không tự tuyên bố đã dùng đúng model.
- Lấy ảnh đúng sản phẩm từ thiết kế/nguồn được cung cấp; upload vào Shopify Files/product media, không đưa ảnh nội dung vào theme `assets`.
- Mỗi sản phẩm phải có **tối thiểu 4 ảnh**. Sản phẩm dưới 4 ảnh phải được liệt kê rõ là chưa đạt, không dùng trung bình toàn bộ nhóm hoặc sản phẩm nhiều ảnh để che phần còn thiếu.
- Nếu sản phẩm trong design chỉ có một ảnh, giữ ảnh đó làm **ảnh 1 — ảnh sản phẩm/catalog**; tạo **ảnh 2 — product life** có đối tượng đang sử dụng đúng sản phẩm theo quy tắc bên dưới; tạo **ảnh 3 và 4 — hai góc nhìn khác của chính sản phẩm**, chẳng hạn mặt sau, bên trái, bên phải hoặc góc nghiêng tùy cấu tạo và góc ảnh gốc. Chọn góc bổ sung có ích để người xem hiểu sản phẩm, không lặp ảnh hoặc chỉ đổi nền để tính đủ 4 ảnh.
- Ảnh góc bổ sung phải nhất quán với ảnh gốc về hình dáng, màu, tỷ lệ và chi tiết nhận diện. Đối chiếu nguồn bổ sung khi có; không tự bịa chi tiết ở mặt khuất. Nếu không đủ căn cứ để dựng một góc, chọn góc khác có thể xác minh hoặc ghi rõ cần thêm ảnh tham chiếu.
- Với mỗi màu thực tế, có ảnh catalog và ảnh lifestyle/ảnh phụ phù hợp màu đó theo quy trình đã dùng cho Strideo. Nhiều màu có thể cần hơn 4 ảnh.
- Ảnh render phải giữ đúng hình dáng và nhận diện sản phẩm, màu variant và tỷ lệ khung ảnh của thiết kế. Không dùng một ảnh màu khác để giả lập đã đủ ảnh cho mọi màu.
- Gắn ảnh catalog làm ảnh chính của variant. Gắn ảnh phụ đúng màu vào variant metafield `custom.secondary_image` theo contract hiện có; kiểm tra definition và kiểu `file_reference` trước khi ghi.
- Với sản phẩm chỉ có một ảnh design, sắp xếp gallery theo thứ tự catalog → product life → góc bổ sung 1 → góc bổ sung 2. Với nhiều màu, tổ chức theo từng màu, bắt đầu bằng cặp catalog/product life rồi đến các góc bổ sung của màu đó; gắn đúng media/metafield cho variant. Thêm alt mô tả đúng sản phẩm, màu và góc nhìn hoặc hành động sử dụng.
- Chờ media ở trạng thái sẵn sàng, rồi kiểm tra URL thực tế và ảnh khi đổi variant.

### Ảnh product life: sản phẩm được sử dụng trong thực tế

**Ảnh product life (lifestyle) phải có đối tượng sử dụng và thể hiện cách sử dụng đúng của chính sản phẩm.** Chỉ đặt sản phẩm trên bàn, trong phòng hoặc trong một không gian đẹp là ảnh bối cảnh/ảnh phụ; không tính là đã có ảnh product life. Người xuất hiện cạnh sản phẩm nhưng không có tương tác sử dụng phù hợp cũng chưa đáp ứng yêu cầu.

#### Hiểu sản phẩm trước khi tạo ảnh

1. Đối chiếu ảnh gốc, category, description, variant và hướng dẫn sử dụng có nguồn để xác định: sản phẩm là gì, dành cho ai, dùng ở đâu trên cơ thể hoặc trong hoạt động nào, và thao tác sử dụng thực tế là gì.
2. Xác định đặc điểm phải giữ nguyên: hình dáng, màu, chất liệu có căn cứ, chi tiết nhận diện, kích thước/tỷ lệ và cấu tạo. Dùng ảnh đúng sản phẩm và đúng màu làm tham chiếu; không chỉ dựa vào tên để tạo một sản phẩm tương tự.
3. Chọn một tình huống sử dụng cụ thể, thiết thực và phù hợp với sản phẩm. Không suy cách dùng chỉ từ ngành hàng: serum dạng nhỏ giọt và dạng vòi bơm cần thao tác khác nhau; các loại đồ chơi cũng cần hoạt động khác nhau.
4. Nếu chưa xác định được cách dùng, kích thước hoặc đối tượng sử dụng phù hợp từ nguồn hiện có, ghi rõ phần thiếu và lấy thông tin trước khi tạo cảnh phụ thuộc vào dữ liệu đó. Không tự bịa công dụng, độ tuổi an toàn hoặc thao tác sử dụng.

#### Ví dụ theo loại sản phẩm

| Loại sản phẩm | Cảnh product life đạt yêu cầu |
| --- | --- |
| Jewelry/trang sức | Người dùng đeo đúng vị trí: nhẫn trên ngón tay, vòng trên cổ tay, dây chuyền trên cổ, hoa tai trên tai. Thấy rõ sản phẩm và tỷ lệ so với cơ thể. |
| Giày | Người dùng mang giày trên chân, đứng hoặc bước đi tự nhiên; kiểu giày, màu và cấu tạo khớp ảnh gốc. Chỉ cầm giày hoặc đặt giày trong phòng chưa thể hiện việc sử dụng. |
| Đồ chơi | Em bé/trẻ nhỏ thuộc nhóm tuổi phù hợp theo nguồn đang thực sự chơi với món đồ đó, chẳng hạn cầm lắc xúc xắc hoặc thao tác với đồ chơi xếp khối. Cảnh, tư thế và mức giám sát phù hợp với hướng dẫn sử dụng; không chỉ đặt đồ chơi cạnh trẻ. |
| Serum | Người dùng cầm đúng chai serum và thực hiện thao tác thoa lên mặt phù hợp với hướng dẫn và loại bao bì, chẳng hạn lấy serum rồi thoa nhẹ bằng tay. Không để đầu nhỏ giọt xuyên vào da, tạo thao tác vô lý hoặc minh họa kết quả điều trị chưa có căn cứ. |

Áp dụng cùng nguyên tắc cho các ngành hàng khác: xác định đối tượng và hành động sử dụng đúng trước, rồi mới chọn bối cảnh, ánh sáng và bố cục.

#### Yêu cầu khi viết prompt và kiểm tra ảnh

- Prompt phải nêu rõ **sản phẩm tham chiếu + variant + đối tượng sử dụng + vị trí tiếp xúc/cách sử dụng + hành động cụ thể + tỷ lệ thực tế + bố cục thấy rõ sản phẩm**. Bối cảnh hỗ trợ hành động sử dụng, không thay thế hành động đó.
- Mẫu prompt: “Dùng ảnh tham chiếu của [sản phẩm, màu]. Giữ nguyên [đặc điểm nhận diện]. Thể hiện [đối tượng phù hợp] đang [hành động sử dụng đúng] tại [vị trí sử dụng], với tỷ lệ sản phẩm so với người đúng theo [nguồn kích thước nếu có]. Bố cục [tỷ lệ khung], thấy rõ sản phẩm và điểm tiếp xúc, tư thế tự nhiên, ánh sáng chân thực.” Bổ sung ràng buộc cụ thể theo sản phẩm, không dùng một prompt chung cho mọi ngành hàng.
- Kiểm tra ảnh sau render bằng mắt với ảnh gốc: đúng sản phẩm/màu, không biến dạng hoặc đổi thiết kế; sản phẩm không bị che đến mức khó nhận diện; kích thước so với người hợp lý.
- Kiểm tra tương tác vật lý: bàn tay/ngón tay, chân, khuôn mặt và tư thế tự nhiên; điểm cầm, đeo hoặc tiếp xúc đúng; không xuyên vật thể, nổi lơ lửng, sai vị trí đeo hoặc có bộ phận thừa. Hành động phải khả thi với cấu tạo thực tế của sản phẩm.
- Kiểm tra mức thiết thực: người xem nhận ra sản phẩm đang được dùng như thế nào và trong tình huống nào. Không dùng cảnh tạo dáng vô lý, đạo cụ lấn át hoặc người chỉ làm nền để gọi là product life.
- Ảnh chưa đạt phải sửa/render lại trước khi upload hoặc gắn làm ảnh lifestyle/`custom.secondary_image`. Khi nguồn chỉ có ảnh bối cảnh, ghi rõ còn thiếu product life; không đổi nhãn để coi đã hoàn thành.
- Alt mô tả đúng sản phẩm, màu và hành động sử dụng nhìn thấy trong ảnh. Lưu nguồn tham chiếu, tình huống sử dụng và kết quả kiểm tra vào receipt/audit.
